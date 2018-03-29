# coding=utf-8
"""
Join or Leave Leifeng sdk

Make sure your hosts file is correct

__author__ = 'zengyuetian'

"""

from lib.constant.request import *
from lib.utility.path import *
from lib.request.header_data import *
from lib.request.http_request import *
import time

# CHANNEL_INFO = [
#     "BA2C40F503AD91178CD6F5CCE37B1DB0",
#     "http://live.play.yunduan.cloutropy.com/live/test.flv",
#     "32"]

# CHANNEL_INFO = [
#     "85FA513E3D6E0A180657D2EA0C1E9DC1",
#     "http://flv.srs.cloutropy.com/wasu/test3.flv",
#     "32"]


CHANNEL_INFO = [
    "473F2DD6307695397D1B42A4D6574C4C",
    "http://flv.srs.cloutropy.com/wasu/test2.flv",
    "32"]

# CHANNEL_INFO = [
#     "23DA046BD3E2F06367C159534CE88A42",
#     "http://flv.srs.cloutropy.com/wasu/test.flv",
#     "32"]


STUN_IP = "stun-hub.cloutropy.com"
STUN_PORT = "8000"
# PUSH_SERVER = "live-push.cloutropy.com"
PUSH_SERVER = "flv.srs.cloutropy.com"

root = PathController.get_root_path()
peer_id_list_file = "{0}/utility/leifeng_controller/leifeng_peerid.txt".format(root)

# get peer ids from peer id list file, one line for one peer id
def get_peer_ids_from_list(peer_file):
    f = open(peer_file, "r")
    ids = []
    lines = f.readlines()
    for line in lines:
        ids.append(line.strip())
    f.close()
    return ids

# join leifeng via send request to stun server
def join_leifeng(httporhttps, stun_ip, stun_port, lf_id, cppc, file_info):
    url = "/join_lf"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    if type(lf_id) != list:
        lf_ids = [lf_id] # change lf_id type, str => list
    else:
        lf_ids = lf_id

    file_id, file_url, file_ppc = file_info

    body_data = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": lf_ids
        # "psize": int(864),
        # "ppc": int(file_ppc),
        # "cppc": int(cppc),
        # "push_server": PUSH_SERVER
    }

    resp = send_request(
        '[join leifeng]',
        httporhttps,
        POST,
        stun_ip,
        stun_port,
        url,
        headers,
        None,
        body_data
    )

    return resp


def leave_leifeng(httporhttps, stun_ip, stun_port, lf_id, file_info):
    url = "/rrpc/leave_leifeng"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    if type(lf_id) != list:
        lf_ids = [lf_id] # change lf_id type, str => list
    else:
        lf_ids = lf_id

    file_id = file_info[0]

    body_data = {
        "file_id": file_id,
        "peer_ids": lf_ids,
    }

    response = send_request(
        '[leave leifeng]',
        httporhttps,
        POST,
        stun_ip,
        stun_port,
        url,
        headers,
        None,
        body_data
    )

    return response

def join_test():
    # get peer id list
    peer_ids = get_peer_ids_from_list(peer_id_list_file)

    print "-------------------------------"
    for pid in peer_ids:
        print str(pid)
    print "-------------------------------"

    response = join_leifeng(HTTP, STUN_IP, STUN_PORT, peer_ids, "1", CHANNEL_INFO)
    print response

def leave_test():
    # get peer id list
    peer_ids = get_peer_ids_from_list(peer_id_list_file)

    print "-------------------------------"
    for pid in peer_ids:
        print str(pid)
    print "-------------------------------"

    response = leave_leifeng(HTTP, STUN_IP, STUN_PORT, peer_ids, CHANNEL_INFO)
    print response

def print_help():
    print "Please use : [join] or [leave]"

###############################################
#
#       Main Function Goes From Here
#
###############################################
if __name__ == "__main__":
    num = 0
    if len(sys.argv) == 1:
        join_test()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "join":
            while True:
                join_test()
                num += 1
                print num
                time.sleep(30*1)

        elif sys.argv[1] == "leave":
            leave_test()
        else:
            print_help()
    else:
        print_help()

