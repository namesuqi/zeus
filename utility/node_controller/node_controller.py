# coding=utf-8
"""
this script running on robot framework machine which can access idc machines

Usage:
$ python utility/node_controller/node_controller.py <type>

The types list as following:
    start       (deploy and start sdk on remote machines - use new sdk, remove old sdk)
    stop        (stop sdk on remote machines and leave leifeng)
    restart     (restart sdk on remote machines - use old sdk)
    peer_id     (only get peer id list from remote machines)

__author__ = 'zengyuetian'

"""

from lib.remote.remote_player import *
from lib.remote.remote_sdk import *
from lib.request.http_request import *

# bj test environment
LEIFENG_IP_LIST = ['122.228.207.106', '58.53.94.36', '61.164.110.152', '61.160.221.183', '61.191.61.133']
LEIFENG_SDK_NUM_LIST = [20, 20, 20, 20, 20]

# product environment
"""
LEIFENG_IP_LIST = ['222.222.12.12', '101.254.185.18', '124.68.11.169', '115.238.245.25', '103.246.152.47',
                   '122.226.181.111', '60.12.69.100', '60.169.74.3', '221.203.235.2', '222.175.232.115',
                   '59.63.166.73', '60.12.145.12']
LEIFENG_SDK_NUM_LIST = [i*4 for i in [8, 8, 4, 4, 4, 4, 4, 4, 8, 4, 8, 4]]


# 9.2 downstream bandwidth test  5 idc
LEIFENG_IP_LIST = ['222.222.12.12', '101.254.185.18', '60.169.74.3', '221.203.235.2',
                   '59.63.166.73']
LEIFENG_SDK_NUM_LIST = [20, 20, 20, 20, 20]
"""

username = "admin"; password = ""
root = PathController.get_root_path()
local_sdk = "{0}/utility/node_controller/liveclient_static".format(root)
peer_info_file = "{0}/utility/node_controller/yunshang.conf.txt".format(root)


# get peer ids from remote machines
def get_peer_ids(peer_file):
    f = open(peer_file, "r")
    ids = []
    lines = f.readlines()
    for line in lines:
        peer_id = json.loads(line).get("peer_id", None)
        ids.append(peer_id)
    f.close()
    return ids


# get peer ids from peer id list file, one line for one peer id
def get_peer_ids_from_list(peer_file):
    f = open(peer_file, "r")
    ids = []
    lines = f.readlines()
    for line in lines:
        ids.append(line.strip())
    f.close()
    return ids


def stop_test():
    player = RemotePlayer(LEIFENG_IP_LIST, LEIFENG_SDK_NUM_LIST, [], local_sdk, username=username, password=password)
    player.stop_sdk()


def start_test():
    player = RemotePlayer(LEIFENG_IP_LIST, LEIFENG_SDK_NUM_LIST, [], local_sdk, username=username, password=password)
    player.stop_sdk()
    player.deploy_sdk()
    player.start_sdk()

    # collect peer ids
    get_peer_info(LEIFENG_IP_LIST, username, password, LEIFENG_SDK_NUM_LIST, peer_info_file)

    # get peer id list
    peer_ids = get_peer_ids(peer_info_file)
    print "-------------------------------"
    print "##### total leifeng {0} #####".format(len(peer_ids))
    for index, ip in enumerate(LEIFENG_IP_LIST):
        print "##### {0} has {1} leifeng #####".format(ip, LEIFENG_SDK_NUM_LIST[index])
        for i in range(LEIFENG_SDK_NUM_LIST[index]):
            print peer_ids[0]
            del peer_ids[0]
    print "-------------------------------"


def restart_test():
    player = RemotePlayer(LEIFENG_IP_LIST, LEIFENG_SDK_NUM_LIST, [], local_sdk, username=username, password=password)
    player.stop_sdk()
    player.restart_sdk()

    # collect peer ids
    get_peer_info(LEIFENG_IP_LIST, username, password, LEIFENG_SDK_NUM_LIST, peer_info_file)

    # get peer id list
    peer_ids = get_peer_ids(peer_info_file)
    print "-------------------------------"
    print "##### total leifeng {0} #####".format(len(peer_ids))
    for index, ip in enumerate(LEIFENG_IP_LIST):
        print "##### {0} has {1} leifeng #####".format(ip, LEIFENG_SDK_NUM_LIST[index])
        for i in range(LEIFENG_SDK_NUM_LIST[index]):
            print peer_ids[0]
            del peer_ids[0]
    print "-------------------------------"


def peer_id_test():
    # collect peer ids
    get_peer_info(LEIFENG_IP_LIST, username, password, LEIFENG_SDK_NUM_LIST, peer_info_file)

    # get peer id list
    peer_ids = get_peer_ids(peer_info_file)
    print "-------------------------------"
    print "##### total leifeng {0} #####".format(len(peer_ids))
    for index, ip in enumerate(LEIFENG_IP_LIST):
        print "##### {0} has {1} leifeng #####".format(ip, LEIFENG_SDK_NUM_LIST[index])
        for i in range(LEIFENG_SDK_NUM_LIST[index]):
            print peer_ids[0]
            del peer_ids[0]
    print "-------------------------------"


def print_help():
    print "Please use control type: [start] or [restart] or [stop] or [peer_id]"


###############################################
#
#       Main Function Goes From Here
#
###############################################
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
    else:
        if sys.argv[1] == "start":
            start_test()
        elif sys.argv[1] == "restart":
            restart_test()
        elif sys.argv[1] == "stop":
            stop_test()
        elif sys.argv[1] == "peer_id":
            peer_id_test()
        else:
            print_help()
