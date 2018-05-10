#!/usr/bin/env python

import os
from unipath import Path
import argparse

def main():
    
    parser = argparse.ArgumentParser(
        description = __doc__,
    )
    parser.add_argument(
        'inputfile', metavar='inputfile',
        help='Input file')
    parser.add_argument(
        'base', metavar='base',
        help='basename')
    parser.add_argument(
        'outputDir', metavar='outputDir',
        help='Output Direction')
    # parse the command line
    args = parser.parse_args()
    inputfile=args.inputfile
    base=args.base
    outputDir = Path(args.outputDir)
    outputDir.mkdir(True)
    

    manipulate_pdb(inputfile, base, outputDir)
    



def manipulate_pdb(fil, base, pfad):
    
    infile = open(fil,"r")
    outfile = file(pfad+'/in.pdb', "w")
    for line in infile:
        if (line.startswith('ATOM') or line.startswith('HETATM')):
            if line[16]=='A':
                li= line[:16]+' '+line[17:]
                outfile.write(li)
            elif line[16]==' ':
                outfile.write(line)
        else:
            outfile.write(line)
    infile.close()


if __name__ == "__main__":
    main()
    