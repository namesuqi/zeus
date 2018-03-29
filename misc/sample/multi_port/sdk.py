# coding=utf-8
# author: zengyuetian

# !/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 30001
BUFSIZE = 1024

ADDR = (HOST, PORT)
sdk_net_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    data = "{0}->sdk".format(data)
    sdk_net_sock.sendto(data, ADDR)

    data, ADDR = sdk_net_sock.recvfrom(BUFSIZE)
    data = "{0}->sdk".format(data)
    if not data:
        break
    print data

sdk_net_sock.close()
