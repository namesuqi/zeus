#!/usr/bin/env bash

# the main entrance for live auto test

# author: Zeng YueTian
# date: 2016/01/18

####################################################
# description: run it with root
# . check OS
# . deploy zeus_agent
# . start robot framework to run test
# . post-processing
# --------------------------------------------------
# ./live.sh:                run test cases with live tag
# ./live.sh start_live:
# ./live.sh stop_live:
# ./live.sh start_peer:     start all peer
# ./live.sh stop_peer:      stop all peer
# ./live.sh reboot:         reboot all node machines
# ./live.sh deploy_hosts:   copy hosts to node machines
# ./live.sh deploy_tsocks:  copy tsocks.conf to node machine
# ./live.sh xxxx:           run test cases with xxxx tag
####################################################


set -o nounset
DIR=$( cd $( dirname -- "$0" ) > /dev/null ; pwd )
echo starting path $DIR
export PYTHONPATH=$DIR
cd $DIR

# include const and function from env.sh
source $DIR/misc/shell/live_env.sh

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


###########################################################
# handle params as remote tool
#   reboot: reboot all node machines
#   deploy_hosts: copy hosts to node machines
#   deploy_tsocks: copy tsocks.conf to node machine
###########################################################
if [ $# -gt 0 ]; then
    echo Parameter is: $1
    if [ $1 = "reboot" ]; then
        # pybot -d live_result --debugfile debug.txt  --include reboot .
        echo start reboot
        cd $DIR/misc/tool/deploy_hosts
        ./sshpass_run_cmd.sh reboot
        exit 0
    elif [ $1 = "deploy_hosts" ]; then
        echo start deploy_hosts
        cd $DIR/misc/tool/deploy_hosts
        ./deploy_hosts.sh hosts
        exit 0
    elif [ $1 = "deploy_tsocks" ]; then
        echo start deploy_tsocks
        cd $DIR/misc/tool/deploy_hosts
        ./deploy_hosts.sh tsocks
        exit 0
    fi
fi

######################################################
# Deploy zeus_agent to servers and start it
######################################################
deploy_rpc

######################################################
# Deploy live folder which contains p2pclient_static
######################################################
deploy_sdks

######################################################
# Start test cases by robot framework
# SUPPORT MULTI TAGS
######################################################
echo start pybot to run test cases
include_string=""
include=" --include "
mkdir -p result    # create dir if not exists
if [ $# -eq 0 ]; then
    # run live case
    pybot -d result --debugfile debug.txt  --include live .
else
    for tag in $@
        do
            include_string=${include_string}${include}${tag}
        done
    echo pybot -d result --debugfile debug.txt $include_string .
    pybot -d result $include_string .
fi



######################################################
# Post-Testing Process (back, copy result and log)
######################################################
webdir="/var/www/html/"
if [ -d $webdir ]; then
    echo copy result to $webdir for apache.
    cp -Rf result $webdir
fi
