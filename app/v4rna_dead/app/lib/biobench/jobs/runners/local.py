import logging
import subprocess
from Queue import Queue
import threading

from biobench.jobs.runners import BaseJobRunner
import biobench.jobs

import os, errno
from time import sleep

log = logging.getLogger( __name__ )

__all__ = [ 'LocalJobRunner' ]

class LocalJobRunner( BaseJobRunner ):
    """
    Job runner backed by a finite pool of worker threads. FIFO scheduling
    """
    STOP_SIGNAL = object()
    def __init__( self, app ):
        """Start the job runner with 'nworkers' worker threads"""
        self.app = app
        # start workers
        self.queue = Queue()
        self.threads = []
        nworkers = self.app.config.local_job_queue_workers
        log.info( "starting workers" )
        for i in range( nworkers  ):
            worker = threading.Thread( target=self.run_next )
            worker.start()
            self.threads.append( worker )
        log.debug( "%d workers ready", nworkers )

    def run_next( self ):
        """Run the next job, waiting until one is available if neccesary"""
        while 1:
            job = self.queue.get()
            if job is self.STOP_SIGNAL:
                return
            try:
                self.run_job( job )
            except:
                log.exception( "Uncaught exception running job" )
                
    def run_job( self, job ):
        job.set_runner( 'local:///', None )
        stderr = stdout = command_line = ''
        # Prepare the job to run
        try:
            job.prepare()
            command_line = self.build_command_line( job )
        except:
            job.fail( "failure preparing job", exception=True )
            log.exception("failure running job '%s'" % job.id)
            return
        # If we were able to get a command line, run the job
        if command_line:
            try:
                log.debug( 'executing: %s' % command_line )
                proc = subprocess.Popen( args = command_line, 
                                         shell = True, 
                                         cwd = job.working_directory, 
                                         stdout = subprocess.PIPE, 
                                         stderr = subprocess.PIPE,
                                         env = os.environ,
                                         preexec_fn = os.setpgrp )
                job.set_runner( 'local:///', proc.pid )
                job.change_state( biobench.jobs.JOB_RUNNING )
                stdout = proc.stdout.read( 32768 )
                stderr = proc.stderr.read( 32768 )
                proc.wait() # reap
                log.debug('execution finished: %s' % command_line)
            except Exception, exc:
                job.fail( "failure running job", exception=True )
                log.exception("failure running job '%s'" % job.id)
                return
        
        # Finish the job                
        try:
            job.finish( stdout, stderr )
        except:
            log.exception("Job wrapper finish method failed")
            job.fail("Unable to finish job", exception=True)

    def put( self, job ):
        """Add a job to the queue (by job identifier)"""
        # Change to queued state before handing to worker thread so the runner won't pick it up again
        job.change_state( biobench.jobs.JOB_QUEUED )
        self.queue.put( job )
    
    def shutdown( self ):
        """Attempts to gracefully shut down the worker threads"""
        log.info( "sending stop signal to worker threads" )
        for i in range( len( self.threads ) ):
            self.queue.put( self.STOP_SIGNAL )
        log.info( "local job runner stopped" )

    def check_pid( self, pid ):
        try:
            os.kill( pid, 0 )
            return True
        except OSError, e:
            if e.errno == errno.ESRCH:
                log.debug( "check_pid(): PID %d is dead" % pid )
            else:
                log.warning( "check_pid(): Got errno %s when attempting to check PID %d: %s" %( errno.errorcode[e.errno], pid, e.strerror ) )
            return False

    def stop_job( self, job ):
        pid = int( job.runner_external_id )
        if not self.check_pid( pid ):
            log.warning( "stop_job(): %s: PID %d was already dead or can't be signaled" % ( job.id, pid ) )
            return
        for sig in [ 15, 9 ]:
            try:
                os.killpg( pid, sig )
            except OSError, e:
                log.warning( "stop_job(): %s: Got errno %s when attempting to signal %d to PID %d: %s" % ( job.id, errno.errorcode[e.errno], sig, pid, e.strerror ) )
                return  # give up
            sleep( 2 )
            if not self.check_pid( pid ):
                log.debug( "stop_job(): %s: PID %d successfully killed with signal %d" %( job.id, pid, sig ) )
                return
        else:
            log.warning( "stop_job(): %s: PID %d refuses to die after signaling TERM/KILL" %( job.id, pid ) )

