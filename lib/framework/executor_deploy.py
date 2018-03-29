# coding=utf-8
"""
Deploy executor

__author__ = 'zengyuetian'

"""

from lib.constant.deploy import *
from lib.framework.executor_base import *
from lib.environment.remote_node_deploy import *
import subprocess


class ExecutorDeploy(ExecutorBase):
    def deploy_agent(self):
        """
        copy agent files to remote node via sshpass，start agent
        """
        root_path = PathController.get_root_path()
        nodes = list()
        for ip in DEPLOY_IP_LIST:
            nodes.append(RemoteNodeDeploy(ip, DEPLOY_USER, DEPLOY_PASSWORD))
        for node in nodes:
            commands = list()
            print "------------------------------------"
            print "deploy_agent for {0}".format(node.ip)
            commands.append(
                'sshpass -p {0} ssh -o StrictHostKeyChecking=no {1}@{2} "rm -rf ~/zeus_agent; mkdir ~/zeus_agent"'
                    .format(node.password, node.user, node.ip))
            commands.append(
                'sshpass -p {0} scp -r {3}/lib/zeus_agent/live* {1}@{2}:~/zeus_agent'
                    .format(node.password, node.user, node.ip, root_path))
            commands.append(
                'sshpass -p {0} ssh {1}@{2} "chmod -R 755 ~/zeus_agent; '
                'cd ~/zeus_agent; ./live_restart.sh > /dev/null 2>&1"'
                    .format(node.password, node.user, node.ip))
            for command in commands:
                p = subprocess.Popen(command, shell=True)
                p.wait()  # wait process finish to avoid parallel execution
                print command

