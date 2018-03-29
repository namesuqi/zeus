#!/usr/bin/env bash

# author: Zeng YueTian
# date: 2016/01/18

# host info
ADMIN="admin"
ADMIN_PASS="yzhxc9!"

ROOT="root"
ROOT_PASS="Yunshang2014"
##### SEED #####
seed1_host="10.6.110.1";seed1_user=$ROOT; seed1_pass=$ROOT_PASS
seed2_host="10.6.110.2";seed2_user=$ROOT; seed2_pass=$ROOT_PASS
seed3_host="10.6.110.3";seed3_user=$ROOT; seed3_pass=$ROOT_PASS
seed4_host="10.6.110.4";seed4_user=$ROOT; seed4_pass=$ROOT_PASS
seed5_host="10.6.110.5";seed5_user=$ROOT; seed5_pass=$ROOT_PASS
seed6_host="10.6.110.6";seed6_user=$ROOT; seed6_pass=$ROOT_PASS
seed7_host="10.6.110.7";seed7_user=$ROOT; seed7_pass=$ROOT_PASS
seed8_host="10.6.110.8";seed8_user=$ROOT; seed8_pass=$ROOT_PASS
##### PEER #####
peer1_host="10.6.111.1";peer1_user=$ROOT; peer1_pass=$ROOT_PASS
peer2_host="10.6.111.2";peer2_user=$ROOT; peer2_pass=$ROOT_PASS
peer3_host="10.6.111.3";peer3_user=$ROOT; peer3_pass=$ROOT_PASS
peer4_host="10.6.111.4";peer4_user=$ROOT; peer4_pass=$ROOT_PASS
peer5_host="10.6.111.5";peer5_user=$ROOT; peer5_pass=$ROOT_PASS
peer6_host="10.6.111.6";peer6_user=$ROOT; peer6_pass=$ROOT_PASS
peer7_host="10.6.111.7";peer7_user=$ROOT; peer7_pass=$ROOT_PASS
peer8_host="10.6.111.8";peer8_user=$ROOT; peer8_pass=$ROOT_PASS
##### PEER #####
peer10_host="10.6.111.10";peer10_user=$ROOT; peer10_pass=$ROOT_PASS
peer11_host="10.6.111.14";peer11_user=$ROOT; peer11_pass=$ROOT_PASS
peer12_host="10.6.111.15";peer12_user=$ROOT; peer12_pass=$ROOT_PASS
peer13_host="10.6.111.16";peer13_user=$ROOT; peer13_pass=$ROOT_PASS



# =============================
# loop for each sdk machine
# copy zeus_agent to servers
# =============================
function deploy_rpc()
{
    echo deploying rpc start
    #for server in seed1 seed2 seed3 seed4 seed5 seed6 seed7 seed8 peer1 peer2 peer3 peer4 peer5 peer6 peer7 peer8
    for server in peer10
        do
            install_rpc $server
        done

    echo deploying rpc end
}


# =============================
# copy zeus_agent files
# start rpc service
# =============================
function install_rpc()
{

    # delete previous version; copy; display
    eval host=\${$1_host}
    eval user=\${$1_user}
    eval pass=\${$1_pass}
    echo ---------------------------------------------------------------------------
    echo $1: $user@$host install_rpc
    # delete previous files
    sshpass -p $pass ssh -o StrictHostKeyChecking=no $user@$host "rm -rf ~/zeus_agent"
    # copy
    sshpass -p $pass scp -r lib/zeus_agent $user@$host:~/
    # display
    #sshpass -p $pass ssh $user@$host "ls zeus_agent"
    # restart rpc remote library
    sshpass -p $pass ssh $user@$host "chmod -R 755 zeus_agent; cd zeus_agent; ./restart_remote.sh > /dev/null 2>&1"
}


# =============================
# loop for sdk machines
# copy sdk folder live to sdk machines
# =============================
function deploy_sdks()
{
    echo deploying sdk start

    # copy sdk bin to seeds machines
    # seed
#    for host in seed1 seed2 seed3 seed4 seed5 seed6 seed7 seed8
#        do
#            install_sdk $host centos
#        done

    # copy sdk bin to peers machines
    #for host in peer1 peer2 peer3 peer4 peer5 peer6 peer7 peer8
    for host in peer10
        do
            install_sdk $host ubuntu
        done

    echo deploying sdk end
}


# =============================
# copy live folder
# chmod to 755
# =============================
function install_sdk()
{

    # delete previous version; copy; display
    eval host=\${$1_host}
    eval user=\${$1_user}
    eval pass=\${$1_pass}
    echo ---------------------------------------------------------------------------
    echo $1: $user@$host $2 install_sdk
    os=$2
    # delete previous files
    sshpass -p $pass ssh -o StrictHostKeyChecking=no $user@$host "rm -rf live; mkdir live"
    # copy
    sshpass -p $pass scp -r misc/bin/live/$os/* $user@$host:~/live/
    # display
    sshpass -p $pass ssh $user@$host "ls live"
    # restart robot remote library
    sshpass -p $pass ssh $user@$host "chmod -R 755 live"
}
