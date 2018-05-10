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
from SuffixTree import SubstringDict
from collections import defaultdict
import time


logging.basicConfig( level=logging.DEBUG )
LOG = logging.getLogger('biobench')
LOG.setLevel( logging.DEBUG )



class StaticHTML( BaseController ):
    def __init__( self, app ):
        self.app = app
    @expose
    def index( self, trans, **kwargs ):
        return trans.fill_template('v4rna/voronoia4rna.mako')
    @expose
    def methods( self, trans, **kwargs ):
        return trans.fill_template('v4rna/methods.mako')
    @expose
    def methods_RefStat( self, trans, **kwargs ):
        return trans.fill_template('v4rna/methods_RefStat.mako')
    @expose
    def references( self, trans, **kwargs ):
        return trans.fill_template('v4rna/references.mako')
    @expose
    def faq( self, trans, **kwargs ):
        return trans.fill_template('v4rna/faq.mako')
    @expose
    def links( self, trans, **kwargs ):
        return trans.fill_template('v4rna/links.mako')
    @expose
    def tutorial( self, trans, **kwargs ):
        return trans.fill_template('v4rna/tutorial.mako')
        
class GeneratorForm( formencode.Schema ):
    use_builtin_gettext = False
    allow_extra_fields = True
    filter_extra_fields = True
    data_pdb = FileUploadValidator( not_empty=False, use_builtin_gettext=False )
    data_idpdb = validators.String( not_empty=False )
    zipped = validators.Bool()

