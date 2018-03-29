# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170803

说明:
1. 作用: 提供时间&时间戳相关的处理函数
2. time: 时间字符串, 格式可以自定义, 如'%Y-%m-%d %H:%M:%S'
   timestamp: 时间戳, 注意区分秒级时间戳(s或second)和毫秒级时间戳(ms或millisecond), 默认为秒级时间戳

"""

import time


def time_to_timestamp(time_string, fmt='%Y-%m-%d %H:%M:%S'):
    # 将时间字符串转化为时间戳(秒级)
    return int(time.mktime(time.strptime(time_string, fmt)))


def timestamp_to_time(second=None, fmt='%Y-%m-%d %H:%M:%S'):
    # 将时间戳(秒级)转化为时间字符串
    return time.strftime(fmt, time.localtime(second))


def to_millisecond(t_object, fmt='%Y-%m-%d %H:%M:%S'):
    # 将timestamp或time转换为毫秒级的时间戳
    try:
        timestamp = int(t_object)
        if len(str(timestamp)) > 12:
            ts_ms = timestamp
        else:
            ts_ms = timestamp * 1000
    except ValueError:
        ts_ms = time_to_timestamp(t_object, fmt) * 1000
    return ts_ms


def get_time_now(fmt='%Y-%m-%d %H:%M:%S'):
    # 获取当前时间
    return time.strftime(fmt, time.localtime())


def get_millisecond_now():
    # 获取当前时间戳(毫秒级)
    return int(time.time() * 1000)


def get_second_now():
    # 获取当前时间戳(秒级)
    return int(time.time())


def get_particular_time(adjust_minute, reference_time=None,
                        output_format='%Y-%m-%d %H:%M:%S', input_format='%Y-%m-%d %H:%M:%S'):
    """
    获取调整指定分钟数后的时间, 默认时间为次日00:00:00
    :param adjust_minute: 指定需要调整的分钟数, 可以为小数
    :param reference_time: 指定调整的对象(时间字符串), 默认为次日00:00:00
    :param output_format: 指定输出的时间字符串的格式
    :param input_format: 指定输入的时间字符串的格式, 必须与reference_time的格式一致
    :return:
    """
    if reference_time is None:
        date = timestamp_to_time(get_second_now() + 86400, '%Y-%m-%d')
        ts = time_to_timestamp(date, '%Y-%m-%d')
    else:
        ts = to_millisecond(reference_time, input_format)/1000

    ts_after_adjust = int(ts + float(adjust_minute) * 60)
    time_after_adjust = timestamp_to_time(ts_after_adjust, output_format)
    return time_after_adjust


def get_particular_date(adjust_day, reference_date=None, output_format='%Y-%m-%d', input_format='%Y-%m-%d'):
    """
    获取调整指定天数后的日期, 默认日期为当天
    :param adjust_day: 指定需要调整的天数, 可以为小数
    :param reference_date: 指定调整的对象(日期), 默认为当天00:00:00
    :param output_format: 指定输出的日期的格式
    :param input_format: 指定输入的日期的格式, 必须与reference_date的格式一致
    :return:
    """
    if reference_date is None:
        ts = time_to_timestamp(get_time_now('%Y-%m-%d'), '%Y-%m-%d')
    else:
        ts = to_millisecond(reference_date, input_format)/1000

    ts_after_adjust = int(ts + float(adjust_day) * 24 * 60 * 60)
    time_after_adjust = timestamp_to_time(ts_after_adjust, output_format)
    return time_after_adjust





