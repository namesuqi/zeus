# coding=utf-8
"""
ONLY used for LIVE testing

__author__ = 'zengyuetian'

"""

import xmlrpclib
from lib.constant.live import *

class Node(object):
    '''
    live related machine，seed: no play, peer: play
    sdk_num = peer_num+seed_num
    '''
    def __init__(self, ip, sdk_num):
        self._ip = ip
        self._sdk_num = sdk_num
        self._rpc_proxy = self.init_rpc_proxy()


    def init_rpc_proxy(self):
        '''
        init rpc server
        :return:void
        '''
        url = 'http://{0}:{1}'.format(self._ip, RPC_PORT)
        return xmlrpclib.ServerProxy(url)


    def peer_play(self, url, video_format='m3u8'):
        '''
        call vlc of node to play live via sdk
        :return:void
        '''
        self._rpc_proxy.StartAllVlcProcess(self._sdk_num, url, video_format)


    def peer_stop(self):
        '''
        stop vlc
        :return: void
        '''
        self._rpc_proxy.StopAllVlcProcess()

    def vod_peer_play(self, url):
        '''
        call vlc of node to play live via sdk
        :return:void
        '''
        self._rpc_proxy.StartAllVlcVodProcess(self._sdk_num, url)

    def vod_peer_stop(self):
        '''
        stop vlc
        :return: void
        '''
        self._rpc_proxy.StopAllVlcVodProcess()


    def start_sdk(self):
        '''
        start all sdk
        :return: void
        '''
        self._rpc_proxy.StartAllSdkProcess(self._sdk_num)

    def stop_sdk(self):
        '''
        stop all sdk
        :return: void
        '''
        self._rpc_proxy.StopAllSdkProcess()


    def start_idc(self):
        '''
        start sdk on idc
        :return: void
        '''
        print "start_idc in"
        self._rpc_proxy.StartAllIdcProcess(self._sdk_num, True)
        print "start_idc out"

    def start_leifeng(self):
        '''
        start all sdk
        :return: void
        '''
        print "start_leifeng in"
        self._rpc_proxy.StartAllIdcProcess(self._sdk_num, True)
        print "start_leifeng out"

    def stop_idc(self):
        '''
        stop sdk on idc
        :return: void
        '''
        self._rpc_proxy.StopAllIdcProcess()

    def stop_leifeng(self):
        '''
        stop all sdk on leifeng
        :return: void
        '''
        self._rpc_proxy.StopAllIdcProcess()

    def stop_some_idc(self):
        '''
        stop some idc sdk
        :return: void
        '''
        self._rpc_proxy.StopSomeIdcProcess(self._sdk_num)

    def stop_some_leifeng(self):
        '''
        stop some leifeng sdk
        :return: void
        '''
        self._rpc_proxy.StopSomeIdcProcess(self._sdk_num)

    def limit_speed(self):
        pass








