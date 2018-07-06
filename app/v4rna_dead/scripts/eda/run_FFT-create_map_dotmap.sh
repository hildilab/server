#!/bin/bash

FILE=$1
Dirdirect=$2
PDB=$3
fofcas=$4
fofcal=$5
tfofcas=$6
tfofcal=$7
BASE=$8
#F1-F1 + asym_unit
if [ "$fofcas" = 'True' ]; then
    exec 1>>$Dirdirect/log_run-fft_nf1-as.txt
    echo -e "title fo-fc_asym-unit \nxyzlim asu \nscale F1 1.0 \nscale F2 1.0 \nFREERFLAG 0 \nlabin -\n  F1=FP SIG1=SIGFP F2=FC PHI=PHIC -\n  FREE= FREE \nend \n" | fft HKLIN ""$Dirdirect/$BASE"_sigmaa1.mtz" MAPOUT ""$Dirdirect/"fo-fc_asym-unit_"$BASE".map" #.tmp
fi
#F1-F1 + atoms_pdb
if [ "$fofcal" = 'True' ]; then
    exec 1>>$Dirdirect/log_run-fft_nf1-at.txt
    echo -e "title fo-fc_all-atoms \nscale F1 1.0 \nscale F2 1.0 \nFREERFLAG 0 \nlabin -\n  F1=FP SIG1=SIGFP F2=FC PHI=PHIC -\n  FREE= FREE \nend \n" | fft HKLIN ""$Dirdirect/$BASE"_sigmaa1.mtz" MAPOUT ""$Dirdirect/"fo-fc_all-atoms_"$BASE"_1_.tmp"
    echo -e "BORDER 5\n" | mapmask MAPIN ""$Dirdirect/"fo-fc_all-atoms_"$BASE"_1_.tmp" MAPOUT ""$Dirdirect/"fo-fc_all-atoms_"$BASE".map" XYZIN ""$PDB""
fi
#F2-F1 + asym_unit
if [ "$tfofcas" = 'True' ]; then
    exec 1>>$Dirdirect/log_run-fft_nf2-as.txt
    echo -e "title 2fo-fc_asym-unit \nxyzlim asu \nscale F1 2.0 \nscale F2 1.0 \nFREERFLAG 0 \nlabin -\n  F1=FWT SIG1=SIGFP F2=FWT PHI=PHIC -\n  FREE= FREE \nend \n" | fft HKLIN ""$Dirdirect/$BASE"_sigmaa1.mtz" MAPOUT ""$Dirdirect/"2fo-fc_asym-unit_"$BASE".map" #.tmp
fi
#F2-F1 + atoms_pdb
if [ "$tfofcal" = 'True' ]; then
    exec 1>>$Dirdirect/log_run-fft_nf2-at.txt
    echo -e "title 2fo-fc_all-atoms \nscale F1 2.0 \nscale F2 1.0 \nFREERFLAG 0 \nlabin -\n  F1=FWT SIG1=SIGFP F2=FWT PHI=PHIC -\n  FREE= FREE \nend \n" | fft HKLIN ""$Dirdirect/$BASE"_sigmaa1.mtz" MAPOUT ""$Dirdirect/"2fo-fc_all-atoms_"$BASE"_1_.tmp"
    echo -e "BORDER 5\n" | mapmask MAPIN ""$Dirdirect/"2fo-fc_all-atoms_"$BASE"_1_.tmp" MAPOUT ""$Dirdirect/"2fo-fc_all-atoms_"$BASE".map" XYZIN ""$PDB""
fi
if [ "$fofcas" = 'False' ] && [ "$fofcal" = 'False' ] && [ "$tfofcas" = 'False' ] && [ "$tfofcal" = 'False' ]; then
    exec 1>>$Dirdirect/log_run-fft.txt
    echo "Error at creation of the maps" > /dev/stderr
fi
exit