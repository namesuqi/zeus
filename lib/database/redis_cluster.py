# coding=utf-8
"""
Business keyword to control redis cluster


"""
import json
from simplejson import JSONEncoder
from rediscluster import StrictRedisCluster
from lib.constant.database import *


# def set_add(peer_id, file_id, file_size, operation):
#     """
#     old
#     redis command prototype:  SADD key member [member ...]
#     insert a task of the sdk in redis
#     :param peer_id:
#     :param file_id:
#     :param file_size:
#     :param operation:
#     :return:
#     """
#     startup_nodes = [{"host": REDIS_HOST, "port": REDIS_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#     s = Template('PPFC_$peerid')
#     key = s.substitute(peerid=peer_id)
#     value = Template(
#          "{\"file_id\":\"$fileid\",\"fsize\": $filesize,\"psize\": 864,\"ppc\": 12,\"operation\": \"$ope\","
#          "\"src\":0, \"priority\": 10}"
#     )
#     value = value.substitute(fileid=file_id, filesize=file_size, ope=operation)
#     return rc.sadd(key, value)


# def set_members(peer_id):
#     """
#     old
#     redis command prototype: SMEMBERS key
#     :param peer_id:
#     :return:
#     """
#     while 1:
#         key = "PPFC_{0}".format(peer_id)
#         value = RedisDB.get(key)
#         if value[1:6] != 'empty':
#             break


# def get_lsm_file_info(lsm_string):
#     """
#     old
#     :param lsm_string:
#     :return:
#     """
#     file_pet = re.compile("\"file_id\": \"(\w*)\",\"file_size\": (\d*)")
#     search_ret = file_pet.search(lsm_string).groups()
#     if search_ret:
#         return search_ret[0], search_ret[1]


# def match_file_id(file_id, lsm):
#     """
#     old
#     :param file_id:
#     :param lsm:
#     :return:
#     """
#     string = lsm
#     return str(string.find(file_id))


# def sorted_sets_add_pushing_files(file_id, operation):
#     """
#     old
#     redis command prototype:  ZADD key score member [score] [member]
#     insert PUSHING_FILES in redis
#     :param file_id:
#     :param operation:
#     :return:
#     """
#     pool = redis.ConnectionPool(host=REDIS_SINGLE_HOST, port=REDIS_SINGLE_PORT, db=0)
#     rc = redis.StrictRedis(connection_pool=pool)
#     s = Template('PUSHING_FILES')
#     key = s.substitute()
#     value = Template("{\"file_id\":\"$fileid\",\"operation\": \"$ope\"}")
#     value = value.substitute(fileid=file_id, ope=operation)
#     timestamp = int(time.time()*1000)
#     return rc.zadd(key, timestamp, value)


# def hash_del(peer_id, file_id):
#     """
#     old
#     redis command prototype:  HDEL key field value
#     :param peer_id:
#     :param file_id:
#     :return:
#     """
#     startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#
#     field = Template('$peerid')
#     field = field.substitute(peerid=peer_id)
#
#     key = Template('FOSC_$file_id')
#     key = key.substitute(file_id=file_id)
#     return rc.hdel(key, field)


# def hash_set(peer_id, file_id, cppc):
#     """
#     old
#     redis command prototype:  HSET key field value
#     :param peer_id:
#     :param file_id:
#     :param cppc:
#     :return:
#     """
#     startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#     field = Template('$peerid')
#     field = field.substitute(peerid=peer_id)
#
#     name = Template('FOSC_$file_id')
#     name = name.substitute(file_id=file_id)
#
#     value = Template("{\"cppc\":\"$cppc\"}")
#     value = value.substitute(cppc=cppc)
#     return rc.hset(name, field, value)


# def hash_get(peer_id, file_id):
#     """
#     old
#     redis command prototype:  HGET key field
#     :param peer_id:
#     :param file_id:
#     :return:
#     """
#     startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#     # rc = StrictRedisCluster(cluster=cluster, db=0)
#     """
#     pool = redis.ConnectionPool(host=REDIS_CLUSTER_HOST_2, port=REDIS_CLUSTER_PORT, db=0)
#     rc = redis.StrictRedis(connection_pool=pool)
#     """
#     s = Template('$peerid')
#     key = s.substitute(peerid=peer_id)
#
#     name = Template('FOSC_$file_id')
#     name = name.substitute(file_id=file_id)
#     value = Template(
#          "{\"cppc\":\"$cppc\"}"
#     )
#     return rc.hget(name, key)





