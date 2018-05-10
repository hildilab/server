from __future__ import with_statement # 2.5 only

import sys, re, logging, os
import threading
import simplejson as json

from biobench.utils import merge_dict, uid
from biobench.jobs import Job
from biobench.framework import expose
import biobench.jobs

import formencode
formencode.api.set_stdtranslation(domain="FormEncode", languages=["en"])
from formencode import validators
import cgi

from routes import url_for
from routes import redirect_to


logging.basicConfig( level=logging.DEBUG )
LOG = logging.getLogger('biobench')
LOG.setLevel( logging.DEBUG )


class BaseController( object ):
    def __init__( self, app ):
        """Initialize an interface for the application 'app'"""
        self.app = app



# TODO: check if a task_id exists when it is requested
class ToolController( BaseController ):
    name = 'toolname'
    def __init__( self, app ):
        BaseController.__init__( self, app )
    def __state_filename( self, trans ):
        #session = trans.tool_sessions[ self.name ]
        session = trans.task_id
        return os.path.join( trans.directory, '%s_%s.js' % (self.name, session) )
    def get_state( self, trans ):
        state = {}
        state_path = self.__state_filename( trans )
        #print '###STATE PATH: ' + state_path
        if os.path.exists( state_path ):
            with open( self.__state_filename( trans ), 'rb' ) as fp:
                raw_state = fp.read()
                if raw_state:
                    state = json.loads( raw_state )
                else:
                    print '###STATE FILE EMPTY###'
        else:
            print '###STATE FILE NOT FOUND###'
        #print '###STATE###\n' + json.dumps( state, sort_keys=True, indent=4 )
        return state
    def set_state( self, trans, dict ):
        with trans.state_lock:
            state = self.get_state( trans )
            status = merge_dict( state, dict )
            with open( self.__state_filename( trans ), 'wb' ) as fp:
                fp.write( json.dumps( state, sort_keys=True, indent=4 ) )
                fp.flush()
                fp.seek(0)
    def get_task_list( self, trans ):
        task_list = []
        if trans.session_id:
            files = os.listdir( trans.directory )
            for f in files:
                if f.startswith( self.name ) and f.endswith( '.js' ):
                    task_list.append( f.split('_')[1][:-3] )
        return task_list
    def save_uploaded_file( self, trans, file_dict ):
        save_path = os.path.join(
            trans.directory, 'upload_%s_%s' % (uid(), file_dict['filename']) )
        with open( save_path, 'wb' ) as fp:
            fp.write( file_dict['content'] )
        return save_path
    def _form( self, trans, **kwargs ):
        # to be implemented by child classes
        pass
    @expose
    def form( self, trans, **kwargs ):
        if not trans.session_id:
            return "Error: No session id."
        return self._form( trans, **kwargs )
    def _task( self, trans, **kwargs ):
        # to be implemented by child classes
        pass
    @expose
    def task( self, trans, **kwargs ):
        if not trans.session_id:
            return "Error: No session id."
        if not trans.task_id:
            return "Error: task id."
        return self._task( trans, **kwargs )
    def formated_state( self, trans, links=False ):
        # TODO: formated option, where every key matching '*_file' is
        #   rendered as a link to view the file
        state = self.get_state( trans )
        if links:
            def file_format( k, v ):
                name = v.replace( trans.directory+os.sep, '' )
                if k.endswith( ('file', 'stderr', 'stdout') ):
                    path = url_for( '/tools/mplot/view', file=name )
                    return "<a href='%s'>%s</a>" % ( path, name )
                else:
                    return name
            state = map_dict_leafs( state, file_format )
            state_str = json.dumps( state, sort_keys=True, indent=4 )
        else:
            state_str = json.dumps( state, sort_keys=True, indent=4 ).replace( trans.directory, '' )
        return state_str
    @expose
    def state( self, trans, **kwargs ):
        trans.response.set_content_type( 'text/plain' )
        return self.formated_state( trans )
    def _get_file( self, trans, file ):
        # TODO: streaming for bigger files
        path = os.path.realpath( os.path.join( trans.directory, file ) )
        #print 'pfade'
        #print path
        #print trans.directory
        #print os.path.commonprefix( [path, trans.directory])
        if trans.directory == os.path.commonprefix( [path, trans.directory] ):
            if os.path.isfile( path ):
                with open( path, 'rb' ) as fp:
                    return fp.read()
            else:
                return 'ERROR: file not available.'
        else:
            return 'ERROR: access restriction.'
    @expose
    def download( self, trans, file ):
        trans.response.headers["Content-Disposition"] = \
            "attachment; filename=%s" % ( os.path.basename(file) )
        return self._get_file( trans, file )
    @expose
    def view( self, trans, file ):
        # TODO: wrap in '<pre>' template
        # TODO: fail-safe for huge files that could overwhelm the browser
        # TODO: everything that is more complex then plain-text-viewing
        #   should be forwarded to provi - how???
        trans.response.set_content_type( 'text/plain' )
        return self._get_file( trans, file )

    
