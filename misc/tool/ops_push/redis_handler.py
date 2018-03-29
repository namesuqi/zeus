# coding=utf-8
"""
Bussiness related Redis Operation

__author__ = 'zengyuetian'

"""
import json
import time
# import demjson
from simplejson import JSONEncoder
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


def set_allow_weight(isp, pro, lp_ip_list):
    rc = redis.StrictRedis(host=REDIS_SINGLE_HOST, port=REDIS_PORT, db=0)
    key = "ALLOW_WEIGHT-" + str(isp)+"_"+str(pro)
    value = lp_ip_list
    # 将dict转成json格式
    value = JSONEncoder().encode(value)
    rc.set(key, value)

if __name__ == "__main__":
    # handler = RedisHandler()
    # print handler.get_all_PNIC()
    # handler.DeletePeerInfo()
    # info = handler.GetPeerInfo("00000001EF90425EB467AC916BABBB52")
    # print info
    # print Parser.GetPeerValue(info, 'natType')
    # handler.FlushAll()
    # RedisHandler().add_stun_peer(["000000000000000", "000001"])
    # get_stun_peer("0000000430E04D43A6E507AEC38EEC59")

    # 100017 350000 福建电信
    # fjdx1 = ["1.0.1.0", "1.0.1.255", "1.0.2.0"]
    # fjdx2 = ["1.0.2.255", "1.0.3.0", "1.0.3.255"]
    # fjdx3 = ["1.1.0.0", "1.1.0.255", "1.1.2.0"]
    # # 100017 440000 广东电信
    # gddx1 = ["1.1.8.0", "1.1.8.255", "1.1.61.255"]
    # gddx2 = ["1.1.9.0", "1.1.9.255", "1.1.62.255"]
    # gddx3 = ["1.1.10.0", "1.1.10.255", "1.1.63.255"]
    # # 1000120 110000 北京北龙中网
    # bjzw1 = ["1.2.2.1", "1.2.2.10", "1.2.2.20"]
    # bjzw2 = ["1.2.2.30", "1.2.2.40", "1.2.2.50"]
    # bjzw3 = ["1.2.2.60", "1.2.2.70", "1.2.2.80"]
    # # 1000189 110000 北京互联网信息中心
    # bjhl1 = ["1.2.4.0", "1.2.4.10", "1.2.4.255"]
    # bjhl2 = ["1.2.8.0", "1.2.8.10", "1.2.8.255"]
    # # 100063 110000 北京方正网络
    # bjfz1 = ["1.12.0.0", "1.12.1.255", "1.12.2.255"]
    # bjfz2 = ["1.12.3.255", "1.12.4.255", "1.12.255.255"]
    # # 100063 220000 吉林方正
    # jlfz1 = ["1.13.0.0", "1.13.0.255", "1.13.1.255"]
    # jlfz2 = ["1.13.2.0", "1.13.3.255", "1.13.4.255"]
    # # 100026 150000 内蒙古联通
    # nmglt1 = ["1.24.0.0", "1.24.7.255", "1.24.8.0"]
    # nmglt2 = ["1.24.15.255", "1.24.24.0", "1.24.31.255"]
    # # 0 999077 香港
    # hk1 = ["1.32.192.0", "1.32.193.255", "1.32.194.255"]
    # hk2 = ["1.32.195.255", "1.32.196.255", "1.32.255.255"]
    # # 0 999079 台湾
    # tw1 = ["1.34.0.0", "1.34.0.1", "1.34.0.255"]
    # tw2 = ["1.34.1.0", "1.34.1.1", "1.34.1.255"]

    # ip列表为空时，福建，广东，北京
    # list1 = []
    # list2 = ["1.0.2.255", "1.0.3.0"]
    # list3 = ["1.1.0.0"]
    # list11 = []
    # list22 = ["1.1.9.0", "1.1.9.255"]
    # list33 = ["1.2.2.0"]
    list1 = ["1.1.1.0", "1.1.1.1", '1.1.1.2']
    list2 = ["2.2.2.0", "2.2.2.1", "2.2.2.2"]
    list3 = ["3.3.3.0", "3.3.3.1", "3.3.3.2"]
    list4 = ["4.4.4.0", "4.4.4.1", "4.4.4.2"]
    list5 = ["5.5.5.0", "5.5.5.1", "5.5.5.2"]
    list6 = ["6.6.6.0", "6.6.6.1", "6.6.6.2"]
    list7 = ["7.7.7.0", "7.7.7.1", "7.7.7.2"]
    list8 = ["8.8.8.0", "8.8.8.1", "8.8.8.2"]
    list9 = ["9.9.9.0", "9.9.9.1", "9.9.9.2"]
    list10 = ["10.10.10.0", "10.10.10.1", "10.10.10.2"]
    list11 = ["11.11.11.0", "11.11.11.1", "11.11.11.2"]
    list12 = ["12.12.12.0", "12.12.12.1", "12.12.12.2"]
    list13 = ["13.13.13.0", "13.13.13.1", "13.13.13.2"]
    list14 = ["14.14.14.0", "14.14.14.1", "14.14.14.2"]
    list15 = ["15.15.15.0", "15.15.15.1", "15.15.15.2"]
    list16 = ["16.16.16.0", "16.16.16.1", "16.16.16.2"]
    list17 = ["17.17.17.0", "17.17.17.1", "17.17.17.2"]
    list18 = ["18.18.18.0", "18.18.18.1", "18.18.18.2"]
    list19 = ["19.19.19.0", "19.19.19.1", "19.19.19.2"]
    list20 = ["20.20.20.0", "19.19.19.1", "19.19.19.2"]
    list21 = ["21.21.21.0", "21.21.21.1", "21.21.21.2"]
    list22 = ["22.22.22.0", "22.22.22.1", "22.22.22.2"]
    list23 = ["23.23.23.0", "23.23.23.1", "23.23.23.2"]
    list24 = ["24.24.24.0", "24.24.24.1", "24.24.24.2"]
    list25 = ["25.25.25.0", "25.25.25.1", "25.25.25.2"]
    list26 = ["26.26.26.0", "26.26.26.1", "26.26.26.2"]
    list27 = ["27.27.27.0", "26.26.26.1", "26.26.26.2"]
    list28 = ["28.28.28.28", "0.0.0.0", "0.0.0.1"]
    list29 = ["29.29.29.29", "0.0.0.0", "0.0.0.1"]
    list30 = ["30.30.30.30", "0.0.0.0", "0.0.0.1"]
    list31 = ["31.31.31.31", "0.0.0.0", "0.0.0.1"]
    list32 = ["32.32.32.32", "0.0.0.0", "0.0.0.1"]
    list33 = ["33.33.33.33", "0.0.0.0", "0.0.0.1"]
    list34 = ["34.34.34.34", "0.0.0.0", "0.0.0.1"]
    list35 = ["35.35.35.35", "0.0.0.0", "0.0.0.1"]
    list36 = ["36.36.36.36", "0.0.0.0", "0.0.0.1"]
    list37 = ["37.37.37.37", "0.0.0.0", "0.0.0.1"]
    list38 = ["38.38.38.38", "0.0.0.0", "0.0.0.1"]
    list39 = ["39.39.39.39", "0.0.0.0", "0.0.0.1"]
    list40 = ["40.40.40.40", "0.0.0.0", "0.0.0.1"]
    list41 = ["41.41.41.41", "0.0.0.0", "0.0.0.1"]
    list42 = ["42.42.42.42", "0.0.0.0", "0.0.0.1"]
    list43 = ["43.43.43.43", "0.0.0.0", "0.0.0.1"]
    list44 = ["44.44.44.44", "0.0.0.0", "0.0.0.1"]
    list45 = ["45.45.45.45", "0.0.0.0", "0.0.0.1", "11.11.11.11", "22.2.2.2", "152.5.51.3"]

    tlist1 = ["1.1.1.0", "1.1.1.1", "255.255.255.255"]
    tlist2 = ["2.2.2.0", "2.2.2.1", "255.255.255.255"]
    tlist3 = ["3.3.3.0", "3.3.3.1", "255.255.255.255"]
    tlist4 = ["4.4.4.0", "4.4.4.1", "255.255.255.255"]
    tlist5 = ["5.5.5.0", "5.5.5.1", "255.255.255.255"]
    tlist6 = ["6.6.6.0", "6.6.6.1", "255.255.255.255"]
    tlist7 = ["7.7.7.0", "7.7.7.1", "255.255.255.255"]
    tlist8 = ["8.8.8.0", "8.8.8.1", "255.255.255.255"]
    tlist9 = ["9.9.9.0", "9.9.9.1", "255.255.255.255"]
    tlist10 = ["10.10.10.0", "10.10.10.1", "255.255.255.255"]
    tlist11 = ["11.11.11.0", "11.11.11.1", "255.255.255.255"]
    tlist12 = ["12.12.12.0", "12.12.12.1", "255.255.255.255"]
    tlist13 = ["13.13.13.0", "13.13.13.1", "255.255.255.255"]
    tlist14 = ["14.14.14.0", "14.14.14.1", "255.255.255.255"]
    tlist15 = ["15.15.15.0", "15.15.15.1", "255.255.255.255"]
    tlist16 = ["16.16.16.0", "16.16.16.1", "255.255.255.255"]
    tlist17 = ["17.17.17.0", "17.17.17.1", "255.255.255.255"]
    tlist18 = ["18.18.18.0", "18.18.18.1", "255.255.255.255"]
    tlist19 = ["19.19.19.0", "19.19.19.1", "255.255.255.255"]
    tlist20 = ["20.20.20.0", "19.19.19.1", "255.255.255.255"]
    tlist21 = ["21.21.21.0", "21.21.21.1", "255.255.255.255"]
    tlist22 = ["22.22.22.0", "22.22.22.1", "255.255.255.255"]
    tlist23 = ["23.23.23.0", "23.23.23.1", "255.255.255.255"]
    tlist24 = ["24.24.24.0", "24.24.24.1", "255.255.255.255"]
    tlist25 = ["25.25.25.0", "25.25.25.1", "255.255.255.255"]
    tlist26 = ["26.26.26.0", "26.26.26.1", "255.255.255.255"]
    tlist27 = ["27.27.27.0", "27.27.27.1", "255.255.255.255"]
    tlist28 = ["28.28.28.28", "0.0.0.0", "255.255.255.255"]
    tlist29 = ["29.29.29.29", "0.0.0.0", "255.255.255.255"]
    tlist30 = ["30.30.30.30", "0.0.0.0", "255.255.255.255"]
    tlist31 = ["31.31.31.31", "0.0.0.0", "255.255.255.255"]
    tlist32 = ["32.32.32.32", "0.0.0.0", "255.255.255.255"]
    tlist33 = ["33.33.33.33", "0.0.0.0", "255.255.255.255"]
    tlist34 = ["34.34.34.34", "0.0.0.0", "255.255.255.255"]
    tlist35 = ["35.35.35.35", "0.0.0.0", "255.255.255.255"]
    tlist36 = ["36.36.36.36", "0.0.0.0", "255.255.255.255"]
    tlist37 = ["37.37.37.37", "0.0.0.0", "255.255.255.255"]
    tlist38 = ["38.38.38.38", "0.0.0.0", "255.255.255.255"]
    tlist39 = ["39.39.39.39", "0.0.0.0", "255.255.255.255"]
    tlist40 = ["40.40.40.40", "0.0.0.0", "255.255.255.255"]
    tlist41 = ["41.41.41.41", "0.0.0.0", "255.255.255.255"]
    tlist42 = ["42.42.42.42", "0.0.0.0", "255.255.255.255"]
    tlist43 = ["43.43.43.43", "0.0.0.0", "255.255.255.255"]
    tlist44 = ["44.44.44.44", "0.0.0.0", "255.255.255.255"]
    tlist45 = ["45.45.45.45", "0.0.0.0", "255.255.255.255", "11.11.11.11", "22.2.2.2", "152.5.51.3"]
    start = True
    while start:
        set_allow_weight("100017", "350000", list1)
        set_allow_weight("100017", "440000", list2)
        set_allow_weight("1000120", "110000", list3)
        set_allow_weight("1000189", "110000", list4)
        set_allow_weight("100063", "110000", list5)
        set_allow_weight("100063", "220000", list6)
        set_allow_weight("100026", "150000", list7)
        set_allow_weight("0", "999077", list8)
        set_allow_weight("0", "999079", list9)
        set_allow_weight("100017", "520000", list10)
        set_allow_weight("100017", "640000", list11)
        set_allow_weight("100027", "370000", list12)
        set_allow_weight("100027", "320000", list13)
        set_allow_weight("100027", "340000", list14)
        set_allow_weight("100026", "230000", list15)
        set_allow_weight("100017", "140000", list16)
        set_allow_weight("100017", "610000", list17)
        set_allow_weight("100027", "440000", list18)
        set_allow_weight("100017", "410000", list19)
        set_allow_weight("1000143", "440000", list20)
        set_allow_weight("100017", "500000", list21)
        set_allow_weight("1000143", "510000", list22)
        set_allow_weight("1000143", "610000", list25)
        set_allow_weight("1000143", "450000", list26)
        set_allow_weight("1000128", "110000", list27)
        set_allow_weight("1000143", "130000", list28)
        set_allow_weight("1000143", "330000", list29)
        set_allow_weight("1000128", "610000", list30)
        set_allow_weight("1000314", "999077", list31)
        set_allow_weight("100026", "530000", list32)
        set_allow_weight("100026", "500000", list33)
        set_allow_weight("100017", "420000", list34)
        set_allow_weight("100026", "440000", list35)
        set_allow_weight("100026", "540000", list36)
        set_allow_weight("100079", "440000", list37)
        set_allow_weight("0", "999078", list38)
        set_allow_weight("100017", "130000", list39)
        set_allow_weight("1000118", "500000", list40)
        set_allow_weight("100017", "620000", list41)
        set_allow_weight("100020", "430000", list42)
        set_allow_weight("1000323", "330000", list43)
        set_allow_weight("100098", "330000", list44)
        set_allow_weight("1000139", "110000", list45)
        time.sleep(60)
        set_allow_weight("100017", "350000", tlist1)
        set_allow_weight("100017", "440000", tlist2)
        set_allow_weight("1000120", "110000", tlist3)
        set_allow_weight("1000189", "110000", tlist4)
        set_allow_weight("100063", "110000", tlist5)
        set_allow_weight("100063", "220000", tlist6)
        set_allow_weight("100026", "150000", tlist7)
        set_allow_weight("0", "999077", tlist8)
        set_allow_weight("0", "999079", tlist9)
        set_allow_weight("100017", "520000", tlist10)
        set_allow_weight("100017", "640000", tlist11)
        set_allow_weight("100027", "370000", tlist12)
        set_allow_weight("100027", "320000", tlist13)
        set_allow_weight("100027", "340000", tlist14)
        set_allow_weight("100026", "230000", tlist15)
        set_allow_weight("100017", "140000", tlist16)
        set_allow_weight("100017", "610000", tlist17)
        set_allow_weight("100027", "440000", tlist18)
        set_allow_weight("100017", "410000", tlist19)
        set_allow_weight("1000143", "440000", tlist20)
        set_allow_weight("100017", "500000", tlist21)
        set_allow_weight("1000143", "510000", tlist22)
        set_allow_weight("1000143", "610000", tlist25)
        set_allow_weight("1000143", "450000", tlist26)
        set_allow_weight("1000128", "110000", tlist27)
        set_allow_weight("1000143", "130000", tlist28)
        set_allow_weight("1000143", "330000", tlist29)
        set_allow_weight("1000128", "610000", tlist30)
        set_allow_weight("1000314", "999077", tlist31)
        set_allow_weight("100026", "530000", tlist32)
        set_allow_weight("100026", "500000", tlist33)
        set_allow_weight("100017", "420000", tlist34)
        set_allow_weight("100026", "440000", tlist35)
        set_allow_weight("100026", "540000", tlist36)
        set_allow_weight("100079", "440000", tlist37)
        set_allow_weight("0", "999078", tlist38)
        set_allow_weight("100017", "130000", tlist39)
        set_allow_weight("1000118", "500000", tlist40)
        set_allow_weight("100017", "620000", tlist41)
        set_allow_weight("100020", "430000", tlist42)
        set_allow_weight("1000323", "330000", tlist43)
        set_allow_weight("100098", "330000", tlist44)
        set_allow_weight("1000139", "110000", tlist45)
        time.sleep(60)
    # 缺失情况一直循环，看是否能这确返回
    # while start:
    #     set_allow_weight("100017", "350000", list1)
    #     set_allow_weight("100017", "440000", list2)
    #     set_allow_weight("1000120", "110000", list3)
    #     time.sleep(60)
    #     set_allow_weight("100017", "350000", list11)
    #     set_allow_weight("100017", "440000", list22)
    #     set_allow_weight("1000120", "110000", list33)
    #     time.sleep(60)



