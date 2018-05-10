from __future__ import with_statement # 2.5 only

import sys, re, logging, os
import cookielib, urllib2
from paste import httpserver
from webob import Request, Response
from webob import exc
import threading
from biobench.framework import base
import simplejson as json
import beaker.middleware

from biobench.jobs import JobManager

from biobench.utils import boolean, uid
from biobench.framework import expose
import biobench.tools.Example
import biobench.tools.JobTest
import biobench.tools.ElectronDensityApplication
import biobench.tools.MPlot
import biobench.tools.Voronoia4RNA

import mako.template
import mako.lookup
import mako.runtime
from unipath import Path
import helpers
from SuffixTree import SubstringDict
from collections import defaultdict

logging.basicConfig( level=logging.DEBUG )
LOG = logging.getLogger('biobench')
LOG.setLevel( logging.DEBUG )


def get_suffix_trees(config):
    dirlink = Path( config)
    dic_pdb = SubstringDict()
    splitdic=SubstringDict()
    titledic=SubstringDict()
    z_score=SubstringDict()
    dataset_list=[]
    for dir, subdir, files in os.walk(dirlink):
        for file in files:
            i=1
            actdir=os.path.join(dir, file)
            f = open(actdir, "r")
            pdb = file[0]+file[1]+file[2]+file[3]
            if pdb!='get_' and pdb!='test':
                dataset_list.append(pdb)
            for line in f:
                if line.startswith("HEADER") or line.startswith("KEYWDS") or line.startswith("AUTHOR"):
                    line = line.strip() 
                    wort = re.split(" *", line)
                    if line.startswith("AUTHOR"):
                        wort = re.split(",*", line)
                    string= str(wort[1:])
                    dic_pdb[string]=pdb
                    dic_pdb[pdb]=pdb
                elif line.startswith("TITLE"):
                    line = line.strip()
                    wort = re.split(" *", line)
                    i=1
                    while i<len(wort):
                        string= wort[i]
                        titledic[string]=pdb
                        i=i+1
                elif line.startswith("SPLIT"):
                    line = line.strip()
                    wort = re.split(" *", line)
                    i=1
                    while i<len(wort):
                        string= wort[i]
                        splitdic[string]=pdb
                        i=i+1
                elif line.startswith('ZSCORE_RMS'):
                    line = line.strip()
                    score=re.split(" *", line)[1]
                    z_score[pdb]=score
                elif line.startswith('ATOM'):
                    break;
            f.close()
    dataset_list.sort()
    newl=[]
    i = 0
    while i<(len(dataset_list)):
        g=i+1
        while ((g<(len(dataset_list))) and (dataset_list[i]==dataset_list[g])):
            g=g+1
        newl.append(dataset_list[i])
        i=g+1
    dataset_list=newl

    
    return dic_pdb, splitdic, titledic, z_score, dataset_list


class BiobenchApplication( object ):
    def __init__( self, **kwargs ):
        self.config = Configuration( **kwargs )
        self.job_manager = JobManager( self )
        self.suffix_trees = get_suffix_trees( self.config.pdb_dataset_link )


class WebApplication( base.WebApplication ):
    def __init__( self, biobench_app  ):
        base.WebApplication.__init__( self )
        self.set_transaction_factory( lambda e: BiobenchWebTransaction( e, biobench_app, self ) )
        # Mako support
        self.mako_template_lookup = mako.lookup.TemplateLookup(
            directories = [ biobench_app.config.template_path ] ,
            module_directory = biobench_app.config.template_cache,
            collection_size = 500,
            output_encoding = 'utf-8' )


