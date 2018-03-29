# coding=utf-8
"""
运维控制台监控服务器后端接口

__author__ = 'zsw'

"""
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def agent_post_heartbeat(protocol, control_monitor_host, control_monitor_port, host_id):
    """
    模拟agent的心跳接口
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param host_id:
    :return:
    """

    url = "/agent/heartbeat"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    body = {
        "host_id": host_id
    }

    response = send_request(
        '[PostAgentHeartbeat]',
        protocol,
        POST,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        body
    )
    return response


@print_trace
def post_monitor_basic(protocol, control_monitor_host, control_monitor_port, body):
    """
    接收agent汇报的流量、负载、内存使用、硬盘使用等基本监测信息，并写入rrdtool数据库
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param body:
    :return:
    """

    url = "/monitor/basic"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[PostMonitorBasic]',
        protocol,
        POST,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        body
    )
    return response


@print_trace
def get_host_load(protocol, control_monitor_host, control_monitor_port, host_id, start_time, end_time, step):
    """
    获取主机的历史负载信息
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param host_id: 主机唯一标示id
    :param start_time: 起始时间戳，单位s
    :param end_time: 截止时间戳，单位s(注意start，end，step的取值，每次最多返回60*24条数据)
    :param step: 时间粒度，单位s，只能取1或60(60秒内的最大值)
    :return:
    """

    url = "/load?hostId={0}&start={1}&end={2}&step={3}".format(str(host_id), str(start_time), str(end_time), str(step))
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[GetHostLoad]',
        protocol,
        GET,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_host_flow(protocol, control_monitor_host, control_monitor_port, host_id, start_time, end_time, step):
    """
    获取主机的历史流量信息
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param host_id:
    :param start_time:
    :param end_time:
    :param step:
    :return:
    """

    url = "/flow?hostId={0}&start={1}&end={2}&step={3}".format(str(host_id), str(start_time), str(end_time), str(step))
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[GetHostFlow]',
        protocol,
        GET,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_host_mem(protocol, control_monitor_host, control_monitor_port, host_id, start_time, end_time, step):
    """
    获取主机的内存使用信息
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param host_id:
    :param start_time:
    :param end_time:
    :param step:
    :return:
    """

    url = "/mem?hostId={0}&start={1}&end={2}&step={3}".format(str(host_id), str(start_time), str(end_time), str(step))
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[GetHostMem]',
        protocol,
        GET,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_host_disk(protocol, control_monitor_host, control_monitor_port, host_id, start_time, end_time, step):
    """
    获取主机的硬盘使用信息
    :param protocol:
    :param control_monitor_host:
    :param control_monitor_port:
    :param host_id:
    :param start_time:
    :param end_time:
    :param step:
    :return:
    """

    url = "/disk?hostId={0}&start={1}&end={2}&step={3}".format(str(host_id), str(start_time), str(end_time), str(step))
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[GetHostDisk]',
        protocol,
        GET,
        control_monitor_host,
        control_monitor_port,
        url,
        headers,
        None,
        None
    )
    return response
