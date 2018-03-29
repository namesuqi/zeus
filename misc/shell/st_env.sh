#!/usr/bin/env bash

# author: Zeng YueTian
# date: 2015/12/31

# host info
# main server is: stun, ts, dir, upload, stats, push, upgrade

ADMIN="admin"
ADMIN_PASS="yzhxc9!"

ROOT="root"
ROOT_PASS="Yunshang2014"

sdk1_host="10.5.0.85"
sdk1_user=$ROOT
sdk1_pass=$ROOT_PASS

sdk2_host="10.5.0.86"
sdk2_user=$ROOT
sdk2_pass=$ROOT_PASS

nat1_host="10.5.0.87"
nat1_user=$ROOT
nat1_pass=$ROOT_PASS

nat2_host="10.5.0.88"
nat2_user=$ROOT
nat2_pass=$ROOT_PASS

stun_host="10.5.0.10"
stun_user=$ADMIN
stun_pass=$ADMIN_PASS

ts_host="10.5.0.57"
ts_user=$ADMIN
ts_pass=$ADMIN_PASS

dir_host="10.5.0.11"
dir_user=$ADMIN
dir_pass=$ADMIN_PASS

upload_host="10.5.0.12"
upload_user=$ADMIN
upload_pass=$ADMIN_PASS

stats_host="10.5.0.61"
stats_user=$ADMIN
stats_pass=$ADMIN_PASS

push_host="10.5.0.67"
push_user=$ADMIN
push_pass=$ADMIN_PASS

upgrade_host="10.5.0.10"
upgrade_user=$ADMIN
upgrade_pass=$ADMIN_PASS

account_host="10.5.0.1"
account_user=$ADMIN
account_pass=$ADMIN_PASS

ctrl_host="10.5.0.12"
ctrl_user=$ADMIN
ctrl_pass=$ADMIN_PASS

recorder_host="10.5.0.12"
recorder_user=$ADMIN
recorder_pass=$ADMIN_PASS

fe_host="10.5.0.12"
analyst_host="10.5.0.13"
redis_host="10.5.0.30"
mongodb_host="10.5.0.50"

# copy zeus_agent to servers
function deploy_agents()
{
    echo deploying agent start
    for server in sdk1 sdk2 nat1 nat2 stun ts dir upload stats push upgrade recorder
        do
            install_agent $server
        done

    echo deploying agent end
}

#install zeus_agent
function install_agent()
{

    # delete previous version; copy; display
    eval host=\${$1_host}
    eval user=\${$1_user}
    eval pass=\${$1_pass}
    echo ---------------------------------------------------------------------------
    echo $1: $user@$host
    # delete previous files
    sshpass -p $pass ssh -o StrictHostKeyChecking=no $user@$host "rm -rf zeus_agent"
    # copy
    sshpass -p $pass scp -r lib/zeus_agent $user@$host:~/
    # display
    sshpass -p $pass ssh $user@$host "ls zeus_agent"
    # restart robot remote library
    sshpass -p $pass ssh $user@$host "chmod -R 755 zeus_agent; cd zeus_agent; ./restart_agent.sh > /dev/null 2>&1"
    sshpass -p $pass ssh $user@$host "/usr/sbin/pm2 list"
    echo ---------------------------------------------------------------------------
}


