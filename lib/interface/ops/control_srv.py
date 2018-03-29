# coding=utf-8
"""
运维控制台control服务器后端接口
__author__ = 'th'

"""
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def ops_user_login(protocol, control_srv_host, control_srv_port, username, password):
    """
    用户登录
    :param protocol:
    :param control_srv_host:
    :param control_srv_port:
    :param username
    :param password
    :return:
    """

    url = "/api/login"

    body_data = {
        "username": username,
        "password": password
    }

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[OpsUserLogin]',
        protocol,
        POST,
        control_srv_host,
        control_srv_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def get_api_hosts_list(protocol, control_srv_host, control_srv_port, session_cookie):
    """
    获取已初始化的主机信息列表
    :param protocol:
    :param control_srv_host:
    :param control_srv_port:
    :return:
    """

    url = "/api/hosts/list"
    headers = HeaderData().Cookie(session_cookie).Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetApiHostsList]',
        protocol,
        GET,
        control_srv_host,
        control_srv_port,
        url,
        headers,
        None,
        None
    )
    return response


def get_api_hosts_removed(protocol, control_srv_host, control_srv_port):
    """
    获取已下架未删除或已删除的主机信息列表
    :param protocol:
    :param control_srv_host:
    :param control_srv_port:
    :return:
    """

    url = "/api/hosts/removed"
    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[GetApiHostsList]',
        protocol,
        GET,
        control_srv_host,
        control_srv_port,
        url,
        headers,
        None,
        None
    )
    return response



