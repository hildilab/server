#!/usr/bin/env python
import os
import shutil
import subprocess
import urllib2
from SuffixTree import SubstringDict
import datetime
import argparse
from unipath import Path
today=str(datetime.datetime.now().strftime("%Y-%m-%d"))



def main():
    
    parser = argparse.ArgumentParser(
        description='Update the Dataset of Voronoia4RNA')

    parser.add_argument(
        'project_dir', metavar='project_dir', nargs='*',
        help='the direction of the folder updater and its scripts e.g. /home/usr/downloads/')

    args = parser.parse_args()
    project_dir=Path(args.project_dir)
    
    prepfile=project_dir+'updater/prepfile.py'
    get_volume=project_dir+'updater/get_volume.exe'
    upload_prepviewing=project_dir+'updater/upload_prepviewing.py'
    getPDB=project_dir+'updater/getPDB.py'

    zwischenordner=project_dir+'newfiles'
    splitdir=project_dir+'split_files/'
    newdir=project_dir+'new_files'
    update_mako(project_dir, zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB)



def update_mako(dir, zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB):
    subprocess.call(['scp -r devenv@proteinformatics:/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/v4rna/base.mako ' + dir ], shell=True)
    file=open(dir+'base.mako', 'r')
    outfile=open(dir+'base_temp.mako', 'w')
    date=''
    for line in file:
        if not line.startswith('                updated'):
            outfile.write(line)
        else:
            outfile.write('                updated '+today+'\n')
            date=line.split()[1]
    file.close()
    os.remove(dir+'base.mako')
    outfile.close()
    os.rename(dir+'base_temp.mako', dir+'base.mako')
    subprocess.call(['scp -r '+dir+'base.mako devenv@proteinformatics:/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/v4rna/base.mako' ], shell=True)
    os.remove(dir+'base.mako')
    get_pdblist(zwischenordner, splitdir, newdir, date, prepfile, get_volume, upload_prepviewing, getPDB)


#get filelist
def get_pdblist(zwischenordner, splitdir, newdir, date, prepfile, get_volume, upload_prepviewing, getPDB):
    print 'get pdb list'
    pdb_list=[]
    url = 'http://www.rcsb.org/pdb/rest/search'
    queryText = """
<?xml version="1.0" encoding="UTF-8"?>

<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ChainTypeQuery</queryType>
    <containsProtein>?</containsProtein>
    <containsDna>N</containsDna>
    <containsRna>Y</containsRna>
    <containsHybrid>N</containsHybrid>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ResolutionQuery</queryType>
    <refine.ls_d_res_high.min>0.0</refine.ls_d_res_high.min>
    <refine.ls_d_res_high.max>3.5</refine.ls_d_res_high.max>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>2</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.DepositDateQuery</queryType>
    <database_PDB_rev.date_original.min>"""+date+"""</database_PDB_rev.date_original.min>
    <database_PDB_rev.date_original.max>"""+today+"""</database_PDB_rev.date_original.max>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>
"""
    req = urllib2.Request(url, data=queryText)
    f = urllib2.urlopen(req)
    result = f.read()
    if result:
        for i in result.split():
            pdb_list.append(i)
        queryText2 = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ChainTypeQuery</queryType>
    <containsProtein>?</containsProtein>
    <containsDna>N</containsDna>
    <containsRna>Y</containsRna>
    <containsHybrid>N</containsHybrid>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <mvStructure.expMethod.value>SOLUTION NMR</mvStructure.expMethod.value>
    <mvStructure.hasExperimentalData.value>Y</mvStructure.hasExperimentalData.value>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>2</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.DepositDateQuery</queryType>
    <database_PDB_rev.date_original.comparator>between</database_PDB_rev.date_original.comparator>
    <database_PDB_rev.date_original.min>"""+date+"""</database_PDB_rev.date_original.min>
    <database_PDB_rev.date_original.max>"""+today+"""</database_PDB_rev.date_original.max>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>
