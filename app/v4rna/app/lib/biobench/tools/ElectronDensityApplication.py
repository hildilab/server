from __future__ import with_statement # 2.5 only
import formencode
from formencode import validators
from formencode import htmlfill
from formencode.schema import SimpleFormValidator
from biobench.tools import BaseController
from biobench.framework import expose
from biobench.utils import boolean, uid
from biobench.tools import ToolController, Cmd, FileUploadValidator
import re, sys, logging, os, cgi, string
from subprocess import Popen
from subprocess import call
import subprocess
import shutil
import simplejson as json
from biobench.jobs import Job
import biobench.jobs
from routes import url_for
from routes import redirect_to
import zipfile
import glob
import zlib

logging.basicConfig( level=logging.DEBUG )
LOG = logging.getLogger('biobench')
LOG.setLevel( logging.DEBUG )


class StaticHTML( BaseController ):
    def __init__( self, app ):
        self.app = app
    @expose
    def index( self, trans, **kwargs ):
        return trans.fill_template('eda/electron_density-webserver.mako')
    @expose
    def methods_EDM( self, trans, **kwargs ):
        return trans.fill_template('eda/methods_EDM.mako')
    @expose
    def methods_Converter( self, trans, **kwargs ):
        return trans.fill_template('eda/methods_Converter.mako')
    @expose
    def references( self, trans, **kwargs ):
        return trans.fill_template('eda/references.mako')
    @expose
    def faq( self, trans, **kwargs ):
        return trans.fill_template('eda/faq.mako')
    @expose
    def links( self, trans, **kwargs ):
        return trans.fill_template('eda/links.mako')
        
class GeneratorForm( formencode.Schema ):
    use_builtin_gettext = False
    allow_extra_fields = True
    filter_extra_fields = True
    ###todo: end=.cif/.pdb;
    data_cif = FileUploadValidator( not_empty=False, use_builtin_gettext=False )
    data_pdb = FileUploadValidator( not_empty=False, use_builtin_gettext=False )
    data_idpdb = validators.String( not_empty=False, min=4, max=4)
    ###todo:alle drei sind noch auszuwaehlen --> idpdb wird gestartet
  #  a = validators.RequireIfMissing(required='data_idpdb', missing='data_pdb') or validators.RequireIfMissing(required='data_idpdb', missing='data_cif') 
   # f = (validators.RequireIfPresent(required='data_cif', present='data_pdb') or validators.RequireIfMissing(required='data_cif', missing='data_idpdb') or validators.RequireIfMissing(required='data_pdb', missing='data_idpdb') or validators.RequireIfMissing(required='data_cif', missing='data_idpdb'))
    omit = validators.String( if_empty='False', if_missing='False' )
    sfcheck = validators.String( if_empty='False', if_missing='False' )
    mapext = validators.String()
    topic = validators.String()
    subtopics = formencode.ForEach(validators.String())
            
