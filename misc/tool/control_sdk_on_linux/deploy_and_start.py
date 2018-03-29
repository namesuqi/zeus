# coding=utf-8
# copy sdk to linux machine
# start sdk one by one on different port
# __author__ = 'zengyuetian'

import paramiko
from lib.utility.path import *
import time

root = PathController.get_root_path()

USERNAME = "admin"
PASSWORD = "yzhxc9!"
SSH_PORT = 22
REMOTE_PATH = '/home/admin/live'
SDK_FILE = 'liveclient_static'
LOCAL_SDK = "{0}/misc/bin/sdk/linux/{1}".format(root, SDK_FILE)
REMOTE_SDK = '{0}/{1}'.format(REMOTE_PATH, SDK_FILE)
SDK_NUM = 10
SDK_PORT_START = 60000
SDK_PORT_STEP = 10

ips = ["192.168.1.151"]


if __name__ == "__main__":
    # start sdk on remote machines and remove folder
    for ip in ips:
        print "Stop SDK for {0}".format(ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, SSH_PORT, USERNAME, PASSWORD)
        ssh.exec_command("killall {0}".format(SDK_FILE))
        ssh.exec_command("rm -rf {0}/*".format(REMOTE_PATH))
        ssh.close()


    # copy sdk to remote machines
    for ip in ips:
        print "Deploy SDK for {0}".format(ip)
        t = paramiko.Transport((ip, SSH_PORT))
        t.connect(username=USERNAME, password=PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(LOCAL_SDK, REMOTE_SDK)
        t.close()

    # start sdk on remote machines
    for ip in ips:
        print "Start SDK for {0}".format(ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, SSH_PORT, USERNAME, PASSWORD)
        ssh.exec_command("chmod 755 {0}".format(REMOTE_SDK))
        for i in range(SDK_NUM):
            print "Copy and start sdk for {0}".format(i)
            command_list = list()
            command_list.append("rm -rf {0}/{1}".format(REMOTE_PATH, i))
            command_list.append("mkdir {0}/{1}".format(REMOTE_PATH, i))
            command_list.append("cp {0} {1}/{2}".format(REMOTE_SDK, REMOTE_PATH, i))
            command_list.append("cd {0}/{1}; nohup ./{2} -p {3} -u 65574 > /dev/null 2>&1 &".
                                format(REMOTE_PATH, i, SDK_FILE, SDK_PORT_START+i*SDK_PORT_STEP))
            for command in command_list:
                ssh.exec_command(command)
                time.sleep(0.1)
                # stdin, stdout, stderr = ssh.exec_command("ls /")
                # print stdout.readlines()
        ssh.close()
