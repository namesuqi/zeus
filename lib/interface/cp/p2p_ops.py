# coding=utf-8
"""
ops相关服务器访问接口

__author__ = 'zsw'

"""


from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *
from lib.sdk.common_tool.ssh_client import SSHClient


@print_trace
def channel_strategy_off(protocol, host, port, file_ids=None):

    url = "/channel/strategy/switch/off"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if file_ids is None:
        body_data = []
    elif type(file_ids) != list:
        body_data = [file_ids]
    else:
        body_data = file_ids

    response = send_request(
        '[ops]',
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
def channel_strategy_on(protocol, host, port, file_ids=None):

    url = "/channel/strategy/switch/on"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if file_ids is None:
        body_data = []
    elif type(file_ids) != list:
        body_data = [file_ids]
    else:
        body_data = file_ids

    response = send_request(
        '[ops]',
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
def get_channel_strategy_status(protocol, host, port):

    url = "/channel/strategy/switch/off"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ops]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def user_strategy_off(protocol, host, port, user_ids=None):

    url = "/user/strategy/switch/off"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if user_ids is None:
        body_data = []
    elif type(user_ids) != list:
        body_data = [user_ids]
    else:
        body_data = user_ids

    response = send_request(
        '[ops]',
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
def user_strategy_on(protocol, host, port, user_ids=None):

    url = "/user/strategy/switch/on"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if user_ids is None:
        body_data = []
    elif type(user_ids) != list:
        body_data = [user_ids]
    else:
        body_data = user_ids

    response = send_request(
        '[ops]',
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
def get_user_strategy_status(protocol, host, port):

    url = "/user/strategy/switch/off"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ops]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def upsert_httpdns_group(protocol, host, port, groupname, *hosts):

    url = "/httpdns/conf/domain_group?groupName=" + str(groupname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = []
    for i in hosts:
        body_data.append(i)

    response = send_request(
        '[opsHttpdns]',
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
def upsert_httpdns_host(protocol, host, port, hostname, ttl, *division):

    url = "/httpdns/conf/domain?name=" + str(hostname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    divisions = []
    for i in division:
        divisions.append(i)
    body_data = {"ttl": ttl, "divisions": divisions}

    response = send_request(
        '[opsHttpdns]',
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
def get_httpdns_group(protocol, host, port, groupname):

    url = "/httpdns/conf/domain_group?groupName=" + str(groupname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_httpdns_groups(protocol, host, port):

    url = "/httpdns/conf/domain_groups"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_httpdns_host(protocol, host, port, hostname):

    url = "/httpdns/conf/domain?name=" + str(hostname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def get_httpdns_hosts(protocol, host, port):

    url = "/httpdns/conf/domains"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def delete_httpdns_host(protocol, host, port, hostname):

    url = "/httpdns/conf/domain?name=" + str(hostname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        DELETE,
        host,
        port,
        url,
        headers,
        None,
        {}
    )
    return response


@print_trace
def delete_httpdns_group(protocol, host, port, groupname):

    url = "/httpdns/conf/domain_group?groupName=" + str(groupname)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[opsHttpdns]',
        protocol,
        DELETE,
        host,
        port,
        url,
        headers,
        None,
        {}
    )
    return response


@print_trace
def ops_join_lf(protocol, host, port, file_url, peer_ids):
    """
    发送拉入雷锋的请求
    :param protocol:
    :param host:
    :param port:
    :param file_url:
    :param peer_ids:
    :return:
    """

    url = "/leifeng/join/by/peers"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_url": file_url,
        "peer_ids": peer_ids
    }

    response = send_request(
        '[opsJoinLf]',
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
def ops_join_lf_by_condition(protocol, host, port, file_url, isp_id, count, user_id='', sdk_support_checksum=''):
    """

    :param protocol:
    :param host:
    :param port:
    :param file_url:
    :param isp_id:
    :param count:
    :param user_id:
    :param sdk_support_checksum:
    :return:
    """
    user_id = str(user_id)
    url = "/leifeng/join/by/condition"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    body_data = {
        'file_url': file_url,
        'isp_id': isp_id,
        'count': count,
        'user_id': user_id,
        'sdk_support_checksum': sdk_support_checksum
    }
    response = send_request(
        '[opsJoinLfByCondition]',
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
def ops_leave_lf(protocol, host, port, file_url, peer_ids):
    """

    :param protocol:协议
    :param host:
    :param port:
    :param file_url:频道的播放url
    :param peer_ids:需要清退的LF的peer_id列表
    :return:
    """

    url = '/leifeng/leave/by/peers'
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    if type(peer_ids) != list:
        peer_ids = [peer_ids]
    body_data = {
        'file_url': file_url,
        'peer_ids': peer_ids,
    }
    response = send_request(
        '[opsLeaveLf]',
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
def ops_leave_lf_by_condition(protocal, host, port, file_url, isp_id, user_id, watermark):
    """

    :param protocal: 协议
    :param host:
    :param port:
    :param file_url:
    :param isp_id: 运营商ID
    :param user_id: PEER ID 前八位
    :param watermark: 保留的LF数量, 仅在isp_id参数存在的时候有意义, 值为0都表示把符合要求的LF都清退
    :return:
    """

    url = '/leifeng/leave/by/condition'
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    if watermark == '':
        body_data = {
            'file_url': file_url,
            'isp_id': isp_id,
            'user_id': user_id,
        }
    else:
        body_data = {
            'file_url': file_url,
            'isp_id': isp_id,
            'user_id': user_id,
            'watermark': watermark
        }
    response = send_request(
        '[opsLeaveLfCondition]',
        protocal,
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
def ssh_command(ip, user, password, cmd):
    """

    :param ip: 连接的HOST IP
    :param user: HOST的用户名
    :param password: HOST的密码
    :param cmd: 命令
    :return:
    """

    ssh = SSHClient(ip, user, password)
    ssh.execute_command(cmd)
