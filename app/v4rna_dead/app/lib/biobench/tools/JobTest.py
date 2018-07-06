from __future__ import with_statement # 2.5 only

import simplejson as json

import formencode
from formencode import validators
from formencode import htmlfill

from biobench.tools import ToolController
from biobench.framework import expose

from biobench.jobs import Job

    
class JobTestController( ToolController ):
    name = 'jobtest'
    def __init__( self, app ):
        """Initialize an interface for the job test tool"""
        self.app = app
    @expose
    def index( self, trans, **kwargs ):
        if trans.session_id:
            self.start_job1( trans )
        return trans.fill_template( 'job_test.mako' )
    @expose
    def status( self, trans, **kwargs ):
        status = self.get_status( trans )
        if status.get('result') == True:
            return json.dumps( status )
        else:
            return json.dumps( status )
    def start_job1( self, trans ):
        job1 = Job(
            trans.app, trans,
            'echo "foobar" > job1_test', {},
            self.job1_finish
        )
        trans.app.job_manager.put( job1 )
        self.set_status( trans, {
            'result': False,
            'status': 'Job1 started'
        })
    def job1_finish( self, job ):
        if job.get_state() != '':
            self.start_job2( job.trans )
            self.set_status( job.trans, {
                'result': False,
                'status': 'Job1 OK, Job2 started'
            })
    def start_job2( self, trans ):
        job1 = Job(
            trans.app, trans,
            'echo "foobar" > job1_test', {},
            self.job2_finish
        )
        trans.app.job_manager.put( job1 )
    def job2_finish( self, job ):
        if job.get_state() != '':
            self.set_status( job.trans, {
                'result': True,
                'status': 'Job1 OK, Job2 OK'
            })
