from __future__ import with_statement # 2.5 only

import sys, re, logging, os, cgi
import simplejson as json

import formencode
from formencode import validators
from formencode import htmlfill


from biobench.tools import ToolController, Cmd, FileUploadValidator
from biobench.framework import expose
from biobench.utils import boolean, uid

from biobench.jobs import Job
import biobench.jobs

from routes import url_for
from routes import redirect_to



logging.basicConfig( level=logging.DEBUG )
LOG = logging.getLogger('biobench')
LOG.setLevel( logging.DEBUG )



class MPlotForm( formencode.Schema ):
    use_builtin_gettext = False
    allow_extra_fields = True
    filter_extra_fields = True
    pdb_file = FileUploadValidator( not_empty=True, use_builtin_gettext=False )
    probe_radius = validators.Number(
        min=0.4, max=3.0, if_empty=1.4, if_missing=1.4, use_builtin_gettext=False )


class MPlotController( ToolController ):
    name = 'mplot'
    def __init__( self, app ):
        """Initialize an interface for the MPlot tool"""
        self.app = app
        self.sco = ScoCmd( self, self.start_jobs )
        self.tmdet = TmdetCmd( self, self.start_jobs )
    @expose
    def index( self, trans, **kwargs ):
        # just return the form for now
        return self.form( trans, **kwargs )
    def _form( self, trans, **kwargs ):
        if not kwargs or not kwargs.get('submit'):
            # form has not been submitted
            html = trans.fill_template( 'mplot/form.mako' )
            # TODO: it would be nice to get the defaults given in the form schema definition...
            return htmlfill.render( html, defaults={} )
        schema = MPlotForm()
        try:
            form = schema.to_python( dict(**kwargs) )
        except validators.Invalid, e:
            html = trans.fill_template( 'mplot/form.mako' )
            return htmlfill.render( html, defaults=e.value, errors=e.error_dict )
        else:
            pdb_file = self.save_uploaded_file( trans, form['pdb_file'] )
            trans.task_id = uid()
            self.init_state( trans )
            self.set_state( trans, {
                'input_pdb': {
                    'file': pdb_file,
                    'status': biobench.jobs.JOB_OK
                },
                self.sco.name: { 'params': { 'probe_radius': form['probe_radius'] } }
            })
            self.start_jobs( trans )
            LOG.debug('mplot jobs started')
            return redirect_to( url_for( '/tools/mplot/task', task_id=trans.task_id ) )
    def _task( self, trans, **kwargs ):
        # get current state
        state = self.get_state( trans )
        state_str = self.formated_state( trans, links=True )
        LOG.debug('got new state')
        # running
        if( state['status'] == biobench.jobs.JOB_RUNNING ):
            return trans.fill_template( 'mplot/wait.mako', state=state_str )
        # finnished
        else:
            if( state['status'] == biobench.jobs.JOB_OK ):
                return trans.fill_template( 'mplot/results.mako', state=state_str )
            else:
                return trans.fill_template( 'mplot/error.mako', state=state_str )
    def init_state( self, trans ):
        self.set_state( trans, {
            'status': biobench.jobs.JOB_INIT,
            'input_pdb': {
                'file': '',
                'status': biobench.jobs.JOB_INIT
            }
        })
        self.tmdet.set_default_state( trans )
        self.sco.set_default_state( trans )
    def start_jobs( self, trans ):
        state = self.get_state( trans )
        if state['input_pdb']['status'] == biobench.jobs.JOB_OK:
            
            state = self.get_state( trans )
            if state[ self.tmdet.name ]['status'] == biobench.jobs.JOB_INIT:
                state[ self.tmdet.name ]['params']['pdb_file'] = state['input_pdb']['file']
                self.set_state( trans, state )
                self.tmdet.start( trans )
            
            state = self.get_state( trans )
            if state[ self.sco.name ]['status'] == biobench.jobs.JOB_INIT:
                state[ self.sco.name ]['params']['pdb_file'] = state['input_pdb']['file']
                self.set_state( trans, state )
                self.sco.start( trans )
            
            state = self.get_state( trans )
            if (state['input_pdb']['status'] == biobench.jobs.JOB_OK and
                state[ self.tmdet.name ]['status'] == biobench.jobs.JOB_OK and
                state[ self.sco.name ]['status'] == biobench.jobs.JOB_OK
            ):
                state['status'] = biobench.jobs.JOB_OK
            elif (state['input_pdb']['status'] == biobench.jobs.JOB_ERROR or
                  state[ self.tmdet.name ]['status'] == biobench.jobs.JOB_ERROR or
                  state[ self.sco.name ]['status'] == biobench.jobs.JOB_ERROR
            ):
                state['status'] = biobench.jobs.JOB_ERROR
            else:
                state['status'] = biobench.jobs.JOB_RUNNING
            self.set_state( trans, state )
    @expose
    def task_list( self, trans ):
        return trans.fill_template(
            'mplot/task_list.mako', task_list=self.get_task_list( trans ) )
        


class ScoCmd( Cmd ):
    name = 'sco'
    cmd = 'contact.py %(pdb_file)s -o %(sco_file)s ' +\
        '-l %(log_file)s -pr %(probe_radius)s'
    params = {
        'pdb_file': '',
        'sco_file': '%(job_dir)s/out.sco',
        'log_file': '%(job_dir)s/log.txt',
        'probe_radius': 1.4
    }


class TmdetCmd( Cmd ):
    name = 'tmdet'
    cmd = 'tmdet.py %(pdb_file)s -o %(tmdet_file)s -f 1'
    params = {
        'pdb_file': '',
        'tmdet_file': '%(job_dir)s/tmdet.xml'
    }

