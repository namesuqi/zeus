#!/usr/bin/python
# coding=utf-8
"""
Change uid by iptables, interrupt one oss data transmission
This script should run on oss_edge machine, like 192.168.3.179
__Author__: JKZ
"""
import os
import time
import sys

interval_time = sys.argv[1]
oss_a = "192.168.3.180"
oss_b = "192.168.3.181"
# init
os.system("iptables -F")

time.sleep(int(interval_time))
while True:
    # print time.time()
    time.sleep(5)
    pid_180 = os.system("iptables -A INPUT -s %s -j DROP" % str(oss_a))
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "kill ", str(oss_a)
    time.sleep(int(interval_time))
    os.system("iptables -F")
    time.sleep(5)
    pid_181 = os.system("iptables -A INPUT -s %s -j DROP" % str(oss_b))
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "kill ", str(oss_b)
    time.sleep(int(interval_time))
    os.system("iptables -F")
