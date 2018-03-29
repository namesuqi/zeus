#!/usr/bin/env bash

# author: Zeng YueTian
# date: 2016/01/18

# host info


ADMIN="admin"
ADMIN_PASS=""

seed1_host="115.238.246.144";seed1_user=$ADMIN; seed1_pass=$ADMIN_PASS
seed2_host="115.238.246.132";seed2_user=$ADMIN; seed2_pass=$ADMIN_PASS
seed3_host="122.226.84.115";seed3_user=$ADMIN; seed3_pass=$ADMIN_PASS
seed4_host="122.226.84.112";seed4_user=$ADMIN; seed4_pass=$ADMIN_PASS
seed5_host="122.226.84.113";seed5_user=$ADMIN; seed5_pass=$ADMIN_PASS
seed6_host="122.226.84.114";seed6_user=$ADMIN; seed6_pass=$ADMIN_PASS
seed7_host="120.92.250.112";seed7_user=$ADMIN; seed7_pass=$ADMIN_PASS
seed8_host="120.92.250.113";seed8_user=$ADMIN; seed8_pass=$ADMIN_PASS

# =============================
# loop for each sdk machine
# copy zeus_agent to servers
# =============================
function deploy_rpc()
{
    echo deploying rpc start
    for server in seed1 seed2 seed3 seed4 seed5 seed6 seed7 seed8
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
    ssh $user@$host "rm -rf ~/zeus_agent"
    # copy # the remote machine must yum install openssh-client
    scp -r lib/zeus_agent $user@$host:~/
    # display
    ssh $user@$host "ls zeus_agent"
    # restart rpc remote library
    ssh $user@$host "chmod -R 755 zeus_agent; cd zeus_agent; ./restart_remote.sh > /dev/null 2>&1"
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
    for host in seed1 seed2 seed3 seed4 seed5 seed6 seed7 seed8
        do
            install_sdk $host centos
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
    ssh $user@$host "rm -rf live; mkdir live"
    # copy # the remote machine must yum install openssh-client
    scp -r misc/bin/live/idc/* $user@$host:~/live/
    # display
    ssh $user@$host "ls live"
    # restart robot remote library
    ssh $user@$host "chmod -R 755 live"
}