class Generator( ToolController ):
    name = 'generator'
    def __init__( self, app ):
        """Initialize an interface for the Generator tool"""
        self.app = app
        self.getPDB = GetPdbCmd( self, self.start_jobs )
        self.getStrucFact = GetStrucFactCmd( self, self.start_jobs )
        self.generatorcmd = GeneratorCmd( self, self.start_jobs )
    @expose
    def index( self, trans, **kwargs ):
        return self.form( trans, **kwargs )
    def _form( self, trans, **kwargs ):
        if not kwargs or not kwargs.get('submit'):
            html = trans.fill_template( 'eda/electron_density-formular.mako' )
            return htmlfill.render( html, defaults={ 'mapext': 'dotmap', 'sfcheck': 'sfcheck', 'subtopics': [ 'fofc_as', 'fofc_al', 'tfofc_as', 'tfofc_al' ] } )
        schema = GeneratorForm()
        try:
            form = schema.to_python( dict(**kwargs) )
        except validators.Invalid, e:
            html = trans.fill_template( 'eda/electron_density-formular.mako')
            return htmlfill.render( html, defaults=e.value, errors=e.error_dict )
        else:
            trans.task_id = uid()
            fofc_ass = 'False'
            fofc_all = 'False'
            tfofc_ass = 'False'
            tfofc_all = 'False'
            for i in form['subtopics']:
                if( i == 'fofc_as' ): fofc_ass = 'True'
                if( i == 'fofc_al' ): fofc_all = 'True'
                if( i == 'tfofc_as' ): tfofc_ass = 'True'
                if( i == 'tfofc_al' ): tfofc_all = 'True'
            if( fofc_ass=='False' and fofc_all=='False' and tfofc_ass=='False' and tfofc_all=='False' ):
                fofc_ass = 'True'
            if (form['omit'] == 'omit'): omitt = 'True'
            else: omitt = 'False'
            if (form['sfcheck'] == 'sfcheck'): sfcheckk = 'True'
            else: sfcheckk = 'False'
            MTZ='False'
            if(form['data_idpdb']!=''):
                BASE = form['data_idpdb']
                self.init_state( trans, pdbid=True )
                self.set_state( trans, {
                    self.getStrucFact.name: { 'pdbid': 'True',
                                              'params': {'data_idpdb': form['data_idpdb'] } }
                })
                self.set_state( trans, {
                    self.getPDB.name: { 'pdbid': 'True',
                                        'params': {'data_idpdb': form['data_idpdb'] } }
                })
                self.set_state( trans, {
                    self.generatorcmd.name: { 'pdbid': 'True',
                                              'params': {'fofc_as': fofc_ass,
                                                         'fofc_al': fofc_all,
                                                         'tfofc_as': tfofc_ass,
                                                         'tfofc_al': tfofc_all,
                                                         'omit': omitt,
                                                         'sfcheck': sfcheckk,
                                                         'mapext': form['mapext'],
                                                         'BASE': BASE,
                                                         'MTZ': MTZ } }
                })
                self.start_jobs( trans )
                LOG.debug('generator jobs started')
                return redirect_to( url_for( '/tools/eda/generator/task', task_id=trans.task_id ) )
            else:
                data_cif = self.save_uploaded_file( trans, form['data_cif'] )
                data_pdb = self.save_uploaded_file( trans, form['data_pdb'] )
                self.init_state( trans, pdbid=False )
                BASE = form['data_cif']['filename']
                BASE = BASE[::-1]
                BASE = re.sub("/.*$", "", BASE)
                EXT = re.sub("\..*$", "", BASE)
                EXT = EXT[::-1]
                BASE = BASE[::-1]
                BASE = re.sub("\..*$", "", BASE)
                BASE = re.sub("-sf.*$", "", BASE)
                EXT = string.upper(EXT)
                MTZ='False'
                if (EXT == 'MTZ'): MTZ='True'
                self.set_state( trans, {
                    'input_fileone': {
                        'ciffile': data_cif,
                        'status': biobench.jobs.JOB_OK
                    },
                    'input_filesec': {
                        'pdbfile': data_pdb,
                        'status': biobench.jobs.JOB_OK
                    },
                    self.generatorcmd.name: { 'pdbid': 'False',
                                              'params': {'fofc_as': fofc_ass,
                                                         'fofc_al': fofc_all,
                                                         'tfofc_as': tfofc_ass,
                                                         'tfofc_al': tfofc_all,
                                                         'omit': omitt,
                                                         'sfcheck': sfcheckk,
                                                         'mapext': form['mapext'],
                                                         'BASE': BASE,
                                                         'MTZ': MTZ } }
                })
                self.start_jobs( trans )
                LOG.debug('generator jobs started')
                return redirect_to( url_for( '/tools/eda/generator/task', task_id=trans.task_id ) )
                
    def _task( self, trans, **kwargs ):
        # get current state
        state = self.get_state( trans )
        state_str = self.formated_state( trans, links=True )
        LOG.debug('got new state')
        # running
        if( state['status'] == biobench.jobs.JOB_RUNNING ):
            return trans.fill_template( 'eda/wait.mako', state=state_str )
        # finnished
        else:
            if( state['status'] == biobench.jobs.JOB_OK ):
                file_status = self.file_status ( trans )
                html = trans.fill_template( 'eda/electron_density-results.mako', file_status=file_status, state=state_str, task_id=trans.task_id )
                return html
            else:
                session=trans.session_id
                job=trans.task_id
                if( state['generatorcmd']['status'] == biobench.jobs.JOB_ERROR ):
                    fehler='Error at convertion.'
                elif( state['getPDB']['status'] == biobench.jobs.JOB_ERROR ):
                    fehler='No pdb-entry in the PDB for your input "'+state[ self.getPDB.name ]['params']['data_idpdb']+'".'
                elif( state['getStrucFact']['status'] == biobench.jobs.JOB_ERROR ):
                    fehler='No structure factor entry in the PDB for your input "'+state[ self.getStrucFact.name ]['params']['data_idpdb']+'".'
                return trans.fill_template( 'eda/error.mako', task_id=trans.task_id, fehler=fehler, job=job, session=session  )
    def init_state( self, trans, pdbid=False ):
        state = self.get_state( trans )
        if (pdbid):
            self.set_state( trans, {
                'status': biobench.jobs.JOB_INIT
            })
            self.getStrucFact.set_default_state( trans )
            self.getPDB.set_default_state( trans )
            self.generatorcmd.set_default_state( trans )
        else:
            self.set_state( trans, {
                'status': biobench.jobs.JOB_INIT,
                'input_fileone': {
                    'ciffile': '',
                    'status': biobench.jobs.JOB_INIT
                },
                'input_filesec': {
                    'pdbfile': '',
                    'status': biobench.jobs.JOB_INIT
                }
            })
            self.generatorcmd.set_default_state( trans )
    def start_jobs( self, trans ):
        state = self.get_state( trans )
        if (state[ self.generatorcmd.name ]['pdbid']=='True'):
            state = self.get_state( trans )
            if state[ self.getStrucFact.name ]['status'] == biobench.jobs.JOB_INIT:
                self.getStrucFact.start( trans )
            state = self.get_state( trans )
            if state[ self.getPDB.name ]['status'] == biobench.jobs.JOB_INIT:
                self.getPDB.start( trans )
            #state = self.get_state( trans )
            if ( state[ self.getStrucFact.name ]['status'] == biobench.jobs.JOB_OK and
                 state[ self.getPDB.name ]['status'] == biobench.jobs.JOB_OK and
                 state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_INIT ):
                self.set_state( trans, {
                    self.generatorcmd.name: { 'params': {'data_cif': state[ self.getStrucFact.name ]['params']['outputdir']+'/in.cif',
                                                         'data_pdb': state[ self.getPDB.name ]['params']['outputdir']+'/in.pdb'} }
                })
           #     self.set_state( trans, state ) # never ever do this
                self.generatorcmd.start( trans )
            state = self.get_state( trans )
            state_update = {}
            if (state[ self.getStrucFact.name ]['status'] == biobench.jobs.JOB_OK and
                state[ self.getPDB.name ]['status'] == biobench.jobs.JOB_OK and
                state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_OK
            ):
                state_update['status'] = biobench.jobs.JOB_OK
            elif (state[ self.getStrucFact.name ]['status'] == biobench.jobs.JOB_ERROR or
                  state[ self.getPDB.name ]['status'] == biobench.jobs.JOB_ERROR or
                  state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_ERROR
            ):
                state_update['status'] = biobench.jobs.JOB_ERROR
            else:
                state_update['status'] = biobench.jobs.JOB_RUNNING
            self.set_state( trans, state_update )
        else:
            if (state['input_fileone']['status'] == biobench.jobs.JOB_OK and
                state['input_filesec']['status'] == biobench.jobs.JOB_OK
            ):
                state = self.get_state( trans )
                state_update = {}
                if state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_INIT:
                    state_update = { self.generatorcmd.name: { 'params': {
                        'data_cif' : state['input_fileone']['ciffile'],
                        'data_pdb': state['input_filesec']['pdbfile']
                    }}}
                    self.set_state( trans, state_update )
                    self.generatorcmd.start( trans )
                state = self.get_state( trans )
                if (state['input_fileone']['status'] == biobench.jobs.JOB_OK and
                    state['input_filesec']['status'] == biobench.jobs.JOB_OK and
                    state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_OK
                ):
                    state_update['status'] = biobench.jobs.JOB_OK
                elif (state['input_fileone']['status'] == biobench.jobs.JOB_ERROR or
                      state['input_filesec']['status'] == biobench.jobs.JOB_ERROR or
                      state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_ERROR
                ):
                    state_update['status'] = biobench.jobs.JOB_ERROR
                else:
                    state_update['status'] = biobench.jobs.JOB_RUNNING
                self.set_state( trans, state_update )
    @expose
    def task_list( self, trans ):
        return trans.fill_template(
            'eda/task_list.mako', task_list=self.get_task_list( trans )
        )
    def file_status ( self, trans ):
        state = self.get_state( trans )
        BASE = state[ self.generatorcmd.name ]['params']['BASE']
        outputdir = state[ self.generatorcmd.name ]['params']['outputdir']
        types = [
                 ['/input.pdb', 'inputpdb'],
                 ['/input.cif', 'inputcif'],
                 ['/input.mtz', 'inputmtz'],
                 ['/2fo-fc_all-atoms_'+BASE+'.ccp4', '2maptc'],
                 ['/2fo-fc_asym-unit_'+BASE+'.ccp4', '2mapsc'],
                 ['/fo-fc_all-atoms_'+BASE+'.ccp4', '1maptc'],
                 ['/fo-fc_asym-unit_'+BASE+'.ccp4', '1mapsc'],
                 ['/2fo-fc_all-atoms_'+BASE+'.map', '2maptm'],
                 ['/2fo-fc_asym-unit_'+BASE+'.map', '2mapsm'],
                 ['/fo-fc_all-atoms_'+BASE+'.map', '1maptm'],
                 ['/fo-fc_asym-unit_'+BASE+'.map', '1mapsm'],
                 ['/sfcheck_'+BASE+'.pdf', 'sfcheckpdf'],
                 ['/'+BASE+'.mtz', 'mtzfile'],
                 ['/sfcheck_ext.map', '2fobsfcalc'],
                 ['/sfcheck_ext.ccp4', '2fobsfcalcc'],
                 ['/sfcheck.hkl', 'omitphases'],
                 ['/log.txt', 'log'],
                 ['/debug.txt', 'debug'],
                 ['/log_cif-to-mtz.txt', 'logcm'],
                 ['/debug_cif-to-mtz.txt', 'debugcm'],
                 ['/log_fourier-calculation.txt', 'logfc'],
                 ['/debug_fourier-calculation.txt', 'debugfc'],
                 ['/log_run-fft_nf1-as.txt', 'log1s'],
                 ['/debug_run-fft_nf1-as.txt', 'debug1s'],
                 ['/log_run-fft_nf1-at.txt', 'log1t'],
                 ['/debug_run-fft_nf1-at.txt', 'debug1t'],
                 ['/log_run-fft_nf2-as.txt', 'log2s'],
                 ['/debug_run-fft_nf2-as.txt', 'debug2s'],
                 ['/log_run-fft_nf2-at.txt', 'log2t'],
                 ['/debug_run-fft_nf2-at.txt', 'debug2t'],
                 ['/log_sfcheck.txt', 'logsf'],
                 ['/sfcheck.log', 'logsfextra'],
                 ['/debug_sfcheck.txt', 'debugsf'],
                 ['/log_omit_map.txt', 'logomit'],
                 ['/debug_omit_map.txt', 'debugomit']]
        file_status = {}
        os.mkdir(outputdir+'/input/')
        os.mkdir(outputdir+'/sfcheck/')
        os.mkdir(outputdir+'/sfcheck/logfiles/')
        os.mkdir(outputdir+'/omit_map/')
        os.mkdir(outputdir+'/omit_map/logfiles/')
        os.mkdir(outputdir+'/density_maps/')
        os.mkdir(outputdir+'/density_maps/logfiles/')
        for file, name in types:
            if( (os.path.isfile(outputdir+file)==True) and (os.stat(outputdir+file)[6]>0)):
                file_status[name]=True
                if name=='inputpdb' or name=='inputcif' or name=='inputmtz':
                    shutil.move(outputdir+file, outputdir+'/input'+file)
                elif name=='sfcheckpdf':
                    shutil.move(outputdir+file, outputdir+'/sfcheck'+file)
                elif name=='logsf' or name=='logsfextra' or name=='debugsf':
                    shutil.move(outputdir+'/'+file, outputdir+'/sfcheck/logfiles'+file)
                elif name=='2fobsfcalc' or name=='2fobsfcalcc' or name=='omitphases':
                    shutil.move(outputdir+file, outputdir+'/omit_map'+file)
                elif name=='logomit' or name=='debugomit':
                    shutil.move(outputdir+file, outputdir+'/omit_map/logfiles'+file)
                elif name=='2maptc' or name=='2mapsc' or name=='1maptc' or name=='1mapsc' or name=='2maptm' or name=='2mapsm' or name=='1maptm' or name=='1mapsm' or name=='mtzfile':
                    shutil.move(outputdir+file, outputdir+'/density_maps'+file)
                elif name=='logcm' or name=='debugcm' or name=='logfc' or name=='debugfc' or name=='log1s' or name=='debug1s' or name=='log1t' or name=='debug1t' or name=='log2s' or name=='debug2s' or name=='log2t' or name=='debug2t':
                    shutil.move(outputdir+file, outputdir+'/density_maps/logfiles'+file)
            else: file_status[name]=False
        try:
            compression = zipfile.ZIP_DEFLATED
        except:
            compression = zipfile.ZIP_STORED
        dir=outputdir
        zip = zipfile.ZipFile(outputdir+"/all.zip", 'w')
        root_len = len(os.path.abspath(dir))
        for root, dirs, files in os.walk(dir):
            archive_root = os.path.abspath(root)[root_len:]
            fi=len(files)
            for f in files:
                if ( fi!=0):
                    fullpath = os.path.join(root, f)
                    archive_name = os.path.join(archive_root, f)
                    for file, name in types:
                        if (file in archive_name):
                            zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
                    fi=fi-1
        zip.close()
        return ( file_status )

    @expose
    def download( self, trans, task_id, filename ):
        state = self.get_state( trans )
        BASE = state[ self.generatorcmd.name ]['params']['BASE']
        outputdir = state[ self.generatorcmd.name ]['params']['outputdir']
        types = [
            ['inputpdb', 'input/input', 'pdb'],
            ['inputcif', 'input/input', 'cif'],
            ['inputmtz', 'input/input', 'mtz'],
            ['2maptm', 'density_maps/2fo-fc_all-atoms_'+BASE, 'map'],
            ['2maptc', 'density_maps/2fo-fc_all-atoms_'+BASE, 'ccp4'],
            ['2mapsm', 'density_maps/2fo-fc_asym-unit_'+BASE, 'map'],
            ['2mapsc', 'density_maps/2fo-fc_asym-unit_'+BASE, 'ccp4'],
            ['1maptm', 'density_maps/1fo-fc_all-atom_'+BASE, 'map'],
            ['1maptc', 'density_maps/1fo-fc_all-atoms_'+BASE, 'ccp4'],
            ['1mapsm', 'density_maps/1fo-fc_asym-unit_'+BASE, 'map'],
            ['1mapsc', 'density_maps/1fo-fc_asym-unit_'+BASE, 'ccp4'],
            ['sfcheckpdf', 'sfcheck/sfcheck_'+BASE, 'pdf'],
            ['mtzfile', 'density_maps/'+BASE, 'mtz'],
            ['2fobsfcalc', 'omit_map/sfcheck_ext', 'map'],
            ['2fobsfcalcc', 'omit_map/sfcheck_ext', 'ccp4'],
            ['omitphases', 'omit_map/sfcheck', 'hkl'],
            ['log', 'log', 'txt'],
            ['debug', 'debug', 'txt'],
            ['logcm', 'density_maps/logfiles/log_cif-to-mtz', 'txt'],
            ['debugcm', 'density_maps/logfiles/debug_cif-to-mtz', 'txt'],
            ['logfc', 'density_maps/logfiles/log_fourier-calculation', 'txt'],
            ['debugfc', 'density_maps/logfiles/debug_fourier-calculation', 'txt'],
            ['log1s', 'density_maps/logfiles/log_run-fft_nf1-as', 'txt'],
            ['debug1s', 'density_maps/logfiles/debug_run-fft_nf1-as', 'txt'],
            ['log1t', 'density_maps/logfiles/log_run-fft_nf1-at', 'txt'],
            ['debug1t', 'density_maps/logfiles/debug_run-fft_nf1-at', 'txt'],
            ['log2s', 'density_maps/logfiles/log_run-fft_nf2-as', 'txt'],
            ['debug2s', 'density_maps/logfiles/debug_run-fft_nf2-as', 'txt'],
            ['log2t', 'density_maps/logfiles/log_run-fft_nf2-at', 'txt'],
            ['debug2t', 'density_maps/logfiles/debug_run-fft_nf2-at', 'txt'],
            ['logsf', 'sfcheck/logfiles/log_sfcheck', 'txt'],
            ['logsfextra', 'sfcheck/logfiles/sfcheck', 'log'],
            ['debugsf', 'sfcheck/logfiles/debug_sfcheck', 'txt'],
            ['logomit', 'omit_map/logfiles/log_omit_map', 'txt'],
            ['debugomit', 'omit_map/logfiles/debug_omit_map', 'txt'],
            ['allzip', 'all', 'zip']
        ]
        dict = {}
        for type, name, ext in types:
            dict[ type ] = os.path.join(
                state[ self.generatorcmd.name ]['params']['outputdir'], '%s.%s' % (name, ext) )
        trans.response.headers["Content-Disposition"] = \
            "attachment; filename=%s" % ( os.path.basename(dict[filename]) )
        return self._get_file( trans, dict[filename] )
