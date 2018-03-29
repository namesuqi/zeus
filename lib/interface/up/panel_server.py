# coding=utf-8

"""
panel相关服务器访问接口

__author__ = sxl

"""


from lib.constant.request import *
from lib.request.cookie_handle import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def panel_auth_login(protocol, panel_host, panel_port, username=None, password=None):
    """
    login to the panel,if pass save cookie
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param username: 登录用户名
    :param password: 登录密码
    :return:
    """
    url = "/panel/api/auth/login"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    if username is None:
        pass
    else:
        body_data.update({
            'username': username
        })

    if password is None:
        pass
    else:
        body_data.update({
            'password': password
        })

    response = send_request(
        '[PanelAuthLogin]',
        protocol,
        POST,
        panel_host,
        panel_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def panel_auth_logout(protocol, panel_host, panel_port, is_login=False):
    """
    logout to the panel
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param is_login: 是否读取本地cookie
    :return:
    """
    url = "/panel/api/auth/logout"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelAuthLogout]',
        protocol,
        POST,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        body_data
    )
    return response


@print_trace
def panel_auth_password(protocol, panel_host, panel_port, old_password=None, new_password=None, is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param old_password: 旧密码
    :param new_password: 新密码
    :param is_login: 是否读取本地cookie
    :return:
    """
    url = "/panel/api/auth/password"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
    }

    if old_password is None:
        pass
    else:
        body_data.update({
            "oldPassword": old_password
        })

    if new_password is None:
        pass
    else:
        body_data.update({
            "newPassword": new_password
        })

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelAuthPassword]',
        protocol,
        PUT,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        body_data
    )
    return response


@print_trace
def panel_auth_userinfo(protocol, panel_host, panel_port, is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param is_login: 是否读取本地cookie
    :return:
    """
    url = "/panel/api/auth/userinfo"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelAuthUserinfo]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_traffic_download(protocol, panel_host, panel_port, start="", end="", step="", playType="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step: required
    :param playType: live/vod/all optional
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/traffic/download"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(playType))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelTrafficDownload]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_traffic_download_summary(protocol, panel_host, panel_port, is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/traffic/download/summary"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelTrafficDownloadSummary]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_traffic_upload(protocol, panel_host, panel_port, start="", end="", step="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step: required
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/traffic/upload"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelTrafficUpload]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_traffic_upload_summary(protocol, panel_host, panel_port, is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/traffic/upload/summary"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelTrafficUploadSummary]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_bandwidth(protocol, panel_host, panel_port, start="", end="", step="", playType="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step: required
    :param playType: live/vod/all optional
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/bandwidth"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(playType))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBandwidth]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_bandwidth_download(protocol, panel_host, panel_port, start="", end="", step="", playType="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step: required
    :param playType: live/vod/all optional
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/bandwidth/download"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(playType))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBandwidthDownload]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_bandwidth_upload(protocol, panel_host, panel_port, start="", end="", step="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step: required
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/bandwidth/upload"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBandwidthUpload]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_buffering_startup(protocol, panel_host, panel_port, start="", end="", playType="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param playType: optional
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/buffering/startup"

    param_box = ("start=" + str(start), "end=" + str(end), "playType=" + str(playType))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBufferingStartup]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_fluency(protocol, panel_host, panel_port, start="", end="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/fluency"

    param_box = ("start=" + str(start), "end=" + str(end))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBufferingStartup]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_peer_active(protocol, panel_host, panel_port, start="", end="", step="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step:
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/peer/active"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelPeerActive]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_peer_online(protocol, panel_host, panel_port, start="", end="", step="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step:
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/peer/online"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelPeerOnline]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_peer_summary(protocol, panel_host, panel_port, is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step:
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/peer/summary"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelPeerSummary]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_bandwidth(protocol, panel_host, panel_port, start="", end="", step="", play_type="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step:
    :param play_type:
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/bandwidth"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(play_type))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBandwidth]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


@print_trace
def panel_bandwidth_download(protocol, panel_host, panel_port, start="", end="", step="", play_type="", is_login=False):
    """
    :param protocol: 协议
    :param panel_host: 服务器
    :param panel_port: 端口
    :param start: 起始时间 required
    :param end: 结束时间 required
    :param step:
    :param play_type:
    :param is_login: 是否读取本地登录信息 cookie
    :return:
    """
    url = "/panel/api/bandwidth/download"

    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(play_type))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if is_login:
        cookie = load_cookies('panel_login_cookie')
    else:
        cookie = None

    response = send_request(
        '[PanelBandwidth]',
        protocol,
        GET,
        panel_host,
        panel_port,
        url,
        headers,
        cookie,
        None
    )
    return response


if __name__ == '__main__':
    # r = panel_auth_login(HTTP, 'panel.shangcdn.com.', '80', 'wasu', '123456')
    # save_cookies(r, 'panel_login_cookie')
    # panel_auth_logout(HTTP, 'panel.shangcdn.com.', '8080')
    # panel_auth_userinfo(HTTP, 'panel.shangcdn.com.', '8080')
    # panel_auth_password(HTTP, 'panel.shangcdn.com.', '8080', '123456', '654321')
    # panel_traffic_download(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', 'live', False)
    # panel_traffic_download_summary(HTTP, 'panel.shangcdn.com.', '8080', True)
    # panel_traffic_upload(HTTP, 'panel.shangcdn.com.', '80', '', 1474946545621, 'minute', True)
    # panel_traffic_upload_summary(HTTP, 'panel.shangcdn.com.', '8080', True)
    ##### panel_bandwidth(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', 'live', True)
    # panel_bandwidth_download(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', 'live', True)
    # panel_bandwidth_upload(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', True)
    # panel_buffering_startup(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'live', True)
    # panel_fluency(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621,  True)
    # panel_peer_active(HTTP, 'panel.shangcdn.com.', '80', 1474905600000, 1474946545621, 'minute', True)
    # panel_peer_online(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', True)
    # panel_peer_summary(HTTP, 'panel.shangcdn.com.', '8080', True)
    # panel_bandwidth(HTTP, 'panel.shangcdn.com.', '80', 1474905600000, 1474946545621, 'minute', 'live', False)
    # panel_bandwidth_download(HTTP, 'panel.shangcdn.com.', '8080', 1474905600000, 1474946545621, 'minute', 'live', True)
    panel_bandwidth_upload(HTTP, 'panel.shangcdn.com.', '80', '', 1474946545621, 'minute', 'live', True)
