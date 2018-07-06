#!/bin/bash

FILE=$1
Dirdirect=$2
BASE=$3
PDBFILE=$4
MTZ=$5
exec 1>>$Dirdirect/log_cif-to-mtz.txt
List=$(information_out_of_file.py $FILE $PDBFILE $MTZ $Dirdirect)
cell_length_a=`echo $List | cut -d' ' -f1`
cell_length_b=`echo $List | cut -d' ' -f2`
cell_length_c=`echo $List | cut -d' ' -f3`
cell_angle_alpha=`echo $List | cut -d' ' -f4`
cell_angle_beta=`echo $List | cut -d' ' -f5`
cell_angle_gamma=`echo $List | cut -d' ' -f6`
free_R_flags=`echo $List | cut -d' ' -f7`
reflns_d_resolution_high=`echo $List | cut -d' ' -f8`
reflns_d_resolution_low=`echo $List | cut -d' ' -f9`
pdb_id=`echo $List | cut -d' ' -f10`
symmetry_space_group_name=`echo $List | cut -d'"' -f2`
if [ "$free_R_flags" = 'True' ]; then
    if [ "$MTZ" = "True" ]; then
        mv $Dirdirect/'input.mtz' $Dirdirect/$BASE"_1_mtz.tmp"
    elif [ "$MTZ" = "False" ]; then
        echo -e "title Convert "$FILE" into "$BASE".mtz \nsymmetry '"$symmetry_space_group_name"' \ncell "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nPNAME "$BASE"_project \nDNAME "$BASE"_dataset \nXNAME "$BASE"_crystal \nend \n" | cif2mtz HKLIN ""$FILE"" HKLOUT ""$Dirdirect/$BASE"_1_mtz.tmp"
    else
        echo "Error at convertion of cif to mtz" $List > /dev/stderr
    fi
    echo -e "NREF 0 \nSYMMETRY \nend \n" | mtzdump HKLIN ""$Dirdirect/$BASE"_1_mtz.tmp"
    if [ "$reflns_d_resolution_high" != 0 ]; then
        echo -e "CELL "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nSYMMETRY '"$symmetry_space_group_name"' \nLABOUT F=FUNI SIGF=SIGFUNI \nRESOLUTION "$reflns_d_resolution_low" \nend \n" | unique HKLOUT ""$Dirdirect/$BASE"_3_mtz.tmp"
        echo -e "LABIN FILE 1  ALLIN \nLABIN FILE 2  ALLIN \nRESOLUTION OVERALL "$reflns_d_resolution_high" "$reflns_d_resolution_low" \nend \n" | cad HKLIN2 ""$Dirdirect/$BASE"_3_mtz.tmp" HKLIN1 ""$Dirdirect/$BASE"_1_mtz.tmp" HKLOUT ""$Dirdirect/$BASE"_4_mtz.tmp"
    else
        echo -e "CELL "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nSYMMETRY '"$symmetry_space_group_name"' \nLABOUT F=FUNI SIGF=SIGFUNI \nend \n" | unique HKLOUT ""$Dirdirect/$BASE"_3_mtz.tmp"
        echo -e "LABIN FILE 1  ALLIN \nLABIN FILE 2  ALLIN \nend \n" | cad HKLIN2 ""$Dirdirect/$BASE"_3_mtz.tmp" HKLIN1 ""$Dirdirect/$BASE"_1_mtz.tmp" HKLOUT ""$Dirdirect/$BASE"_4_mtz.tmp"
    fi
    echo -e "COMPLETE FREE=FREE \nend \n" | freerflag HKLIN ""$Dirdirect/$BASE"_4_mtz.tmp"  HKLOUT ""$Dirdirect/$BASE"_5_mtz.tmp"
    echo -e "EXCLUDE FUNI SIGFUNI \nEND \n" | mtzutils HKLIN ""$Dirdirect/$BASE"_5_mtz.tmp" HKLOUT ""$Dirdirect/$BASE".mtz"
elif [ "$free_R_flags" = 'False' ]; then
    if [ "$MTZ" = "True" ]; then
        mv $Dirdirect/'input.mtz' $Dirdirect/$BASE"_1_mtz.tmp"
    elif [ "$MTZ" = "False" ]; then
        echo -e "title Convert "$BASE".cif into "$BASE".mtz \nsymmetry '"$symmetry_space_group_name"' \ncell "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nPNAME "$BASE"_project \nDNAME "$BASE"_dataset \nXNAME "$BASE"_crystal \nend \n" | cif2mtz HKLIN ""$FILE"" HKLOUT ""$Dirdirect/$BASE"_1_mtz.tmp"
    else
        echo "Error at convertion of cif to mtz" $List > /dev/stderr
    fi
    echo -e "NREF 0 \nSYMMETRY \nend \n" | mtzdump HKLIN ""$Dirdirect/$BASE"_1_mtz.tmp"
    if [ "$reflns_d_resolution_high" != 0 ]; then
        echo -e "CELL "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nSYMMETRY '"$symmetry_space_group_name"' \nLABOUT F=FUNI SIGF=SIGFUNI \nRESOLUTION "$reflns_d_resolution_low" \nend \n" | unique HKLOUT ""$Dirdirect/$BASE"_3_mtz.tmp"
    else
        echo -e "CELL "$cell_length_a" "$cell_length_b" "$cell_length_c" "$cell_angle_alpha" "$cell_angle_beta" "$cell_angle_gamma" \nSYMMETRY '"$symmetry_space_group_name"' \nLABOUT F=FUNI SIGF=SIGFUNI \nend \n" | unique HKLOUT ""$Dirdirect/$BASE"_3_mtz.tmp"
    fi
    echo -e "FREERFRAC 0.05 \nend \n" | freerflag HKLIN ""$Dirdirect/$BASE"_3_mtz.tmp" HKLOUT ""$Dirdirect/$BASE"_4_mtz.tmp"
    echo -e "LABI FILE 2  E1=FreeR_flag \nLABI FILE 1  ALLIN \nend \n" | cad HKLIN2 ""$Dirdirect/$BASE"_4_mtz.tmp" HKLIN1 ""$Dirdirect/$BASE"_1_mtz.tmp" HKLOUT ""$Dirdirect/$BASE"_5_mtz.tmp"
    echo -e "COMPLETE FREE=FreeR_flag \nend \n" | freerflag HKLIN ""$Dirdirect/$BASE"_5_mtz.tmp"  HKLOUT ""$Dirdirect/$BASE".mtz"
else
    echo "Error at convertion of cif to mtz" $List > /dev/stderr
fi
exit