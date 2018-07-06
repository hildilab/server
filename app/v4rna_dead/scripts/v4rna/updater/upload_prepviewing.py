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
    z_score_all_atNum=0
    for line in infile:
        if (line.startswith('ATOM') or line.startswith('HETATM')):
            m=line.split()
            vdwvol=float(m[-3])  #VOLUME INSIDE VAN-DER-WAALS SPHERE
            sevol=float(m[-2])   #VOLUME IN 1.4 ANGSTROM LAYER OUTSIDE VDW-SPHERE
            if vdwvol==0.0:
                ppdd='0.0'
                print fil, line
            elif (vdwvol+sevol)==0.0:
                ppdd= '999.99'
                print fil, line
            else:
                ppdd="%.3f" % (vdwvol/(vdwvol+sevol))
            if ((line.startswith('ATOM') and (line.endswith('1\r\n') or line.endswith('1\n'))) or (line.startswith('HETATM') and (line.endswith('1\r\n') or line.endswith('1\n')))):
                atom=line[12:16].split()[0]
                residue=line[17:20].split()[0]
                m=line.split()
                vdwvol=m[-3]  #VOLUME INSIDE VAN-DER-WAALS SPHERE
                sevol=m[-2]   #VOLUME IN 1.4 ANGSTROM LAYER OUTSIDE VDW-SPHERE
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
                outfilesec.write('ZSCORE_RMS '+"%.3f" % (math.sqrt(z_score_all/z_score_all_atNum))+'\r\n')
            else: outfilesec.write('ZSCORE_RMS '+"%.3f" % (math.sqrt(z_score_all/0.00001))+'\r\n')
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
                LOG.error( "vdw volume zero. %s" % l )
            elif (vdwvol+sevol)==0.0:
                packdens = 999.99
                LOG.error( "sum of vdw volume and excluded volume zero. %s" % l )
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
