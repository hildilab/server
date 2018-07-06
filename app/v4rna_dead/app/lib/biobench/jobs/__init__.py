from __future__ import with_statement

import logging, threading, sys, os, time, traceback, shutil


from biobench.utils import from_json_string, uid


from Queue import Queue, Empty

log = logging.getLogger( __name__ )

# States for running a job.
JOB_RUNNING, JOB_QUEUED, JOB_WAIT, JOB_ERROR, JOB_INPUT_ERROR, JOB_INPUT_DELETED, JOB_READY, JOB_DELETED, JOB_ADMIN_DELETED, JOB_OK, JOB_INIT, JOB_CREATED = 'running', 'queued', 'wait', 'error', 'input_error', 'input_deleted', 'ready', 'deleted', 'admin_deleted', 'ok', 'init', 'created'

# This file, if created in the job's working directory, will be used for
# setting advanced metadata properties on the job and its associated outputs.
# This interface is currently experimental, is only used by the upload tool,
# and should eventually become API'd
TOOL_PROVIDED_JOB_METADATA_FILE = 'biobench.json'

class JobManager( object ):
    """
    Highest level interface to job management.
    
    TODO: Currently the app accesses "job_queue" and "job_stop_queue" directly.
          This should be decoupled. 
    """
    def __init__( self, app ):
        self.app = app
        if self.app.config.get( "enable_job_running", True ):
            # The dispatcher launches the underlying job runners
            self.dispatcher = DefaultJobDispatcher( app )
            # Queues for starting and stopping jobs
            self.job_queue = JobQueue( app, self.dispatcher )
        else:
            self.job_queue = NoopQueue()
    def shutdown( self ):
        self.job_queue.shutdown()
    def put( self, job ):
        self.job_queue.put( job )

class Sleeper( object ):
    """
    Provides a 'sleep' method that sleeps for a number of seconds *unless*
    the notify method is called (from a different thread).
    """
    def __init__( self ):
        self.condition = threading.Condition()
    def sleep( self, seconds ):
        self.condition.acquire()
        self.condition.wait( seconds )
        self.condition.release()
    def wake( self ):
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

class JobQueue( object ):
    """
    Job manager, waits for jobs to be runnable and then dispatches to 
    a JobRunner.
    """
    STOP_SIGNAL = object()
    def __init__( self, app, dispatcher ):
        """Start the job manager"""
        self.app = app
        self.job_lock = False
        # Keep track of the pid that started the job manager, only it
        # has valid threads
        self.parent_pid = os.getpid()
        # Contains new jobs. Note this is not used if track_jobs_in_database is True
        self.queue = Queue()
        # Contains jobs that are waiting (only use from monitor thread)
        ## This and jobs_to_check[] are closest to a "Job Queue"
        self.waiting_jobs = []
        # Helper for interruptable sleep
        self.sleeper = Sleeper()
        self.running = True
        self.dispatcher = dispatcher
        self.monitor_thread = threading.Thread( target=self.__monitor )
        self.monitor_thread.start()   
        log.info( "job manager started" )
        if self.app.config.get( 'enable_job_recovery', True ):
            self.__check_jobs_at_startup()
    
    def __check_jobs_at_startup( self ):
        """
        Checks all jobs that are in the 'new', 'queued' or 'running' state in
        the job directory
        """
        for job in []: # TODO
            self.queue.put( job )
    
    def __monitor( self ):
        """
        Continually iterate the waiting jobs, checking is each is ready to 
        run and dispatching if so.
        """
        # HACK: Delay until after forking, we need a way to do post fork notification!!!
        time.sleep( 10 )
        while self.running:
            try:
                self.__monitor_step()
            except:
                log.exception( "Exception in monitor_step" )
            # Sleep
            self.sleeper.sleep( 1 )
    
    def __monitor_step( self ):
        """
        Called repeatedly by `monitor` to process waiting jobs.
        """
        # Pull all new jobs from the queue at once

        # Get job objects and append to watch queue for any which were
        # previously waiting
        jobs_to_check = []
        for job in self.waiting_jobs:
            jobs_to_check.append( job )
        try:
            while 1:
                message = self.queue.get_nowait()
                if message is self.STOP_SIGNAL:
                    return
                # Unpack the message
                job = message
                # Get the job object and append to watch queue
                jobs_to_check.append( job )
        except Empty:
            pass
        
        # Iterate over new and waiting jobs and look for any that are 
        # ready to run
        new_waiting_jobs = []
        for job in jobs_to_check:
            try:
                self.dispatcher.put( job )
            except Exception, e:
                log.exception( "failure running job '%s'" % job.id )
        # Update the waiting list
        self.waiting_jobs = new_waiting_jobs
    
    def put( self, job ):
        """Add a job to the queue"""
        self.queue.put( job )
        self.sleeper.wake()
    
    def shutdown( self ):
        """Attempts to gracefully shut down the worker thread"""
        if self.parent_pid != os.getpid():
            # We're not the real job queue, do nothing
            return
        else:
            log.info( "sending stop signal to worker thread" )
            self.running = False
            self.queue.put( self.STOP_SIGNAL )
            self.sleeper.wake()
            log.info( "job queue stopped" )
            self.dispatcher.shutdown()