class Generator( ToolController ):
    name = 'generator'
    def __init__( self, app ):
        """Initialize an interface for the Generator tool"""
        self.app = app
        self.generatorcmd = GeneratorCmd( self, self.start_jobs )
        self.prepgeneratorcmd = PrepGeneratorCmd( self, self.start_jobs )
        self.postgeneratorcmd = PostGeneratorCmd( self, self.start_jobs )
    @expose
    def index( self, trans, **kwargs ):
        return self.form( trans, **kwargs )
    def _form( self, trans, **kwargs ):
        dataset_list=trans.app.suffix_trees[4]

        if not kwargs or not kwargs.get('submit'):
            html = trans.fill_template( 'v4rna/v4rna-formular.mako', dataset_list=dataset_list)
            return htmlfill.render( html, defaults={  } )
        schema = GeneratorForm()
        try:
            form = schema.to_python( dict(**kwargs) )
        except validators.Invalid, e:
            html = trans.fill_template( 'v4rna/v4rna-formular.mako', dataset_list=dataset_list)
            return htmlfill.render( html, defaults=e.value, errors=e.error_dict )
        else:
            dic_pdb=trans.app.suffix_trees[0]
            splitdic=trans.app.suffix_trees[1]
            titledic=trans.app.suffix_trees[2]
            z_score=trans.app.suffix_trees[3]
            dirlink=trans.app.config.pdb_dataset_link
            if(form['data_idpdb']!=''):
                term=form['data_idpdb']
                if (',' in term) or ('.' in term):
                    term=filter(lambda c: c not in ",.", term)
                term = term.upper()
                searchstring=re.split(" *", term)
                grosseliste=[]; tgrosseliste=[];liste=[];
                for element in searchstring:
                    s = dic_pdb[element]
                    ts=titledic[element]
                    tgrosseliste = list(sorted(set(ts)))+tgrosseliste
                    grosseliste = list(sorted(set(s)))+grosseliste
                glist=[];tglist=[]
                for elem in grosseliste:
                    if elem!='in.p':
                        glist.append(elem)
                for elem in tgrosseliste:
                    if elem!='in.p':
                        tglist.append(elem)
                grosseliste=glist
                tgrosseliste=tglist
                tgrosseliste.sort()
                grosseliste.sort()
                count=defaultdict(int)
                tcount=defaultdict(int)
                for eintrag in grosseliste:
                    count[eintrag] +=1
                for eintrag in tgrosseliste:
                    tcount[eintrag] +=1
                listes=sorted(count.items(), lambda x,y: cmp(x[1],y[1]), reverse=True)
                tlistes=sorted(tcount.items(), lambda x,y: cmp(x[1],y[1]), reverse=True)
                i=0; liste=[]; alllist=[]; zscorelist=[]
                alllist=tlistes+listes
                anzahl = str(len(alllist))
                while (i<len(alllist)):# and i<50):
                    liste=liste+[alllist[i][0]]
                    i=i+1
                for elem in searchstring:
                    i=0;
                    while i<len(listes):
                        if elem == listes[i][0]:
                            liste=[elem]
                        i=i+1
                    if splitdic[elem]!=[] and elem!= 'in.p' and elem!='in_s':
                        if splitdic[elem]==elem or splitdic[elem][0]==elem:
                            liste=splitdic[elem]
                        else:
                            liste=splitdic[elem]+liste
                
                zipped = form['zipped']
                if zipped==True:
                    workdir=trans.directory
                    lister=[]
                    for element in liste:
                        lister.append(element+'.pdb')
                        lister.append(element+'.pdb.vol')
                        lister.append(element+'.pdb.vol.extended.vol')
                    try:
                        compression = zipfile.ZIP_DEFLATED
                    except:
                        compression = zipfile.ZIP_STORED
                    zip = zipfile.ZipFile(workdir+"/all.zip", 'w')
                    root_len = len(os.path.abspath(dirlink))
                    for root, dirs, files in os.walk(dirlink):
                        archive_root = os.path.abspath(root)[root_len:]
                        fi=len(files)
                        for f in files:
                            if ( fi!=0) and f in lister:
                                fullpath = os.path.join(root, f)
                                archive_name = os.path.join(archive_root, f)
                                zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
                                fi=fi-1
                    zip.close()  
                headerlist=[]
                if liste == []:
                    liste=['']
                    headerlist=['']
                    zscorelist=['']
                else:
                    for eleme in liste:
                        f=dirlink+'/'+eleme+'.pdb/'+eleme+'.pdb'
                        m=open(f, "r")
                        l=''
                        if z_score[eleme]==[]:
                            zscorelist.append('error')
                        else: zscorelist.append(z_score[eleme][0])
                        for line in m:
                            if line.startswith("TITLE"):
                                wort = line.lower()
                                string= str(wort[10:])
                                l=l+string
                            elif line.startswith("REMARK"):
                                break
                        headerlist=headerlist+[l]
                        m.close()
                html = trans.fill_template( 'v4rna/v4rna-formular.mako', liste=liste, headerlist=headerlist, proviurl=trans.app.config.provi_url, environurl=trans.app.config.host_url, dataset_list=dataset_list, 
zscorelist=zscorelist, pdb_dataset_link=trans.app.config.pdb_dataset_link, zipped=zipped, anzahl=anzahl )
                return html
            elif (form['data_pdb']!=None):
                trans.task_id = uid()
                data_pdb = self.save_uploaded_file( trans, form['data_pdb'] )
                self.init_state( trans, pdbid=False )
                #prozess
                BASE = form['data_pdb']['filename']
                BASE = BASE[::-1]
                BASE = re.sub("/.*$", "", BASE)
                BASE = BASE[::-1]
                BASE = re.sub("\..*$", "", BASE)
                BASE = re.sub("-sf.*$", "", BASE)
                self.set_state( trans, {
                    'input_filesec': {
                        'pdbfile': data_pdb,
                        'status': biobench.jobs.JOB_OK
                    },
                    self.prepgeneratorcmd.name: { 'pdbid': 'False',
                                              'params': {
                                                         'BASE': BASE} }
                })
                self.set_state( trans, {
                    self.generatorcmd.name: { 'pdbid': 'False',
                                              'params': {'BASE': BASE} }
                })
		self.set_state( trans, {
		    self.postgeneratorcmd.name: { 'pdbid': 'False',
						  'params': {} }
		})
                self.start_jobs( trans )
                LOG.debug('generator jobs started')
                return redirect_to( url_for( 'task', task_id=trans.task_id ) )
            else:
                html = trans.fill_template( 'v4rna/v4rna-formular.mako', dataset_list=dataset_list )
                return html
                
    def _task( self, trans, **kwargs ):
        # get current state
        state = self.get_state( trans )
        state_str = self.formated_state( trans, links=True )
        LOG.debug('got new state')
        # running
        if( state['status'] == biobench.jobs.JOB_RUNNING ):
            return trans.fill_template( 'v4rna/wait.mako', state=state_str, task_id=trans.task_id )
        # finnished
        else:
	    errorfileabfang=open(state[ self.generatorcmd.name ]['params']['outputdir']+'/stderr.txt','rw')
	    tidelti="false"
	    for line in errorfileabfang:
		if line.startswith("Application tried to create a"):
		    tidelti="true"
		    break;
		else:
		    break
	    errorfileabfang.close()
	    if tidelti=="true":
		os.remove(state[ self.generatorcmd.name ]['params']['outputdir']+'/stderr.txt')
	    	f = file(state[ self.generatorcmd.name ]['params']['outputdir']+'/stderr.txt','w')
            if( state['status'] == biobench.jobs.JOB_OK ):
                file_status = self.file_status ( trans )
		provipath=state[ self.postgeneratorcmd.name ]['params']['outputdir']+'/'+state[ self.generatorcmd.name ]['params']['BASE']+'.provi'
                provipath=provipath.split('/jobs/')[1]
                html = trans.fill_template( 'v4rna/v4rna-results.mako', file_status=file_status, state=state_str, task_id=trans.task_id, environurl=trans.app.config.host_url, proviurl=trans.app.config.provi_url, provipath=provipath )
                return html
	    elif (tidelti=="true"):
