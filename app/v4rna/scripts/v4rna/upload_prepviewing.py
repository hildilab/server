#! /usr/bin/env python
from __future__ import division
import os, re
from unipath import Path
import shutil
import tempfile, argparse
import shlex, subprocess
from array import array
import logging, sys
from time import *
from SuffixTree import SubstringDict
from collections import defaultdict
import math
import os.path
import simplejson

logging.basicConfig()
LOG = logging.getLogger('prep')
LOG.setLevel( logging.ERROR )


def main():
    # create the parser
    parser = argparse.ArgumentParser(
        description = __doc__,
    )
    # add the arguments
    parser.add_argument('-dir', help='output directory')
    parser.add_argument('-pdb', help='pdb file')
    parser.add_argument('-vol', help='volume file')
    # parse the command line
    args = parser.parse_args()
    dirlink = Path(args.dir)
    volfile=args.vol
    pdbfile=args.pdb
    
    #packing density + extended_vol_file:
    packing_density_file(dirlink, volfile)
    #calculate files for provi
    alex_script(dirlink, volfile, pdbfile)
    # make .provi file
    provi_file(dirlink, volfile, pdbfile)
    

    







    
    
#packing density + extended_vol_file
def packing_density_file(dirlink, volfile):
    fil= volfile
    infile = open(fil,"r")
    outfile = file(fil+'.extended_temp.vol', "w")
    z_score_all=0
    z_score_all_protein=0
    z_score_all_atNum=0
    z_score_all_atNum_protein=0
    for line in infile:
        if (line.startswith('ATOM') or line.startswith('HETATM')):
            m=line.split()
            vdwvol=float(m[-3])  #VOLUME INSIDE VAN-DER-WAALS SPHERE
            sevol=float(m[-2])   #VOLUME IN 1.4 ANGSTROM LAYER OUTSIDE VDW-SPHERE
            if vdwvol==0.0:
                ppdd='0.0'
               # print fil, line
            elif (vdwvol+sevol)==0.0:
                ppdd= '999.99'
                #print fil, line
            else:
                ppdd="%.3f" % (vdwvol/(vdwvol+sevol))
            if ((line.startswith('ATOM') and (line.endswith('1\r\n') or line.endswith('1\n'))) or (line.startswith('HETATM') and (line.endswith('1\r\n') or line.endswith('1\n')))):
                atom=line[12:16].split()[0]
                residue=line[17:20].split()[0]
                m=line.split()
                vdwvol=m[-3]  #VOLUME INSIDE VAN-DER-WAALS SPHERE
                sevol=m[-2]   #VOLUME IN 1.4 ANGSTROM LAYER OUTSIDE VDW-SPHERE
               # print vdwvol, sevol
                if float(vdwvol)==0.0:
                    zscore_per_atom_str=""
                elif (float(vdwvol)+float(sevol))==0.0:
                    zscore_per_atom_str=""
                else:
                    density=(float(vdwvol)/(float(vdwvol)+float(sevol)))
                    if residue in ['G', 'C', 'A', 'U']:
                        protordic={"G":{"C1*":"C4H1b","C3*":"C4H1s","O6":"O1H0u","C5*":"C4H2s","O4*":"O2H0s","O1P":"O1H0u","C8":"C3H1s","O2*":"O2H1u","C2":"C3H0s","C6":"C3H0s","C5":"C3H0s","C4":"C3H0s","O2P":"O1H0u","P":"P4H0u","C2*":"C4H1s","N1":"N3H1s","N2":"N3H2u","N3":"N2H0b","C4*":"C4H1b","N7":"N2H0b","O5*":"O2H0b","N9":"N3H0u","O3*":"O2H0b"},"A":{"C1*":"C4H1b","C3*":"C4H1s","C5*":"C4H2s","O4*":"O2H0s","O1P":"O1H0u","C8":"C3H1s","O2*":"O2H1u","N6":"N3H2u","C2":"C3H1s","C6":"C3H0s","C5":"C3H0s","C4":"C3H0s","O2P":"O1H0u","P":"P4H0u","C2*":"C4H1s","N1":"N2H0s","N3":"N2H0b","C4*":"C4H1b","N7":"N2H0b","O5*":"O2H0b","N9":"N3H0u","O3*":"O2H0b"},"C":{"C5*":"C4H2s","C1*":"C4H1b","O4*":"O2H0s","C3*":"C4H1s","O5*":"O2H0b","O1P":"O1H0u","O2P":"O1H0u","C6":"C3H1t","P":"P4H0u","O3*":"O2H0b","O2*":"O2H1u","C4*":"C4H1b","C2":"C3H0s","C2*":"C4H1s","N1":"N3H0u","N3":"N2H0s","N4":"N3H2u","O2":"O1H0u","C5":"C3H1b","C4":"C3H0s"},"U":{"C5*":"C4H2s","C1*":"C4H1b","O4*":"O2H0s","N3":"N3H1s","C3*":"C4H1s","O5*":"O2H0b","O1P":"O1H0u","O2P":"O1H0u","C6":"C3H1t","P":"P4H0u","O3*":"O2H0b","O2*":"O2H1u","C4*":"C4H1b","C2":"C3H0s","C2*":"C4H1s","N1":"N3H0u","O4":"O1H0u","O2":"O1H0u","C5":"C3H1b","C4":"C3H0s"},"T":{"C5*":"C4H2s","C1*":"C4H1b","O4*":"O2H0s","N3":"N3H1s","C3*":"C4H1s","O5*":"O2H0b","O1P":"O1H0u","O2P":"O1H0u","C6":"C3H1t","P":"P4H0u","O3*":"O2H0b","O2*":"O2H1u","C4*":"C4H1b","C2":"C3H0s","C2*":"C4H1s","N1":"N3H0u","O4":"O1H0u","C7":"C4H3u","O2":"O1H0u","C5":"C3H0b","C4":"C3H0s"}}
                        ref_packing={"G":{"C4H1b":"0.748","C4H1s":"0.805","O1H0u":"0.567","C4H2s":"0.673","O2H0s":"0.699","C3H1s":"0.672","O2H1u":"0.572","C3H0s":"0.829","P4H0u":"0.807","N3H1s":"0.765","N3H2u":"0.620","N2H0b":"0.664","O2H0b":"0.702","N3H0u":"0.854"},"A":{"C4H1b":"0.754","C4H1s":"0.805","C4H2s":"0.669","O2H0s":"0.689","O1H0u":"0.559","C3H1s":"0.673","O2H1u":"0.569","N3H2u":"0.613","C3H0s":"0.833","P4H0u":"0.808","N2H0s":"0.744","N2H0b":"0.662","O2H0b":"0.703","N3H0u":"0.853"},"C":{"C4H2s":"0.667","C4H1b":"0.740","O2H0s":"0.693","C4H1s":"0.808","O2H0b":"0.701","O1H0u":"0.567","C3H1t":"0.707","P4H0u":"0.806","O2H1u":"0.573","C3H0s":"0.831","N3H0u":"0.849","N2H0s":"0.762","N3H2u":"0.603","C3H1b":"0.635"},"U":{"C4H2s":"0.676","C4H1b":"0.750","O2H0s":"0.689","N3H1s":"0.736","C4H1s":"0.801","O2H0b":"0.700","O1H0u":"0.550","C3H1t":"0.708","P4H0u":"0.813","O2H1u":"0.579","C3H0s":"0.809","N3H0u":"0.845","C3H1b":"0.631"}}
                        ref_deviation={"G":{"C4H1b":"0.090","C4H1s":"0.087","O1H0u":"0.083","C4H2s":"0.087","O2H0s":"0.089","C3H1s":"0.091","O2H1u":"0.089","C3H0s":"0.092","P4H0u":"0.089","N3H1s":"0.084","N3H2u":"0.084","N2H0b":"0.087","O2H0b":"0.088","N3H0u":"0.085"},"A":{"C4H1b":"0.074","C4H1s":"0.065","C4H2s":"0.064","O2H0s":"0.064","O1H0u":"0.064","C3H1s":"0.076","O2H1u":"0.086","N3H2u":"0.060","C3H0s":"0.000","P4H0u":"0.086","N2H0s":"0.064","N2H0b":"0.064","O2H0b":"0.063","N3H0u":"0.060"},"C":{"C4H2s":"0.073","C4H1b":"0.077","O2H0s":"0.083","C4H1s":"0.073","O2H0b":"0.083","O1H0u":"0.069","C3H1t":"0.078","P4H0u":"0.083","O2H1u":"0.083","C3H0s":"0.078","N3H0u":"0.068","N2H0s":"0.070","N3H2u":"0.068","C3H1b":"0.079"},"U":{"C4H2s":"0.087","C4H1b":"0.088","O2H0s":"0.089","N3H1s":"0.08","C4H1s":"0.087","O2H0b":"0.089","O1H0u":"0.087","C3H1t":"0.089","P4H0u":"0.089","O2H1u":"0.090","C3H0s":"0.088","N3H0u":"0.086","C3H1b":"0.089"}}
                        if atom=='OP1':atom='O1P'
                        if atom=='OP2':atom='O2P'
                        if atom=='OP3':atom='O2P'
                        for elem in atom:
                            if elem=='\'': atom=atom.replace("\'", "*")
                        reffi=float(ref_deviation[residue][protordic[residue][atom]])
                        if reffi==0.0:
                            zscore_per_atom_str=""
                        else:
                            zscore_per_atom=((density-float(ref_packing[residue][protordic[residue][atom]]))/float(ref_deviation[residue][protordic[residue][atom]]))**2
                            z_score_all=z_score_all+zscore_per_atom
                            zscore_per_atom_str="%.3f" % zscore_per_atom
                            z_score_all_atNum=z_score_all_atNum+1
                    elif residue in ["ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY","HIS","ILE","LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"]:
                        ref_packing_protein={"ALA":{"C":"0.810","CA":"0.756","CB":"0.582","N":"0.754","O":"0.606"},"ARG":{"C":"0.820","CA":"0.775","CB":"0.664","CD":"0.674","CG":"0.660","CZ":"0.778","N":"0.763","NE":"0.696","NH1":"0.616","NH2":"0.601","O":"0.610"},"ASN":{"C":"0.813","CA":"0.779","CB":"0.666","CG":"0.777","N":"0.754","ND2":"0.604","O":"0.612","OD1":"0.587"},"ASP":{"C":"0.816","CA":"0.775","CB":"0.656","CG":"0.742","N":"0.747","O":"0.614","OD1":"0.616","OD2":"0.602"},"CYS":{"C":"0.812","CA":"0.774","CB":"0.661","N":"0.747","O":"0.601","SG":"0.592"},"GLN":{"C":"0.820","CA":"0.776","CB":"0.663","CD":"0.774","CG":"0.664","N":"0.769","NE2":"0.602","O":"0.616","OE1":"0.569"},"GLU":{"C":"0.822","CA":"0.775","CB":"0.659","CD":"0.738","CG":"0.653","N":"0.766","O":"0.612","OE1":"0.597","OE2":"0.590"},"GLY":{"C":"0.781","CA":"0.660","N":"0.728","O":"0.598"},"HIS":{"C":"0.819","CA":"0.779","CB":"0.660","CD2":"0.633","CE1":"0.629","CG":"0.849","N":"0.758","ND1":"0.681","NE2":"0.677","O":"0.606"},"ILE":{"C":"0.842","CA":"0.791","CB":"0.754","CD1":"0.571","CG1":"0.651","CG2":"0.588","N":"0.762","O":"0.611"},"LEU":{"C":"0.819","CA":"0.786","CB":"0.659","CD1":"0.572","CD2":"0.571","CG":"0.738","N":"0.763","O":"0.613"},"LYS":{"C":"0.819","CA":"0.777","CB":"0.658","CD":"0.645","CE":"0.653","CG":"0.665","N":"0.761","NZ":"0.643","O":"0.612"},"MET":{"C":"0.819","CA":"0.778","CB":"0.662","CE":"0.597","CG":"0.664","N":"0.765","O":"0.609","SD":"0.606"},"PHE":{"C":"0.823","CA":"0.777","CB":"0.657","CD1":"0.634","CD2":"0.624","CE1":"0.606","CE2":"0.603","CG":"0.861","CZ":"0.605","N":"0.759","O":"0.605"},"PRO":{"C":"0.815","CA":"0.767","CB":"0.632","CD":"0.678","CG":"0.632","N":"0.853","O":"0.603"},"SER":{"C":"0.809","CA":"0.768","CB":"0.642","N":"0.739","O":"0.608","OG":"0.595"},"THR":{"C":"0.824","CA":"0.782","CB":"0.730","CG2":"0.584","N":"0.752","O":"0.611","OG1":"0.596"},"TRP":{"C":"0.828","CA":"0.775","CB":"0.658","CD1":"0.627","CD2":"0.788","CE2":"0.807","CE3":"0.638","CG":"0.839","CH2":"0.612","CZ2":"0.618","CZ3":"0.608","N":"0.758","NE1":"0.649","O":"0.611"},"TYR":{"C":"0.824","CA":"0.779","CB":"0.657","CD1":"0.637","CD2":"0.631","CE1":"0.620","CE2":"0.619","CG":"0.860","CZ":"0.787","N":"0.761","O":"0.606","OH":"0.572"},"VAL":{"C":"0.835","CA":"0.787","CB":"0.735","CG1":"0.585","CG2":"0.586","N":"0.757","O":"0.609"}}
                        ref_deviation_protein={"ALA":{"C":"0.046","CA":"0.053","CB":"0.049","N":"0.058","O":"0.058"},"ARG":{"C":"0.050","CA":"0.051","CB":"0.049","CD":"0.055","CG":"0.053","CZ":"0.057","N":"0.053","NE":"0.063","NH1":"0.062","NH2":"0.065","O":"0.060"},"ASN":{"C":"0.050","CA":"0.050","CB":"0.051","CG":"0.053","N":"0.055","ND2":"0.066","O":"0.059","OD1":"0.074"},"ASP":{"C":"0.047","CA":"0.051","CB":"0.055","CG":"0.055","N":"0.056","O":"0.061","OD1":"0.075","OD2":"0.075"},"CYS":{"C":"0.049","CA":"0.052","CB":"0.051","N":"0.055","O":"0.058","SG":"0.067"},"GLN":{"C":"0.049","CA":"0.049","CB":"0.052","CD":"0.053","CG":"0.051","N":"0.052","NE2":"0.058","O":"0.062","OE1":"0.072"},"GLU":{"C":"0.047","CA":"0.049","CB":"0.051","CD":"0.057","CG":"0.053","N":"0.052","O":"0.058","OE1":"0.074","OE2":"0.080"},"GLY":{"C":"0.056","CA":"0.052","N":"0.058","O":"0.060"},"HIS":{"C":"0.052","CA":"0.050","CB":"0.053","CD2":"0.062","CE1":"0.062","CG":"0.044","N":"0.056","ND1":"0.077","NE2":"0.090","O":"0.058"},"ILE":{"C":"0.049","CA":"0.051","CB":"0.052","CD1":"0.053","CG1":"0.055","CG2":"0.049","N":"0.048","O":"0.057"},"LEU":{"C":"0.049","CA":"0.045","CB":"0.048","CD1":"0.050","CD2":"0.051","CG":"0.058","N":"0.052","O":"0.060"},"LYS":{"C":"0.049","CA":"0.052","CB":"0.051","CD":"0.055","CE":"0.060","CG":"0.051","N":"0.053","NZ":"0.079","O":"0.060"},"MET":{"C":"0.050","CA":"0.050","CB":"0.053","CE":"0.053","CG":"0.053","N":"0.053","O":"0.060","SD":"0.058"},"PHE":{"C":"0.058","CA":"0.048","CB":"0.051","CD1":"0.054","CD2":"0.055","CE1":"0.059","CE2":"0.058","CG":"0.039","CZ":"0.060","N":"0.055","O":"0.057"},"PRO":{"C":"0.042","CA":"0.055","CB":"0.055","CD":"0.051","CG":"0.055","N":"0.043","O":"0.064"},"SER":{"C":"0.048","CA":"0.053","CB":"0.053","N":"0.055","O":"0.061","OG":"0.069"},"THR":{"C":"0.051","CA":"0.052","CB":"0.054","CG2":"0.057","N":"0.052","O":"0.061","OG1":"0.075"},"TRP":{"C":"0.055","CA":"0.047","CB":"0.047","CD1":"0.054","CD2":"0.051","CE2":"0.057","CE3":"0.057","CG":"0.043","CH2":"0.058","CZ2":"0.054","CZ3":"0.058","N":"0.056","NE1":"0.060","O":"0.061"},"TYR":{"C":"0.058","CA":"0.048","CB":"0.050","CD1":"0.054","CD2":"0.054","CE1":"0.056","CE2":"0.057","CG":"0.040","CZ":"0.056","N":"0.054","O":"0.058","OH":"0.058"},"VAL":{"C":"0.050","CA":"0.050","CB":"0.057","CG1":"0.052","CG2":"0.051","N":"0.048","O":"0.057"}}
                        if ref_packing_protein[residue].has_key(atom):
                            for elem in atom:
                                if elem=='\'': atom=atom.replace("\'", "*")
                            reffi=float(ref_deviation_protein[residue][atom])
                            if reffi==0.0:
                                zscore_per_atom_str=""
                            else:
                                zscore_per_atom_protein=((density-float(ref_packing_protein[residue][atom]))/float(ref_deviation_protein[residue][atom]))**2
                                z_score_all_protein=z_score_all_protein+zscore_per_atom_protein
                                zscore_per_atom_str="%.3f" % zscore_per_atom_protein
                                z_score_all_atNum_protein=z_score_all_atNum_protein+1
                        else: zscore_per_atom_str=""
                    else: zscore_per_atom_str=""
            else: zscore_per_atom_str=""
            newline=line[:82]+' '+ppdd+' '+zscore_per_atom_str+'\r\n'
            outfile.write(newline)
        else:
            outfile.write(line)
    infile.close()
    outfile.close()
    infilesec=open(fil+'.extended_temp.vol',"r")
    outfilesec=file(fil+'.extended.vol', "w")
    
    for line in infilesec:
        if line.startswith('RESOLT') :
            outfilesec.write(line)
            if z_score_all_atNum!=0:
                outfilesec.write('ZSCORE_RMS_RNA '+"%.3f" % (math.sqrt(z_score_all/z_score_all_atNum))+'\r\n')
                if z_score_all_atNum_protein!=0:
                    outfilesec.write('ZSCORE_RMS_ALL '+"%.3f" % (math.sqrt(z_score_all_protein+z_score_all/z_score_all_atNum_protein+z_score_all_atNum))+'\r\n')
                else: outfilesec.write('ZSCORE_RMS_ALL '+"%.3f" % (math.sqrt(z_score_all/z_score_all_atNum))+'\r\n')
            else: outfilesec.write('ZSCORE_RMS '+"%.3f" % (math.sqrt(z_score_all/0.00001))+'\r\n')
            if z_score_all_atNum_protein!=0:
                outfilesec.write('ZSCORE_RMS_PROTEIN '+"%.3f" % (math.sqrt(z_score_all_protein/z_score_all_atNum_protein))+'\r\n')
                if z_score_all_atNum!=0:
                    outfilesec.write('ZSCORE_RMS_ALL '+"%.3f" % (math.sqrt(z_score_all_protein+z_score_all/z_score_all_atNum_protein+z_score_all_atNum))+'\r\n')
                else: outfilesec.write('ZSCORE_RMS_ALL '+"%.3f" % (math.sqrt(z_score_all_protein/z_score_all_atNum_protein))+'\r\n')
            else: outfilesec.write('ZSCORE_RMS_PROTEIN '+"%.3f" % (math.sqrt(z_score_all_protein/0.00001))+'\r\n')
        else: outfilesec.write(line)
    infilesec.close()
    os.remove(fil+'.extended_temp.vol')