class BiobenchWebTransaction( base.DefaultWebTransaction ):
    """
    Encapsulates web transaction specific state for the Biobench application
    """
    def __init__( self, environ, app, webapp ):
        self.app = app
        self.webapp = webapp
        self.environ = environ
        
        from pprint import pformat
        LOG.debug( pformat(environ['PATH_INFO'] + '?' + environ['QUERY_STRING']) )
        
        base.DefaultWebTransaction.__init__( self, environ )
        
        cookie_dict = {}
        if 'HTTP_COOKIE' in self.environ:
            for cookie in self.environ['HTTP_COOKIE'].split(';'):
                LOG.debug( 'COOKIE: ' + cookie )
                name, value = cookie.strip().split('=', 1)
                cookie_dict[name] = value
        LOG.debug( cookie_dict )
        self.session_id = cookie_dict.get( 'biobenchsession' )
        LOG.debug( self.session_id )
        
        #self.__init_storage()
        self.__init_cookiejar()
        self.__init_directory()
        self.__init_tools()
        LOG.debug( self.tool_sessions )
    
    def __init_tools( self ):
        LOG.debug( self.session )
        LOG.debug( self.environ['beaker.session'] )
        if 'tool_sessions' not in self.session:
            self.session['tool_sessions'] = {}
        self.tool_sessions = self.session['tool_sessions']
        if 'tool_lock' not in self.session:
            self.session['tool_lock'] = threading.Lock()
        self.tool_lock = self.session['tool_lock']
        
        if 'state_lock' not in self.session:
            self.session['state_lock'] = threading.Lock()
        self.state_lock = self.session['state_lock']
        if 'job_finish_lock' not in self.session:
            self.session['job_finish_lock'] = threading.Lock()
        self.job_finish_lock = self.session['job_finish_lock']
        
        query_dict = {}
        if self.environ['QUERY_STRING']:
            for param in self.environ['QUERY_STRING'].split('&'):
                LOG.debug( param )
                if param:
                    name, value = param.split('=')
                    query_dict[name] = value
        if 'task_id' in query_dict:
            self.task_id = query_dict['task_id']
        else:
            self.task_id = None
        
        with self.tool_lock:
            for tool in ['jobtest', 'mplot']:
                if tool not in self.tool_sessions:
                    self.tool_sessions[ tool ] = uid()
        LOG.debug( self.session )
        LOG.debug( self.environ['beaker.session'] )
    
    def __init_directory( self ):
        if self.session_id:
            self.directory  = \
                os.path.join( self.app.config.job_working_directory, self.session_id )
            if not os.path.exists( self.directory ):
                os.mkdir( self.directory )
    
    def __init_storage(self):
        if 'storage' in self.environ['beaker.session']:
            pass
        else:
            self.session['storage'] = DataStorage()
        self.storage = self.session['storage']
    
    def __init_cookiejar(self):
        if 'cookiejar' in self.environ['beaker.session']:
            pass
        else:
            self.session['cookiejar'] = cookielib.CookieJar()
        self.cookiejar = self.session['cookiejar']
    @base.lazy_property
    def template_context( self ):
        return dict()
    def fill_template(self, filename, **kwargs):
        """
        Fill in a template, putting any keyword arguments on the context.
        """
        return self.fill_template_mako( filename, **kwargs )
    def fill_template_mako( self, filename, **kwargs ):
        template = self.webapp.mako_template_lookup.get_template( filename )
        template.output_encoding = 'utf-8' 
        #data = dict( caller=self, t=self, trans=self, h=helpers, util=util, request=self.request, response=self.response, app=self.app )
        data = dict( caller=self, t=self, trans=self, h=helpers, request=self.request, response=self.response, app=self.app )
        data.update( self.template_context )
        data.update( kwargs )
        return template.render( **data )



def app_factory( global_conf, **kwargs ):
    conf = global_conf.copy()
    conf.update(kwargs)
    
    biobench_app = BiobenchApplication( **kwargs )
    webapp = WebApplication( biobench_app )
    
    webapp.add_controller( 'ToolExample', biobench.tools.Example.ExampleController(webapp) )
    webapp.add_route('/tools/example/:action', controller='ToolExample', action='index')
    
    webapp.add_controller( 'JobTest', biobench.tools.JobTest.JobTestController(webapp) )
    webapp.add_route('/tools/jobtest/:action', controller='JobTest', action='index')
    
    webapp.add_controller( 'EDAstaticHTML', biobench.tools.ElectronDensityApplication.StaticHTML(webapp) )
    webapp.add_route('/tools/eda/:action', controller='EDAstaticHTML', action='index')
    
    webapp.add_controller( 'EDAGenerator', biobench.tools.ElectronDensityApplication.Generator(webapp) )
    webapp.add_route('/tools/eda/generator/:action', controller='EDAGenerator', action='index')
    
    webapp.add_controller( 'EDAConverter', biobench.tools.ElectronDensityApplication.Converter(webapp) )
    webapp.add_route('/tools/eda/converter/:action', controller='EDAConverter', action='index')
    
    webapp.add_controller( 'EDABrixConverter', biobench.tools.ElectronDensityApplication.Converter(webapp,brix=True) )
    webapp.add_route('/tools/eda/brix_converter/:action', controller='EDABrixConverter', action='index')
    
    webapp.add_controller( 'MPlot', biobench.tools.MPlot.MPlotController(webapp) )
    webapp.add_route('/tools/mplot/:action', controller='MPlot', action='index')
    
    webapp.add_controller( 'V4RNAstaticHTML', biobench.tools.Voronoia4RNA.StaticHTML(webapp) )
    webapp.add_route('/tools/v4rna/:action', controller='V4RNAstaticHTML', action='index')
    
    webapp.add_controller( 'V4RNAGenerator', biobench.tools.Voronoia4RNA.Generator(webapp) )
    webapp.add_route('/tools/v4rna/generator/:action', controller='V4RNAGenerator', action='index')
        
    webapp = wrap_in_middleware( webapp, global_conf, **kwargs )
    webapp = wrap_in_static( webapp, global_conf, **kwargs )
    
    from paste.deploy.config import ConfigMiddleware
    webapp = ConfigMiddleware( webapp, global_conf )
    
    return webapp


