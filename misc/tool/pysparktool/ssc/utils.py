# encoding: utf-8
import hashlib
import time
import json
from elasticsearch import Elasticsearch
import etcd


def json_parse(info):
    """
    JSON解析
    :param info: 
    :return: 
    """
    # info[1]为自己真实数据  info[0] spark stream自带
    data = json.loads(info[1])
    return data


def send_es(config, index, datas, doc_type='logs', cat="bops"):
    """
    ES存储
    :param cat: 
    :param doc_type: 
    :param index: 
    :param config: 
    :param datas: 
    :return: 
    """
    try:
        for data in datas:
            rdd_id = hashlib.md5(cat + str(int(time.time() * 1000))).hexdigest()
            es = Elasticsearch(hosts=config.ES_HOSTS)
            res = es.index(index=index,
                           doc_type=doc_type, id=rdd_id, body=data)
    except Exception as e:
        print e


def read_etcd_key(config, key_name, key_path=""):
    """
    读取指定目录下指定key中的内容
    :param key_name:
    :param key_path:
    :return:
    """
    value_list = {}
    try:
        client = etcd.Client(host=config.ETCD_HOST, port=config.ETCD_PORT, allow_redirect=False)
        r = client.read(str(key_path) + str(key_name), recursive=True, sorted=True)
        for child in r.children:
            try:
                dict_value = json.loads(child.value)
            except:
                dict_value = child.value
            value_list[child.key] = dict_value
        return value_list
    except etcd.EtcdKeyNotFound:
        # do something
        return value_list


def get_etcd_key(config):
    etcd_key = {}
    original_etcd_key = read_etcd_key(config, "/business/httpdns/v2/province_group", )
    for a_original in original_etcd_key:
        for a_key in original_etcd_key[a_original]:
            etcd_key[a_key] = a_original.split('/')[-1]
    return etcd_key