#calculate files for provi
def alex_script(dirlink, volfile, pdbfile):    
    
    prep_pdb( pdbfile )
    prep_volume( volfile, pdbfile )

# calculate files for provi
def memoize(f):
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

@memoize
def get_pdb_coord_dict(pdb_file):
    pdb_fp = open(pdb_file)
    coord_dict = {}
    i = 1
    for l in pdb_fp:
        if l.startswith('ATOM') or l.startswith('HETATM'):
            key = ( float(l[30:38]), float(l[38:46]), float(l[46:54]) )
            if key in coord_dict:
                LOG.error( "coords already in dict. %s" % str(key) )
            else:
                coord_dict[ key ] = i
                i += 1
    pdb_fp.close()
    return coord_dict

@memoize
def get_pdb_index_dict(pdb_file):
    pdb_fp = open(pdb_file)
    index_dict = {}
    i = 1
    for l in pdb_fp:
        if l.startswith('ATOM') or l.startswith('HETATM'):
            index_dict[ i ] = l
            i += 1
    pdb_fp.close()
    return index_dict

def prep_volume(vol_file, pdb_file):
    vol_fp = open(vol_file)
    name, ext = os.path.splitext(vol_file)
    holes_out_fp = open( "%s.atmsele" % (vol_file), "w")
    prop_out_fp = open( "%s.atmprop" % (vol_file), "w")

    pdb_coord_dict = get_pdb_coord_dict(pdb_file)
    pdb_index_dict = get_pdb_index_dict(pdb_file)
    vol_index_dict = {}

    vol_lines = [None] * len(pdb_coord_dict)
    hole_lines = []
    
    i = 1
    for l in vol_fp:
        if l.startswith('ATOM') or l.startswith('HETATM'):
            key = ( float(l[30:38]), float(l[38:46]), float(l[46:54]) )
            if key in pdb_coord_dict:
                j = pdb_coord_dict[key]
                vol_lines[ j-1 ] = l
                vol_index_dict[ i ] = j
                i += 1
            else:
                LOG.error( "vol coords not in pdb coords dict. %s" % str(key) )
        elif l.startswith('HOLE NUMBER'):
            hole_lines.append( l )

    if len(pdb_coord_dict) != len(vol_index_dict):
        LOG.warning( "number of atoms in vol and pdb coord dicts differs." )

    for l in hole_lines:
        ls = l[12:].split()
        neighbours = []
        for nb in ls[1:]:
            nb = int(nb)
            if nb in vol_index_dict:
                neighbours.append( vol_index_dict[nb] )
            else:
                LOG.error( "hole neighbour index not found. %s" % nb )
        neighbours.sort()
        # zero based atomindex
        neighbours = " ".join([ str(nb-1) for nb in neighbours ])
        holes_out_fp.write( "HOLE_NUMBER_%s %s\n" % (ls[0], neighbours) )

    prop_out_fp.write('volume_vdw#-1 volume_vdw_1_4#-1 buried_flag#-1 packing_density#-1\n')
    for i, l in enumerate(vol_lines):
        if l:
            ls = l.split()
            vdwvol = float(ls[-3])  #VOLUME INSIDE VAN-DER-WAALS SPHERE
            sevol = float(ls[-2])   #VOLUME IN 1.4 ANGSTROM LAYER OUTSIDE VDW-SPHERE
            if vdwvol==0.0:
                packdens = 0.0
  #              LOG.error( "vdw volume zero. %s" % l )
            elif (vdwvol+sevol)==0.0:
                packdens = 999.99
   #             LOG.error( "sum of vdw volume and excluded volume zero. %s" % l )
            else:
                packdens = (vdwvol/(vdwvol+sevol))
            out_line = '%s %.2f\n' % (l[67:82], packdens)
        else:
            out_line = '-1 -1 -1 -1\n'
            LOG.warning( "no volume data for line: %s" % pdb_index_dict[ i+1 ].strip('\n') )
        prop_out_fp.write( out_line )

    vol_fp.close()
    prop_out_fp.close()
    holes_out_fp.close()

