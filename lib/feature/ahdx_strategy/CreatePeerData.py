# coding=utf-8
"""
将随机生成的peer信息写入TXT

"""
import json
import socket
from random import Random, random

import struct
import os
from lib.decorator.trace import *
from lib.feature.ahdx_strategy.RangePeerInfo import RangePeerInfo


class CreatePeerData(object):

    @print_trace
    def CreatePeerId(self, peer_nums=20):

        PEER_ID = RangePeerInfo().RangePeerId(int(peer_nums))

        with open(os.path.abspath(os.path.dirname(__file__)) + "/peerid.txt", "w") as f:
            json.dump(PEER_ID, f)  # 将peerID信息写入当前目录下的peerid.txt中


    @print_trace
    def CreatePeerBody(self, peer_nums=20):

        PEER_BODY = RangePeerInfo().RangePeerBody(int(peer_nums))

        with open(os.path.abspath(os.path.dirname(__file__)) + "/peerbody.txt", "w") as f:
            json.dump(PEER_BODY, f)  # 将peer_body信息写入当前目录下的peerbody.txt中

    @print_trace
    def ReadPeerInfo(self):
        '''
        将peerid.txt和peerbody.txt中的数据读取出来，并返回peerid和peerbody
        :return:
        '''

        with open(os.path.abspath(os.path.dirname(__file__)) + "/peerid.txt", "r") as f:
            PEER_ID = json.load(f)

        with open(os.path.abspath(os.path.dirname(__file__)) + "/peerbody.txt", "r") as f:
            PEER_BODY = json.load(f)

        return (PEER_ID, PEER_BODY)


    @print_trace
    def CreateFlowId(self, randomlength):
        """
        随机生成Flow汇报的id
        :param randomlength:
        :return:
        """
        id_str = ''
        chars = 'ABCDE0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            id_str += chars[random.randint(0, length)]
        return id_str

    @print_trace
    def CreatePeerIdData(self, peer_nums=20):
        data = ""
        data1 = ""
        PEER_ID = RangePeerInfo().RangePeerId(int(peer_nums))
        for i in range(0, int(peer_nums)):
            data = data + PEER_ID[i] + ",\n"
            data1 = data1 + '"' + PEER_ID[i] + '",\n'
        fileHandle =  open(os.path.abspath(os.path.dirname(__file__)) + "/peerid1.txt", "w")
        fileHandle.write(data)
        fileHandle =  open(os.path.abspath(os.path.dirname(__file__)) + "/peerid2.txt", "w")
        fileHandle.write(data1)

    @print_trace
    def CreatePeerBodyData(self, peer_nums=20):
        data = ""
        PEER_BODY = RangePeerInfo().RangePeerBodyData(int(peer_nums))
        for i in range(0, int(peer_nums)):
            data = data + PEER_BODY[i] + "\n"
        fileHandle =  open(os.path.abspath(os.path.dirname(__file__)) + "/peerbody2.txt", "w")
        fileHandle.write(data)

if __name__ == "__main__":

        #CreatePeerData().CreatePeerId(200)
        #CreatePeerData().CreatePeerBody(200)
        #CreatePeerData().CreateFlowId(32)
        #print os.path.abspath(os.path.dirname(__file__))
        CreatePeerData().CreatePeerBodyData(1000)


else:
    pass
