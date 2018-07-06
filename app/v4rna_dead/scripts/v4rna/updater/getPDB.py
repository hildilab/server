#!/usr/bin/env python

from unipath import Path
import os, logging, argparse, sys
import warnings
from urllib2 import Request, urlopen


def download_pdb(pdbId):
    pdb_download_urls = ["http://198.202.122.52/pdb/files/","http://198.202.122.51/pdb/files/","http://www.rcsb.org/pdb/files/"]
    
    for pdb_url in pdb_download_urls:
        try:
            url = "%s%s.pdb" % (pdb_url, pdbId)
            req = Request(url)
            response = urlopen(req)
            return response.read()
        except:
            pass
    raise Exception('No pdb download connection available.')


def main():
    warnings.simplefilter('ignore', Warning)

    parser = argparse.ArgumentParser(
        description='Download PDB files')

    parser.add_argument(
        'pdbIds', metavar='pdbId', nargs='*',
        help='a PDB ID to be downloaded')
    parser.add_argument(
        '-i', '--inputFile',
        help='one pdb id per line')
    parser.add_argument(
        '-o', '--outputDir', default=Path(os.getcwd()),
        help='the directory where the PDB files are downloaded to '
             '(default: current directory)')
    parser.add_argument(
        '-f', '--outputFilenameTemplate', default='{pdbId}.pdb',
        help='a template string used to name the output file; the string {pdbId} gets replaced with the actual pdb id '
             '(default: {pdbId}.pdb)')
    parser.add_argument(
        '-e', '--errorFile',
        help='error file name')

    args = parser.parse_args()
    
    pdbIdList = []
    if args.pdbIds:
        pdbIdList = args.pdbIds
    if args.inputFile:
        for pdbId in open(args.inputFile):
            try:
                pdbId = pdbId.strip()[0:4]
            except IndexError:
                pass
            else:
                pdbIdList.append(pdbId.strip())
    
    pdbIdList = [pdbId.lower() for pdbId in pdbIdList]
    
    pdbIdList = list(set(pdbIdList))
    
    outputDir = Path(args.outputDir)
    outputDir.mkdir(True)
    
    if args.errorFile:
        try:
            errorFile = open(args.errorFile, 'w')
        except:
            errorFile = None
    else:
        errorFile = None
    error = None
    error_list = []
    for pdbId in pdbIdList:
        try:
            filename = Path(outputDir, args.outputFilenameTemplate.replace('{pdbId}', pdbId))
            lines = download_pdb(pdbId)
            open(filename,'wb').write(lines)
        except Exception, e:
            error = 'Exception: %s\n' % (e)
            error_list.append( error )
            if error:
                if errorFile:
                    errorFile.write(error)
                    errorFile.flush()
    Path(outputDir, 'obsolete').rmdir()
    if error_list and not errorFile:
        logging.error( error_list )
    sys.exit(0)


if __name__ == "__main__":
    main()