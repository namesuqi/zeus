# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170814
__reference__ = "lib/database/etcd_handler.py"

作用: 操作etcd数据库中的数据
说明: 针对lf调度策略系统的测试需要对原函数进行修改

"""

import etcd

from lib.interface.strategy.lf_strategy.lib.const import ETCD_HOST, ETCD_PORT


# ---------------------------------------------------------------------------------------------------------------------


def analysis_etcd_result(etcd_result, field=None, leaves_only=False):
    """
    根据读取etcd的返回结果, 解析并获取期望的数据
    :param etcd_result: etcd的返回结果 (生成器)
    :param field: 期望获取的部分, None表示获取全部
    :param leaves_only: 是否只获取最底层的结果, 为False时返回result中包含的所有key, 为True时返回result中最底层的所有key
    :return:
    """
    result = []
    for r in etcd_result.get_subtree(leaves_only):
        if field is None:
            result.append(r)
        else:
            result.append(getattr(r, field))
    return result

# ---------------------------------------------------------------------------------------------------------------------


def get_etcd_result(key_name, key_path, host=ETCD_HOST, port=ETCD_PORT):
    # 获取指定目录下的所有信息 (返回结果为etcd结果的生成器, 需进一步解析)
    if not key_path.endswith("/"):
        key_path += "/"

    client = etcd.Client(host=host, port=port, allow_redirect=False, read_timeout=5)
    etcd_result = client.read("{0}{1}".format(key_path, key_name), recursive=True, sorted=True)

    return etcd_result

# ---------------------------------------------------------------------------------------------------------------------


def set_etcd_key(key, value, key_path, host=ETCD_HOST, port=ETCD_PORT, **kwargs):
    """
    在指定目录下添加或更新key-value
    :param key:
    :param value:
    :param key_path: 指定目录
    :param kwargs: 其他可选参数, 更多详细说明请见官方文档
            {ttl: int,  # 过期时间
             dir: bool,  # 是否为目录, 默认为False
             append: bool,  # 是否根据value自动创建新的key, 默认为False
             prevValue: str,  # compare key to this value, and swap only if corresponding
             prevIndex: int,  # modify key only if actual modifiedIndex matches the provided one
             prevExist: bool,  # If false, only create key; if true, only update key
             ...}
    :return:
    """
    if not key_path.endswith("/"):
        key_path += "/"

    client = etcd.Client(host=host, port=port, allow_redirect=False)
    print "key:", key, "value:", value
    client.write("{0}{1}".format(key_path, key), value, kwargs)


def del_etcd_key(key_name, key_path, recursive=None, if_dir=None, host=ETCD_HOST, port=ETCD_PORT):
    """
    删除指定key
    :param key_name:
    :param key_path:
    :param recursive: bool, 是否删除该key目录下的所有key-value
    :param if_dir: bool, 该key是否为目录
    :return:
    """
    if not key_path.endswith("/"):
        key_path += "/"

    client = etcd.Client(host=host, port=port, allow_redirect=False)
    print "del -- key:", key_name, "recursive:", recursive
    client.delete("{0}{1}".format(key_path, key_name), recursive, if_dir)

# ---------------------------------------------------------------------------------------------------------------------







