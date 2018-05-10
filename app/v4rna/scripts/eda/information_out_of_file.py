#!/usr/bin/env python

import argparse
import os, re
from unipath import Path
import shutil

"""
This script gets the informations out of the cif file, which are needed
for the convertion.
"""

def main():

    # create the parser
    parser = argparse.ArgumentParser(
        description = __doc__,
    )
    # add the arguments
    parser.add_argument(
        'inputfile', metavar='inputfile',
        help='Input file')
    parser.add_argument(
        'inputpdb', metavar='inputpdb',
        help='Input pdb')
    parser.add_argument(
        'mtz', metavar='mtz')
    parser.add_argument(
        'outputDir', metavar='outputDir',
        help='Output Direction')
    # parse the command line
    args = parser.parse_args()
    inputfile=args.inputfile
    inputpdb=args.inputpdb
    mtz=args.mtz
    outputDir = Path(args.outputDir)
    outputDir.mkdir(True)
    
    cell_length_a=0
    cell_length_b=0
    cell_length_c=0
    cell_angle_alpha=0
    cell_angle_beta=0
    cell_angle_gamma=0
    reflns_d_resolution_high=0
    reflns_d_resolution_low=0
    symmetry_space_group_name=0
    symmetry_Int_Tables_number=0
    free_R_flags='False'
    if (mtz == 'True'):
        copy_inputfile = outputDir + "/input.mtz"
        shutil.copy(inputfile, copy_inputfile)
    else:
        copy_inputfile = outputDir + "/input.cif"
        shutil.copy(inputfile, copy_inputfile)
    copy_inputpdb = outputDir + "/input.pdb"
    shutil.copy(inputpdb, copy_inputpdb)
    
    infile = open(inputfile,"r")
    for line in infile:
        if line.startswith('_cell.length_a'):
            m = re.split(" *", line)
            cell_length_a=m[1]
        elif line.startswith('_cell.length_b'):
            m = re.split(" *", line)
            cell_length_b=m[1]
        elif line.startswith('_cell.length_c'):
            m = re.split(" *", line)
            cell_length_c=m[1]
        elif line.startswith('_cell.angle_alpha'):
            m = re.split(" *", line)
            cell_angle_alpha=m[1]
        elif line.startswith('_cell.angle_beta'):
            m = re.split(" *", line)
            cell_angle_beta=m[1]
        elif line.startswith('_cell.angle_gamma'):
            m = re.split(" *", line)
            cell_angle_gamma=m[1]
        elif line.startswith('_reflns.d_resolution_high'):
            m = re.split(" *", line)
            reflns_d_resolution_high=m[1]
        elif line.startswith('_reflns.d_resolution_low'):
            m = re.split(" *", line)
            reflns_d_resolution_low=m[1]
        elif line.startswith('_symmetry.space_group_name'):
            m = re.split("'", line)
            symmetry_space_group_name=m[1]
        elif line.startswith('_symmetry.Int_Tables_number'):
            m = re.split(" *", line)
            symmetry_Int_Tables_number=m[1]
        elif line.startswith('_refln.status'):
            free_R_flags = 'True'
    infile.close()
    pdb_cell_length_a=0
    pdb_cell_length_b=0
    pdb_cell_length_c=0
    pdb_cell_angle_alpha=0
    pdb_cell_angle_beta=0
    pdb_cell_angle_gamma=0
    pdb_symmetry_space_group_name=0
    pdbID=''
    pdb_reflns_d_resolution_high=0
    pdb_reflns_d_resolution_low=0
    inpdb = open(inputpdb,"r")
    for line in inpdb:
        if line.startswith('REMARK   4'):
            m = re.split(" *", line)
            if m[2]!='\n':
                pdbID=m[2]
        elif line.startswith('REMARK   3   RESOLUTION RANGE HIGH (ANGSTROMS)'):
            m = re.split(" *", line)
            pdb_reflns_d_resolution_high=m[7]
        elif line.startswith('REMARK   3   RESOLUTION RANGE LOW  (ANGSTROMS)'):
            m = re.split(" *", line)
            pdb_reflns_d_resolution_low=m[7]
        elif line.startswith('CRYST1'):
            m = re.split(" *", line)
            pdb_cell_length_a=m[1]
            pdb_cell_length_b=m[2]
            pdb_cell_length_c=m[3]
            pdb_cell_angle_alpha=m[4]
            pdb_cell_angle_beta=m[5]
            pdb_cell_angle_gamma=m[6]
            pdb_symmetry_space_group_name_list=m[7:-2] 
            pdb_symmetry_space_group_name=' '.join(str(n) for n in pdb_symmetry_space_group_name_list)
    inpdb.close()
    
    if cell_length_a != 0:    
        print cell_length_a + cell_length_b + cell_length_c
    else:
        print pdb_cell_length_a  + " " + pdb_cell_length_b  + " " + pdb_cell_length_c
    if cell_angle_alpha != 0:
        print cell_angle_alpha + cell_angle_beta + cell_angle_gamma
    else:
        print pdb_cell_angle_alpha  + " " + pdb_cell_angle_beta  + " " + pdb_cell_angle_gamma
    print free_R_flags
    if reflns_d_resolution_high !=0:
        print reflns_d_resolution_high + " " + reflns_d_resolution_low
    else:
        print pdb_reflns_d_resolution_high + " " + pdb_reflns_d_resolution_low
    print pdbID
    if (symmetry_space_group_name == 0) & (symmetry_Int_Tables_number!=0):
        print '"' + symmetry_Int_Tables_number + '"'
    elif symmetry_space_group_name != 0:
        print '"' + symmetry_space_group_name + '"'
    else:
        print '"' + pdb_symmetry_space_group_name + '"'
    
if __name__ == "__main__":
    main()
os.sys.exit(0)