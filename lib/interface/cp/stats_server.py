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
def business_report_v2_downloads(url, vvid, report_type, firstplaytime, bufferingcount,
                                 timestamp, duration, app_bytes, cdn_bytes, p2p_bytes, *del_num):
    """
    SDK3.7版本以上的商务汇报-下载汇报段
    :param url:
    :param vvid: 一次点播/直播业务的唯一标枳号
    :param report_type: 商务业务类型："download","vod", "live"
    :param firstplaytime: 可选，启播时间，seconds
    :param bufferingcount: 可选，卡顿次数
    :param timestamp: 该部分流量统计时刻 (UNIX)，单位毫秒
    :param duration: 该部分流量数据收集持续时间，单位秒
    :param app_bytes: 发送给本地播放器的字节数
    :param cdn_bytes: 从CDN下载的字节数
    :param p2p_bytes: 从P2P下载的字节数
    :param del_num: 删除字段对应的序号(L), 注意序号从0开始; 可变参数自动生成Tuple
    :return:
    """
    L = ["timestamp", "duration", "app", "cdn", "p2p", "flow",
         "url", "vvid", "type", "firstplaytime", "bufferingcount", "flows", "download", "downloads"]
    #       6       7       8       9                   10             11       12          13
    flow = {"timestamp": timestamp,
            "duration": duration,
            "app": app_bytes,
            "cdn": cdn_bytes,
            "p2p": p2p_bytes}
    for x in del_num:
        if x in (0,1,2,3,4):
            del flow[L[x]]
    if 5 in del_num:
        flows = []
    else:
        flows = [flow]
    download = {"url": url,
                "vvid": vvid,
                "type": report_type,
                "firstplaytime": firstplaytime,
                "bufferingcount": bufferingcount,
                "flows": flows}
    for x in del_num:
        if x in (6,7,8,9,10,11):
            del download[L[x]]
    if 12 in del_num:
        downloads = []
    elif 13 in del_num:
        downloads = None
    else:
        downloads = [download]
    return downloads


@print_trace
def business_report_v2_uploads(timestamp, duration, bytes, *del_num):
    """
    SDK3.7版本以上的商务汇报-上传汇报段
    :param timestamp: 该部分流量统计时刻 (UNIX)，单位毫秒
    :param duration: 该部分流量数据收集持续时间，单位秒
    :param bytes: 下载或上传字节数
    :param del_num: 删除字段对应的序号(L), 注意序号从0开始; 可变参数自动生成Tuple
    :return:
    """
    L = ["timestamp", "duration", "bytes", "flow", "flows", "uploads"] # 注意参数为0 1 2时与参数为3时的区别
    #       0              1        2       3       4           5
    flow = {"timestamp": timestamp,
            "duration": duration,
            "bytes": bytes}
    for x in del_num:
        if x in (0,1,2):
            del flow[L[x]]
    if 3 in del_num:
        flows = []
    else:
        flows = [flow]
    if 4 in del_num:
        uploads = {}
    elif 5 in del_num:
        uploads = None
    else:
        uploads = {"flows": flows}
    return uploads


@print_trace
def business_report_v2_distributes(url, report_type, timestamp, duration, bytes, *del_num):
    """
    SDK3.7版本以上的商务汇报-PushServer向SDK推送数据流量汇报段
    :param url:
    :param report_type:商务业务类型："download","vod", "live"
    :param timestamp: 该部分流量统计时刻 (UNIX)，单位毫秒
    :param duration: 该部分流量数据收集持续时间，单位秒
    :param bytes: 下载或上传字节数
    :param del_num: 删除字段对应的序号(L), 注意序号从0开始; 可变参数自动生成Tuple
    :return:
    """
    L = ["timestamp", "duration", "bytes", "flow", "url", "type", "flows", "distribute", "distributes"]
    #       0               1       2       3       4       5       6           7           8
    flow = {"timestamp": timestamp,
            "duration": duration,
            "bytes": bytes}
    for x in del_num:
        if x in (0,1,2):
            del flow[L[x]]
    if 3 in del_num:
        flows = []
    else:
        flows = [flow]
    distribute = {"url": url,
                  "type": report_type,
                  "flows": flows}
    for x in del_num:
        if x in (4,5,6):
            del distribute[L[x]]
    if 7 in del_num:
        distributes = []
    elif 8 in del_num:
        distributes = None
    else:
        distributes = [distribute]
    return distributes


