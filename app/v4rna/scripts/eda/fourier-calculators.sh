#!/bin/bash

CIF_FILE=$1
MTZ_FILE=$2
Dirdirect=$3
PDB=$4
BASE=$5
MTZ=$6
exec 1>>$Dirdirect/log_fourier-calculation.txt
List=$(information_out_of_file.py $CIF_FILE $PDB $MTZ $Dirdirect)
symmetry_space_group_name=`echo $List | cut -d'"' -f2`
free_R_flags=`echo $List | cut -d' ' -f7`
if [ "$MTZ" = 'True' ]; then
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FREE=FREE \nlabout - \n  FC=FC PHIC=PHIC \nMODE SFCALC - \n  XYZIN - \n  HKLIN \nsymmetry '"$symmetry_space_group_name"' \nend \n" | sfall HKLIN ""$Dirdirect/$BASE".mtz" HKLOUT ""$Dirdirect/$BASE"_1_fourier.tmp" XYZIN ""$PDB""
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FC=FC PHIC=PHIC \nlabout DELFWT=DELFWT FWT=FWT WCMB=WCMB \nranges 20 - \n    1000 \nsymmetry '"$symmetry_space_group_name"' \npartial - \n  damp 1.0 \nend \n" | sigmaa HKLIN ""$Dirdirect/$BASE"_1_fourier.tmp" HKLOUT ""$Dirdirect/$BASE"_sigmaa1.mtz"
elif [ "$free_R_flags" = 'True' ]; then
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FREE=FREE \nlabout - \n  FC=FC PHIC=PHIC \nMODE SFCALC - \n  XYZIN - \n  HKLIN \nsymmetry '"$symmetry_space_group_name"' \nend \n" | sfall HKLIN ""$Dirdirect/$BASE".mtz" HKLOUT ""$Dirdirect/$BASE"_1_fourier.tmp" XYZIN ""$PDB""
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FC=FC PHIC=PHIC \nlabout DELFWT=DELFWT FWT=FWT WCMB=WCMB \nranges 20 - \n    1000 \nsymmetry '"$symmetry_space_group_name"' \npartial - \n  damp 1.0 \nend \n" | sigmaa HKLIN ""$Dirdirect/$BASE"_1_fourier.tmp" HKLOUT ""$Dirdirect/$BASE"_sigmaa1.mtz" 
elif [ "$free_R_flags" = 'False' ]; then
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FREE=FREE \nlabout - \n  FC=FC PHIC=PHIC \nMODE SFCALC - \n  XYZIN - \n  HKLIN \nsymmetry '"$symmetry_space_group_name"' \nend \n" | sfall HKLIN ""$Dirdirect/$BASE".mtz" HKLOUT ""$Dirdirect/$BASE"_1_fourier.tmp" XYZIN ""$PDB""
    echo -e "title Impoved Fourier coefficients using calculated phases of "$BASE" for Coot \nLABIN  FP=FP SIGFP=SIGFP FC=FC PHIC=PHIC \nlabout DELFWT=DELFWT FWT=FWT WCMB=WCMB \nranges 20 - \n    1000 \nsymmetry '"$symmetry_space_group_name"' \npartial - \n  damp 1.0 \nend \n" | sigmaa HKLIN ""$Dirdirect/$BASE"_1_fourier.tmp" HKLOUT ""$Dirdirect/$BASE"_sigmaa1.mtz" 
else
    echo "Error at fourier calculations" $List> /dev/stderr
fi
exit