#postgenerator prozess einfuegen
		#state = self.get_state( trans )
		#print "tut1"
                state[ self.postgeneratorcmd.name ]['status'] = biobench.jobs.JOB_INIT
                self.set_state( trans, {
                    self.postgeneratorcmd.name: { 'params': {
                                                            'data_pdb': state[ self.prepgeneratorcmd.name ]['params']['outputdir']+'/in.pdb',
                                                            'outvol': state[ self.generatorcmd.name ]['params']['outputdir']+'/'+state[ self.generatorcmd.name ]['params']['BASE']+'.vol'
                                                         } }
                })
                self.postgeneratorcmd.start( trans )
                state = self.get_state( trans )
                state_update = {}
		state['status'] = biobench.jobs.JOB_OK
                file_status = self.file_status ( trans )
		if file_status['volfile']==True:
		    file_status['provi']=True
		provipaths=state[ self.postgeneratorcmd.name ]['params']['outputdir']+'/'+state[ self.generatorcmd.name ]['params']['BASE']+'.provi'
                provipath=provipaths.split('/jobs/')[1]
		restpath=provipaths.split('/jobs/')[0]+'/jobs/'+provipath.split('/')[0]+'/'
		
		state = self.get_state( trans )
                #state_update = {}
		#state['status'] = biobench.jobs.JOB_OK
		
		#change .js for no error
		shutil.copy(restpath+'generator_'+trans.task_id+'.js', restpath+'generator_'+trans.task_id+'old.js')
		os.remove(restpath+'generator_'+trans.task_id+'.js')
		jsfilechange=open(restpath+'generator_'+trans.task_id+'old.js','rw')
		newjsfilechange=file(restpath+'generator_'+trans.task_id+'.js','w')
		for line in jsfilechange:
		    if line.startswith('    "status": "error"'):
			newjsfilechange.write('    "status": "ok"')
		    elif line.startswith('        "status": "error",'):
			newjsfilechange.write('        "status": "ok",')
		    else: newjsfilechange.write(line)
		jsfilechange.close()
		os.remove(restpath+'generator_'+trans.task_id+'old.js')
		newjsfilechange.close()
		return trans.fill_template( 'v4rna/wait.mako', state=state_str, task_id=trans.task_id )
                html = trans.fill_template( 'v4rna/v4rna-results.mako', file_status=file_status, task_id=trans.task_id, environurl=trans.app.config.host_url, proviurl=trans.app.config.provi_url, provipath=provipath )
                #return html
            else:
                session=trans.session_id
                job=trans.task_id
                fehler=''
                if( state['generatorcmd']['status'] == biobench.jobs.JOB_ERROR ):
                    fehler='Error at convertion.'
                return trans.fill_template( 'v4rna/error.mako', task_id=trans.task_id, fehler=fehler, job=job, session=session  )
    def init_state( self, trans, pdbid=False ):
        state = self.get_state( trans )
        if ( not pdbid):
            self.set_state( trans, {
                'status': biobench.jobs.JOB_INIT,
                'input_filesec': {
                    'pdbfile': '',
                    'status': biobench.jobs.JOB_INIT
                }
            })
            self.prepgeneratorcmd.set_default_state( trans )
            self.generatorcmd.set_default_state( trans )
	    self.postgeneratorcmd.set_default_state( trans )
            
    def start_jobs( self, trans ):
        state = self.get_state( trans )
        if (state[ self.generatorcmd.name ]['pdbid']=='False'):
            if (state['input_filesec']['status'] == biobench.jobs.JOB_OK):
                state = self.get_state( trans )
                state_update = {}
                if( state['input_filesec']['status'] == biobench.jobs.JOB_OK and
		    state[ self.prepgeneratorcmd.name ]['status'] == biobench.jobs.JOB_INIT ):
                    state_update = { self.prepgeneratorcmd.name: { 'params': {
                        'data_pdb': state['input_filesec']['pdbfile']
                    }}}
                    self.set_state( trans, state_update )
                    self.prepgeneratorcmd.start( trans )
                state = self.get_state( trans )
                if ( state['input_filesec']['status'] == biobench.jobs.JOB_OK and
                    state[ self.prepgeneratorcmd.name ]['status'] == biobench.jobs.JOB_OK and
                    state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_INIT ):
                    self.set_state( trans, {
                        self.generatorcmd.name: { 'params': {'data_pdb': state[ self.prepgeneratorcmd.name ]['params']['outputdir']+'/in.pdb'} }
                   })
                    self.generatorcmd.start( trans )
                state = self.get_state( trans )
		if ( state['input_filesec']['status'] == biobench.jobs.JOB_OK and
                    state[ self.prepgeneratorcmd.name ]['status'] == biobench.jobs.JOB_OK and
                    state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_OK and
                    state[ self.postgeneratorcmd.name ]['status'] == biobench.jobs.JOB_INIT):
                    self.set_state( trans, {
                        self.postgeneratorcmd.name: { 'params': {
                                                                    'data_pdb': state[ self.prepgeneratorcmd.name ]['params']['outputdir']+'/in.pdb',
                                                                    'outvol': state[ self.generatorcmd.name ]['params']['outputdir']+'/'+state[ self.generatorcmd.name ]['params']['BASE']+'.vol'
                                                                 } }
                   })
                    self.postgeneratorcmd.start( trans )
                state = self.get_state( trans )
                state_update = {}
                
                
                if (state['input_filesec']['status'] == biobench.jobs.JOB_OK and
                    state[ self.prepgeneratorcmd.name ]['status'] == biobench.jobs.JOB_OK and
                    state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_OK and
		    state[ self.postgeneratorcmd.name ]['status'] == biobench.jobs.JOB_OK
                ):
                    state_update['status'] = biobench.jobs.JOB_OK
                elif (state['input_filesec']['status'] == biobench.jobs.JOB_ERROR or
                      state[ self.prepgeneratorcmd.name ]['status'] == biobench.jobs.JOB_ERROR or
                      state[ self.generatorcmd.name ]['status'] == biobench.jobs.JOB_ERROR or
		      state[ self.postgeneratorcmd.name ]['status'] == biobench.jobs.JOB_ERROR
                ):
                    state_update['status'] = biobench.jobs.JOB_ERROR
                else:
                    state_update['status'] = biobench.jobs.JOB_RUNNING
                self.set_state( trans, state_update )
                
            
