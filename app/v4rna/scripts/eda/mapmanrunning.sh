#!/bin/bash

FILE=$1
BASE=$2
EXT=$3
FORMAT=$(echo "$EXT" | tr '[a-z]' '[A-Z]')
NEWEXT=$4
NEWFORMAT=$(echo "$NEWEXT" | tr '[a-z]' '[A-Z]')
SNEWFORMAT=$(echo "$NEWEXT" | tr '[A-Z]' '[a-z]')
Dirdirect=$5
exec 1>>$Dirdirect/log.txt
exec 2>>$Dirdirect/debug.txt
Direct=$(pwd)
cd $Dirdirect
Newfile=${FILE##*/}
cp $FILE $Dirdirect/$Newfile
NEWBASE=$BASE.$SNEWFORMAT
if [ "$NEWFORMAT" == 'MASK' ]; then
    echo -e "zp 50000000 2\nre slot $Newfile $FORMAT\nwr slot $NEWBASE $NEWFORMAT 0.0010\nquit\n" | lx_mapman
    exit
elif [ "$NEWFORMAT" == 'MAP' ]; then
    echo -e "zp 50000000 2\nre slot $Newfile $FORMAT\nwr slot $NEWBASE CCP4\nquit\n" | lx_mapman
    exit
else
    echo -e "zp 50000000 2\nre slot $Newfile $FORMAT\nwr slot $NEWBASE $NEWFORMAT\nquit\n" | lx_mapman
fi
cd $Direct
exit