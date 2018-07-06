#!/bin/bash
source env/bin/activate
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#echo "current: " $DIR

export DISPLAY=":0.0"

export BIOBENCH_GET_VOLUME=$PWD/contrib/get_volume.exe

#echo "BIOBENCH_GET_VOLUME:"
#echo $BIOBENCH_GET_VOLUME

export PATH=$DIR/contrib:$PATH
export PATH=$DIR/scripts:$PATH

### User settings
DEV_DIR=$PWD

### Obligatory settings

# directory of python environment for biobench-v4rna
APP_ENV_DIR="${DEV_DIR}/env/"

# directory where the biobench-v4rna application resides, i.e. the run.sh file
APP_DIR="${DEV_DIR}/"

#echo "dirs: " $APP_ENV_DIR "  " $APP_DIR


############################################################################
### DON'T CHANGE ANYTHING BELOW UNLESS YOU REALLY KNOW WHAT YOU'RE DOING ###
############################################################################

SCRIPT_PATH=$0
SCRIPT_FILE=$(basename $0)


if [ "$1" == "help" ]; then
    echo -e "
    OPTIONS help status dev kill

    help: prints this help

    status: show if $SCRIPT_FILE is running or not

    dev: for development, disables file logging and turns off
    the automatic respawning

    kill: kills the oldest previously started process started
    by this script that is still running

    no options: for production server, automatic respawning on crash
    best run as 'nohup $SCRIPT_FILE > /dev/null 2>&1 &'
    "
    exit 0
fi

# log files
PASTER_LOG_FILE="paster.log"
RESPAWN_LOG_FILE="respawn.log"
# activate the python environment
cd $APP_ENV_DIR
# source bin/activate  # already done in second line...

# os dependend ps command
if [ "$(uname)" == "Darwin" ]; then
    PS_CMD="ps -ef"
else
    PS_CMD="ps ef -o uid,pid,cmd"
fi

# find the first process (lowest PID) for SCRIPT_PATH
SCRIPT_PID=$($PS_CMD | grep $SCRIPT_PATH | grep -v grep | awk '{print $2}' | head -n 1)

# info
# echo -e "
#     SCRIPT_FILE: $SCRIPT_FILE
#     SCRIPT_PATH: $SCRIPT_PATH
#     SCRIPT_PID: $SCRIPT_PID
# "

# show some status
if [ "$1" == "status" ]; then
    if [ "$SCRIPT_PID" == "" -o "$SCRIPT_PID" == "$$" ]; then
        echo "$SCRIPT_FILE not running"
    else
        echo "$SCRIPT_FILE running as process group $SCRIPT_PID"
    fi
    exit 0
fi

# if requested kill the application
if [ "$1" == "kill" ]; then
    echo "killing process group $SCRIPT_PID"
    # negate PID to kill the whole process group
    kill -9 -$SCRIPT_PID
    exit 0
fi

# start the application
cd $APP_DIR
if [ "$1" == "dev" ]; then
    echo "dev mode, no logging, no automatic respawing"
    ./run.sh
else
    # start the application and restart it if
    # it does not ends with the exit code '0'
    until ./run.sh --log-file $PASTER_LOG_FILE; do
        EXIT_CODE=$?
        PID=$$
        echo "$(date): $SCRIPT_FILE (PID ${PID}) crashed with exit code ${EXIT_CODE}. Respawning..." >> $RESPAWN_LOG_FILE
        # sleep for a second to remove strain from the system
        # in case the application keeps crashing repeatedly
        sleep 1
    done
fi
