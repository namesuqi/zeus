# -*- coding: utf-8 -*-
"""
    mock udp 请求的 src ip 与 port
    stun go的压力测试会用到该库
    __author__ = 'sxl'
"""
import socket

import binascii
import dpkt


class MockSender:
    def __init__(self, dst, dport, src, sport=10000):
        self.dst = socket.gethostbyname(dst)
        self.dport = dport
        self.src = src
        self.sport = sport

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.sock.connect((self.dst, 1))

    def send(self, ip_packet):
        self.sock.sendall(str(ip_packet))

    def process(self, msg):
        u = dpkt.udp.UDP()
        u.sport = self.sport
        u.dport = self.dport
        u.data = msg
        u.ulen = len(u)

        # IP 的 str 会触发 IP 的校验和计算，也会触发 TCP UDP 的校验和计算
        # TCP/UDP的校验和是： 源IP，目的IP，协议，TCP或UDP包（头+内容）
        # u.sum = ?

        i = dpkt.ip.IP(data=u)
        # i.off = dpkt.ip.IP_DF # frag off
        i.p = dpkt.ip.IP_PROTO_UDP
        i.src = socket.inet_aton(self.src)  # xp sp2之后 禁止发送非本机IP地址的数据包；linux, server无限制
        i.dst = socket.inet_aton(self.dst)
        i.len = len(i)

        self.send(i)

    def __del__(self):
        self.sock.close()


def send_mock_src_ip_request(dst_ip, dst_port, src_ip, src_port, send_data):
    sender = MockSender(dst=dst_ip, dport=dst_port, src=src_ip, sport=src_port)
    sender.process(binascii.a2b_hex(send_data))


if __name__ == '__main__':
    # send_data = nat_update_req_data('6666666666ABCDEABCDEABCDE1000000', 1, "192.168.1.39", 60000, True)
    # print send_data
    # send_mock_src_ip_request('192.168.1.202', 9000, '192.168.1.254', 60001, send_data)
    # rsp = sdk_nat_update_req('192.168.1.202', 9000, '6666666666ABCDEABCDEABCDE1000000', 1, "192.168.1.39", 60000, 60000
    #                          , True)
    # print parse_stun_rsp_data(rsp)
    pass