def prep_pdb(pdb_file):
    pdb_fp = open(pdb_file)
    name, ext = os.path.splitext(pdb_file)
    pdb_out_fp = open( "%s_short%s" % (name, ext), "w")
    
    for line in pdb_fp:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            pdb_out_fp.write( line[:54]+'\n' )

    pdb_fp.close()
    pdb_out_fp.close()

# make .provi file
def provi_file(dirlink, volfile, pdbfile ):
    pdb = volfile
    vol = volfile+'.extended.vol'
    arg = volfile.split('/')[-1]
    arg = arg[0:-4]
    foo=[
            {
                    "dir":"voronoia",
                    "filename":pdbfile,
                    "type":"pdb",
                    "applet":"default"
            },
            {
                    "dir":"voronoia",
                    "filename":volfile+'.atmsele',
                    "type":"atmsele",
                    "applet":0,
                    "when":0
            },
            {
                    "dir":"voronoia",
                    "filename":volfile+'.atmprop',
                    "type":"atmprop",
                    "applet":0,
                    "when":0
            },
            {
                    "type":"function",
                    "funcname":"Provi.Bio.Voronoia.register",
                    "when":1,
                    "params":{
                            "holes_ds":"DATASET_1"
                    }
            },
            {
                    "type":"widget",
                    "widgetname":"Provi.Bio.AtomSelection.GridWidget",
                    "applet":0,
                    "when":1,
                    "params":{
                            "type": "voronoia",
                            "heading":"Cavities",
                            "hide_eids":["filter", "sort", "type", "property"],
                            "parent_id":"tab_widgets"
                    }
            },
            {
                    "type":"widget",
                    "widgetname":"Provi.Bio.AtomProperty.AtomPropertyGroupWidget",
                    "applet":0,
                    "when":2,
                    "params":{
                            "heading":"Packing",
                            "dataset": "DATASET_2",
                            "filter_properties":["packing_density", "z_score"],
                            "parent_id":"tab_widgets",
                            "colorize_on_init": True
                    }
            }
    ]
    jsondump=simplejson.dumps(foo,indent=4,sort_keys=True)
    f=open(dirlink+"/"+arg+".provi",'w')
    f.write(jsondump)
    f.close()



if __name__ == "__main__":
    main()
