# coding=utf-8
"""
随机生成一定数量的peerid 和 peer_body列表

"""

import socket
from random import Random, random

import struct

from lib.decorator.trace import *

class RangePeerInfo(object):

    def __init__(self):
        self.peer_id_list = []
        self.peer_body_list = []


    @print_trace
    def RangePeerId(self, peer_nums=20):
        '''
        随机生成一定数量的peer_id列表，默认生成20个
        :param peer_nums: peer_id数量
        :return:
        '''

        for i in range(peer_nums):
            peer_id = RangePeerInfo().GetRandomId()
            self.peer_id_list.append(peer_id)

        return self.peer_id_list

    @print_trace
    def RangePeerBody(self, peer_nums=20):
        '''
        随机生成一定数量的peer_body（peer login需要的数据），默认生成20个
        :param peer_nums:
        :return:
        '''
        for i in range(peer_nums):
            peer_ip = RangePeerInfo().GetRandomIp()
            peer_body = {'natType': 0, 'privateIP': peer_ip, 'publicIP': peer_ip, 'version': '2.3.0', 'privatePort': 53155, 'publicPort': 53155}
            self.peer_body_list.append(peer_body)

        return self.peer_body_list


    @print_trace
    def GetRandomId(self, randomlength=20):
        '''
        生成32位字符串，且前八位为可设定的prefix
        :param randomlength: 需要随机生成的字符串长度
        :return:
        '''
        prefix = "00010040"
        id_str = ''
        chars = 'ABCDE0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            id_str += chars[random.randint(0, length)]
        last_str = "AAAA"
        peer_id = prefix + id_str + last_str

        return peer_id


    @print_trace
    def GetRandomIp(self):
        '''
        随机生成IP
        :return:
        '''

        RANDOM_IP_POOL = ['192.168.10.222/0']
        random = Random()
        str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
        str_ip_addr = str_ip.split('/')[0]
        str_ip_mask = str_ip.split('/')[1]
        ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
        mask = 0x0
        for i in range(31, 31 - int(str_ip_mask), -1):
            mask = mask | ( 1 << i)
        ip_addr_min = ip_addr & (mask & 0xffffffff)
        ip_addr_max = ip_addr | (~mask & 0xffffffff)

        return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

    @print_trace
    def RangePeerBodyData(self, peer_nums=20):
        '''
        随机生成一定数量的peer_body（peer login需要的数据），默认生成20个
        :param peer_nums:
        :return:
        '''
        for i in range(peer_nums):
            peer_ip = RangePeerInfo().GetRandomIp()
            peer_body = '0,"' + peer_ip + '","' + peer_ip + '",' + '"2.3.0",53155,53155'
            self.peer_body_list.append(peer_body)

        return self.peer_body_list


if __name__ == "__main__":

    # print Peer_data().get_random_id()
    # print Peer_data().get_random_ip()
    # print Peer_data().range_peer_id()
    # s = Peer_data().range_peer_body()
    # print s[0]

    pass
