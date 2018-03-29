# coding=utf-8
"""
stats相关服务器访问接口

__author__ = 'dh'


"""


from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def report_dns_error(protocol, msg_id, host, port, peer_id, timestamp, error_type, domain):
    """
    DNS_FAILED or HTTPDNS_FAILED
    :param protocol:
    :param msg_id:字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param domain:
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "domian": domain
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_lsm_damaged(protocol, msg_id, host, port, peer_id, timestamp, error_type, file_id):
    """
    lsm damaged error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param file_id:
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "file_id": file_id
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_file_damaged(protocol, msg_id, host, port, peer_id, timestamp, error_type, file_id, chunk_id):
    """
    file damaged error
    :param protocol: 协议
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param file_id:
    :param chunk_id:
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "file_id": file_id,
            "chunk_id": chunk_id
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_piece_duplicated(protocol, msg_id, host, port, peer_id, timestamp, error_type, file_id, chunk_id,
                            piece_index):
    """
    piece duplicated error
    :param protocol: 协议
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param file_id:
    :param chunk_id:
    :param piece_index:
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "file_id": file_id,
            "chunk_id": chunk_id,
            "piece_index": piece_index
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_http_request_error(protocol, msg_id, host, port, peer_id, timestamp, error_type, error_url,
                              status_code, server_ip, error_message):
    """
    http request error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param error_url: HTTP失败的URL
    :param status_code: HTTP返回的status code
    :param server_ip: 服务器IP地址
    :param error_message: 失败的原因
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "url": error_url,
            "status_code": status_code,
            "ip": server_ip,
            "error_message": error_message
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_push_server_error(protocol, msg_id, host, port, peer_id, timestamp, error_type, error_url,
                             error_message):
    """
    http request error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param error_url: HTTP失败的URL
    :param error_message: 失败的原因
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "url": error_url,
            "error_message": error_message
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_stun_unconnected_error(protocol, msg_id, host, port, peer_id, timestamp, error_type, error_url,
                                  stun_ip):
    """
    http request error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param error_url: HTTP失败的URL
    :param stun_ip: 失败的原因
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "url": error_url,
            "ip": stun_ip
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_send_to_udp_failed(protocol, msg_id, host, port, peer_id, timestamp, error_type):
    """
    http request error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
def report_rrpc_failed(protocol, msg_id, host, port, peer_id, timestamp, error_type, rrpc_id, error_message):
    """
    http request error
    :param protocol:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param timestamp: 错误产生的时间
    :param error_type: 错误类型
    :param rrpc_id: rrpc名称
    :param error_message: 错误原因
    :return:
    """

    url = "/sdk/error_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    errors = [
        {
            "timestamp": timestamp,
            "type": error_type,
            "rrpc_id": rrpc_id,
            "error_message": error_message
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "errors": errors
    }

    response = send_request(
        '[PeerErrorReport]',
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
