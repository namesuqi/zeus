# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170810

作用: 针对peer模块的测试用例

"""

import time
import threading

from lib.interface.strategy.lf_strategy.backup.case_various_module import peer_online
from lib.interface.strategy.lf_strategy.lib.log_handler import logger
from lib.interface.strategy.lf_strategy.lib.utility import set_range
from lib.interface.strategy.lf_strategy.lib.time_handler import get_particular_date, get_millisecond_now, to_millisecond





# ---------------------------------------------------------------------------------------------------------------------

day_1 = get_particular_date(0) + " "
day_2 = get_particular_date(1) + " "
day_3 = get_particular_date(2) + " "
adjust_second = 0  # 根据跨天切换点调整
# adjust_second = -8*60*60  # 8小时时区差

# ---------------------------------------------------------------------------------------------------------------------

# 测试用例格式: [prefix_range, peer_index_range, ssid_start, start_time, end_time, {case_condition, ...}]
c = [1, [1, 100], 0, day_1+"12:00:00", day_2+"12:00:00", {}]

# ---------------------------------------------------------------------------------------------------------------------

# 可选参数一览, 详细说明请见对应的函数内的说明
# peer_online(prefix_range, peer_index_range, ssid_start, start_time=get_time_now(), end_time="2020-01-01 00:00:00",
#             login_count=1, login_interval=3*60, heartbeat_interval=1*60, hb_per_pi=-1, adjust_second=0,
#             province_id="p_1", isp_id="i_1", sdk_version="3.15.0", peer_unique_id="AB"*3)


def multi_peer_online(case_interval, *case_suites, **conditions):
    """
    多线程执行peer模块长时间运行部分的用例
    :param case_suites: 测试用例集的组合
    一个测试用例(case)的格式为[prefix_range, peer_index_range, ssid_start, start_time, end_time, {case_condition, ...}]
    一个测试用例集(case_suite)的格式为[case_1, case_2, ..., {cases_condition}]
    :param conditions: 对各个case_suite中的所有cases生效, 可添加的条件请见上面的说明, 或参考对应函数内的说明;
                       cases_condition: 对该case_suite中的所有cases生效; case_condition: 对该case生效
                       condition的优先级: case_condition > cases_condition > conditions
    :return:
    """
    assert int(case_interval) > 0
    for case_suite in case_suites:
        if isinstance(case_suite[-1], dict):
            cases_condition = dict(conditions, **case_suite.pop())
        else:
            cases_condition = conditions
        for case in case_suite:
            if isinstance(case[-1], dict):
                case_condition = dict(cases_condition, **case[-1])
            else:
                case_condition = cases_condition
            t = threading.Thread(target=peer_online, args=(case[0], case[1], case[2], case[3], case[4]),
                                 kwargs=case_condition)
            t.start()
            time.sleep(int(case_interval))


def add_peer_by_interval(end_time, interval, case):
    """
    每隔一定时间加入一批新的节点执行同样的用例
    :param end_time: case的结束时间, 可以为时间戳或"YYYY-MM-DD HH:MM:SS"格式的时间字符串
    :param interval: 每批节点的间隔时间
    :param case: 格式应为[prefix_range, peer_index_range, ssid_start, start_time, end_time, {case_condition, ...}]
                 case中的start_time和end_time不会生效, 也可将格式简化[prefix_range, peer_index_range, ssid_start, {...}]
    :return:
    """
    assert int(interval) > 0
    # 设定case的条件
    if isinstance(case[-1], dict):
        case_condition = dict(case[-1], **{"end_time": end_time})
    else:
        case_condition = {"end_time": end_time}
    # 使peer_id的后缀的值逐次递增
    pid_start, pid_end = set_range(case[1])
    differ = pid_end - pid_start
    # 每隔一定时间加入新的peer_id
    end_ts_ms = to_millisecond(end_time)
    while get_millisecond_now() < end_ts_ms:
        t = threading.Thread(target=peer_online, args=(case[0], [pid_start, pid_end], case[2]), kwargs=case_condition)
        t.setDaemon(True)
        t.start()
        pid_start += differ + 1
        pid_end += differ + 1
        time.sleep(interval)


if __name__ == "__main__":
    logger.setLevel("WARN")

    # multi_peer_online(3, adjust_second=adjust_second)

    add_peer_by_interval("2017-08-15 16:55:00", 30,
                         [1, [1, 3], 0, {"login_count": 5, "login_interval": 3*60,
                                         "heartbeat_interval": 20, "hb_per_pi": -1}])