@print_trace
def business_report_v2(protocol, host, port, report_id, peer_id, duration, downloads, uploads, distributes, *del_num):
    """
    商务汇报，使用SDK版本[3.7, latest]
    :param protocol:
    :param host:
    :param port:
    :param report_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param duration: 该部分流量数据收集持续时间，可选，单位秒
    :param downloads: 下载汇报段, 见business_report_v2_downloads()
    :param uploads: 上传汇报段, 见business_report_v2_uploads()
    :param distributes: PushServer向SDK推送数据流量汇报段, 见business_report_v2_distributes()
    :param del_num: 删除字段对应的序号(L), 注意序号从0开始; 可变参数自动生成Tuple
    :return:
    """

    url = "/sdk/business_report/v2"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    L = ["id", "peer_id", "duration", "downloads", "uploads", "distributes"]
    body_data = {
        "id": report_id,
        "peer_id": peer_id,
        "duration": duration,
        "downloads": downloads,
        "uploads": uploads,
        "distributes": distributes
    }
    for x in del_num:
        if x in (0,1,2,3,4,5):
            del body_data[L[x]]

    response = send_request(
        '[PeerBusinessReportV2]',
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
def peer_business_report_v2(protocol, host, port, msg_id, peer_id, duration, download_url, download_vvid,
                            download_type, download_firstplaytime, download_bufferingcount, download_timestamp,
                            download_duration, download_app, download_cdn, download_p2p, upload_timestamp,
                            upload_duration, upload_bytes, distributes_url, distributes_type, distributes_timestamp,
                            distributes_duration, distributes_bytes):
    """
    商务汇报，使用SDK版本[3.7, latest]
    :param protocol:
    :param host:
    :param port:
    :param msg_id: 字符串类型,消息的唯一标识，用以实现重复上报的幂等性，便于数据平台的数据清洗
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param duration: 该部分流量数据收集持续时间，可选，单位秒
    :param download_url:
    :param download_vvid: 一次点播/直播业务的唯一标枳号
    :param download_type: 播放类型,包括"download","live","vod"
    :param download_firstplaytime: 可选，启播时间，seconds
    :param download_bufferingcount: 可选，卡顿次数
    :param download_timestamp: 该部分流量统计时刻 (UNIX)，单位毫秒
    :param download_duration:
    :param download_app: 发送给本地播放器的字节数
    :param download_cdn: 从CDN下载的字节数
    :param download_p2p: 从P2P下载的字节数
    :param upload_timestamp:
    :param upload_duration:
    :param upload_bytes:
    :param distributes_url:
    :param distributes_type: "live","vod"
    :param distributes_timestamp:
    :param distributes_duration:
    :param distributes_bytes:
    :return:
    """

    url = "/sdk/business_report/v2"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    download_flows = [
        {
            "timestamp": download_timestamp,
            "duration": download_duration,
            "app": download_app,
            "cdn": download_cdn,
            "p2p": download_p2p
        }
    ]

    downloads = [
        {
            "url": download_url,
            "vvid": download_vvid,
            "type": download_type,
            "firstplaytime": download_firstplaytime,
            "bufferingcount": download_bufferingcount,
            "flows": download_flows
        }
    ]

    upload_flows = [
        {
            "timestamp": upload_timestamp,
            "duration": upload_duration,
            "bytes": upload_bytes
        }
    ]

    uploads = {
        "flows": upload_flows
    }

    distributes_flows = [
        {
            "timestamp": distributes_timestamp,
            "duration": distributes_duration,
            "bytes": distributes_bytes
        }
    ]

    distributes = [
        {
            "url": distributes_url,
            "type": distributes_type,
            "flows": distributes_flows
        }
    ]

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "duration": duration,
        "downloads": downloads,
        "uploads": uploads,
        "distributes": distributes

    }

    response = send_request(
        '[PeerBusinessReportV2]',
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
def peer_business_report(protocol, msg_id, host, port, peer_id, download_url, download_vvid, download_type,
                         download_timestamp, download_duration, download_bytes, upload_timestamp, upload_duration,
                         upload_bytes):
    """
    :param protocol: 协议
    :param msg_id:字符串类型 消息的唯一标识 用以实现重复上报的幂等性 便于数据平台的数据清洗
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param download_url:下载汇报段的url
    :param download_vvid: 一次点播/直播业务的唯一标枳号
    :param download_type: 播放类型,包括"download","live","vod",
    :param download_timestamp:下载汇报段flow的时间戳
    :param download_duration:下载汇报段flow的duration
    :param download_bytes:下载汇报段flow的下载字节
    :param upload_timestamp:上传汇报段flow的时间戳
    :param upload_duration: 上传汇报段flow的duration
    :param upload_bytes:上传汇报段flow的上传字节
    :return:
    """

    url = "/sdk/business_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    download_flows = [
        {
            "timestamp": download_timestamp,
            "duration": download_duration,
            "bytes": download_bytes
        }
    ]

    downloads = [
        {
            "url": download_url,
            "vvid": download_vvid,
            "type": download_type,
            "flows": download_flows
        }
    ]

    upload_flows = [
        {
            "timestamp": upload_timestamp,
            "duration": upload_duration,
            "bytes": upload_bytes
        }
    ]

    uploads = {
        "flows": upload_flows
    }

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "downloads": downloads,
        "uploads": uploads

    }

    response = send_request(
        '[PeerBusinessReportV1]',
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
def peer_business_report_upload(protocol, msg_id, host, port, peer_id, upload_timestamp, upload_duration,
                                upload_bytes):
    """
    :param protocol: 协议
    :param msg_id:字符串类型 消息的唯一标识 用以实现重复上报的幂等性 便于数据平台的数据清洗
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param upload_timestamp:上传汇报段flow的时间戳
    :param upload_duration: 上传汇报段flow的duration
    :param upload_bytes:上传汇报段flow的上传字节
    :return:
    """

    url = "/sdk/business_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    downloads = []

    upload_flows = [
        {
            "timestamp": upload_timestamp,
            "duration": upload_duration,
            "bytes": upload_bytes
        }
    ]

    uploads = {
        "flows": upload_flows
    }

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "downloads": downloads,
        "uploads": uploads

    }

    response = send_request(
        '[PeerBusinessReportV1]',
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
def peer_business_report_download(protocol, msg_id, host, port, peer_id, download_url, download_vvid,
                                  download_type, download_timestamp, download_duration, download_bytes):
    """
    :param protocol: 协议
    :param msg_id:字符串类型 消息的唯一标识 用以实现重复上报的幂等性 便于数据平台的数据清洗
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param download_url:下载汇报段的url
    :param download_vvid: 一次点播/直播业务的唯一标枳号
    :param download_type: 播放类型,包括"download","live","vod",
    :param download_timestamp:下载汇报段flow的时间戳
    :param download_duration:下载汇报段flow的duration
    :param download_bytes:下载汇报段flow的下载字节
    :return:
    """

    url = "/sdk/business_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    download_flows = [
        {
            "timestamp": download_timestamp,
            "duration": download_duration,
            "bytes": download_bytes
        }
    ]

    downloads = [
        {
            "url": download_url,
            "vvid": download_vvid,
            "type": download_type,
            "flows": download_flows
        }
    ]

    upload_flows = []

    uploads = {
        "flows": upload_flows
    }

    body_data = {
        "id": msg_id,
        "peer_id": peer_id,
        "downloads": downloads,
        "uploads": uploads

    }

    response = send_request(
        '[PeerBusinessReportV1]',
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
def peer_statistic_report(protocol, host, port, msg_id=None, report_timestamp=None, peer_id=None, duration=None,
                          connections=None, accept_streams=None, denied_streams=None):
    """
    客户端P2P Connection汇报（该接口还未实现）
    :param protocol:
    :param host:
    :param port:
    :param msg_id:
    :param report_timestamp:
    :param peer_id:
    :param duration:
    :param connections:
    :param accept_streams:
    :param denied_streams:
    :return:
    """

    url = "/sdk/statistic_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "id": msg_id,
        "timestamp": report_timestamp,
        "peer_id": peer_id,
        "duration": duration,
        "connections": connections,
        "accept_streams": accept_streams,
        "denied_streams": denied_streams
    }

    response = send_request(
        '[SdkStatisticReport]',
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


if __name__ == "__main__":
    PID = "6666666666ABCDEABCDEABCDE1000000"

