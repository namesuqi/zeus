#!/usr/bin/env python
# coding=utf-8
"""
zeus remote lib

__author__ = 'zengyuetian'

copy this file to remote machine and run:
python robot_agent.py

note：must run this script with correct user
"""

import sys
import os
import re
import traceback
import json
import hashlib
import time



"""
下面是常量
"""
SDK_FILE = "ys_service_static"
SDK_PATH = "/root/sdk"
SDK_DATA_BOARD_PORT = "32717"
AGENT_PATH = "/root/zeus_agent"
def print_trace(function):
    '''
    print trace if any exception occurs
    :param function: wrapper
    '''
    def wrapper(*args, **kw):
        try:
            return function(*args, **kw)
        except Exception, e:
            traceback.print_exc()
            raise e
    return wrapper

class RobotAgent(object):
    """
    remote control SDK
    """
    def StartSDK(self):
        '''
        MUST enter sdk dir, then execute bin to create yunshang/yunshang.conf which has unique peerid
        :return: None
        '''
        command = "cd {0}; ./{1} &".format(SDK_PATH, SDK_FILE)
        print command
        os.system(command)


    def StopSDK(self):
        command = r"ps aux | grep ys_service_static |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9"
        print command
        os.system(command)

    def RestartSDK(self):
        self.StopSDK()
        self.StartSDK()

    @print_trace
    def GetSDKUdpPort(self):
        '''
        parse SDK's UDP port
        :return:port
        '''
        command = r'netstat -nlap |grep p2p | grep udp'
        result = os.popen(command, 'r').read()
        print "***netstat result is {0}".format(result)
        ######################################################################################################
        # udp        0      0 0.0.0.0:46551           0.0.0.0:*                           22208/p2pclient_sta
        ######################################################################################################
        results = result.split()
        ip_port = results[3]
        print "***ip_port is {0}".format(ip_port)
        port = ip_port.split(":")[1]
        print "***port is {0}".format(port)
        return port


    @print_trace
    def GetPeerID(self):
        '''
        get peer_id from yunshang/yunshang.conf
        :return:peerid
        '''
        conf_file = '{0}/yunshang/yunshang.conf'.format(SDK_PATH)
        with open(conf_file, 'r') as f:
            line = f.read()
        return json.loads(line).get('peer_id', None)

    @print_trace
    def DeleteConfFile(self):
        '''
        delete yunshang/yunshang.conf
        :return:peerid
        '''
        conf_file = '{0}/yunshang/yunshang.conf'.format(SDK_PATH)
        return os.system("rm -rf {0}".format(conf_file))


    @print_trace
    def StartVod(self, byte_district, url, user):
        command = 'curl  --header "Range: bytes={0}" -o vod.file "http://127.0.0.1:32717/vod?url={1}&user={2}" &'.format(byte_district, url, user)
        print command
        os.system(command)

    @print_trace
    def StopVod(self):
        command = r"ps aux | grep curl |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9"
        print command
        os.system(command)


    @print_trace
    def StartCdn(self, byte_district, url):
        command = 'curl --header "Range: bytes={0}" -o cdn.file "{1}"  &'.format(byte_district, url)
        print command
        os.system(command)


    @print_trace
    def DownloadM3U8Url(self, url_type, url, username=None):

        if url_type == "hls":
            m3u8_url = "http://127.0.0.1:32717/hls?url={0}&user={1}".format(url, username)
        elif url_type == "cdn":
            m3u8_url = url
        else:
            print "URL TYPE ERROR!"
            exit()
        command = "curl -o {0}.m3u8 \"{1}\" &".format(url_type, m3u8_url)
        print command
        os.system(command)


    @print_trace
    def DownloadM3U8File(self, url_type, url_name, seg_num):
        url_file = AGENT_PATH + '/' + url_name
        all_lines = file(url_file, 'r')
        url_list = []
        i = 0
        for ts_url in all_lines:
            if url_type == "cdn":
                url_filter = r"(http://.*)"
            elif url_type == "hls":
                url_filter = r"(/vhls/user/.*)"
            else:
                pass
            rel_file_url = re.match(url_filter, ts_url)
            if rel_file_url:
                url_list.append(rel_file_url.group(1))
        all_lines.close()
        for seg_url in url_list:
            file_name = "{0}.{1}" .format(i, url_type)
            if url_type == "cdn":
                download_url = seg_url
            elif url_type == "hls":
                download_url = "http://127.0.0.1:32717" + seg_url
            else:
                pass
            command = "curl -o {0} \"{1}\" &".format(file_name, download_url)
            print command
            os.system(command)
            i += 1
            if i > int(seg_num):
                break

    """
    remote control servers
    """
    def StartServer(self, name):
        pass

    def StopServer(self, name):
        pass

    def RestartServer(self, name):
        pass


    """
    remote control NAT machines
    """

    @print_trace
    def SwitchToNatType(self, nat_type, stun, me, peer, peer_port=None):
        '''
        根据信息切换NAT类型
        :param nat_type:切换成的NAT类型
        :param stun: stun服务器地址
        :param me: 本nat机地址
        :param peer: 另一sdk机地址
        :param peer_port: 另一sdk机端口
        :return: void
        '''

        command_list = list()
        command_list.append('ufw default allow') # 默认允许所有的通过
        command_list.append('ufw enable')   # 启动ufw
        command_list.append('iptables -t nat -F')  # 删除表中所有规则
        # command_list.append('iptables -I INPUT -p tcp --dport 22 -j ACCEPT') # 保证ssh能够连通
        # command_list.append('iptables -I OUTPUT -p tcp --sport 22 -j ACCEPT') # 保证ssh能够连通
        # command_list.append('iptables -I INPUT -p tcp --dport 8270 -j ACCEPT')  # 保证Robot Remote能够连通
        # command_list.append('iptables -I OUTPUT -p tcp --sport 8270 -j ACCEPT')  # 保证Robot Remote能够连通

        if nat_type == "0":  # 0-Public
            print "NAT type is 0-Public, do nothing"

        elif nat_type == "1": # 1-Full Cone NAT
            print "NAT type is 1-Full Cone NAT"
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} -o eth0 -j MASQUERADE'.format(stun))

        elif nat_type == "2":
            print "NAT type is 2-Restricted Cone NAT"
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} -o eth0 -j SNAT --to-source {1}'.format(stun, me))

        elif nat_type == "3": # 3-Port Restricted Cone NAT
            print "NAT type is 3-Port Restricted Cone NAT"
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} --dport 9000 -o eth0 -j SNAT --to-source {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} --dport 9002 -o eth0 -j SNAT --to-source {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} --dport {1} -o eth0 -j SNAT --to-source {0}:{1}'.format(peer, peer_port))

        elif nat_type == "4": # 4-Symmetric NAT
            print "NAT type is 4-Symmetric NAT"
            command_list.append('iptables -t nat -A PREROUTING -i eth0 -p udp --sport 9000 -j DNAT --to-destination {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A POSTROUTING -o eth0 -p udp --dport 9000 -j SNAT --to-source {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A PREROUTING -i eth0 -p udp --sport 9002 -j DNAT --to-destination {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A POSTROUTING -o eth0 -p udp --dport 9002 -j SNAT --to-source {0}:{1}'.format(me, peer_port))
            command_list.append('iptables -t nat -A POSTROUTING -p udp -d {0} --dport 12345 -o eth0 -j SNAT --to-source {0}:{1}'.format(peer, peer_port))
        else:
            raise Exception("NAT type {0} is not correct".format(nat_type))

        command_list.append("iptables -A INPUT -i eth0 -p udp -j DROP")
        print "***command_list is: "
        print command_list
        # execute iptables commands to switch NAT type
        for command in command_list:
            os.system(command)


    """
        common method goes here
    """
    def get_command_result(self, command):
        pass


    def list_dir_files(self, dir_name):
        return os.listdir(dir_name)


    @print_trace
    def GetFileMd5(self, filename):
        """
        获得大文件的MD5
        :param filename:大文件名
        :return:md5值
        """
        # if not os.path.isfile(filename):
        #     print filename, "not exists"
        #     return
        myhash = hashlib.md5()
        url_file = AGENT_PATH + '/' + filename
        f = file(url_file, 'rb')
        print f
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()


##############################
# Start on remote machine
##############################
if __name__ == '__main__':
    from robotremoteserver import RobotRemoteServer
    RobotRemoteServer(RobotAgent(), *sys.argv[1:])

    ###############################################################
    # for debugging
    #ZeusLibrary().PlayVod("vod.cloutropy.com/700m.avi", "leigang")
    ###############################################################