#    @expose
#    def task_list( self, trans ):
#        return trans.fill_template(
#            'v4rna/task_list.mako', task_list=self.get_task_list( trans )
#        )
    def file_status ( self, trans ):
        state = self.get_state( trans )
        BASE = state[ self.generatorcmd.name ]['params']['BASE']
        outputdir = state[ self.generatorcmd.name ]['params']['outputdir']
	outputdirprovi = state[ self.postgeneratorcmd.name ]['params']['outputdir']
        types = [
                 ['/'+BASE+'.vol', 'volfile'],
		 ['/'+BASE+'.provi', 'provi'],
		 ['/'+BASE+'.vol.extended.vol', 'exvol'],
                 ['/test.log', 'info'],
                 ['/stdout.txt', 'stdout'],
                 ['/stderr.txt', 'stderr']
                 ]
        file_status = {}
	#print "lol"
        for file, name in types:
            if( ( (os.path.isfile(outputdirprovi+file)==True) and (os.stat(outputdirprovi+file)[6]>0) ) or ( (os.path.isfile(outputdir+file)==True) and (os.stat(outputdir+file)[6]>0) ) ):
                file_status[name]=True
		#print "True"
		#print name + outputdir+outputdirprovi
            else:
		file_status[name]=False
		#print "False"
		#print name + outputdir+outputdirprovi
	if file_status['volfile']==True:
	    file_status['provi']=True
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
    def download( self, trans, filename, task_id ):
        state = self.get_state( trans )
        if task_id=='1':
            dict = {}
            output = trans.directory
            dict[ filename ] = os.path.join(output, 'all.zip')
        else:
            BASE = state[ self.generatorcmd.name ]['params']['BASE']
            outputdir = state[ self.generatorcmd.name ]['job_dir']
            types = [
                ['volfile', BASE, 'vol'],
		['exvol', BASE, 'vol.extended.vol'],
                ['info', 'test', 'log'],
                ['stdout', 'stdout', 'txt'],
                ['stderr', 'stderr', 'txt']
            ]
            dict = {}
            for type, name, ext in types:
                dict[ type ] = os.path.join(
                    outputdir, '%s.%s' % (name, ext) )
        trans.response.headers["Content-Disposition"] = \
            "attachment; filename=%s" % ( os.path.basename(dict[filename]) )
            
        return self._get_file( trans, dict[filename] )
        
    @expose
    def download2( self, trans, filename, task_id, codefile ):
        dirlink=trans.app.config.pdb_dataset_link
        state = self.get_state( trans )
        if task_id=='2':
            #zipping
            workdir=trans.directory
            lister=[]
            lister.append(codefile+'.pdb')
            lister.append(codefile+'.pdb.vol')
            lister.append(codefile+'.pdb.vol.extended.vol')
            try:
                compression = zipfile.ZIP_DEFLATED
            except:
                compression = zipfile.ZIP_STORED
            zip = zipfile.ZipFile(workdir+"/"+codefile+".zip", 'w')
            root_len = len(os.path.abspath(dirlink))
            for root, dirs, files in os.walk(dirlink):
                archive_root = os.path.abspath(root)[root_len:]
                fi=len(files)
                for f in files:
                    if ( fi!=0) and f in lister:
                        fullpath = os.path.join(root, f)
                        archive_name = os.path.join(archive_root, f)
                        zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
                        fi=fi-1
            zip.close() 
            dict = {}
            output = trans.directory
            dict[ filename ] = os.path.join(output, codefile+'.zip')
        elif task_id=='1':
            dict = {}
            output = trans.directory
            dict[ filename ] = os.path.join(output, 'all.zip')
        else:
            BASE = state[ self.generatorcmd.name ]['params']['BASE']
            outputdir = state[ self.generatorcmd.name ]['job_dir']
            types = [
                ['volfile', BASE, 'vol'],
                ['info', 'test', 'log'],
                ['stdout', 'stdout', 'txt'],
                ['stderr', 'stderr', 'txt']
            ]
            dict = {}
            for type, name, ext in types:
                dict[ type ] = os.path.join(
                    outputdir, '%s.%s' % (name, ext) )
        trans.response.headers["Content-Disposition"] = \
            "attachment; filename=%s" % ( os.path.basename(dict[filename]) )
            
        return self._get_file( trans, dict[filename] )
        
    @expose
    def old_tasks( self, trans, **kwargs ):
	task_list=self.get_task_list( trans )
	output = trans.directory
	zeit=[]
	for elem in task_list:
		zeit.append((elem, time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(output+'/generator_'+elem+'.js')))))
        return trans.fill_template('v4rna/old_tasks.mako', task_list=self.get_task_list( trans ), zeit=zeit)

class PrepGeneratorCmd( Cmd ):
    name = 'prepgeneratorcmd'
    pdbid = ''
    cmd = 'python /home/webit/app/v4rna/scripts/v4rna/prepfile.py %(data_pdb)s %(BASE)s %(outputdir)s'
    params = {
        'data_pdb': '',
        'outputdir': '%(job_dir)s',
        'BASE': ''
    }

class GeneratorCmd( Cmd ):
    name = 'generatorcmd'
    pdbid = ''
    cmd = 'wine /home/webit/app/v4rna/contrib/get_volume.exe ex:0.1 rad:protor i:%(data_pdb)s ' +\
          'o:%(outputdir)s/%(BASE)s.vol'
    params = {
        'data_pdb': '',
        'outputdir': '%(job_dir)s',
        'BASE': ''
    }
class PostGeneratorCmd( Cmd ):
    name = 'postgeneratorcmd'
    pdbid = ''
    cmd = 'python /home/webit/app/v4rna/scripts/v4rna/upload_prepviewing.py -dir %(outputdir)s -vol %(outvol)s -pdb %(data_pdb)s'
    params = {
        'data_pdb': '',
        'outputdir': '%(job_dir)s',
        'outvol': ''
    }
