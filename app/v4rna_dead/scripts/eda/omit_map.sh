#!/bin/bash

MTZFILE=$1
PDBFILE=$2
Dirdirect=$3
mapext=$4
exec 1>>$Dirdirect/log_omit_map.txt
echo -e "_DOC Y \nNOMIT 2 \nMAP Y \nOUT Y \nLABIN F=FP SIGF=SIGFP" | sfcheck HKLIN ""$MTZFILE"" XYZIN ""$PDBFILE"" PATH_SCR ""$Dirdirect"/" PATH_OUT ""$Dirdirect"/"
if [ "$mapext" = "dotccp4" ]; then
    mv sfcheck_ext.map sfcheck_ext.ccp4
fi
exit