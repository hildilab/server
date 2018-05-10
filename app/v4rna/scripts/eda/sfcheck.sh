#!/bin/bash

MTZFILE=$1
PDBFILE=$2
Dirdirect=$3
BA=$4
BASE=$(echo "$BA" | tr '[a-z]' '[A-Z]')
exec 1>>$Dirdirect/log_sfcheck.txt
echo -e "_DOC Y \n_LABIN F=FP SIGF=SIGFP FREE=FREE" | sfcheck HKLIN ""$MTZFILE"" XYZIN ""$PDBFILE"" PATH_SCR ""$Dirdirect"/" PATH_OUT ""$Dirdirect"/"
ps2pdfwr sfcheck_$BASE.ps sfcheck_$BA.pdf
exit