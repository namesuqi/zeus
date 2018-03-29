# coding=utf-8
"""
Bussiness related Redis Operation

__author__ = 'zengyuetian'

"""
from string import Template

import redis
import json
from lib.data.json_parser import JsonParser
from lib.constant.host import *

class RedisHandler(object):
    def __init__(self, host=REDIS_IP, port=REDIS_PORT, db=0):
        self._db = redis.StrictRedis(host=host, port=port, db=0)

    def DeletePeerInfo(self):
        peers = self.get_all_PNIC()
        for peer in peers:
            self._db.delete(peer)

    def get_all_PNIC(self):
        return self._db.keys("PNIC_*")


    def GetPeerInfo(self, peer_id):
        '''
        read peer id information from redis
        :param peer_id:
        :return:
        '''
        peer_info = self._db.get("PNIC_{0}".format(peer_id))
        return peer_info

    def DeleteKeysWithPrefix(self, prefix):
        '''
        delete all key with specified prefix
        :param prefix:
        :return:
        '''
        keys = self._db.keys(prefix + "*")
        for key in keys:
            self._db.delete(key)

    def FlushAll(self):
        '''
        flush current redis database
        :return:
        '''
        self._db.flushdb()

    def AddPrefetchFile(self, file_id, operation):
        '''
        add prefetch task for vod-push
        :param file_id:
        :param operation:download or delete
        :return:
        '''
        key = "PUSHING_FILES"
        value_data = Template(
             "{\"file_id\":\"$fileid\",\"operation\": \"$ope\"}"
        )
        value = value_data.substitute(fileid=file_id, ope=operation)
        self._db.zadd(key, 10, value)
        print file_id, operation






if __name__ == "__main__":
    # handler = RedisHandler()
    print ""
    # RedisHandler().AddPrefetchFile("74DA6014794F4C7184E52D1B84D7317B", "delete")
    #print handler.get_all_PNIC()
    #handler.DeletePeerInfo()
    # info = handler.GetPeerInfo("00000001EF90425EB467AC916BABBB52")
    # print info
    # print Parser.GetPeerValue(info, 'natType')
    # handler.FlushAll()


