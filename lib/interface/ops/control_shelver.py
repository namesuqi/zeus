# coding=utf-8
"""
运维控制台上架服务器后端接口

__author__ = 'th'

"""
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def get_initialized_hosts(protocol, control_shelver_host, control_shelver_port):
    """
    获取已初始化的主机信息列表
    :param protocol:
    :param control_shelver_host:
    :param control_shelver_port:
    :return:
    """

    url = "/hosts/list"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetInitializedHosts]',
        protocol,
        GET,
        control_shelver_host,
        control_shelver_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_removed_hosts(protocol, control_shelver_host, control_shelver_port):
    """
    获取已申请，但未初始化的主机信息列表
    :param protocol:
    :param control_shelver_host:
    :param control_shelver_port:
    :return:
    """

    url = "/hosts/removed"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetRemovedHosts]',
        protocol,
        GET,
        control_shelver_host,
        control_shelver_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def agent_post_host(protocol, control_shelver_host, control_shelver_port, host_id, host_os_value, host_ip_value,
                    hostname_value, cpu_value, mem_value, df_statistics_value, step, timestamp, counter="GAGUE",
                    tags=""):
    """
    模拟agent向上架服务器汇报主机信息
    :param protocol:
    :param control_shelver_host:
    :param control_shelver_port:
    :param host_id:
    :param host_os_value: 主机操作系统
    :param host_ip_value: 主机ip地址
    :param hostname_value:
    :param cpu_value: cpu核数
    :param mem_value: 内存总容量(单位KB)
    :param df_statistics_value: 磁盘总容量，单位KB
    :param step: 汇报间隔，单位s
    :param timestamp: 时间戳，单位s
    :param counter: 暂时忽略
    :param tags: 暂时忽略
    :return:
    """

    url = "/hosts"
    body_data = []
    metric_dict = {
        "host.os": host_os_value,
        "host.ip": host_ip_value,
        "host.hostname": hostname_value,
        "cpu.mount": cpu_value,
        "mem.memtotal": mem_value,
        "df.statistics.total": df_statistics_value
    }
    for k, v in metric_dict.items():
        body_simple = {
            "endpoint": host_id,
            "metric": k,
            "value": v,
            "step": step,
            "counterType": counter,
            "tags": tags,
            "timestamp": timestamp
        }
        body_data.append(body_simple)

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[AgentPostHost]',
        protocol,
        POST,
        control_shelver_host,
        control_shelver_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def update_host(protocol, control_shelver_host, control_shelver_port, host_id, update_key, new_value):
    """
    更新某台主机的登记信息
    :param protocol:
    :param control_shelver_host:
    :param control_shelver_port:
    :param host_id:
    :param update_key:
    :param new_value:
    :return:
    """
    url = "/hosts/info"

    body_data = {
        "host_id": host_id,
        "update_key": update_key,
        "new_value": new_value
    }

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[UpdateHost]',
        protocol,
        PUT,
        control_shelver_host,
        control_shelver_port,
        url,
        headers,
        None,
        body_data
    )
    return response
