# coding=utf-8
"""
Bussiness related Etcd Operation

__author__ = 'zsw'

"""
import json
import etcd

# ETCD_HOST = "192.168.1.251"
# ETCD_PORT = 2379
from lib.constant.database import ETCD_HOST, ETCD_PORT


def read_etcd_key(key_name, key_path=""):
    """
    读取指定目录下指定key中的内容
    :param key_name:
    :param key_path:
    :return:
    """
    client = etcd.Client(host=ETCD_HOST, port=ETCD_PORT, allow_redirect=False)
    value_list = {}
    try:
        r = client.read(str(key_path) + str(key_name), recursive=True, sorted=True)
        for child in r.children:
            print("%s: %s" % (child.key, child.value))
            try:
                dict_value = json.loads(child.value)
            except:
                dict_value = child.value
            value_list[child.key] = dict_value
        return value_list
    except Exception as error:
        # do something
        print error
        return None


def set_etcd_key(key_name, key_value, key_path=""):
    """
    在指定目录下添加指定key-value
    :param key_name: 要添加的key
    :param key_value: value
    :param key_path: 目录，即在该目录下添加该key
    :return:
    """
    client = etcd.Client(host=ETCD_HOST, port=ETCD_PORT, allow_redirect=False)
    set_key = str(key_path) + str(key_name)
    if str(key_value).startswith("{") or str(key_value).startswith("["):
        set_value = json.dumps(key_value)
    else:
        set_value = key_value
    client.write(set_key, set_value)
    print "Set key:", set_key
    print "Set value:", set_value


def del_etcd_key(key_name, key_path=""):
    """
    删除指定key，若key_name为目录则删除目录和所有子键
    :param key_name: key
    :param key_path:
    :return:
    """
    client = etcd.Client(host=ETCD_HOST, port=ETCD_PORT, allow_redirect=False)
    del_key = str(key_path) + str(key_name)
    print "Delete :", del_key
    try:
        client.delete(del_key, recursive=True)
    except Exception as err:
        print err


def etcd_set_group(group, key_path="", default_value=None, deep_dark=False):
    """
    set一组key-value
    :param group:
    :param key_path:
    :param default_value:
    :param deep_dark:
    :return:
    """
    if default_value is None:
        for k, v in group.iteritems():
            set_etcd_key(k, v, key_path)
    else:
        for k, v in group.iteritems():
            if type(v) == dict and deep_dark:
                for k2, v2 in v.iteritems():
                    v[k2] = default_value
            set_etcd_key(k, v, key_path)


def etcd_del_group(group, key_path=""):
    for k in group.keys():
        del_etcd_key(k, key_path)


if __name__ == "__main__":

    # del_etcd_key("/business/httpdns/v2")
    # etcd_set_group(CONFIG_TEST_OFFICE)
    read_etcd_key("/business/httpdns/v2")


