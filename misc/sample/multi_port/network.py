# coding=utf-8
# author: zengyuetian

# !/usr/bin/env python
# -*- coding:UTF-8 -*-

from socket import *
from time import ctime

SDK_NET_HOST = '127.0.0.1'

SDK_NET_PORT = 30001
NET_PUSH_PORT = 30002
BUFSIZE = 1024

SDK_NET_ADDR = (SDK_NET_HOST, SDK_NET_PORT)
sdk_net_sock = socket(AF_INET, SOCK_DGRAM)
sdk_net_sock.bind(SDK_NET_ADDR)

NET_PUSH_ADDR = (SDK_NET_HOST, NET_PUSH_PORT)
net_push_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    print 'wating for message...'
    data, addr1 = sdk_net_sock.recvfrom(BUFSIZE)

    data = "{0}->net".format(data)
    net_push_sock.sendto(data, NET_PUSH_ADDR)
    print "...received data is ", data

    data, addr2 = net_push_sock.recvfrom(BUFSIZE)
    data = "{0}->net".format(data)
    sdk_net_sock.sendto(data, addr1)
    print "...send data is ", data
    print '...send to:', addr1

sdk_net_sock.close()