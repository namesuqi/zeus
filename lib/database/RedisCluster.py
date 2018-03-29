# coding=utf-8
"""
Business keyword to control redis cluster
precondition: pip install redis-py-cluster

"""

from redisdb import RedisDB
from rediscluster import StrictRedisCluster
from string import Template
from lib.constant.database import *
import re
import time
import redis


def SADD(peer_id, file_id, file_size, operation):
    """
    insert a task of the sdk in redis
    :param peer_id:
    :param file_id:
    :param file_size:
    :param operation:
    :return:
    """
    startup_nodes = [{"host": REDIS_HOST, "port": REDIS_PORT}]
    rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    s = Template('PPFC_$peerid')
    KEY = s.substitute(peerid=peer_id)
    value = Template(
         "{\"file_id\":\"$fileid\",\"fsize\": $filesize,\"psize\": 864,\"ppc\": 12,\"operation\": \"$ope\",\"src\":0, \"priority\": 10}"
    )
    VALUE = value.substitute(fileid=file_id, filesize=file_size, ope=operation)
    return rc.sadd(KEY, VALUE)

def SMEMBERS(peer_id):
    while (1):
        KEY = "PPFC_{0}".format(peer_id)
        VALUE = RedisDB.get(KEY)
        if VALUE[1:6] != 'empty':
            break


def GetLsmFileInfo(lsm_string):
    file_pet = re.compile("\"file_id\": \"(\w*)\",\"file_size\": (\d*)")
    search_ret = file_pet.search(lsm_string).groups()
    if search_ret:
        return search_ret[0], search_ret[1]


def MatchFileId(file_id, lsm):
    string = lsm
    return str(string.find(file_id))

def ZADD_PUSHING_FILES(file_id, operation):
    """
    insert PUSHING_FILES in redis
    :param file_id:
    :param operation:
    :return:
    """
    pool=redis.ConnectionPool(host=REDIS_SINGLE_HOST, port=REDIS_SINGLE_PORT, db=0)
    rc = redis.StrictRedis(connection_pool=pool)
    s = Template('PUSHING_FILES')
    KEY = s.substitute()
    value = Template("{\"file_id\":\"$fileid\",\"operation\": \"$ope\"}")
    VALUE = value.substitute(fileid=file_id, ope=operation)
    timestamp = int(time.time()*1000)
    return rc.zadd(KEY, timestamp, VALUE)