def wrap_in_middleware( app, global_conf, **local_conf  ):
    conf = global_conf.copy()
    conf.update(local_conf)
    
    app = beaker.middleware.SessionMiddleware( app, conf )
    app = GetSessionMiddleware( app, conf )
    
    #from paste.translogger import TransLogger
    #app = TransLogger( app, conf )
    
    from paste import httpexceptions
    app = httpexceptions.make_middleware( app, conf )
    
    from paste.debug import prints
    app = prints.PrintDebugMiddleware( app, conf )
    
    from weberror import evalexception
    app = evalexception.EvalException( app, conf )
    
    return app


def wrap_in_static( app, global_conf, **local_conf ):
    from paste.urlmap import URLMap
    from biobench.middleware.static import CacheableStaticURLParser as Static
    urlmap = URLMap()
    # Merge the global and local configurations
    conf = global_conf.copy()
    conf.update(local_conf)
    # Get cache time in seconds
    cache_time = conf.get( "static_cache_time", None )
    if cache_time is not None:
        cache_time = int( cache_time )
    # Send to dynamic app by default
    urlmap["/"] = app
    # Define static mappings from config
    urlmap["/static"] = Static( conf.get( "static_dir" ), cache_time )
    urlmap["/staticpdb"] = Static( conf.get( "pdb_dataset_link" ), cache_time )
    urlmap["/staticjob"] = Static( conf.get( "job_link" ), cache_time )
    print conf.get( "static_favicon_dir" )
    #urlmap["/favicon.ico"] = Static( conf.get( "static_favicon_dir" ), cache_time )
    return urlmap
    

# TODO: 'new' keyword to init new session
class GetSessionMiddleware( object ):
    def __init__( self, app, conf ):
        self.app = app
        self.conf = conf
    def __call__( self, environ, start_response ):
        query_dict = {}
        if environ['QUERY_STRING']:
            for param in environ['QUERY_STRING'].split('&'):
                LOG.debug( param )
                if param:
                    name, value = param.split('=')
                    query_dict[name] = value
        LOG.debug( environ['QUERY_STRING'] )
        LOG.debug( query_dict )
        if 'session_id' in query_dict:
            environ['HTTP_COOKIE'] = 'provisessionX=%s' % query_dict['session_id']
        return self.app(environ, start_response)

    
class Configuration( object ):
    def __init__( self, **kwargs ):
        self.config_dict = kwargs
        self.root = kwargs.get( 'root_dir', '.' )
        self.provi_url = kwargs.get( 'provi_url', 'http://localhost:7070' )
        self.host_url = kwargs.get( 'host_url', 'http://localhost:6060' )
        self.base_tag_href = kwargs.get( 'base_tag_href', 'http://proteinformatics.charite.de/voronoia4rna/' )
        self.pdb_dataset_link = kwargs.get( 'pdb_dataset_link')
        self.template_path = kwargs.get( 'template_path' )
        self.template_cache = kwargs.get( 'template_cache' )
        self.start_job_runners = kwargs.get( 'start_job_runners' )
        self.local_job_queue_workers = int( kwargs.get( 'local_job_queue_workers', 4 ) )
        self.job_working_directory = kwargs.get( 'job_working_directory' )
        
    def get( self, key, default ):
        return self.config_dict.get( key, default )

