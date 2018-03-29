# coding=utf-8
"""
IDC node control entrance class

__author__ = 'zengyuetian'

"""

from lib.constant.idc import *
from lib.framework.executor_base import *
from lib.environment.remote_node_sdk import *
import subprocess


class ExecutorIdc(ExecutorBase):
    def deploy_agent(self):
        """
        copy agent files to remote node without password，start agent
        """
        root_path = PathController.get_root_path()
        nodes = list()
        for ip in IDC_IP_LIST:
            nodes.append(RemoteNodeSdk(ip, "admin", ""))
        for node in nodes:
            commands = list()
            print "------------------------------------"
            print "deploy_agent for {0}".format(node.ip)
            commands.append(
                'ssh -o StrictHostKeyChecking=no {0}@{1} "rm -rf ~/zeus_agent; mkdir ~/zeus_agent"'
                    .format(node.user, node.ip))
            commands.append(
                'scp -r {2}/lib/zeus_agent/live* {0}@{1}:~/zeus_agent'
                    .format(node.user, node.ip, root_path))
            commands.append(
                'ssh {0}@{1} "chmod -R 755 ~/zeus_agent; cd ~/zeus_agent; ./live_restart.sh > /dev/null 2>&1"'
                    .format(node.user, node.ip))
            for command in commands:
                p = subprocess.Popen(command, shell=True)
                p.wait()  # wait process finish to avoid parallel execution
                print command

    def deploy_sdk(self):
        """
        copy sdk files to remote node without password
        """
        root_path = PathController.get_root_path()
        nodes = list()
        for ip in IDC_IP_LIST:
            nodes.append(RemoteNodeSdk(ip, "admin", ""))
        for node in nodes:
            commands = list()
            print "------------------------------------"
            print "deploy_sdk for {0}".format(node.ip)
            commands.append(
                'ssh -o StrictHostKeyChecking=no {0}@{1} "rm -rf ~/live; mkdir ~/live"'
                    .format(node.user, node.ip))
            commands.append(
                'scp -r {2}/misc/bin/live/idc/* {0}@{1}:~/live'
                    .format(node.user, node.ip, root_path))
            commands.append(
                'ssh {0}@{1} "chmod -R 755 ~/live"'
                    .format(node.user, node.ip))
            for command in commands:
                p = subprocess.Popen(command, shell=True)
                p.wait()  # wait process finish to avoid parallel execution
                print command
