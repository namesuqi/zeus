# coding=utf-8

"""

boss系统-服务API

__author__ = 'liwenxuan'

"""


import hashlib
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


# 计费模块相关的接口
@print_trace
def get_customer_info(protocol, host, port, api_access_key, timestamp, sign, prefix, *del_num):
    """
    boss-对内接口 : 获取客户信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param prefix: 需要获取的客户信息中, 该客户的其中一个prefix
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "prefix"]
    #                    0               1           2       3

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_customer_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "prefix": prefix}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_customer_info"][field_list[i]]

    response = send_request(
        '[BossGetCustomerInfo]',
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
def get_billing_rule(protocol, host, port, api_access_key, timestamp, sign, prefix, category, *del_num):
    """
    boss-对内接口 : 获取客户计费规则信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param prefix: 需要获取的计费规则信息对应的prefix
    :param category: 需要获取计费规则信息对应的类别, "upload"或"download"
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "prefix", "category"]
    #                   0               1          2        3          4

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_billing_rule": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "prefix": prefix,
            "category": category}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_billing_rule"][field_list[i]]

    response = send_request(
        '[BossGetBillingRule]',
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


# Panel对接接口
@print_trace
def get_activity_number(protocol, host, port, api_access_key, timestamp, sign, customer_id, *del_num):
    """
    boss-对内接口 : 获取客户当前节点信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id"]
    #                   0               1          2            3

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_activity_number": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_activity_number"][field_list[i]]

    response = send_request(
        '[BossGetActivityNumber]',
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
def get_activity_info(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, *del_num):
    """
    boss-对内接口 : 获取客户历史活跃节点信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end"]
    #                   0               1          2            3           4       5

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_activity_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_activity_info"][field_list[i]]

    response = send_request(
        '[BossGetActivityInfo]',
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
def get_activity_online_info(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, *del_num):
    """
    boss-对内接口 : 获取客户历史在线节点信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end"]
    #                   0               1          2            3           4       5

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_activity_online_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_activity_online_info"][field_list[i]]

    response = send_request(
        '[BossGetActivityOnlineInfo]',
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
def get_traffic_info(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, step, *del_num):
    """
    boss-对内接口 : 获取客户历史流量信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end", "step"]
    #                   0               1          2            3           4       5       6

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_traffic_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end,
            "step": step}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_traffic_info"][field_list[i]]

    response = send_request(
        '[BossGetTrafficInfo]',
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
def get_bandwidth_info(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, step, *del_num):
    """
    boss-对内接口 : 获取客户历史带宽信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param step: 需要获取的信息的时间间隔 "day" or "hour" or "minute" -- "minute"代表5分钟
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end", "step"]
    #                   0               1          2            3           4       5       6

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_bandwidth_info": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end,
            "step": step}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_bandwidth_info"][field_list[i]]

    response = send_request(
        '[BossGetBandwidthInfo]',
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
def get_qos_startup(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, *del_num):
    """
    boss-对内接口 : 获取客户启播时间分布信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end"]
    #                   0               1          2            3           4       5

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_qos_startup": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_qos_startup"][field_list[i]]

    response = send_request(
        '[BossGetQosStartup]',
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
def get_qos_buffer(protocol, host, port, api_access_key, timestamp, sign, customer_id, start, end, *del_num):
    """
    boss-对内接口 : 获取客户卡顿次数分布信息
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param customer_id: 客户对应的id
    :param start: 请求获取信息的时间段的起始时间
    :param end: 请求获取信息的时间段的结束时间
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign", "customer_id", "start", "end"]
    #                   0               1          2            3           4       5

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_qos_buffer": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign,
            "customer_id": customer_id,
            "start": start,
            "end": end}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_qos_buffer"][field_list[i]]

    response = send_request(
        '[BossGetQosBuffer]',
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
def get_customers(protocol, host, port, api_access_key, timestamp, sign, *del_num):
    """
    boss-对内接口 : 获取客户列表(客户id及客户名称)
    :param protocol:
    :param host:
    :param port:
    :param api_access_key: 内部应用的access_key, 四十位十六进制
    :param timestamp: 鉴权参数, 时间戳, 单位为秒, 非负整数
    :param sign: 鉴权参数, MD5加密后的值, 三十二位十六进制
    :param del_num: 控制字段缺失的序号
    :return:
    """

    field_list = ["api_access_key", "timestamp", "sign"]
    #                   0               1          2

    url = "/api/internal"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "get_customers": {
            "api_access_key": api_access_key,
            "timestamp": timestamp,
            "sign": sign}}
    for i in del_num:
        if i in range(len(field_list)):
            del body_data["get_customers"][field_list[i]]

    response = send_request(
        '[BossGetCustomers]',
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


