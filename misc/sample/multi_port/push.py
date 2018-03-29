# coding=utf-8
# author: zengyuetian

from socket import *
from time import ctime

HOST = '127.0.0.1'
NET_PUSH_PORT = 30002
BUFSIZE = 1024

NET_PUSH_ADDR = (HOST, NET_PUSH_PORT)

net_push_sock = socket(AF_INET, SOCK_DGRAM)
net_push_sock.bind(NET_PUSH_ADDR)

while True:
    print 'wating for message...'
    data, addr = net_push_sock.recvfrom(BUFSIZE)
    print "...received data is ", data
    print '...received from and retuned to:', addr

    data = "{0}->push".format(data)
    print '...send data:', data
    net_push_sock.sendto(data, addr)


net_push_sock.close()