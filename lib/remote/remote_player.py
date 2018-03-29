# coding=utf-8
"""
control sdk and vlc on remote machine

__author__ = 'zengyuetian'

"""

import paramiko
import time
from lib.utility.path import *
root = PathController.get_root_path()


USERNAME = "admin"
PASSWORD = "yzhxc9!"
SSH_PORT = 22

REMOTE_PATH = '/home/admin/live'
SDK_FILE = 'liveclient_static'

REMOTE_SDK = '{0}/{1}'.format(REMOTE_PATH, SDK_FILE)

SDK_PORT_START = 60000
SDK_PORT_STEP = 10

class RemotePlayer(object):

    def __init__(self, ips, sdk_nums, urls, local_sdk, username=USERNAME, password=PASSWORD):
        self.local_sdk = local_sdk
        self.sdk_nums = sdk_nums
        self.ips = ips
        self.urls = urls
        self.username = username
        self.password = password
        print [username, password]

    def stop_play(self):
        # start sdk on remote machines and remove folder
        for ip in self.ips:
            print "Stop real play for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("killall {0}".format(SDK_FILE))
            # ssh.exec_command("killall vlc")
            ssh.exec_command("killall mplayer")
            ssh.close()

    def stop_fake_play(self):
        for ip in self.ips:
            print "Stop fake play for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("killall python")
            ssh.close()


    def stop_sdk(self):
        # start sdk on remote machines and remove folder
        for ip in self.ips:
            print "Stop sdk for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("killall {0}".format(SDK_FILE))
            ssh.close()

    def start_play(self):
        # start sdk on remote machines and remove folder
        for index, ip in enumerate(self.ips):
            print "Start real play for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            for i in range(self.sdk_nums[index]):
                port = i * SDK_PORT_STEP + SDK_PORT_START
                url = "http://127.0.0.1:{0}/live_flv/user/wasu?url={1}".format(port, self.urls[index])
                # command = "nohup vlc -I dummy --novideo {0} >> /home/admin/vlc_{1}.log &".format(url, i)
                command = "nohup mplayer -framedrop -hardframedrop {0} > /dev/null 2>&1 &".format(url, i)
                print command
                ssh.exec_command(command)
                time.sleep(0.1)
            ssh.close()

    def start_fake_play(self):
        # start sdk on remote machines and remove folder
        for index, ip in enumerate(self.ips):
            print "Start fake play for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            for i in range(self.sdk_nums[index]):
                port = i * SDK_PORT_STEP + SDK_PORT_START
                url = "http://127.0.0.1:{0}/live_flv/user/wasu?url={1}".format(port, self.urls[index])
                command = "nohup python /home/admin/fake_player/main.py {0} > /dev/null 2>&1 &".format(url, i)
                print command
                ssh.exec_command(command)
                time.sleep(0.1)
            ssh.close()

    def start_sdk(self):
        # start sdk on remote machines and remove folder
        for index, ip in enumerate(self.ips):
            print "Start SDK for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("chmod +x {0}".format(REMOTE_SDK))
            for i in range(self.sdk_nums[index]):
                port = i * SDK_PORT_STEP + SDK_PORT_START
                print "Start SDK for port {0}".format(port)
                ssh.exec_command("mkdir -p {0}/{1}".format(REMOTE_PATH, i))
                ssh.exec_command("cp {0} {1}/{2}/{3}".format(REMOTE_SDK, REMOTE_PATH, i, SDK_FILE))
                time.sleep(0.05)
                p2pclient = "cd {0}/{1} && nohup ./{2}".format(REMOTE_PATH, i, SDK_FILE)
                command = "{0} -p {1} > /dev/null 2>&1 &".format(p2pclient, port)
                print "Command is: " + command
                ssh.exec_command(command)
            ssh.close()

    def restart_sdk(self):
        # restart sdk on remote machines
        for index, ip in enumerate(self.ips):
            print "Start SDK for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("chmod +x {0}".format(REMOTE_SDK))
            for i in range(self.sdk_nums[index]):
                port = i * SDK_PORT_STEP + SDK_PORT_START
                print "Restart SDK for port {0}".format(port)
                p2pclient = "cd {0}/{1} && nohup ./{2}".format(REMOTE_PATH, i, SDK_FILE)
                command = "{0} -p {1} > /dev/null 2>&1 &".format(p2pclient, port)
                print "Command is: " + command
                ssh.exec_command(command)
            ssh.close()

    def deploy_sdk(self):
        # delete sdk on remote machines
        for ip in self.ips:
            print "Start Clean for {0}".format(ip)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, SSH_PORT, self.username, self.password)
            ssh.exec_command("killall {0}".format(SDK_FILE))
            time.sleep(1) #
            ssh.exec_command("rm -rf {0}/".format(REMOTE_PATH))
            ssh.exec_command("rm -rf {0}".format(REMOTE_PATH))
            time.sleep(0.01)
            ssh.exec_command("mkdir -p {0}".format(REMOTE_PATH))
            ssh.close()

        # copy sdk to remote machines
        for ip in self.ips:
            command = 'scp -r {0} {1}@{2}:{3}'.format(self.local_sdk, self.username, ip, REMOTE_PATH)
            print "Start Deploy SDK for {0}".format(ip)
            os.system(command)
            print "End Deploy SDK for {0}".format(ip)


















