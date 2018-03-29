# coding=utf-8
"""
idc, leifeng, live testsuite related functions and keywords

__author__ = 'zengyuetian'

"""

from lib.decorator.trace import *
from lib.decorator.log import *
from lib.constant.live import *
from lib.constant.idc import *
from lib.constant.leifeng import *
from lib.constant.vod import *
from lib.environment.node import Node


class Live(object):
    '''
    assign sdk number according to constant data list
    '''

    def __init__(self):
        self.seed_host_num = None
        self.peer_host_num = None
        self.vod_peer_host_num = None
        self.idc_host_num = None
        self.leifeng_host_num = None
        self.seed_node_list = None
        self.peer_node_list = None
        self.vod_peer_node_list = None
        self.idc_node_list = None
        self.leifeng_node_list = None

    @print_trace
    def InitSdkNumForSeed(self, host_num, sdk_num=None):
        '''
        init seed node list
        :param host_num: seed machine number
        :param sdk_num: sdk number for every host
        :return:void
        '''
        self.seed_host_num = int(host_num)
        self.seed_node_list = []
        for i in range(self.seed_host_num):
            if sdk_num is None:
                node = Node(SEED_IP_LIST[i], SEED_SDK_NUM_LIST[i])
            else:
                node = Node(SEED_IP_LIST[i], int(sdk_num))
            self.seed_node_list.append(node)

    @print_trace
    def InitSdkNumForPeer(self, host_num=None, sdk_num=None):
        '''
        init peer node list
        :param host_num: peer host number
        :param sdk_num: sdk number for every host
        :return:void
        '''
        if host_num is None:
            host_num = len(PEER_IP_LIST)
        self.peer_host_num = int(host_num)
        self.peer_node_list = []
        for i in range(self.peer_host_num):
            if sdk_num is None:
                node = Node(PEER_IP_LIST[i], PEER_SDK_NUM_LIST[i])
            else:
                node = Node(PEER_IP_LIST[i], int(sdk_num))
            self.peer_node_list.append(node)

    @print_trace
    def InitSdkNumForVodPeer(self, host_num, sdk_num=None):
        '''
        init vod peer node list
        :param host_num: peer host number
        :param sdk_num: sdk number for every host
        :return:void
        '''
        self.vod_peer_host_num = int(host_num)
        self.vod_peer_node_list = []
        for i in range(self.vod_peer_host_num):
            if sdk_num is None:
                node = Node(VOD_IP_LIST[i], VOD_SDK_NUM_LIST[i])
            else:
                node = Node(VOD_IP_LIST[i], int(sdk_num))
            self.vod_peer_node_list.append(node)

    @print_trace
    def InitSdkNumForIDC(self, host_num=None, sdk_num=None):
        '''
        init IDC node list
        :param host_num: idc machine number
        :param sdk_num: sdk number
        :return:void
        '''
        print "InitSdkNumForIDC in"
        if host_num is None:
            host_num = len(IDC_IP_LIST)
        self.idc_host_num = int(host_num)
        self.idc_node_list = []
        for i in range(self.idc_host_num):
            if sdk_num is None:
                node = Node(IDC_IP_LIST[i], IDC_SDK_NUM_LIST[i])
            else:
                node = Node(IDC_IP_LIST[i], int(sdk_num))
            self.idc_node_list.append(node)
        print "InitSdkNumForIDC out"

    @print_trace
    def InitKillSdkNumForIDC(self, host_num, sdk_num=None):
        '''
        int IDC node list
        :param host_num: idc machine
        :param sdk_num: how many sdk process will be kill
        :return:void
        '''
        print "InitKillSdkNumForIDC in"
        self.idc_host_num = int(host_num)
        self.idc_node_list = []
        for i in range(self.idc_host_num):
            if sdk_num is None:
                node = Node(IDC_IP_LIST[i], IDC_SDK_NUM_TO_KILL[i])
            else:
                node = Node(IDC_IP_LIST[i], int(sdk_num))
            self.idc_node_list.append(node)
        print "InitKillSdkNumForIDC out"

    @print_trace
    def InitSdkNumForLeifeng(self, host_num=None, sdk_num=None):
        '''
        init Leifeng node list
        :param host_num: leifeng number
        :param sdk_num: sdk number
        :return:void
        '''
        print "InitSdkNumForLeifeng in"
        if host_num is None:
            host_num = len(LEIFENG_IP_LIST)
        self.leifeng_host_num = int(host_num)
        self.leifeng_node_list = []
        for i in range(self.leifeng_host_num):
            if sdk_num is None:
                node = Node(LEIFENG_IP_LIST[i], LEIFENG_SDK_NUM_LIST[i])
            else:
                node = Node(LEIFENG_IP_LIST[i], int(sdk_num))
            self.leifeng_node_list.append(node)
        print "InitSdkNumForLeifeng out"

    @print_trace
    def InitKillSdkNumForLeifeng(self, host_num, sdk_num=None):
        '''
        int IDC node list
        :param host_num: idc machine
        :param sdk_num: how many sdk process will be kill
        :return:void
        '''
        print "InitKillSdkNumForLeifeng in"
        self.leifeng_host_num = int(host_num)
        self.leifeng_node_list = []
        for i in range(self.leifeng_host_num):
            if sdk_num is None:
                node = Node(LEIFENG_IP_LIST[i], LEIFENG_SDK_NUM_TO_KILL[i])
            else:
                node = Node(LEIFENG_IP_LIST[i], int(sdk_num))
            self.leifeng_node_list.append(node)
        print "InitKillSdkNumForLeifeng out"

    @print_trace
    def StopSdkForSeed(self):
        '''
        stop all sdk on seed
        :return:
        '''
        for node in self.seed_node_list:
            node.stop_sdk()

    @print_trace
    def StopSdkForPeer(self):
        '''
        stop all sdk on peer
        :return:void
        '''
        for node in self.peer_node_list:
            node.stop_sdk()

    @print_trace
    def StopSdkForVodPeer (self):
        '''
        stop all sdk on vod peer
        :return:void
        '''
        for node in self.vod_peer_node_list:
            node.stop_sdk()


    @print_trace
    def StopSdkForIDC(self):
        '''
        stop all sdk process on idc
        :return:void
        '''
        print "StopSdkForIDC in"
        for node in self.idc_node_list:
            print node._ip + " is stopping"
            node.stop_idc()
        print "StopSdkForIDC out"

    @print_trace
    def StopSdkForLeifeng(self):
        '''
        stop all leifeng sdk process
        :return:void
        '''
        print "StopSdkForLeifeng in"
        for node in self.leifeng_node_list:
            print node._ip + " is stopping"
            node.stop_leifeng()
        print "StopSdkForLeifeng out"

    @print_trace
    def StopSomeSdkForIDC(self):
        '''
        stop some sdk processes on idc
        :return:void
        '''
        print "StopSomeSdkForIDC in"
        for node in self.idc_node_list:
            print node._ip + " is stopping"
            node.stop_some_idc()
        print "StopSomeSdkForIDC out"

    @print_trace
    def StopSomeSdkForLeifeng(self):
        '''
        stop some sdk processes on leifeng
        :return:void
        '''
        print "StopSomeSdkForLeifeng in"
        for node in self.leifeng_node_list:
            print node._ip + " is stopping"
            node.stop_some_leifeng()
        print "StopSomeSdkForLeifeng out"

    @print_trace
    def StartSdkForSeed(self):
        '''
        start sdk on seed
        :return:void
        '''
        for node in self.seed_node_list:
            print node._ip + " is starting"
            node.start_sdk()

    @print_trace
    def StartSdkForIDC(self):
        '''
        start sdk on idc
        :return:void
        '''
        print "StartSdkForIDC in"
        for node in self.idc_node_list:
            print node._ip + " is starting"
            node.start_idc()
        print "StartSdkForIDC out"

    @print_trace
    def StartSdkForLeifeng(self):
        '''
        start sdk on leifeng
        :return:void
        '''
        print "StartSdkForLeifeng in"
        for node in self.leifeng_node_list:
            print node._ip + " is starting"
            node.start_leifeng()
        print "StartSdkForLeifeng out"

    @print_trace
    def StartSdkForPeer(self):
        '''
        start sdk on peer
        :return:void
        '''
        for node in self.peer_node_list:
            node.start_sdk()

    @print_trace
    def StartSdkForVodPeer(self):
        '''
        start sdk on vod peer
        :return:void
        '''
        for node in self.vod_peer_node_list:
            print node._ip + " is starting"
            node.start_sdk()

    @print_trace
    @log_func_args
    def StartLiveForPeer(self, url, video_format='m3u8'):
        '''
        start vlc to play on peer
        :return:void
        '''
        for node in self.peer_node_list:
            node.peer_play(url, video_format)

    @print_trace
    @log_func_args
    def StopLiveForPeer(self):
        '''
        stop vlc on peer
        :return:void
        '''
        for node in self.peer_node_list:
            print node._ip + " is stopping"
            node.peer_stop()

    @print_trace
    @log_func_args
    def StartVodForPeer(self, url):
        '''
        start vlc to play on peer
        :return:void
        '''
        for node in self.vod_peer_node_list:
            print node._ip + " is starting"
            node.vod_peer_play(url)

    @print_trace
    @log_func_args
    def StopVodForPeer(self):
        '''
        stop vlc on peer
        :return:void
        '''
        for node in self.vod_peer_node_list:
            print node._ip + " is stopping"
            node.vod_peer_stop()



    def recalculate_num(self, machine_num, seed_num, peer_num):
        # formalize sdk number
        self.seed_num = self.normalize_num(machine_num, seed_num)
        self.seed_num_per_machine = self.seed_num / machine_num
        self.peer_num = self.normalize_num(machine_num, peer_num)
        self.peer_num_per_machine = self.peer_num / machine_num

        print "seed_num:{0}, seed_num_per_machine:{1}, peer_num:{2}, peer_num_per_machine:{3}". \
            format(self.seed_num, self.seed_num_per_machine, self.peer_num, self.peer_num_per_machine)


    def normalize_num(self, machine_num, num):
        if num % machine_num != 0:
            num = (num/machine_num + 1) * machine_num
        print num
        return num


if __name__ == "__main__":
    live = Live()












