# coding=utf-8

"""

处理时间戳与日期

form参考 : '%Y-%m-%d %H:%M:%S'

__author__ = 'liwenxuan'
20170602

"""


import time


def time_to_timestamp(time_string):
    # 将格式为"YYYY-MM-DD HH:MM:SS"的时间字符串转化为时间戳
    return int(time.mktime(time.strptime(time_string, '%Y-%m-%d %H:%M:%S')))


def timestamp_to_time(second, form='%Y-%m-%d %H:%M:%S'):
    # 将时间戳转化为时间字符串
    return time.strftime(form, time.localtime(second))


def get_time_now():
    # 获取当前时间, 输出格式为"YYYY-MM-DD HH:MM:SS"
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_millisecond_now():
    # 获取当前毫秒级时间戳
    return int(time.time() * 1000)


def get_second_now():
    # 获取当前秒级时间戳
    return int(time.time())


def get_date_to_int(second=None):
    # 获取指定时间戳对应的日期的数字格式(yyyymmdd)
    date = time.strftime('%Y-%m-%d', time.localtime(second))
    date_to_int = date.replace("-", "")
    return int(date_to_int)


def get_time_to_int(second=None):
    # 获取指定时间戳对应的日期和时间的数字格式(mmddHHMM)
    date = time.strftime('%m-%d %H:%M', time.localtime(second))
    time_to_int = date.replace("-", "").replace(":", "").replace(" ", "")
    return int(time_to_int)


def get_second_to_int(second=None):
    # 获取指定时间戳对应的日期和时间的数字格式(ddHHMMSS)
    date = time.strftime('%d %H:%M:%S', time.localtime(second))
    second_to_int = date.replace(":", "").replace(" ", "")
    return int(second_to_int)


# 期望时间的秒级时间戳与毫秒级时间戳之间的转换
def second_to_second(form, ts_second=None):
    # 时间戳(秒)转化为期望时间戳(秒), 如 期望获得当天00:00的时间戳
    date = time.strftime(form, time.localtime(ts_second))  # ts to date
    timestamp = time.mktime(time.strptime(date, form))  # date to ts
    return int(timestamp)


def millisecond_to_millisecond(form, ts_millisecond=None):
    # 时间戳(毫秒)转化为期望时间戳(毫秒), 如 期望获得当天00:00的时间戳
    if ts_millisecond is None:
        ts_second = None
    else:
        ts_second = ts_millisecond/1000
    date = time.strftime(form, time.localtime(ts_second))  # ts to date
    ts_second = time.mktime(time.strptime(date, form))  # date to ts
    ts_millisecond = int(ts_second)*1000
    return ts_millisecond


def second_to_millisecond(form, ts_second=None):
    # 时间戳(秒)转化为期望时间戳(毫秒), 如 期望获得当天00:00的时间戳
    date = time.strftime(form, time.localtime(ts_second))  # ts to date
    ts_second = time.mktime(time.strptime(date, form))  # date to ts
    ts_millisecond = int(ts_second)*1000
    return ts_millisecond


def millisecond_to_second(form, ts_millisecond=None):
    # 时间戳(毫秒)转化为期望时间戳(秒), 如 期望获得当天00:00的时间戳
    if ts_millisecond is None:
        ts_second = None
    else:
        ts_second = ts_millisecond/1000
    date = time.strftime(form, time.localtime(ts_second))  # ts to date
    ts_second = time.mktime(time.strptime(date, form))  # date to ts
    return int(ts_second)


# 取特定时间段的起始时间
def period_five_minutes(timestamp):
    # 获取当前五分钟段的起始时间的时间戳
    if len(str(timestamp)) < 12:
        remainder = timestamp % 300
    else:
        remainder = timestamp % 300000
    return timestamp - remainder


# 取范围内的所有date
def get_date_list_by_date(start_date, end_date):
    # 取[start_date, end_date]中的所有date
    start_timestamp = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
    end_timestamp = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))
    date_list = []
    for i in range(start_timestamp, end_timestamp + 1, 86400):
        date_list.append(time.strftime("%Y-%m-%d", time.localtime(i)))
    return date_list


if __name__ == "__main__":
    pass
    print get_time_to_int()
    # print second_to_second("%Y-%m-%d %H", int(time.time()-86400))
    # print millisecond_to_millisecond("%Y-%m-%d %H", 1488358800000)
    # print period_five_minutes(1488358851000)



