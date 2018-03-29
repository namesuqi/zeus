#!/usr/bin/python
# coding=utf-8
"""
get lf_file from remote machine

__author__ = 'zsw'

"""
import json
import os
from lib.decorator.trace import *
import paramiko
from lib.utility.path import *
#paramiko.util.log_to_file('/tmp/sshout')
from lib.feature.lf_control_bj.lf_data import *

SDK_PATH = "/home/admin/live"
# ROBOT_ZEUS_PATH = "/root/zhangshuwei"
ROBOT_ZEUS_PATH = PathController.get_root_path()
LOCAL_DIR = PathController.get_root_path()  # local zeus folder
YUNSHANG_FILE = 'yunshang.conf'
PEER_IDS_FILE = "{0}/lib/feature/lf_control_bj/{1}.txt".format(ROBOT_ZEUS_PATH, YUNSHANG_FILE)
print "Peer_ID file: " + PEER_IDS_FILE
class GetLfFile(object):

    @print_trace
    def GetAllInfo(self, ip_list=LF_IP_LIST, username="admin", passwd="", num_list=LF_NUM_LIST, file_name=YUNSHANG_FILE):
        '''
        get lf_file from lfs' machine (robot: python run.py server update_lf_ids (/root/zhangshuwei))
        :param ip_list: LF_IP_LIST
        :param username:
        :param passwd:
        :param num_list: lf num on each machine
        :param file_name: needed to get
        :return:
        '''

        fp = open(PEER_IDS_FILE, "w+")

        m = 0  # choose lf_num for each lf_ip
        for lf_ip in ip_list:
            lf_num = num_list[m]
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(lf_ip, 22, username, passwd, timeout=5)

            for i in range(1, int(lf_num)+1):
                cmd = "cat {0}/{1}/yunshang/{2}".format(SDK_PATH, i, file_name)
                stdin, stdout, stderr = ssh.exec_command(cmd)
                line = stdout.readline()
                print "IP:" + lf_ip + "; DIR: " + str(i) + "; LINE: " + line
                fp.write(line)
                fp.write("\n")

            ssh.close()
            m += 1
        fp.close()
        # command = "cp {0}/lib/feature/stun_rrpc/yunshang.conf.txt {0}/lib/feature/lf_control_bj/yunshang.conf.txt".format(ROBOT_ZEUS_PATH)
        # os.system(command)

    @print_trace
    def GetLfInfo(self):
        '''
        get file from robot
        :return:
        '''
        t = paramiko.Transport(ROBOT_IP, 22)
        t.connect(username=ROBOT_USER, password=ROBOT_PASSWD)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = '{0}/lib/feature/lf_control_bj/{1}.txt'.format(ROBOT_ZEUS_PATH, YUNSHANG_FILE)
        localpath = '{0}/lib/feature/lf_control_bj/{1}.txt'.format(LOCAL_DIR, YUNSHANG_FILE)
        sftp.get(remotepath, localpath)
        print "done"
        t.close()

    @print_trace
    def GetPeerID(self, n=20):
        '''
        get peer_id_list from yunshang.conf.txt
        :return:peerid
        '''

        f = open(PEER_IDS_FILE, "r")
        LF_ID_LIST = []
        for i in range(int(n)):
            line = f.readline()
            peer_id = json.loads(line).get("peer_id", None)
            LF_ID_LIST.append(peer_id)
        f.close()

        return LF_ID_LIST



if __name__ == '__main__':

    # GetLfFile().GetAllInfo("192.168.1.64", "admin", "yzhxc9!", 20, "yunshang.conf")
    # GetLfFile().GetPeerID()
    # GetLfFile().GetLfInfo()
    pass