"""
        req2 = urllib2.Request(url, data=queryText2)
        f2 = urllib2.urlopen(req2)
        result2 = f2.read()
        if result2:
            for i in result2.split():
                pdb_list.append(i)
        print pdb_list
        file_download(pdb_list, zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB)
    else:
        queryText3 = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ChainTypeQuery</queryType>
    <containsProtein>?</containsProtein>
    <containsDna>N</containsDna>
    <containsRna>Y</containsRna>
    <containsHybrid>N</containsHybrid>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <mvStructure.expMethod.value>SOLUTION NMR</mvStructure.expMethod.value>
    <mvStructure.hasExperimentalData.value>Y</mvStructure.hasExperimentalData.value>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>2</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <queryType>org.pdb.query.simple.DepositDateQuery</queryType>
    <database_PDB_rev.date_original.comparator>between</database_PDB_rev.date_original.comparator>
    <database_PDB_rev.date_original.min>"""+date+"""</database_PDB_rev.date_original.min>
    <database_PDB_rev.date_original.max>"""+today+"""</database_PDB_rev.date_original.max>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>
"""
        req3 = urllib2.Request(url, data=queryText3)
        f3 = urllib2.urlopen(req3)
        result3 = f3.read()
        if result3:
            for i in result3.split():
                pdb_list.append(i)
            print pdb_list
            file_download(pdb_list, zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB)
        else:
            print "No new structures" 



#download files
def file_download(pdb_list, zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB):
    print 'file_download'
    os.mkdir(zwischenordner)
    os.mkdir(splitdir)
    for elem in pdb_list:
        subprocess.call('python '+getPDB+' '+elem+' -o '+zwischenordner+' -f '+elem+'.pdb', shell=True)
    ordnerorganisation(zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB)
    
    
#ordner werden erstellt + splited files gemerged
def ordnerorganisation(zwischenordner, splitdir, newdir, prepfile, get_volume, upload_prepviewing, getPDB):
    print 'ordnerorganisation'
    #splitfiles gesucht
    nichtpassendefiles=[]
    splitpdblist=[]
    splitdic = SubstringDict()
    for dir, subdir, files in os.walk(zwischenordner):
        for file in files:
            actdir=os.path.join(dir, file)
            pdbs=open(actdir, "r")
            for line in pdbs:
                if line.startswith("SPLIT"):
                    
                    splitpdblist.append(line.split()[1])
                    spliti=line.split()
                    firsti=spliti[1]
                    spliti=spliti[2:]
                    for i in spliti:
                        splitdic[firsti]=i
                    nichtpassendefiles.append(dir+'/'+file)
                    break
            pdbs.close()
    splitpdblist=list(set(sorted(splitpdblist)))
    for elem in nichtpassendefiles:
        shutil.move(elem, splitdir+elem[-8:])
    #split mergen
    for elem in splitpdblist:
        newsplit=open(zwischenordner+'/'+elem+'.pdb', 'a')
        oldsplit=open(splitdir+elem+'.pdb', 'r')
        for line in oldsplit:
            if not line.startswith('END') and not line.startswith('MASTER') and not line.startswith('CONECT'):
                newsplit.write(line)
        oldsplit.close()
        os.remove(splitdir+elem+'.pdb')
        splitlist=list(set(sorted(splitdic[elem])))
        for pdb in splitlist:
            oldressplit=open(splitdir+pdb+'.pdb', 'r')
            for line in oldressplit:
                if line.startswith("ATOM") or line.startswith("HETATM"):
                    newsplit.write(line)
            oldressplit.close()
            os.remove(splitdir+pdb+'.pdb')
        newsplit.write('END')
        newsplit.close()
    os.removedirs(splitdir)
    #ordner erstellt
    os.mkdir(newdir)
    for dir, subdir, files in os.walk(zwischenordner):
        for file in files:
            os.mkdir(newdir+'/'+file+'/')
            shutil.move(dir+'/'+file, newdir+'/'+file)
    os.removedirs(zwischenordner)
    ausrechnen(newdir, prepfile, get_volume, upload_prepviewing, getPDB)

def ausrechnen(newdir, prepfile, get_volume, upload_prepviewing, getPDB):
    print 'vol file generation'
    for dir, subdir, files in os.walk(newdir):
        for file in files:
            if file.endswith('.pdb') and not (file.startswith('in.pdb') or file.startswith('in_short.pdb')):
                print file, 'in preparation'
                subprocess.call(['python', prepfile, dir+'/'+file, file, dir], shell=False)
                subprocess.call(['wine', get_volume, 'ex:0.1', 'rad:', 'protor', 'i:'+dir+'/'+'in.pdb', 'o:'+dir+'/'+file+'.vol'], shell=False)
                subprocess.call(['python', upload_prepviewing, '-dir', dir, '-vol', dir+'/'+file+'.vol', '-pdb', dir+'/in.pdb'], shell=False)
                subprocess.call(['mv ' + dir + ' /mnt/bigdisk/voronoia4rna/dataset_voronoia/'], shell=True)
                subprocess.call(['rm -rf '+dir], shell=True)
    os.removedirs(newdir)

if __name__ == "__main__":
    main()