# def cluster_set_rem(peer_id, file_id, cppc, version, nat_type, public_ip, public_port, private_ip, private_port):
#     """
#     cluster按照需求的规则删除set下某一个key的一个value
#     :param peer_id:
#     :param file_id:
#     :param cppc:
#     :param version:
#     :param nat_type:
#     :param public_ip:
#     :param public_port:
#     :param private_ip:
#     :param private_port:
#     :return:
#     """
#     startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#     key = "{FOSC_" + str(file_id) + "_000000}"
#
#     value = Template(
#         "{\"version\":\"$version\",\"natType\":$nat_type,\"publicIP\":\"$public_ip\","
#         "\"publicPort\":$public_port,\"privateIP\":\"$private_ip\","
#         "\"privatePort\":$private_port,\"isp_id\":\"000000\",\"peer_id\":\"$peer_id\","
#         "\"cppc\":$cppc}"
#         )
#
#     value = value.substitute(version=version, nat_type=nat_type, public_ip=public_ip, public_port=public_port,
#                              private_ip=private_ip, private_port=private_port, peer_id=peer_id, cppc=cppc)
#     return rc.srem(key, value)




# def cluster_zrange_lfc(file_id, isp="000000"):
#     '''
#     :param file_id:
#     :param isp:
#     :return:
#     '''
#     startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
#                      {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
#     rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#     key = "LFC_" + str(file_id) + "_" + str(isp)
#     # list = rc.zrange(key, 0, -1, False, True)  # list: [value, score]
#     # for i in range(len(list)):
#     #     print list[i]
#     # if len(list) > 0:
#     #     print "time needed for overdue", int(list[0][1])-int(time.time())
#     return rc.zrange(key, 0, -1, desc=False, withscores=True)


# def cluster_zrange_lfcmgr():
#     '''
#     :return:
#     '''
#     rc = StrictRedisCluster("10.5.100.2", 6379)
#     key = "LFCacheManageZset"
#     # list = rc.zrange(key, 0, -1, False, True)
#     # for i in range(len(list)):
#     #     print list[i]
#     # if len(list) > 0:
#     #     print "time needed for overdue", int(list[0][1])-int(time.time())
#     return rc.zrange(key, 0, -1, desc=False, withscores=True)


startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
                 {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
                 {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)


def cluster_setex_pnic(ttl, peer_id, sdk_version, nat_type, public_ip, public_port, private_ip, private_port,
                       province_id, isp_id, city_id, stun_ip, country="CN"):
    """
    在redis中写入某节点的PNIC信息，并设定其有效存活时间
    :param ttl: expire time
    :param peer_id:
    :param sdk_version:
    :param nat_type:
    :param public_ip:
    :param public_port:
    :param private_ip:
    :param private_port:
    :param province_id:
    :param isp_id:
    :param city_id:
    :param stun_ip:
    :param country:
    :return:
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    key = "PNIC_" + str(peer_id)

    value = {
        "peer_id": str(peer_id),
        "version": str(sdk_version),
        "natType": int(nat_type),
        "publicIP": str(public_ip),
        "publicPort": int(public_port),
        "privateIP": str(private_ip),
        "privatePort": int(private_port),
        "country": str(country),
        "province_id": str(province_id),
        "isp_id": str(isp_id),
        "city_id": str(city_id),
        "stunIP": str(stun_ip)
    }
    # 将dict转成json格式
    value = JSONEncoder().encode(value)
    rc.setex(key, int(ttl), value)


def cluster_fosc_add(file_id, isp, peer_id, sdk_version, nat_type, public_ip, public_port, private_ip, private_port,
                     province_id, stun_ip, cppc=1):
    """
    在FOSC中set value，若非必要，尽量使用cache_report或control_report请求汇报，由ts-go服务器写入FOSC
    目前服务器维护seed list不只单单使用FOSC，还涉及到LFC，LFCacheManageZset
    :param file_id: 该key所对应的file_id
    :param isp: 该key所对应的isp
    :param peer_id:
    :param sdk_version:
    :param nat_type:
    :param public_ip:
    :param public_port:
    :param private_ip:
    :param private_port:
    :param province_id:
    :param stun_ip:
    :param cppc:
    :return:
    """

    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    key = "{FOSC_" + str(file_id) + "_" + str(isp) + "}"
    value = {
        "peer_id": str(peer_id),
        "version": str(sdk_version),
        "natType": int(nat_type),
        "publicIP": str(public_ip),
        "publicPort": int(public_port),
        "privateIP": str(private_ip),
        "privatePort": int(private_port),
        "province_id": str(province_id),
        "stunIP": str(stun_ip),
        "cppc": int(cppc)
    }
    # 将dict转成json格式
    value = JSONEncoder().encode(value)
    rc.sadd(key, value)


def cluster_card_key(card_key, *args):
    """
    统计该key对应集合中的元素数量
    :param card_key:
    :param args: 拼接key
    :return:
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # key = "{FOSC_" + str(file_id) + "_" + str(isp) + "}"
    # 如果有多个参数，将多个参数拼接成一个key
    if args:
        for i in args:
            card_key = str(card_key) + str(i)

    # 判断该key对应的类型
    key_type = rc.type(card_key)
    if str(key_type) == "set":
        element_nums = rc.scard(card_key)
    elif str(key_type) == "zset":
        element_nums = rc.zcard(card_key)
    else:
        # print "Type should be set or zset !!!"
        element_nums = 0
    return element_nums


def cluster_delete_keys(prefix, *args):
    """
    delete all key with specified prefix
    :param prefix:
    :return:
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # 如果有多个参数，将多个参数拼接成一个key
    if args:
        for i in args:
            prefix = str(prefix) + str(i)
    keys = rc.keys("*" + prefix + "*")
    for key in keys:
        rc.delete(key)


def cluster_set_get(smembers_key, *args):
    """
    返回该key对应集合的所有元素
    redis command prototype: SMEMBERS key
    :param smembers_key:
    :param args: 拼接key，传参举例：cluster_set_get("{FOSC_", file_id, "_", isp, "}")
    :return:
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # 如果有多个参数，将多个参数拼接成一个key
    if args:
        for i in args:
            smembers_key = str(smembers_key) + str(i)
    val = rc.smembers(smembers_key)

    members_list = []
    for i in val:
        members_list.append(json.loads(i))
    # members_sort = sorted(members_list, key=lambda member: member["peer_id"])
    # for member in members_sort:
    #     print member
    return members_list


def cluster_string_get(string_key, *args):
    """
    返回该key(string类型)对应的value,ttl
    redis command prototype: get key
    :param string_key:
    :param args: 拼接key，传参举例：get("PNIC_", peer_id)
    :return: dict格式{"ttl": ttl, "value": value}
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # 如果有多个参数，将多个参数拼接成一个key
    match = False
    if args:
        for i in args:
            string_key = str(string_key) + str(i)
    result = {}
    if rc.exists(string_key):
        a = json.loads(rc.get(string_key))
        result["value"] = byteify(a)
        result["ttl"] = rc.ttl(string_key)

    return result


def cluster_string_match(match_key):
    """
    匹配相关key
    :param match_key: eg. "PNIC*"
    :return:
    """
    # startup_nodes = [{"host": REDIS_CLUSTER_HOST, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_2, "port": REDIS_CLUSTER_PORT},
    #                  {"host": REDIS_CLUSTER_HOST_3, "port": REDIS_CLUSTER_PORT}]
    # rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    match_keys = rc.keys(str(match_key))
    match_result = dict()
    for i in match_keys:
        print i
        match_result[i] = json.loads(rc.get(i))
    return match_result


def byteify(input_json):
    """
    handle json unicode to str
    :param input_json:
    :return:
    """
    if isinstance(input_json, dict):
        return {byteify(key): byteify(value) for key, value in input_json.iteritems()}
    elif isinstance(input_json, list):
        return [byteify(element) for element in input_json]
    elif isinstance(input_json, unicode):
        return input_json.encode('utf-8')
    else:
        return input


if __name__ == "__main__":

    # cluster_set_add("00010026408B9F4AB0E85524E25043D3", "272E603BA82C4B0E817A124960E1D1AD", 1, '3.0.0', 1,
    #                 '1.1.1.1', 56379, '1.2.3.4', 11331)
    # cluster_get_pnic("0000000447904EE184946F885D0BFDCA")

    FOSC_KEY = "{FOSC_85FA513E3D6E0A180657D2EA0C1E9DC1_000000}"
    # cluster_card_key("LFCacheManageZset")

    # file_id = file_id = "".ljust(32, "F")
    # cluster_delete_keys("{FOSC_", file_id)
    # ISP_LIST = ["100017", "100026", "000000"]
    # for isp in ISP_LIST:
    #     print "--------------%s------------------" % isp
    #     cluster_set_get("{FOSC_", file_id, "_", isp, "}")

    # s = cluster_string_get("PNIC_", "00000002C38F7379772F25E1746EB23")

