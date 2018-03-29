# coding=utf-8
# author: zengyuetian

import uuid
from random import choice
import random
import json
# import demjson

pc_info_list = []
memory_M_list = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
memory_K_list = map(lambda x: x*1024, memory_M_list)
cpu_list = [1, 2, 4, 8, 16, 32, 64]
disk_G_list = [1, 2, 5, 10, 40, 80, 100, 256, 512, 1024, 2048]
disk_B_list = map(lambda x: x*1024*1024*1024, disk_G_list)

server_name_list = ['push-mgr', 'sparkCluster', 'kafka', 'flumeMonitor', 'collector', 'redis-single', 'upgrade',
                    'courier', 'live-channel', 'tracker_go', 'seed-mgr', 'tracker', 'redis-mq', 'channel-mgr',
                    'live-push/flat-flv-srv', 'stun', 'redis-cluster', 'funnel', 'RDS', 'opsPanel', 'recorder-ts',
                    'opsMonitor', 'flumeConf5rv', 'opsStats', 'sparkStreaming', 'mongod', 'stun-redis',
                    'upload', 'mongos', 'dir']

def create_random_mac():
    """
    生成随机MAC地址
    :return:
    """
    mac = [0x52, 0x54, 0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%x" % x, mac))


def create_net_card_dict(index):
    """
    创建网卡信息的字典
    :param index:
    :return:
    """
    return {
        "network_cards": [
            {
                "name": "eth0",
                "ip": "192.168.0.{0}".format(index),
                "mac": create_random_mac()
            },
            {
                "name": "eth1",
                "ip": "192.168.1.{0}".format(index),
                "mac": create_random_mac()
            },
            {
                "name": "eth2",
                "ip": "192.168.2.{0}".format(index),
                "mac": create_random_mac()
            }
        ]
    }


if __name__ == "__main__":
    for i in range(100):
        node = dict()
        node["hostname"] = str(uuid.uuid1()).replace("-", "")
        node["cpu"] = {"cpus": choice(cpu_list)}
        node["mem"] = {"capacity": choice(memory_K_list)}
        node["disk"] = {"capacity": choice(disk_B_list)}
        node["net"] = create_net_card_dict(i)
        node["server_name"] = choice(server_name_list)
        pc_info_list.append(node)

    new_json = json.dumps(pc_info_list)
    print new_json
