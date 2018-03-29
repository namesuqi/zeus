# coding=utf-8

"""
panel相关服务器访问接口

__author__ = zjy

"""
from lib.constant.request import *
from lib.request.cookie_handle import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def bandwidth_get_p2p(protocol, monitor_host, monitor_port, start, end, step, play_type='live', tenant='all'):
    url = "/monitor/api/bandwidth/download"

    param_box = ("start=" + str(start), "end=" + str(end), "step="+str(step), "playType="+str(play_type), "tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[BandwidthgetP2p]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def bandwidth_get_download(protocol, monitor_host, monitor_port, start, end, step, play_type='all', tenant='all'):
    url = "/monitor/api/bandwidth/download/timeline"

    param_box = ("start=" + str(start), "end=" + str(end), "step="+str(step), "playType="+str(play_type), "tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[BandwidthgetDownload]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def bandwidth_get_upload(protocol, monitor_host, monitor_port, start, end, step, tenant='all'):
    url = "/monitor/api/bandwidth/upload/timeline"

    param_box = ("start=" + str(start), "end=" + str(end), "step="+str(step), "tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    response = send_request(
        '[BandwidthgetUpload]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def channel_get_summary(protocol, monitor_host, monitor_port, fileId):
    url = "/monitor/api/channel/summary?fileId="+str(fileId)
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ChannelgetSummary]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def channel_get_peer(protocol, monitor_host, monitor_port, fileId, start, end):
    url = "/monitor/api/channel/peer"

    param_box = ("fileId=" + str(fileId), "start=" + str(start), "end=" + str(end))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ChannelgetPeer]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def channel_get_lfratio(protocol, monitor_host, monitor_port, fileId, start, end):
    url = "/monitor/api/channel/lfRatio"

    param_box = ("fileId=" + str(fileId), "start=" + str(start), "end=" + str(end))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ChannelgetLfRatio]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def channel_get_fileid(protocol, monitor_host, monitor_port):
    url = "/monitor/api/channel/fileId"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[ChannelgetFileId]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def peer_get_summary(protocol, monitor_host, monitor_port, tenant='all'):
    url = "/monitor/api/peer/summary?tenant="+str(tenant)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[PeerGetSummary]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def peer_get_active(protocol, monitor_host, monitor_port, start, end, step, tenant='all'):
    url = "/monitor/api/peer/active/timeline"
    param_box = ("start=" + str(start), "end=" + str(end), "step="+str(step),"tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[PeerGetActive]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def peer_get_online(protocol, monitor_host, monitor_port, start, end, step, tenant='all'):
    url = "/monitor/api/peer/online/timeline"
    param_box = ("start=" + str(start), "end=" + str(end), "step="+str(step),"tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[PeerGetOnline]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def summary(protocol, monitor_host, monitor_port):
    url = "/monitor/api/summary"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[summary]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def flow_get_download_summary(protocol, monitor_host, monitor_port, play_type='all', tenant='all'):
    url = "/monitor/api/flow/download/summary"
    param_box = ("playType=" + str(play_type),"tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[FlowGetSummary]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def flow_get_download(protocol, monitor_host, monitor_port, start, end, step, play_type='all', tenant='all'):
    url = "/monitor/api/flow/download/timeline"
    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "playType=" + str(play_type),"tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[FlowGetDownload]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def flow_get_upload(protocol, monitor_host, monitor_port, start, end, step, tenant='all'):
    url = "/monitor/api/flow/upload/timeline"
    param_box = ("start=" + str(start), "end=" + str(end), "step=" + str(step), "tenant="+str(tenant))

    param_url = ""

    for param in param_box:
        if param[-1] != "=":
            param_url = param_url + "&" + param

    if param_url.find("&") != -1:
        url += param_url.replace("&", "?", 1)
    else:
        pass
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[FlowGetUpload]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def flow_get_upload_summary(protocol, monitor_host, monitor_port, tenant='all'):
    url = "/monitor/api/flow/upload/summary?tenant=" + str(tenant)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[FlowGetSummary]',
        protocol,
        GET,
        monitor_host,
        monitor_port,
        url,
        headers,
        None,
        None
    )
    return response

if __name__== '__main__':
    # bandwidth_get_p2p(HTTP,  'monitor.shangcdn.com.', '8080',  1474905600000, 1474946545621, 2, 'live', 'all')
    # bandwidth_get_download(HTTP,  'monitor.shangcdn.com.', '8080',  1474905600000, 1474946545621, 2, 'all', 'all')
    # bandwidth_get_upload(HTTP,  'monitor.shangcdn.com.', '8080', 1474905600000, 1474946545621, 2, 'all')
    # channel_get_summary(HTTP,  'monitor.shangcdn.com.', '8080', 'D460BE98C5B062E0C458438117C6416E')
    # channel_get_peer(HTTP,  'monitor.shangcdn.com.', '8080',  'D460BE98C5B062E0C458438117C6416E', 1474905600000, 1474946545621)
    # channel_get_lfratio(HTTP,  'monitor.shangcdn.com.', '8080',  'D460BE98C5B062E0C458438117C6416E', 1474905600000, 1474946545621)
    # channel_get_fileid(HTTP,  'monitor.shangcdn.com.', '8080')
    # peer_get_summary(HTTP,'monitor.shangcdn.com.', '8080', 'all')
    # peer_get_active(HTTP,'monitor.shangcdn.com.', '8080', 1474905600000, 1474946545621, 2, 'all')
    # peer_get_online(HTTP, 'monitor.shangcdn.com.', '8080', 1474905600000, 1474946545621, 2, 'all')
    # summary(HTTP,'monitor.shangcdn.com.', '8080')
    # flow_get_download_summary(HTTP, 'monitor.shangcdn.com.','8080', 'all', 'all')
    # flow_get_download(HTTP, 'monitor.shangcdn.com.', '8080', 1474905600000, 1474946545621, 2, 'all', 'all')
    # flow_get_upload(HTTP, 'monitor.shangcdn.com.','8080', 1474905600000, 1474946545621, 2, 'all')
    flow_get_upload_summary(HTTP,'monitor.shangcdn.com.','8080', 'all')