#      return open( dict[ filename ] ).read()

class GetPdbCmd( Cmd ):
    name = 'getPDB'
    pdbid = ''
    cmd = 'getPDB.py %(data_idpdb)s -o %(outputdir)s -f in.pdb'
    params = {
        'data_idpdb': '',
        'outputdir': '%(job_dir)s'
    }
    
class GetStrucFactCmd( Cmd ):
    name = 'getStrucFact'
    pdbid = ''
    cmd = 'getStrucFact.py %(data_idpdb)s -o %(outputdir)s -f in.cif'
    params = {
        'data_idpdb': '',
        'outputdir': '%(job_dir)s'
    }

class GeneratorCmd( Cmd ):
    name = 'generatorcmd'
    pdbid = ''
    cmd = 'master_selection_sed.sh %(data_cif)s %(data_pdb)s %(fofc_as)s ' +\
          '%(fofc_al)s %(tfofc_as)s %(tfofc_al)s %(omit)s %(sfcheck)s ' +\
          '%(mapext)s %(outputdir)s %(BASE)s %(MTZ)s'
    params = {
        'data_cif': '', 'data_pdb': '',
        'fofc_as': '', 'fofc_al': '',
        'tfofc_as': '', 'tfofc_al': '',
        'omit': '', 'sfcheck': '',
        'mapext': '',
        'outputdir': '%(job_dir)s',
        'BASE': '',
        'MTZ': ''
    }

