#!/usr/bin/env bash

# the main entrance for idc seeds control

# author: Zeng YueTian
# date: 2016/01/30

####################################################
# description: run it with root
# . check OS
# . deploy zeus_agent
# . start robot framework to run test
# . post-processing
# --------------------------------------------------
# ./idc.sh start                update sdk and start all sdk
# ./idc.sh stop                 not update sdk and stop all sdk
# ./idc.sh restart              not update sdk and only restart all sdk
####################################################


set -o nounset
DIR=$( cd $( dirname -- "$0" ) > /dev/null ; pwd )
echo starting path $DIR
export PYTHONPATH=$DIR
cd $DIR

# include const and function from env.sh
source $DIR/misc/shell/idc_env.sh

####################################################
# Get OS Type
####################################################
echo Get OS type
issue_info=`cat /etc/issue`
echo $issue_info
os=`echo $issue_info | awk -F ' ' '{print $1}'`

if [ $os = 'Ubuntu' ]; then
    echo Operating System is Ubuntu
else
    os='CentOS'
    echo Operating System is CentOS
fi

if [ $# -gt 0 ]; then
    if [ $1 = "restart" -o $1 = "stop" ]; then
        echo ONLY start or stop sdk, NOT deploy anything
    else
        deploy_rpc
        deploy_sdks
    fi
else    # $1 = "start"
    deploy_rpc
    deploy_sdks
fi




######################################################
# Start test cases by robot framework
# SUPPORT MULTI TAGS
######################################################
echo start pybot to run IDC test cases

# create dir if not exists
mkdir -p result

# run idc cases
pybot -d result --include $1 .



######################################################
# Post-Testing Process (back, copy result and log)
######################################################
webdir="/var/www/html/"
if [ -d $webdir ]; then
    echo copy result to $webdir for apache.
    cp -Rf result $webdir
fi
