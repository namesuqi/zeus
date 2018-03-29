# coding=utf-8
"""
运维控制台部署服务器后端接口

__author__ = 'th'

"""
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def get_available_services(protocol, control_deploy_host, control_deploy_port):
    """
    获取可部署服务
    :param protocol:
    :param control_deploy_host:
    :param control_deploy_port:
    :return:
    """

    url = "/available/services"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetAvailableServices]',
        protocol,
        GET,
        control_deploy_host,
        control_deploy_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_all_servers(protocol, control_deploy_host, control_deploy_port):
    """
    获取所有已分配主机的服务信息，包括状态信息
    :param protocol:
    :param control_deploy_host:
    :param control_deploy_port:
    :return:
    """

    url = "/all/servers"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetAllServers]',
        protocol,
        GET,
        control_deploy_host,
        control_deploy_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_archive_version(protocol, control_deploy_host, control_deploy_port, server_name):
    """
    从Archive服务器获取指定服务的可用版本返给Control
    :param protocol:
    :param control_deploy_host:
    :param control_deploy_port:
    :param server_name
    :return:
    """

    url = "/archive/versions?servername=" + server_name
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetArchiveVersion]',
        protocol,
        GET,
        control_deploy_host,
        control_deploy_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def set_service_hosts(protocol, control_deploy_host, control_deploy_port, server_name, host_id):
    """
    为服务分配主机
    :param protocol:
    :param control_deploy_host:
    :param control_deploy_port:
    :return:
    """

    url = "/service/hosts"

    body_data = {
        "server_name": server_name,
        "host_id": host_id
    }

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[SetServiceHosts]',
        protocol,
        POST,
        control_deploy_host,
        control_deploy_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def post_host_servers(protocol, host, port, host_id, server_version, value, counter, server_name, status, timestamp=1491876339, step=60, value2=0):
    """
    接收agent汇报的服务信息，包括服务运行的状态信息
    服务运行异常时，接收agent秒级的服务状态信息汇报
    :param protocol:
    :param host:
    :param port:
    :param server_name
    :param host_id
    :return:
    """

    url = "/host/servers"

    body_data = [
        {
            "endpoint": host_id,
            "metric": server_version,
            "value": value,
            "step": step,
            "counterType": counter,
            "tags": server_name,
            "timestamp": timestamp
        },
        {
            "endpoint": host_id,
            "metric": status,
            "value": value2,
            "step": step,
            "counterType": counter,
            "tags": server_name,
            "timestamp": timestamp
        }
    ]

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[PostHostServers]',
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
def server_ctrl(protocol, control_deploy_host, control_deploy_port, server_ctrl, host_id, release, server_name, server_version):
    """
    服务相关操作
    :param protocol:
    :param control_deploy_host:
    :param control_deploy_port:
    :return:
    """

    url = "/server/ctrl"

    body_data = {
        "topic": server_ctrl,
        "data": {
             "hostIds": host_id,
             "env": release,
             "serverName": server_name,
             "serverVersion":  server_version
        }
    }

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[SetServiceHosts]',
        protocol,
        POST,
        control_deploy_host,
        control_deploy_port,
        url,
        headers,
        None,
        body_data
    )
    return response

