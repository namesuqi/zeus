# coding=utf-8
"""
Bussiness related Redis Operation

__author__ = 'zengyuetian'

"""
import json
import demjson

import redis
from string import Template
from lib.constant.database import *


def delete_keys_with_prefix(prefix):
    """
    delete all key with specified prefix
    :param prefix:
    :return:
    """
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    keys = rc.keys("*" + prefix + "*")
    for key in keys:
        rc.delete(key)


def flush_all():
    """
    删除当前数据库中的所有Key
    :return:
    """
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    rc.flushdb()


def clear_redis_list(key):
    """
    清空某个列表类型的key的所有值
    :param key:
    :return:
    """
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    rc.ltrim(key, 0, 0)
    rc.lpop(key)


def delete_keys(prefix, *args):
    """
    delete all key with specified prefix
    :param prefix:
    :return:
    """
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    # 如果有多个参数，将多个参数拼接成一个key
    if args:
        for i in args:
            prefix = str(prefix) + str(i)
    keys = rc.keys("*" + prefix + "*")
    for key in keys:
        rc.delete(key)


def operate_file_url(operation, file_url, file_id=None, tenant_name=None, REDIS_SINGLE_HOST=REDIS_SINGLE_HOST):
    """
    操作redis中的F1_[file_url]_FLV, add/set, delete/del, select/get
    :return:
    """
    operation = operation.lower()
    if operation not in ("add", "set", "delete", "del", "select", "get"):
        raise operation("operation must be in (add, set, delete, del, select, get)")

    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    key = "F1_%s_FLV" %(file_url)

    if operation in ("delete", "del"):
        print "delete_ok", rc.delete(key)
        return

    if rc.exists(key) == False and operation in ("add", "set"):
        value = demjson.encode({"file_id":file_id, "file_url":file_url, "tenant_name":tenant_name})
        rc.setex(key, 18000, value)
    if operation in ("add", "set", "select", "get"):
        keys_info = ["file_id", "file_url", "tenant_name"]
        file_value = rc.get(key)
        file_info = []
        if file_value:
            file_value_json = json.loads(file_value)  # str => json
            for key in keys_info:
                file_info.append(file_value_json[key])
            return file_info
        else:
            print "This key does not exist."
            return


def add_stun_peer(peer_id, pub_ip="101.81.15.129", pub_port="36900", pri_ip="192.168.1.2", pri_port="36900", nat_type=0):
    """
    add key STUN_${peer_id} to redis-single
    :param peer_id: str(one peer) or list(peers)
    :param pub_ip:
    :param pri_ip:
    :param pub_port:
    :param pri_port:
    :param nat_type:
    :return:
    """
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    if type(peer_id) != list:
        peer_id = [peer_id]

    for pid in peer_id:
        key = Template('STUN_$peerid')
        KEY = key.substitute(peerid=pid)
        value = Template(
         "{\"nat_type\":$nat_type,\"pub_ip\":\"$pub_ip\",\"pub_port\":$pub_port,\"pri_ip\":\"$pri_ip\","
         "\"pri_port\":$pri_port}"
        )
        VALUE = value.substitute(nat_type=nat_type, pub_ip=pub_ip, pub_port=pub_port, pri_ip=pri_ip, pri_port=pri_port)
        rc.setex(KEY, 300, VALUE)


def get_stun_peer(peer_id):
    """
    根据peer_id查询redis中STUN_[peer_id]的信息
    :param peer_id:
    :return:
    """
    keys_info = ["nat_type", "pub_port", "pri_port", "pri_ip", "pub_ip"]

    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    key = Template('STUN_$peerid')
    KEY = key.substitute(peerid=peer_id)
    stun_peer_value = rc.get(KEY)

    stun_peer_info = []
    if stun_peer_value:
        stun_peer_json = json.loads(stun_peer_value)  # str -> json
        # print a.keys()
        # print a.values()
        for key in keys_info:
            stun_peer_info.append(stun_peer_json[key])
        return stun_peer_info
    else:
        return None


if __name__ == "__main__":
    # handler = RedisHandler()
    # print handler.get_all_PNIC()
    # handler.DeletePeerInfo()
    # info = handler.GetPeerInfo("00000001EF90425EB467AC916BABBB52")
    # print info
    # print Parser.GetPeerValue(info, 'natType')
    # handler.FlushAll()
    # RedisHandler().add_stun_peer(["000000000000000", "000001"])
    get_stun_peer("0000000430E04D43A6E507AEC38EEC59")
    pass


