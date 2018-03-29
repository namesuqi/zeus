# coding=utf-8
# author=JKZ
import hashlib
import json
import redis
import requests
from rediscluster import StrictRedisCluster
from simplejson import JSONEncoder

REDIS_CLUSTER_NODES = [{"host": "172.16.2.169", "port": 6379},
                       {"host": "172.16.2.170", "port": 6379},
                       {"host": "172.16.2.171", "port": 6379}]
REDIS_SINGLE_HOST = "172.16.2.168"
REDIS_SINGLE_PORT = 6379

STUN_HUB_HOST = "172.16.2.169"
STUN_HUB_PORT = 8000

STUN_PUB_IP = "47.93.61.152"
STUN_PRI_IP = "172.16.2.168"


def get_file_id_by_md5(file_url, rules=True):
    file_url = str(file_url)
    if rules:
        if file_url.startswith("http://"):
            file_url = file_url[7:]
        else:
            print "This file_url '%s' is not correct" % str(file_url)
    file_id = str(hashlib.md5(file_url).hexdigest()).upper()
    return file_id


def get_peer_ids_from_redis(redis_cluster_hosts):
    """
    get all peer_id PNIC_ form redis-cluster
    :param redis_cluster_hosts:
    :return:
    """

    rc = StrictRedisCluster(startup_nodes=redis_cluster_hosts, decode_responses=True)
    match_keys = rc.keys("PNIC_*")
    peer_id_list = list()
    for pnic_key in match_keys:
        peer_id = str(pnic_key)[5:]
        peer_id_list.append(peer_id)
    return peer_id_list


def get_file_urls_from_redis(redis_single_host, redis_single_port):
    """
    get all file_url F1_{file_url}_FLV from redis-single
    :param redis_single_host:
    :param redis_single_port:
    :return:
    """
    rc = redis.StrictRedis(host=redis_single_host, port=redis_single_port, db=0)
    match_keys = rc.keys("F1_*")
    file_url_list = list()
    for file_key in match_keys:
        file_url = str(file_key)[3:-4]
        file_url_list.append(file_url)
    return file_url_list


def join_leifeng(host, port, file_id, file_url, peer_ids):
    """
    send join_lf request to stun-hub
    :param host:
    :param port:
    :param file_url:
    :param peer_ids:
    :param file_id:
    :return:
    """

    url = "http://" + str(host) + ":" + str(port) + "/join_lf"

    headers = dict()
    headers['content-type'] = 'application/json'
    headers['accept'] = 'application/json'

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": peer_ids
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(body_data))

    print "##############  join LF  #################"
    print "status_code: {0}".format(response.status_code)
    print "url: {0}".format(url)
    print "data: {0}".format(body_data)
    print "resp: {0}".format(response.text)
    print "########################################"
    return response


def leave_leifeng(host, port, file_id, peer_ids):
    """
    send leave_lf request to stun-hub
    :param host:
    :param port:
    :param file_id:
    :param peer_ids:
    :return:
    """

    url = "http://" + str(host) + ":" + str(port) + "/leave_lf"

    headers = dict()
    headers['content-type'] = 'application/json'
    headers['accept'] = 'application/json'

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "peer_ids": peer_ids
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(body_data))

    print "##############  leave LF  #################"
    print "status_code: {0}".format(response.status_code)
    print "url: {0}".format(url)
    print "data: {0}".format(body_data)
    print "text: {0}".format(response.text)
    print "########################################"
    return response


def lpush_rrpc_join_lf(redis_single_host, redis_single_port, stun_ip, file_id, file_url, peer_ids):
    rc = redis.StrictRedis(host=redis_single_host, port=redis_single_port, db=0)
    RRPC_KEY = "RRPC_" + str(stun_ip)
    if type(peer_ids) is not list: peer_ids = [peer_ids]
    value = {
        "cmd": "join_lf",
        "file_id": str(file_id),
        "file_url": str(file_url),
        "peer_ids": peer_ids
    }
    # 将dict转成json格式
    value = JSONEncoder().encode(value)
    rc.lpush(RRPC_KEY, value)


def lpush_rrpc_leave_lf(redis_single_host, redis_single_port, stun_ip, file_id, peer_ids):
    rc = redis.StrictRedis(host=redis_single_host, port=redis_single_port, db=0)
    RRPC_KEY = "RRPC_" + str(stun_ip)
    if type(peer_ids) is not list: peer_ids = [peer_ids]
    value = {
        "cmd": "leave_lf",
        "file_id": str(file_id),
        "peer_ids": peer_ids
    }
    # 将dict转成json格式
    value = JSONEncoder().encode(value)
    rc.lpush(RRPC_KEY, value)

if __name__ == "__main__":
    file_url = None  # if file_url is None, use all file_url; else please set file_url, like file_url="http://xxx.flv"
    action = "join_lf"  # support action: "join_lf", "leave_lf"
    lf_num = 20  # how many sdk will become lf
    stun_pri = True
    if stun_pri:
        stun_ip = STUN_PRI_IP
    else:
        stun_ip = STUN_PUB_IP
    lf_ids = get_peer_ids_from_redis(redis_cluster_hosts=REDIS_CLUSTER_NODES)
    if len(lf_ids) > int(lf_num):
        lf_ids = lf_ids[:int(lf_num)]

    if file_url is None:
        file_url_list = get_file_urls_from_redis(redis_single_host=REDIS_SINGLE_HOST,
                                                 redis_single_port=REDIS_SINGLE_PORT)
    else:
        file_url_list = [file_url]

    for file_url in file_url_list:
        file_id = get_file_id_by_md5(file_url=file_url)
        if action == "join_lf":
            # join_leifeng(host=STUN_HUB_HOST, port=STUN_HUB_PORT, file_id=file_id, file_url=file_url, peer_ids=lf_ids)
            lpush_rrpc_join_lf(redis_single_host=REDIS_SINGLE_HOST, redis_single_port=REDIS_SINGLE_PORT,
                               stun_ip=stun_ip, file_id=file_id, file_url=file_url, peer_ids=lf_ids)
        elif action == "leave_lf":
            # leave_leifeng(host=STUN_HUB_HOST, port=STUN_HUB_PORT, file_id=file_id, peer_ids=lf_ids)
            lpush_rrpc_leave_lf(redis_single_host=REDIS_SINGLE_HOST, redis_single_port=REDIS_SINGLE_PORT,
                                stun_ip=stun_ip, file_id=file_id, peer_ids=lf_ids)




