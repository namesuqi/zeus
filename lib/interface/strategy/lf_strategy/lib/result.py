# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170813

作用: 根据输入数据计算输出结果

"""

from lib.interface.strategy.lf_strategy.lib.time_handler import to_millisecond


# ---------------------------------------------------------------------------------------------------------------------

# from random import choice
#
# # 各字段取随机值时的范围
# province_id_random_range = [1, 2, 3]
# isp_id_random_range = [1, 2, 3]
# sdk_version_random_range = ["3.11.0", "3.12.0", "3.12.5"]
# op_random_range = ["add", "-", "-", "-", "del"]
# p2p_enable_random_range = [True, True, False]
#
#
# # 使一组logs中部分字段的值随机
# def send_random(function_name, *random_fileds, **other_params):
#     pass

# ---------------------------------------------------------------------------------------------------------------------


def get_peer_result(start_time, end_time, login_count, pi_interval, hb_interval, hb_per_pi, adjust_second=-8*60*60):
    start_ts_ms = to_millisecond(start_time)
    end_ts_ms = to_millisecond(end_time)
    # start_breakpoint = time_to_timestamp(timestamp_to_time(start_ts_ms/1000, "%Y-%m-%d"), "%Y-%m-%d") * 1000
    print start_ts_ms
    tt = start_ts_ms
    print tt % 86400000
    start_breakpoint = start_ts_ms - tt % 86400000
    print start_breakpoint
    print start_breakpoint + adjust_second * 1000

    # day_list = [bp for bp in range(start_breakpoint, end_ts_ms, 86400000)]
    # day_list.append(end_ts_ms)
    # print day_list

    # breakpoint_ts_ms = 10**13
    #
    # sum_duration = min((heartbeat_interval * hb_per_pi), login_interval) * (login_count - 1) + (heartbeat_interval * hb_per_pi)
    # duration_list = []
    # du = duration = 0
    # ts_ms = start_ts_ms
    # for d in range(login_count-1):
    #     du = min((heartbeat_interval * hb_per_pi), login_interval)
    #     if (ts_ms + du) < breakpoint_ts_ms:
    #         ts_ms += du
    #         duration += du
    #     else:
    #         duration_list.append(duration)
    #         duration = 0

    # return {day1: (duration, online_count), ...}


def get_channel_result(play_count, p2p_ratio, lf_valid_count, lf_invalid_count):
    pass
    # return join_count, leave_count


get_peer_result("2017-08-14 00:05:00", "2017-08-15 06:00:00", 1, 10, 3, 3)