class Cmd( object ):
    name = 'cmd'
    cmd = ''
    params = {}
    def __init__( self, tool, on_finish=None ):
        self.tool = tool
        self.on_finish = on_finish
    def set_default_state( self, trans ):
        self.tool.set_state( trans, { self.name: {
            'status': biobench.jobs.JOB_INIT,
            'job_dir': '',
            'stdout': '%(job_dir)s/stdout.txt',
            'stderr': '%(job_dir)s/stderr.txt',
            'params': self.params
        }})
    def get_params( self, trans ):
        return self.tool.get_state( trans )[ self.name ]['params']
    def get_status( self, trans ):
        return self.tool.get_state( trans )[ self.name ]['status']
    def get_dir( self, trans ):
        return self.tool.get_state( trans )[ self.name ]['job_dir']
    def start( self, trans ):
        state = self.tool.get_state( trans )
        params = state[ self.name ]['params']
        job = Job( trans.app, trans, self.cmd, params, self.finish )
        trans.app.job_manager.put( job )
        wd = { 'job_dir': job.working_directory }
        state_update = {
            self.name: {
                'status': job.get_state(),
                'params': job.params,
                'job_dir': job.working_directory,
                'stdout': state[ self.name ]['stdout'] % wd,
                'stderr': state[ self.name ]['stderr'] % wd
            }
        }
        #LOG.debug( json.dumps( state_update, sort_keys=True, indent=4 ) )
        self.tool.set_state( trans, state_update )
    def finish( self, job, trans ):
        state = self.tool.get_state( trans )
        state_update = { self.name: { 'status': job.get_state() } }
        self.tool.set_state( trans, state_update )
        with open( state[ self.name ]['stdout'], 'wb' ) as fp:
            fp.write( job.stdout )
        with open( state[ self.name ]['stderr'], 'wb' ) as fp:
            fp.write( job.stderr )
        if( self.on_finish and hasattr( self.on_finish, "__call__" ) ):
            self.on_finish( trans )



class FileUploadValidator(validators.FancyValidator): 
    def _to_python(self, value, state): 
        if str(value.__class__.__name__)=='FieldStorage':
        #if isinstance(value, cgi.FieldStorage): 
            filename = value.filename 
            content = value.value 
        elif str(value.__class__.__name__)=='str':
        #elif isinstance(value, str): 
            filename = None 
            content = value
        else:
            filename = None 
            content = None
        return dict(value=value, filename=filename, content=content) 


def map_dict_leafs( d, func, key=None ):
    if isinstance(d, dict): 
        return dict([ (k, map_dict_leafs( v, func, key=k )) for k,v in d.iteritems() ]) 
    elif isinstance(d, list): 
        return [ map_dict_leafs( x, func ) for x in d ] 
    else: 
        return func( key, d )


