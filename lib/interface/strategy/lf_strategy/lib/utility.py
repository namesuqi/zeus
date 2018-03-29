# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170808

作用: lf调度策略测试需要的其他函数

"""

from random import random


def set_value_by_reuse_ratio_mode(reuse_ratio_mode):
    # 根据放大比的类型或具体值, 获得upload, download值; 目前只支持"invalid", "random"和具体值
    if isinstance(reuse_ratio_mode, (int, float, long)):
        if reuse_ratio_mode == -1:
            upload = download = 0
        elif reuse_ratio_mode == 0:
            upload = 0
            download = int(random() * 1000)
        elif reuse_ratio_mode > 0:
            download = int(random() * 10)
            if download == 0:
                upload = int(reuse_ratio_mode)
            else:
                upload = int(download * reuse_ratio_mode)
        else:
            raise ValueError("reuse_ratio should be in {-1, [0, +∞)}")
    elif isinstance(reuse_ratio_mode, str):
        if reuse_ratio_mode == "random":
            upload = int(random() * 1000) + 1
            download = int(random() * 1000)
        elif reuse_ratio_mode == "invalid":
            upload = 0
            download = int(random() * 100)
        else:
            raise ValueError("Only support 'random' and 'invalid' mode temporarily")
    else:
        raise ValueError("reuse_ratio_mode should be number(reuse_ratio) or mode('random' or 'invalid')")

    return upload, download


def set_value_by_p2p_ratio(p2p_ratio):
    # 根据p2p占比的值, 获得p2p, cdn值
    p2p_ratio = round(p2p_ratio, 5)
    if p2p_ratio == -1:
        p2p = cdn = 0
    elif p2p_ratio >= 0:
        multiple = int(random() * 1000) + 1
        p2p = p2p_ratio * 10000 * multiple
        cdn = (1 - p2p_ratio) * 10000 * multiple
    else:
        raise ValueError("p2p_ratio should be in {-1, [0, +∞)}")

    return int(p2p), int(cdn)


def get_reuse_ratio(upload, download):
    # 根据upload, download值计算放大比
    if upload == 0 and download == 0:
        reuse_ratio = -1.0
    elif upload != 0 and download == 0:
        reuse_ratio = float(upload)
    else:
        reuse_ratio = float(upload)/float(download)
    return reuse_ratio


def get_p2p_ratio(p2p, cdn):
    # 根据p2p, cdn值计算p2p占比
    if (p2p + cdn) == 0:
        p2p_ratio = -1.0
    else:
        p2p_ratio = float(p2p)/float(p2p + cdn)
    return p2p_ratio


def set_range(ob_range):
    """
    将单个值或范围值转换为数值范围, 如 [1, 10]
    :param ob_range: 可以为单个值, 如 1, "1", 也可以为范围值, 如 [1, 10]
    :return:
    """    
    try:
        if isinstance(ob_range, (int, long, str)):
            return [int(ob_range), int(ob_range)]
        elif isinstance(ob_range, (list, tuple)) and len(ob_range) == 2:
            return [int(ob_range[0]), int(ob_range[1])]
        else:
            raise TypeError("range should be like 10, or [10, 11]")
    except:
        raise ValueError("range should be like 10, or [10, 11]")


def get_random(ob_range):
    """
    获取指定数值范围内的随机值(浮点数); 注: 范围为[1, 10]时, 实际取值范围为[1, 10)
    :param ob_range: 可以为单个值, 如 1, "1", 也可以为范围值, 如 [1, 10]
    :return:
    """    
    try:
        if isinstance(ob_range, (int, float, long, str)):
            return float(ob_range)
        elif isinstance(ob_range, (list, tuple)) and len(ob_range) == 2:
            start, end = float(ob_range[0]), float(ob_range[1])
            return random() * (end - start) + start
        else:
            raise TypeError("range should be like 10, or [0, 10]")
    except:
        raise ValueError("range should be like 10, or [0, 10]")


def set_peer_id_list(prefix_range, peer_index_range, unique_id=0):
    """
    获取peer_id列表, peer_id个数为(prefix数 * peer_index数 * 1)
    :param prefix_range: peer_id的prefix的范围, 可以为单个值, 也可以为范围值, 如 [1, 10] (两边都取到)
    :param peer_index_range: peer_id的index的范围, 取值方式同上
    :param unique_id: 当prefix和index都相同时, 用来标识不同组的peer_id
    :return:
    """
    prefix_start, prefix_end = set_range(prefix_range)
    peer_index_start, peer_index_end = set_range(peer_index_range)
    peer_id_list = [str(i).zfill(8) + "F"*8 + str(unique_id).zfill(7) + "F" + str(j).zfill(8)
                    for i in xrange(prefix_start, prefix_end + 1) for j in xrange(peer_index_start, peer_index_end + 1)]
    return peer_id_list


def set_ssid_list(prefix_range, peer_index_range, unique_id=0):
    """
    获取ssid列表, ssid个数为(prefix数 * peer_index数 * 1)
    :param prefix_range: peer_id的prefix的范围, 可以为单个值, 也可以为范围值, 如 [1, 10] (两边都取到)
    :param peer_index_range: peer_id的index的范围, 取值方式同上
    :param unique_id: 当peer_id的prefix和index都相同时, 用来标识同一个peer_id的不同ssid
    :return:
    """
    prefix_start, prefix_end = set_range(prefix_range)
    peer_index_start, peer_index_end = set_range(peer_index_range)
    ssid_list = [str(i).zfill(3) + "D" + str(j).zfill(3) + "D" + str(unique_id).zfill(4)
                 for i in xrange(prefix_start, prefix_end + 1) for j in xrange(peer_index_start, peer_index_end + 1)]
    return ssid_list


def set_file_id_list(file_id_range, unique_id=0):
    """
    获取file_id列表
    :param file_id_range: file_id的范围, 可以为单个值, 也可以为范围值, 如 [1, 10] (两边都取到)
    :param unique_id: 当file_id的范围相同时, 用来标识不同的file_id
    :return:
    """
    file_id_start, file_id_end = set_range(file_id_range)
    file_id_list = [str(unique_id).zfill(3) + "F" + str(i).zfill(4) for i in xrange(file_id_start, file_id_end + 1)]
    return file_id_list


if __name__ == "__main__":
    pass
    # get_peer_id_list([1, 10], [1, 10])  # length = 100





