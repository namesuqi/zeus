# coding=utf-8
"""
account related api interface

__author__ = 'zengyuetian'

"""
from lib.constant.request import *
from lib.request.authentication import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def account_login(protocol, host, port, username=None, password=None):
    """
    panel用户登录接口
    :param protocol:协议
    :param host: 账号服务器
    :param port: 账号服务器端口
    :param username: 用户名
    :param password: 密码
    :return: 响应
    """

    # easy reading format
    url = "/panel/api/auth/login"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "username": username,
        "password": password
    }
    response = send_request(
        '[AccountLogin]',
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
def account_logout(protocol, host, port, session_cookie=None):
    """
    panel用户注销登录
    :param protocol: 协议
    :param host: 账号服务器
    :param port: 端口
    :param session_cookie: 需要注销的用户的登录cookie
    :return: 响应
    """
    url = "/panel/api/auth/logout"

    headers = HeaderData().Cookie(session_cookie).Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[AccountLogout]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def account_get_user_info(protocol, host, port, session_cookie=None):
    """
    获取指定cookie对应的登录用户的信息
    :param protocol: 协议
    :param host: 服务器
    :param port: 端口
    :param session_cookie: 需要用户的登录cookie
    :return: 响应
    """
    url = "/panel/api/auth/userinfo"

    headers = HeaderData().Cookie(session_cookie).Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[AccountGetUserInfo]', protocol,
        GET,
        host,
        port,
        url,
        headers
    )

    return response


@print_trace
def account_signature(protocol, host, port,username=None, password=None, type=None, delay=0, *datas):
    """
    根据signature和username校验传输
    :param protocol: 协议
    :param host: 服务器
    :param port: 端口
    :param username: 用户名
    :param password: 密码
    :param type: hash计算方法， md5, sha1, hmac...
    :param delay:延迟时间
    :param datas:
    :return:响应
    """
    url = "/auth/signature"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    data_string = ""
    for data in datas:
        data_string = data_string + data + "\n"

    signature, date = get_md5_with_date_offset(data_string + password + "\n", int(delay))
    body_data = {
        "crypto_type": type,
        "segments": datas,
        "date": date,
        "signature": signature
    }
    if (username is not None) and (username != ""):
        body_data["username"] = username

    response = send_request(
        '[account_signature]',
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
def account_add(protocol, host, port, username, password, phone, email, source="", groups=[]):
    """
    添加用户
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param username:用户名
    :param password:密码
    :param phone:电话号码
    :param email:邮件地址
    :param source:源数据类型信息
    :param groups:所属group，列表
    :return:响应
    """
    url = "/add_user"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    data = {
        "username": username,
        "password": password,
        "phoneNum": phone,
        "emailAddress": email,
        "sourceInfo": source,
        "groups": [groups]
    }

    response = send_request(
        '[account_add]', protocol,
         POST,
         host,
         port,
         url,
         headers,
         None,
         data
    )

    return response

@print_trace
def account_add_group(protocol, host, port, group):
    '''
    添加用户组
    :param group:
    :return:
    '''
    url = "/group"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    data = {"group": group}

    response = send_request('[account_add_group]', protocol,
         POST,
         host,
         port,
         url,
         headers,
         None,
         data)
    return response

@print_trace
def AccountGetAllUserInfo (protocol, host, port):
     """
    获取所有用户的信息
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :return:响应
    """

     url = '/admin/customers/'

     headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

     response = send_request('[GetAllUserInfo]', protocol,
                 GET,
                 host,
                 port,
                 url,
                 headers,
                 None,
                 None)
     return response

@print_trace
def account_assign_user_group (protocol, host, port, username, oldgroup, newgroup):
    '''
    给用户分配组
    :param protocol:
    :param host:
    :param port:
    :param username:
    :param oldgroup:
    :param newgroup:
    :return:
    '''
    url = '/user_group'

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    data = {
        "owner": username,
        "groups": [oldgroup, newgroup]
    }

    response= send_request('[account_assign_user_group]', protocol,
                                'PUT',
                                host,
                                port,
                                url,
                                headers,
                                None,
                                data)
    return response

@print_trace
def account_get_user_info_by_uid(protocol, host, port, uid=None):
    '''
    提取用户信息
    :param protocol:
    :param host:
    :param port:
    :param uid:
    :return:
    '''
    url = "/get_user_info?uid=" + str(uid)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_get_user_info_by_uid]',
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
def account_update_user_info(protocol, host, port, uid, old_passwd, new_passwd, phone="", email=""):
    '''
    修改用户部分信息
    :param protocol:
    :param host:
    :param port:
    :param uid:
    :param old_passwd:
    :param new_passwd:
    :param phone:
    :param email:
    :return:
    '''
    url = "/update_user_info"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    body_data = {
        "uid": uid,
        "old_password": old_passwd,
        "new_password": new_passwd,
        "phoneNum": phone,
        "emailAddress": email
    }

    response = send_request(
        '[account_update_user_info]',
        protocol,
        PUT,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )
    return response

@print_trace
def account_get_channel(protocol, host, port, username):
    '''
    获取指定用户的渠道号
    :param protocol:
    :param host:
    :param port:
    :param username:
    :return:
    '''
    url = "/get_channel_id?username=" + username

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_get_channel]',
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
def account_get_all_channel(protocol, host, port):
    '''
    获取所有用户的渠道号
    :param protocol:
    :param host:
    :param port:
    :return:
    '''
    url = "/get_user_channels"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_get_all_channel]',
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
def account_get_groups(protocol, host, port):
    '''
    获取所有组名
    :param protocol:
    :param host:
    :param port:
    :return:
    '''
    url = "/admin/groups"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_get_groups]',
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
def account_query_user_info(protocol, host, port, username):
    '''
    管理员查询每个用户owner的所有信息
    :param protocol:
    :param host:
    :param port:
    :param username:
    :return:
    '''
    url = "/admin/customers/" + username

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_query_user_info]',
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
def account_get_id_by_username(protocol, host, port, username):
    '''
    根据用户名username获取对应的用户id
    :param protocol:
    :param host:
    :param port:
    :param username:
    :return:
    '''
    url = "/user_id?username=" + username

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[account_get_id_by_username]',
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