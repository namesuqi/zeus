# coding=utf-8
"""
copy local file to remote machine

__author__ = 'zengyuetian'

"""

import paramiko
from lib.utility.path import *
root = PathController.get_root_path()


USERNAME = "admin"
PASSWORD = "yzhxc9!"
SSH_PORT = 22


class RemoteDeployer(object):

    def __init__(self, ips, username=USERNAME, password=PASSWORD):
        self.ips = ips
        self.username = username
        self.password = password
        print [username, password]

    def deploy_folder(self, local_dir, remote_dir, kill_proc=None):
        # delete files on remote machines
        for ip in self.ips:
            print "Start Clean for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            if kill_proc is not None:
                ssh.exec_command("killall {0}".format(kill_proc))
                print "kill process {0}".format(kill_proc)
            ssh.exec_command("rm -rf {0}".format(remote_dir))
            ssh.exec_command("mkdir -p {0}".format(remote_dir))
            ssh.close()

        # copy sdk to remote machines
        for ip in self.ips:
            command = 'scp -r {0}/* {1}@{2}:{3}'.format(local_dir, self.username, ip, remote_dir)
            print "Start Deploy files for {0}".format(ip)
            os.system(command)
            print "End Deploy files for {0}".format(ip)
