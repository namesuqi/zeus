# coding=utf-8

"""

boss系统-客户API

__author__ = 'zsw'

"""

from lib.constant.request import *
from lib.decorator.trace import *
from lib.request.header_data import *
from lib.request.http_request import *


# 上游
@print_trace
def activity_info(protocol, host, port, api_access_key, timestamp, sign, start_day, end_day, *del_num):
    """
    boss-上游客户 : 获取日活节点信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start_day: 请求获取信息的时间段的起始日期
    :param end_day: 请求获取信息的时间段的结束日期
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start_day", "end_day"]
    #                   0               1          2          3           4

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "activity_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start_day": start_day,
            "end_day": end_day
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["activity_info"][field_list[i]]

    response = send_request(
        '[BossActivityInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def activity_online_info(protocol, host, port, api_access_key, timestamp, sign, start, end, *del_num):
    """
    boss-上游客户 : 获取在线节点信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end"]
    #                    0               1          2        3      4

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "activity_online_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["activity_online_info"][field_list[i]]

    response = send_request(
        '[BossActivityOnlineInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def up_traffic_info(protocol, host, port, api_access_key, timestamp, sign, start, end, step, *del_num):
    """
    boss-上游客户 : 获取流量信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end", "step"]
    #                    0               1          2        3      4       5

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "up_traffic_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end,
            "step": step
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["up_traffic_info"][field_list[i]]

    response = send_request(
        '[BossUpTrafficInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def up_bandwidth_info(protocol, host, port, api_access_key, timestamp, sign, start, end, step, *del_num):
    """
    boss-上游客户 : 获取带宽信息接口
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end", "step"]
    #                    0               1          2        3      4       5

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "up_bandwidth_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end,
            "step": step
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["up_bandwidth_info"][field_list[i]]

    response = send_request(
        '[BossUpBandwidthInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


# 下游
@print_trace
def customer_domain_read(protocol, host, port, api_access_key, timestamp, sign, domains=None,  *del_num):
    """
    boss-下游客户 : 查询域名信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param domains:
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "domains"]
    #                   0               1           2         3

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "customer_domain_read": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "domains": domains
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["customer_domain_read"][field_list[i]]

    response = send_request(
        '[BossCustomerDomainRead]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def customer_domain_create(protocol, host, port, api_access_key, timestamp, sign, domain_names, *del_num):
    """
    boss-下游客户 : 添加新域名
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param domain_names: 需要添加的域名的列表，[{"domain_name": "a.com"}, {"domain_name": "b.com"}]
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "domain_names"]
    #                   0               1          2             3

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "customer_domain_create": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "domain_names": domain_names
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["customer_domain_create"][field_list[i]]

    response = send_request(
        '[BossCustomerDomainCreate]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def customer_domain_delete(protocol, host, port, api_access_key, timestamp, sign, domain_names, *del_num):
    """
    boss-下游客户 : 删除域名
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param domain_names: 需要删除的域名的列表，[{"domain_name": "a.com"}, {"domain_name": "b.com"}]
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "domain_names"]
    #                     0               1          2        3

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "customer_domain_delete": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "domain_names": domain_names
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["customer_domain_delete"][field_list[i]]

    response = send_request(
        '[BossCustomerDomainDelete]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def down_traffic_total(protocol, host, port, api_access_key, timestamp, sign, start, end, domain=None, *del_num):
    """
    boss-下游客户 : 获取SDK播放流量汇总信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param domain: 可选, 指定域名信息, 不指定则认为请求所有域名的信息
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end", "domain"]
    #                    0               1          2        3      4       5

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "down_traffic_total": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end,
            "domain": domain
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["down_traffic_total"][field_list[i]]

    response = send_request(
        '[BossDownTrafficTotal]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def down_traffic_info(protocol, host, port, api_access_key, timestamp, sign, start, end, step, domain=None, *del_num):
    """
    boss-下游客户 : 获取SDK播放流量信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param domain: 可选, 指定域名信息, 不指定则认为请求所有域名的信息
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end", "step", "domain"]
    #                    0               1          2        3      4       5       6

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "down_traffic_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end,
            "step": step,
            "domain": domain
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["down_traffic_info"][field_list[i]]

    response = send_request(
        '[BossDownTrafficInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def down_bandwidth_info(protocol, host, port, api_access_key, timestamp, sign, start, end, step, domain=None, *del_num):
    """
    boss-下游客户 : 获取SDK播放带宽信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param domain: 可选, 指定域名信息, 不指定则认为请求所有域名的信息
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "end", "step", "domain"]
    #                    0               1          2        3      4       5       6

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "down_bandwidth_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "end": end,
            "step": step,
            "domain": domain
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["down_bandwidth_info"][field_list[i]]

    response = send_request(
        '[BossDownBandwidthInfo]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def down_minute_traffic(protocol, host, port, api_access_key, timestamp, sign, start, domains=None, *del_num):
    """
    boss-下游客户(云端) : 获取五分钟段内的流量汇总信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 某客户的access_key值, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param start: 请求获取信息的时间段的起始时间
    :param domain: 可选, 指定域名信息, 不指定则认为请求所有域名的信息
    :param del_num: 控制字段缺失的序号
    :return:
    """
    field_list = ["api_access_key", "timestamp", "sign", "start", "domains"]
    #                    0               1          2        3        4

    url = "/api/external"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "down_minute_traffic": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "start": start,
            "domains": domains
        }
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["down_minute_traffic"][field_list[i]]

    response = send_request(
        '[BossDownMinuteTraffic]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


