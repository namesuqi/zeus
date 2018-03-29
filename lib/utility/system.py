# coding=utf-8
"""
Get OS related system information
Control processes

__author__ = 'zengyuetian'

"""

import subprocess
import paramiko
import time
import os
import psutil
import re
import sys
from lib.utility.path import *

def StartSdkOnWindows():
    root_path = PathController.get_root_path()
    sdk = '{0}/misc/bin/sdk/windows/p2pclient.exe'.format(root_path)
    child = subprocess.Popen(sdk)
    return child

def KillSdkOnWindows(proc_name):
    os.system('TASKKILL /F /IM {0}'.format(proc_name))

def StopSdkOnWindows(proc):
    proc.kill()


def GetProcessMemoryOnWindows(x):
    for proc in psutil.process_iter():
        proc_name = str(proc)
        f = re.compile(x, re.I)
        if f.search(proc_name):
            # get private memory of the process
            print proc.memory_info().private
            #print aa.split('pid=')

def GetProcessMemoryOnLinux(ip, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, pwd)
    stdin, stdout, stderr = ssh.exec_command("python /tmp/get_sdk_memory.py")
    print stdout.readlines()
    ssh.close()



def DeploySdkToLinux(ip, user, pwd):
    root_path = PathController.get_root_path()
    sdk = '{0}/misc/bin/sdk/linux/p2pclient_static'.format(root_path)
    sh_file = '{0}/misc/bin/sdk/linux/start_sdk.sh'.format(root_path)
    py_file = '{0}/misc/bin/sdk/linux/get_sdk_memory.py'.format(root_path)
    t = paramiko.Transport((ip, 22))
    t.connect(username=user, password=pwd)
    sftp = paramiko.SFTPClient.from_transport(t)

    remotepath = '/tmp/p2pclient_static'
    localpath = sdk
    sftp.put(localpath, remotepath)

    localpath = sh_file
    remotepath = '/tmp/start_sdk.sh'
    sftp.put(localpath, remotepath)

    localpath = py_file
    remotepath = '/tmp/get_sdk_memory.py'
    sftp.put(localpath, remotepath)
    t.close()

def StartSdkOnLinux(ip, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, pwd)
    ssh.exec_command("cd ~; chmod 777 /tmp/start_sdk.sh; chmod 777 /tmp/p2pclient_static")
    # ssh.exec_command("nohup /tmp/p2pclient_static &")
    ssh.exec_command("nohup /tmp/start_sdk.sh > /dev/null 2>&1 &")
    # ssh.close()


def KillSdkOnLinux(ip, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, pwd)
    ssh.exec_command("killall p2pclient_static ")
    ssh.close()


# if __name__ == "__main__":
#     GetProcessMemoryOnWindows("p2pclient")
#     exit(0)
#
#     proc = StartSdkOnWindows()
#     time.sleep(2000)
#     StopSdkOnWindows(proc)

if __name__ == "__main__":
    DeploySdkToLinux("192.168.1.115", "root", "Yunshang2014")
    StartSdkOnLinux("192.168.1.115", "root", "Yunshang2014")
    time.sleep(60)
    KillSdkOnLinux("192.168.1.115", "root", "Yunshang2014")


