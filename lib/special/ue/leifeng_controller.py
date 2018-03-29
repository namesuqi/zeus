# coding=utf-8
# control leifeng
# author: zengyuetian

from lib.interface.cp.stun_server import join_leifeng
from lib.special.ue.sdk_controller import *


@print_trace
def start_deploy_lf(ip, lf_num):
    deploy_lf(ip, lf_num)


@print_trace
def start_lf(ip, lf_num, port=LF_PORT_START):
    start_lf_sdk(ip, lf_num, port)


@print_trace
def stop_lf(ip):
    stop_sdk(ip)
    deploy_lf_clean(ip)


@print_trace
def get_lf_peer_id_list(ip, lf_num, port=LF_PORT_START):
    peer_ids = list()
    count = 0
    for i in range(lf_num):
        url = "http://{0}:{1}{2}".format(ip, port + count, "/ajax/conf")
        headers = dict()
        headers["accept"] = 'application/json'
        headers["content-type"] = 'application/json'
        res = requests.get(url, headers=headers)
        peer_id = json.loads(res.content).get("peer_id", None)
        # cmd = "curl http://{0}:{1}{2}".format(ip, port + count, "/ajax/conf")
        # result = remote_execute_result(ip, ROOT_USER, ROOT_PASSWD, cmd)
        # peer_id = json.loads(result).get("peer_id", None)
        peer_ids.append(peer_id)
        count += 3
    if len(peer_ids) != lf_num:
        print "#########################################"
        print "## JOIN LF FAIL!!! EXPECT {0} ,REAL {1} ##".format(lf_num, len(peer_ids))
        print "#########################################"
        exit(0)

    return peer_ids


@print_trace
def start_join_lf(peer_ids):
    if peer_ids is []:
        print "JOIN LF FAIL! LF LIST IS NONE"
        exit(0)
    rsp = join_leifeng('HTTP', STUN_THUNDER_IP, STUN_THUNDER_PORT, file_id=FILE_ID, file_url=FILE_URL, peer_ids=peer_ids)
    if rsp.text.find('sent_count'):
        pass
    else:
        print "#########################################"
        print "##########   JOIN LF FAIL!!!  ###########"
        print "#########################################"


@print_trace
def check_lf_num(ip):
    check_cmd = "ps aux | grep ys_| grep -v grep| wc -l"
    result = remote_execute_result(ip, ADMIN_USER, ADMIN_PASSWD, check_cmd)
    return int(result)


def lf_main(lf_num):
    if check_lf_num(LF_IP) == lf_num * 2:
        pass
    else:
        deploy_lf_clean(LF_IP)
        start_deploy_lf(LF_IP, lf_num)
        start_lf(LF_IP, lf_num)
        peer_ids = get_lf_peer_id_list(LF_IP, lf_num)
        time.sleep(20)
        start_join_lf(peer_ids)


if __name__ == '__main__':
    lf_main(3)