class ConverterForm( formencode.Schema ):
    use_builtin_gettext = False
    allow_extra_fields = True
    filter_extra_fields = True
    data = FileUploadValidator( not_empty=True, use_builtin_gettext=False )
    maptype = validators.String()
    
class BrixForm( formencode.Schema ):
    use_builtin_gettext = False
    allow_extra_fields = True
    filter_extra_fields = True
    data = FileUploadValidator( not_empty=True, use_builtin_gettext=False )
   
class Converter( ToolController ):
    name = 'converter'
    def __init__( self, app, brix=False ):
        self.app = app
        self.brix = brix
        self.convertercmd = ConverterCmd( self, self.start_jobs )
    @expose
    def index( self, trans, **kwargs ):
        return self.form( trans, **kwargs )
    def _form( self, trans, **kwargs ):
        brix=self.brix
        if not kwargs or not kwargs.get('submit'):
            if self.brix==True:
                html = trans.fill_template( 'eda/brix_to_map-formular.mako')
            else:
                html = trans.fill_template( 'eda/EM_converter-formular.mako')
            return htmlfill.render( html, defaults={ 'maptype': 'CCP4' } )
        if self.brix==True:
            schema = BrixForm()
        else:
            schema = ConverterForm()
        try:
            form = schema.to_python( dict(**kwargs) )
        except validators.Invalid, e:
            if self.brix==True:
                html = trans.fill_template( 'eda/brix_to_map-formular.mako')
            else:
                html = trans.fill_template( 'eda/EM_converter-formular.mako')
            return htmlfill.render( html, defaults=e.value, errors=e.error_dict )
        else:
            data = self.save_uploaded_file( trans, form['data'] )
            trans.task_id = uid()
            self.init_state( trans )
            BASE = form['data']['filename']
            BASE = BASE[::-1]
            BASE = re.sub("/.*$", "", BASE)
            EXT = re.sub("\..*$", "", BASE)
            EXT = EXT[::-1]
            BASE = BASE[::-1]
            BASE = re.sub("\..*$", "", BASE)
            EXT = string.upper(EXT)
            if EXT == 'MAP':
                EXT = 'CCP4'
            else:
                EXT = EXT
            if self.brix == True:
                self.set_state( trans, {
                    'input_file': {
                        'file': data,
                        'status': biobench.jobs.JOB_OK
                    },
                    self.convertercmd.name: { 'params': {'BASE': BASE, 'EXT': 'BRIX', 'maptype': 'MAP', 'BRIX': 'True' } }
                })
            else:
                self.set_state( trans, {
                    'input_file': {
                        'file': data,
                        'status': biobench.jobs.JOB_OK
                    },
                    self.convertercmd.name: { 'params': {'BASE': BASE, 'EXT': EXT, 'maptype': form['maptype'], 'BRIX': 'False' } }
                })
            self.start_jobs( trans )
            LOG.debug('converter jobs started')
            return redirect_to( url_for( '/tools/eda/converter/task', task_id=trans.task_id ) )
    def _task( self, trans, **kwargs ):
        brix = self.brix
        # get current state
        state = self.get_state( trans )
        
        state_str = self.formated_state( trans, links=True )
        LOG.debug('got new state')
        # running
        if( state['status'] == biobench.jobs.JOB_RUNNING ):
            return trans.fill_template( 'eda/wait.mako', state=state_str )
        # finnished
        else:
            file_status = self.file_status ( trans )
            if( state['status'] == biobench.jobs.JOB_OK ):
                if (state[ self.convertercmd.name ]['params']['BRIX'] == 'True'):
                    html = trans.fill_template( 'eda/brix_to_map-results.mako', file_status=file_status, state=state_str, task_id=trans.task_id  )
                else:
                    html = trans.fill_template( 'eda/EM_converter-results.mako', file_status=file_status, state=state_str, task_id=trans.task_id )
                return html
            else:
                session=trans.session_id
                job=trans.task_id
                fehler='Error at convertion.'  
                return trans.fill_template( 'eda/error.mako', task_id=trans.task_id, fehler=fehler, job=job, session=session)
    def init_state( self, trans ):
        self.set_state( trans, {
            'status': biobench.jobs.JOB_INIT,
            'input_file': {
                'file': '',
                'status': biobench.jobs.JOB_INIT
            }
        })
        self.convertercmd.set_default_state( trans )
    def start_jobs( self, trans ):
        state = self.get_state( trans )
        if state['input_file']['status'] == biobench.jobs.JOB_OK:
            state = self.get_state( trans )
            if state[ self.convertercmd.name ]['status'] == biobench.jobs.JOB_INIT:
                self.set_state( trans, { self.convertercmd.name: { 'params': { 'data': state['input_file']['file'] } } } )
                self.convertercmd.start( trans )
            state = self.get_state( trans )
            state_update = {}
            if (state['input_file']['status'] == biobench.jobs.JOB_OK and
                state[ self.convertercmd.name ]['status'] == biobench.jobs.JOB_OK
            ):
                state_update['status'] = biobench.jobs.JOB_OK
            elif (state['input_file']['status'] == biobench.jobs.JOB_ERROR or
                  state[ self.convertercmd.name ]['status'] == biobench.jobs.JOB_ERROR
            ):
                state_update['status'] = biobench.jobs.JOB_ERROR
            else:
                state_update['status'] = biobench.jobs.JOB_RUNNING
            self.set_state( trans, state_update )
    @expose
    def task_list( self, trans ):
        return trans.fill_template(
            'eda/task_list.mako', task_list=self.get_task_list( trans )
        )
        
    def file_status ( self, trans ):
        state = self.get_state( trans )
        outputdir = state[ self.convertercmd.name ]['job_dir']
        BASE = state[ self.convertercmd.name ]['params']['BASE']
        types = [
                 ['/'+BASE+'.ccp4', 'ccp4'],
                 ['/'+BASE+'.map', 'map'],
                 ['/'+BASE+'.oldezd', 'oldezd'],
                 ['/'+BASE+'.mask', 'mask'],
                 ['/'+BASE+'.newezd', 'newezd'],
                 ['/'+BASE+'.envelope', 'envelope'],
                 ['/'+BASE+'.x-plor', 'x-plor'],
                 ['/'+BASE+'.dsn6', 'dsn6'],
                 ['/'+BASE+'.brix', 'brix'],
                 ['/'+BASE+'.xplor', 'xplor'],
                 ['/'+BASE+'.cns', 'cns'],
                 ['/'+BASE+'.ezd', 'ezd'],
                 ['/'+BASE+'.amore', 'amore'],
                 ['/'+BASE+'.omap', 'omap'],
                 ['/'+BASE+'.turbo', 'turbo'],
                 ['/'+BASE+'.mp', 'mp'],
                 ['/log.txt', 'log'],
                 ['/debug.txt', 'debug']
            ]
        file_status = {}
        for file, name in types:
            if (os.path.isfile(outputdir+file)==True) and (os.stat(outputdir+file)[6]>0):
                file_status[name]=True
            else: file_status[name]=False
        try:
            compression = zipfile.ZIP_DEFLATED
        except:
            compression = zipfile.ZIP_STORED
        zout = zipfile.ZipFile(outputdir+"/all.zip", "w")
        files=[]
        for file, name in types:
            if( (os.path.isfile(outputdir+file)==True) and (os.stat(outputdir+file)[6]>0)):
                files.append(outputdir+file)
        counter = len(files)
        for i in files:
            if (i in glob.glob(outputdir+"/*")) & (counter!=0):
                zout.write( i, os.path.basename(i), compression)
            counter = counter-1
        zout.close()
        return ( file_status )
        
    @expose
    def download( self, trans, task_id, filename ):
        state = self.get_state( trans )
        outputdir = state[ self.convertercmd.name ]['job_dir']
        BASE = state[ self.convertercmd.name ]['params']['BASE']
        types = [
            ['inputpdb', 'input', 'pdb'],
            ['log', 'log', 'txt'],
            ['debug', 'debug', 'txt'],
            ['all', 'all'+BASE, 'zip'],
            ['ccp4', BASE, 'ccp4'],
            ['map', BASE, 'map'],
            ['oldezd', BASE, 'oldezd'],
            ['mask', BASE, 'mask'],
            ['newezd', BASE, 'newezd'],
            ['envelope', BASE, 'envelope'],
            ['x-plor', BASE, 'x-plor'],
            ['dsn6', BASE, 'dsn6'],
            ['brix', BASE, 'brix'],
            ['xplor', BASE, 'xplor'],
            ['cns', BASE, 'cns'],
            ['ezd', BASE, 'ezd'],
            ['amore', BASE, 'amore'],
            ['omap', BASE, 'omap'],
            ['turbo', BASE, 'turbo'],
            ['mp', BASE, 'mp'],
            ['allzip', 'all', 'zip']
        ]
        dict = {}
        for type, name, ext in types:
            dict[ type ] = os.path.join(
                state[ self.convertercmd.name ]['params']['outputdir'], '%s.%s' % (name, ext) )
        trans.response.headers["Content-Disposition"] = \
            "attachment; filename=%s" % ( os.path.basename(dict[filename]) )
        return self._get_file( trans, dict[filename] )

class ConverterCmd( Cmd ):
    name = 'convertercmd'
    cmd = 'mapmanrunning.sh %(data)s %(BASE)s %(EXT)s %(maptype)s %(outputdir)s'
    params = {
        'data': '',
        'BASE': '',
        'EXT': '',
        'maptype': '',
        'outputdir': '%(job_dir)s'
    }
