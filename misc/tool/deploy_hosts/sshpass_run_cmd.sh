#!/usr/bin/env bash

# author: Zeng YueTian
# date: 2015/12/31

# deploy /etc/hosts file
# need root privilege

ADMIN="admin"
ADMIN_PASS="yzhxc9!"

ROOT="root"
ROOT_PASS="Yunshang2014"

seed1_host="10.6.110.1";seed1_user=$ROOT; seed1_pass=$ROOT_PASS
seed2_host="10.6.110.2";seed2_user=$ROOT; seed2_pass=$ROOT_PASS
seed3_host="10.6.110.3";seed3_user=$ROOT; seed3_pass=$ROOT_PASS
seed4_host="10.6.110.4";seed4_user=$ROOT; seed4_pass=$ROOT_PASS
seed5_host="10.6.110.5";seed5_user=$ROOT; seed5_pass=$ROOT_PASS
seed6_host="10.6.110.6";seed6_user=$ROOT; seed6_pass=$ROOT_PASS
seed7_host="10.6.110.7";seed7_user=$ROOT; seed7_pass=$ROOT_PASS
seed8_host="10.6.110.8";seed8_user=$ROOT; seed8_pass=$ROOT_PASS

peer1_host="10.6.111.1";peer1_user=$ROOT; peer1_pass=$ROOT_PASS
peer2_host="10.6.111.2";peer2_user=$ROOT; peer2_pass=$ROOT_PASS
peer3_host="10.6.111.3";peer3_user=$ROOT; peer3_pass=$ROOT_PASS
peer4_host="10.6.111.4";peer4_user=$ROOT; peer4_pass=$ROOT_PASS
peer5_host="10.6.111.5";peer5_user=$ROOT; peer5_pass=$ROOT_PASS
peer6_host="10.6.111.6";peer6_user=$ROOT; peer6_pass=$ROOT_PASS
peer7_host="10.6.111.7";peer7_user=$ROOT; peer7_pass=$ROOT_PASS
peer8_host="10.6.111.8";peer8_user=$ROOT; peer8_pass=$ROOT_PASS


# copy zeus_agent to servers
function run_commands()
{
    command=$1
    echo Run $command start
    for server in seed1 seed2 seed3 seed4 seed5 seed6 seed7 seed8 peer1 peer2 peer3 peer4 peer5 peer6 peer7 peer8
        do
            run_command $server $command
        done

    echo Run $command end
}

#install zeus_agent
function run_command()
{

    # delete previous version; copy; display
    eval host=\${$1_host}
    eval user=\${$1_user}
    eval pass=\${$1_pass}
    echo ---------------------------------------------------------------------------
    echo $1: $user@$host

    command=$2
    # reboot
    sshpass -p $pass ssh -o StrictHostKeyChecking=no $user@$host $command
    echo ---------------------------------------------------------------------------
}

command=$1
run_commands $command
