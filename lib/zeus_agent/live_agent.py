# coding=utf-8
"""
for rpc remote control
running one remote node machine

only for：
    1. live testing

__author__ = 'zengyuetian'

"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import Binary
import datetime
import os
import time
import logging
import logging.config
import logging.handlers


P2PCLIENT_PORT = 60000
P2PCLIENT_PORT_STEP = 10
P2PCLIENT = "p2pclient_static"
LIVECLIENT = "liveclient_static"
RPC_PORT = 19527


IDC_LIVE_DIR = "/home/admin/live"
IDC_ZEUS_DIR = "/home/admin/zeus_agent"


LIVE_DIR = "/root/live"
ZEUS_DIR = "/root/zeus_agent"
LOG_DIR = "/tmp/log"

logger = None

class RpcService(object):
    def execute(self, command):
        '''
        get command return value
        :param command:
        :return:
        '''
        logger.info("execute: " + command)
        result = os.popen(command, 'r').read()
        return result

    def KillProcessWithKeyword(self, keyword):
        """
        kill processes according to keyword
        :param keyword:
        :return:void
        """
        logger.info("KillProcessWithKeyword: " + keyword)
        process_ids = self.get_process_ids(keyword)
        for process_id in process_ids:
            command = "kill -9 %s" % process_id
            os.system(command)

    def KillSomeProcessWithKeyword (self, keyword, sdk_num):
        """
        kill processes according to keyword
        :param keyword:
        :return:void
        """
        logger.info("KillProcessWithKeyword: " + keyword)
        process_ids = self.get_process_ids(keyword)
        process_num = sdk_num * 2
        if process_num <= len(process_ids):
            process_ids = process_ids[0: process_num]
        for process_id in process_ids:
            command = "kill -9 %s" % process_id
            os.system(command)

    def StopAllSdkProcess(self):
        '''
        stop all sdk processes
        :return:void
        '''
        logger.info("StopAllSdkProcess")
        keyword = "p2pclient_static"
        self.KillProcessWithKeyword(keyword)

    def StopAllIdcProcess(self):
        '''
        stop sdk processes on IDC machine
        :return:void
        '''
        logger.info("StopAllIdcProcess")
        keyword = "liveclient_static"
        self.KillProcessWithKeyword(keyword)

    def StopSomeIdcProcess (self, sdk_num):
        '''
        stop sdk processes on IDC machine
        :return:void
        '''
        logger.info("StopSomeIdcProcess")
        keyword = "liveclient_static"
        self.KillSomeProcessWithKeyword(keyword, sdk_num)


    def StartAllSdkProcess(self, sdk_num):
        '''
        loop to start specific number of sdk processes
        :param sdk_num: process number
        :return:void
        '''
        logger.info("StartAllSdkProcess")
        self.install_sdk(sdk_num)
        for i in range(1, sdk_num+1):
            port = (i-1)*P2PCLIENT_PORT_STEP + P2PCLIENT_PORT
            logger.info("StartSdkProcess {0} at port {1}".format(str(i), str(port)))
            #p2pclient = "cd {0}/{1} && tsocks {0}/{1}/{2}".format(LIVE_DIR, str(i), P2PCLIENT)  # include tsocks to access network
            p2pclient = "cd {0}/{1} && {0}/{1}/{2}".format(LIVE_DIR, str(i), P2PCLIENT)
            #command = "{0} -a {1} &".format(p2pclient, port)
            command = "{0} -p {1} -u 65574 &".format(p2pclient, port) # prefix=00010026
            os.system(command)
            time.sleep(0.1)


    def StartAllIdcProcess(self, sdk_num, is_leifeng=False):
        '''
        loop to start specific number of sdk processes on IDC
        :param sdk_num: process number
        :return:void
        '''
        logger.info("StartAllIdcProcess")
        self.install_sdk_for_idc(sdk_num)
        for i in range(1, sdk_num+1):
            port = (i-1)*P2PCLIENT_PORT_STEP + P2PCLIENT_PORT
            logger.info("StartIdcProcess {0} at port {1}".format(str(i), str(port)))
            live_client = "cd {0}/{1} && {0}/{1}/{2}".format(IDC_LIVE_DIR, str(i), LIVECLIENT)
            # live_client = "ulimit -c 2000000 && cd {0}/{1} && {0}/{1}/{2}".format(IDC_LIVE_DIR, str(i), LIVECLIENT)
            if is_leifeng: # prefix=00010026
                command = "{0} -p {1} -u 65574 &".format(live_client, port)
            else:
                command = "{0} -p {1} &".format(live_client, port)
            logger.info(command)
            os.system(command)
            time.sleep(0.1)


    def get_process_ids(self, keyword):
        """
        get process id list
        :param keyword:
        :return:void
        """
        logger.info("get_process_ids: " + keyword)
        command = "ps aux | grep %s |grep -v grep |awk -F ' ' '{print $2}'" % keyword
        logger.info(command)
        result = os.popen(command, 'r').read()
        results = result.split()
        return results

    def install_sdk(self, sdk_num):
        '''
        remove live dirs and copy sdk to 1, 2, 3 ...
        '''
        logger.info("install_sdk")
        for i in range(1, sdk_num+1):
            folder = "{0}/{1}".format(LIVE_DIR, str(i))
            command = "rm -rf "+ folder
            logger.info(command)
            os.system(command)

            command = "mkdir " + folder
            logger.info(command)
            os.system(command)

            command = "cp {0}/{1} {2}".format(LIVE_DIR, P2PCLIENT, folder)
            logger.info(command)
            os.system(command)

    def install_sdk_for_idc(self, sdk_num):
        '''
        remove live dirs and copy sdk to 1, 2, 3 ...
        '''
        logger.info("install_sdk_for_idc")
        for i in range(1, sdk_num+1):
            folder = "{0}/{1}".format(IDC_LIVE_DIR, str(i))
            command = "rm -rf "+ folder
            logger.info(command)
            os.system(command)

            command = "mkdir " + folder
            logger.info(command)
            os.system(command)

            command = "cp {0}/{1} {2}".format(IDC_LIVE_DIR, LIVECLIENT, folder)
            logger.info(command)
            os.system(command)



    def StopAllVlcProcess(self):
        '''
        stop all vlc
        '''
        logger.info("StopAllVlcProcess")
        keyword = "vlc"
        self.KillProcessWithKeyword(keyword)

    def StartAllVlcProcess(self, peer_num, url, video_format='m3u8', user='admin'):
        '''
        start all vlc to play
        :peer_num:player number
        :url:sdk plays url
        :user:username，default:admin，root can not run vlc directly
        ************** ATTENTION ***************
        use silent mode for vlc，or "cvlc" command
        otherwise vlc fails due to no console
        #command = 'cvlc --novideo {0} &'.format(full_url)
        '''
        logger.info("StartAllVlcProcess")
        for i in range(1, peer_num + 1):
            port = (i - 1) * P2PCLIENT_PORT_STEP + P2PCLIENT_PORT
            full_url = self.format_live_url(port, url, video_format)
            #full_url = "http://vod.cloutropy.com/video1.mp4"
            command = 'su {0} -c "vlc -I dummy --novideo {1} >> /home/admin/vlc.log" &'.format(user, full_url)
            logger.info("VLC comand is: " + command)
            os.system(command)


    def StopAllVlcVodProcess(self):
        '''
        stop all vlc
        '''
        logger.info("StopAllVlcVodProcess")
        keyword = "vlc"
        self.KillProcessWithKeyword(keyword)


    def StartAllVlcVodProcess (self, peer_num, url, user='admin'):
        '''
        start all vlc to play
        :peer_num:player number
        :url:sdk plays url
        :user:username，default:admin，root can not run vlc directly
        ************** ATTENTION ***************
        use silent mode for vlc，or "cvlc" command
        otherwise vlc fails due to no console
        #command = 'cvlc --novideo {0} &'.format(full_url)
        '''
        logger.info("StartAllVlcVodProcess")
        for i in range(1, peer_num + 1):
            port = (i - 1) * P2PCLIENT_PORT_STEP + P2PCLIENT_PORT
            full_url = self.format_vod_url(port, url)
            command = 'su {0} -c "vlc -I dummy --repeat --novideo {1} >> /home/admin/vlc.log" &'.format(user, full_url)
            logger.info("VLC comand is: " + command)
            os.system(command)

    def format_live_url(self, port, url, video_format='m3u8'):
        # video_format : flv, m3u8
        return "http://localhost:{0}/live_{2}/user/simshi?url={1}".format(port, url, video_format)

    def format_vod_url(self, port, url):
        return "http://localhost:{0}/user/thunder/vod?url={1}".format(port, url)

    '''
    only for framework unit testing
    '''

    def ping(self):
        return True

    def now(self):
        return datetime.datetime.now()

    def show_type(self, arg):
        return (str(arg), str(type(arg)), arg)

    def raises_exception(self, msg):
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        data = bin.data
        response = Binary(data)
        return response

if __name__ == "__main__":
    '''
    start logging for debugging
    '''
    log_path = LOG_DIR
    BRIEF_LENGTH = 1024
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = log_path + "/live_test.log"
    handler = logging.handlers.RotatingFileHandler \
        (log_file, maxBytes=1024 * 1024, backupCount=5)
    fmt = '%(asctime)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger('ta')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("================================")
    logger.info("***** Live Automation Test *****")
    logger.info("================================")


    '''
    start service on 0.0.0.0 to listen to all interfaces
    '''
    server = SimpleXMLRPCServer(('0.0.0.0', RPC_PORT),
                                logRequests=True,
                                allow_none=True)

    server.register_introspection_functions()
    server.register_multicall_functions()
    server.register_instance(RpcService())

    try:
        print 'use control-c to exit'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'exiting'