class Job( object ):
    """
    Convenience methods for running processes and state management.
    """
    def __init__( self, app, trans, cmd, params, on_finish=None ):
        self.app = app
        self.trans = trans
        #self.queue = app.queue
        #self.session_id = app.session_id
        self.id = uid()
        self.on_finish = on_finish
        self.working_directory = \
            os.path.join( self.trans.directory, str( self.id ) )
        for k, v in params.iteritems():
            params[ k ] = str(v) % { 'job_dir': self.working_directory }
        self.params = params
        self.command_line = cmd % self.params
        self.state = JOB_CREATED
        self.info = None
        self.traceback = None
        self.runner_name = 'local:///'
        self.runner_external_id = None
    def prepare( self ):
        """
        Prepare the job to run by creating the working directory.
        """
        if not os.path.exists( self.working_directory ):
            os.mkdir( self.working_directory )
    def fail( self, message, exception=False ):
        """
        Indicate job failure by setting state and message.
        """
        if exception:
            # Save the traceback immediately in case we generate another
            # below
            self.traceback = traceback.format_exc()
            # Get the exception
            etype, evalue, tb =  sys.exc_info()
        self.state = JOB_ERROR
        self.info = message
        self.cleanup()
    def change_state( self, state, info = False ):
        if info:
            self.info = info
        self.state = state
    def get_state( self ):
        return self.state
    def set_runner( self, runner_url, external_id ):
        self.runner_name = runner_url
        self.runner_external_id = external_id
    def finish( self, stdout, stderr ):
        """
        Called to indicate that the associated command has been run. Updates 
        the output datasets based on stderr and stdout from the command, and
        the contents of the output files. 
        """
        # if the job was deleted, don't finish it
        if self.state == JOB_DELETED:
            self.cleanup()
            return
        elif self.state == JOB_DELETED:
            # Job was deleted by an administrator
            self.fail( self.info )
            return
        if stderr:
            self.state = JOB_ERROR
        else:
            self.state = JOB_OK
        # Save stdout and stderr    
        self.stdout = stdout
        self.stderr = stderr
        log.debug( "job '%s' ended" % self.id )
        if( self.on_finish and hasattr(self.on_finish, "__call__") ):
            with self.trans.job_finish_lock:
                self.on_finish( self, self.trans )
        self.cleanup()
    def cleanup( self ):
        # remove temporary files
        try:
            pass
        except:
            log.exception( "Unable to cleanup job '%s'" % self.id )
    def get_command_line( self ):
        return self.command_line


class DefaultJobDispatcher( object ):
    def __init__( self, app ):
        self.app = app
        self.job_runners = {}
        start_job_runners = ["local"]
        if app.config.start_job_runners is not None:
            start_job_runners.extend( app.config.start_job_runners.split(",") )
        for name in start_job_runners:
            self._load_plugin( name )

    def _load_plugin( self, name ):
        module_name = 'biobench.jobs.runners.' + name
        try:
            module = __import__( module_name )
        except:
            log.exception( 'Job runner is not loadable: %s' % module_name )
            return
        for comp in module_name.split( "." )[1:]:
            module = getattr( module, comp )
        if '__all__' not in dir( module ):
            log.error( 'Runner "%s" does not contain a list of exported classes in __all__' % module_name )
            return
        for obj in module.__all__:
            display_name = ':'.join( ( module_name, obj ) )
            runner = getattr( module, obj )
            self.job_runners[name] = runner( self.app )
            log.debug( 'Loaded job runner: %s' % display_name )
            
    def put( self, job ):
        try:
            runner_name = ( job.runner_name.split(":", 1) )[0]
            log.debug( "dispatching job '%s' to %s runner" %( job.id, runner_name ) )
            self.job_runners[runner_name].put( job )
        except KeyError:
            log.error( 'put(): (%s) Invalid job runner: %s' % ( job.id, runner_name ) )
            job_wrapper.fail( 'Unable to run job due to a misconfiguration of the Biobench job running system.  Please contact a site administrator.' )

    def stop( self, job ):
        runner_name = ( job.job_runner_name.split(":", 1) )[0]
        log.debug( "stopping job '%s' in %s runner" %( job.id, runner_name ) )
        try:
            self.job_runners[runner_name].stop_job( job )
        except KeyError:
            log.error( 'stop(): (%s) Invalid job runner: %s' % ( job.id, runner_name ) )
            # Job and output dataset states have already been updated, so nothing is done here.
    
    def shutdown( self ):
        for runner in self.job_runners.itervalues():
            runner.shutdown()



class NoopQueue( object ):
    """
    Implements the JobQueue / JobStopQueue interface but does nothing
    """
    def put( self, *args ):
        return
    def shutdown( self ):
        return

