#!/bin/bash

FILE=$1
PDB=$2
fofcas=$3
fofcal=$4
tfofcas=$5
tfofcal=$6
omit=$7
sfcheck=$8
mapext=$9
Dirdirect=${10}
BASE=${11}
MTZ=${12}
exec 1>>$Dirdirect/log.txt
bash cif_to_mtz.sh $FILE $Dirdirect $BASE $PDB $MTZ
bash fourier-calculators.sh $FILE $BASE.mtz $Dirdirect $PDB $BASE $MTZ
if [ "$mapext" = "dotccp4" ]; then
    bash run_FFT-create_map.sh $BASE.mtz $Dirdirect $PDB $fofcas $fofcal $tfofcas $tfofcal $BASE
fi
if [ "$mapext" = "dotmap" ]; then
    bash run_FFT-create_map_dotmap.sh $BASE.mtz $Dirdirect $PDB $fofcas $fofcal $tfofcas $tfofcal $BASE
fi
if [ "$sfcheck" = "True" ]; then
    bash sfcheck.sh $Dirdirect/$BASE.mtz $PDB $Dirdirect $BASE
fi
if [ "$omit" = "True" ]; then
    bash omit_map.sh $Dirdirect/$BASE.mtz $PDB $Dirdirect $mapext
fi
exit