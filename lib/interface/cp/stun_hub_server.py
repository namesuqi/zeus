# coding=utf-8
"""
stun-hub related api test keyword

__author__ = 'liwenxuan'

"""

from lib.constant.request import *
from lib.decorator.trace import *
from lib.request.header_data import *
from lib.request.http_request import *


@print_trace
def hub_join_lf(protocol, host, port, file_id="", file_url="", peer_ids=""):
    """
    向stun-hub发送拉入雷锋的请求
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param file_url:
    :param peer_ids:
    :return:
    """

    url = "/join_lf"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunHubJoinLf]',
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
def hub_leave_lf(protocol, host, port, file_id="", peer_ids=""):
    """
    向stun-hub发送清退雷锋的请求
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param peer_ids:
    :return:
    """

    url = "/leave_lf"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunHubLeaveLf]',
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
def hub_p2p_enable(protocol, host, port, peer_ids=""):
    """
    向stun-hub发送开启指定节点p2p功能的请求
    :param protocol:
    :param host:
    :param port:
    :param peer_ids:
    :return:
    """

    url = "/p2p_enable"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunHubP2pEnable]',
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
def hub_p2p_disable(protocol, host, port, peer_ids=""):
    """
    向stun-hub发送禁用指定节点p2p功能的请求
    :param protocol:
    :param host:
    :param port:
    :param peer_ids:
    :return:
    """

    url = "/p2p_disable"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunHubP2pDisable]',
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
def hub_lf_rrpc(protocol, host, port):
    """
    stun向stun-hub发送获取雷锋的rrpc请求
    :param protocol:
    :param host:
    :param port:
    :return:
    """

    url = "/lf_rrpc"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[StunHubLfRrpc]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        {}
    )
    return response

