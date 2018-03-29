# coding=utf-8
# author: TangHong
# propose: create live push monitor for kafka reading
# steps:   create 600 different ip addresses

import random
import time
import os

LOG_FILE = "/home/admin/logs/livepush_monitor_topic_network.log"


def write_network_log(name, timestamp, receive, transmit, ip, host):
    """
    根据传入的参数，写一行log到日志文件
    :param name: 网卡名
    :param timestamp: 时间戳
    :param receive: 该网卡收到的数据流量
    :param transmit: 该网卡发出的数据流量
    :param ip: 网卡地址
    :param host: 机器唯一标识
    :return: none
    """
    line = "topic=network_card_flow\x1f" \
           "name={0}\x1f" \
           "timestamp={1}\x1f" \
           "receive={2}\x1f" \
           "transmit={3}\x1f" \
           "ip={4}\x1f" \
           "host_id={5}\x1f" \
           "detail_info=test" \
        .format(name, timestamp, receive, transmit, ip, host)

    os.system('echo {0} >> {1}'.format(line, LOG_FILE))
    print "write network logs"


if __name__ == "__main__":

    ips = set()  # a set to contains ip addresses
    group_num = 10
    net_name = ["net0", "net1", "net2"]
    part1 = [1, 1, 1, 116, 1, 1, 1, 202, 123, 202]
    part2 = [24, 4, 116, 62, 32, 50, 51, 97, 80, 97]
    part3 = [24, 4, 0, 4, 192, 0, 128, 38, 168, 40]

    while True:
        timestamp = int(time.time())
        print "---------------------------"
        print timestamp

        name = random.choice(net_name)
        receive_num = random.randint(60000000, 100000000)
        transmit_num = random.randint(50000000, 60000000)
        part4_value = str(random.randint(1, 60))
        host_id = timestamp

        for i in range(group_num):
            ip = str(part1[i]) + "." + str(part2[i]) + "." + str(part3[i]) + "." + part4_value
            write_network_log(name, timestamp, receive_num, transmit_num, ip, host_id)
            ips.add(ip)

        time.sleep(1)  # write 10 logs per second
        print("Total ip address number is {0}".format(len(ips)))
