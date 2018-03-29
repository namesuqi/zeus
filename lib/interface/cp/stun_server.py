# coding=utf-8
"""
stun related api test keyword

__author__ = 'zengyuetian'

"""
import sys
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def join_leifeng(protocol, host, port, file_id="", file_url="", peer_ids=""):

    url = "/rrpc/join_leifeng"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunJoinLeifeng]',
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
def leave_leifeng(protocol, host, port, file_id="", peer_ids=""):

    url = "/rrpc/leave_leifeng"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunLeaveLeifeng]',
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
def rrpc_rsm_report(protocol, host, port, peer_id):

    url = "/rrpc/rsm_report"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "peer_id": peer_id
    }

    response = send_request(
        '[StunRrpcRsmReport]',
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
def rrpc_p2p_disable(protocol, host, port, peer_ids):

    url = "/rrpc/p2p_disable"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunRrpcP2pDisable]',
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
def rrpc_p2p_enable(protocol, host, port, peer_ids):

    url = "/rrpc/p2p_enable"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "peer_ids": peer_ids
    }

    response = send_request(
        '[StunRrpcP2pDisable]',
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
def connect_rrpc_join(protocol, host, port, file_id="", file_url="", peer_ids=""):
    """
    验证stun的8000端口关闭, 连接请求被拒绝(超时时间为20s)
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param file_url:
    :param peer_ids:
    :return:
    """

    url = "/rrpc/join_leifeng"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": peer_ids
    }

    try:
        response = send_request(
            '[StunJoinLeifeng]',
            protocol,
            POST,
            host,
            port,
            url,
            headers,
            None,
            body_data,
            20
        )
        return response
    except Exception:
        errortype, value, traceback=sys.exc_info() # 记录错误并分段赋值
        if "Errno 10060" or "Errno 110" in str(value): # 确认连接失败原因是连接超时,10060-Windows/110-Linux
            return "CONNECT_FAIL"
        else:
            return value


@print_trace
def connect_rrpc_leave(protocol, host, port, file_id="", peer_ids=""):
    """
    验证stun的8000端口关闭, 连接请求被拒绝(超时时间为20s)
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param peer_ids:
    :return:
    """

    url = "/rrpc/leave_leifeng"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if type(peer_ids) != list:
        peer_ids = [peer_ids]

    body_data = {
        "file_id": file_id,
        "peer_ids": peer_ids
    }

    try:
        response = send_request(
            '[StunJoinLeifeng]',
            protocol,
            POST,
            host,
            port,
            url,
            headers,
            None,
            body_data,
            20
        )
        return response
    except Exception:
        errortype, value, traceback=sys.exc_info()
        if "Errno 110" or "Errno 10060" in str(value):
            return "CONNECT_FAIL"
        else:
            return value


@print_trace
def stun_inner_query_peer(protocol, host, port, peer_id=""):
    """
    查询内部节点信息
    :param protocol:
    :param host:
    :param port:
    :param peer_id:
    :return:
    """
    url = "/inner_query/peer/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[StunInnerQueryPeer]',
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
def stun_inner_query_count(protocol, host, port):
    url = "/inner_query/count"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[StunInnerQueryCount]',
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


