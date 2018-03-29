# coding=utf-8
"""
channel server related api 

"""

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *
from lib.request.authentication import *


@print_trace
def channel_start_live_flv(protocol, host, port, user, pid, url):
    """
    sdk start playing live channel with source "flv", request information
    :param protocol: http or https
    :param host:
    :param port: channel server port
    :param user: username
    :param pid: peer id
    :param url: rtmp url
    :return:
    """

    url = "/startliveflv?user=" + str(user) + "&pid=" + str(pid) + "&url=" + str(url)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[channel_start_live_flv]',
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
def channel_start_channel(protocol, host, port, user, pid, url):
    """
    文件播放/下载
    :param protocol:
    :param host:
    :param port:
    :param user:用户名
    :param pid:设备唯一标识符, 128位UUID, 使用HEX编码
    :param url:请求文件的URL，使用URL encoding. String
    :return:
    """

    url = "/startchannel?user=" + str(user) + "&pid=" + str(pid) + "&url=" + str(url)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[channel_start_channel]',
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
def channel_start_hls(protocol, host, port, user, pid, _url):
    """
    sdk start playing live channel with source "hls", request information
    :param protocol:
    :param host:
    :param port:
    :param user:用户名
    :param pid:设备唯一标识符, 128位UUID, 使用HEX编码
    :param _url:请求文件的URL，使用URL encoding. String
    :return:
    """

    url = "/starthls?user=" + str(user) + "&pid=" + str(pid) + "&url=" + str(_url)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[channel_start_hls]',
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
def channel_create(protocol, host, port, ch_name, ch_source_pro, ch_source, ch_source_port,
                stream_name, tenant_name, stream_rate=500, ch_capability=None, ch_factor=0.5, flash_slice=12,
                flash_delay=30, flash_interval=10):
    '''
    create live channel
    :param protocol:
    :param host: channel server host
    :param port: channel server port
    :param ch_name: channel_name
    :param ch_source_pro: channel_source_protocol
    :param ch_source: channel_source
    :param ch_source_port: channel_source_port
    :param stream_name: steam_name
    :param tenant_name: username of the company
    :param stream_rate: stream_rate
    :param ch_capability: channel_capability
    :param ch_factor: channel_factor
    :param flash_slice: flash_slice
    :param flash_delay: flash_delay
    :param flash_interval: flash_interval
    :return:
    '''

    url = "/live/channel"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    body_data = {
        "channel_name": ch_name,
        "channel_source_protocol": ch_source_pro,
        "channel_source": ch_source,
        "channel_source_port": ch_source_port,
        "stream_name": stream_name,
        "tenant_name": tenant_name,
        "stream_rate": int(stream_rate),
        "channel_capability": str(ch_capability),
        "channel_factor": float(ch_factor),
        "flash_slice": int(flash_slice),
        "flash_delay": int(flash_delay),
        "flash_interval": int(flash_interval)
    }

    response = send_request(
        '[channel_create]',
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
def channel_update(protocol, host, port, ch_id, body):
    '''
    update channel info by channel_id
    :param protocol:
    :param host:
    :param port:
    :param ch_id: channel_id
    :return:
    '''

    url = "/live/channel/" + str(ch_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    body_data = body

    response = send_request(
        '[channel_update]',
        protocol,
        'PUT',
        host,
        port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def channel_get_info(protocol, host, port, ch_id, tenant_name):
    '''
    get channel's info by channel_id
    :param protocol:
    :param host:
    :param port:
    :param ch_id: channel_id
    :param tenant_name:
    :return:
    '''

    url = "/live/channel/" + str(ch_id) + "?tenant_name=" + str(tenant_name)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_get_info]',
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
def channel_delete(protocol, host, port, ch_id, tenant_name):
    '''
    delete channel by channel_id
    :param protocol:
    :param host:
    :param port:
    :param ch_id: channel_id
    :param tenant_name:
    :return:
    '''

    url = "/live/channel/" + str(ch_id) + "?tenant_name=" + str(tenant_name)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_delete]',
        protocol,
        DELETE,
        host,
        port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def channel_start(protocol, host, port, ch_id, tenant_name):
    '''
    start channel by channel_id
    :param protocol:
    :param host: channel server host
    :param port: channel server port
    :param ch_id: channel_id
    :param tenant_name:
    :return:
    '''

    url = "/live/channel/" + str(ch_id) + "/start?tenant_name=" + str(tenant_name)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_start]',
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
def channel_stop(protocol, host, port, ch_id, tenant_name):
    '''
    stop channel by channel_id
    :param protocol: http or https
    :param host: channel server host
    :param port: channel server port
    :param ch_id: channel_id
    :param tenant_name:
    :return:
    '''

    url = "/live/channel/" + str(ch_id) + "/stop?tenant_name=" + str(tenant_name)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_stop]',
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
def channel_get_list(protocol, host, port, tenant_name):
    '''
    get user's channel_list by tenant_name
    :param protocol:
    :param host:
    :param port:
    :param tenant_name:
    :return:
    '''

    url = "/live/channel?tenant_name=" + str(tenant_name)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_get_list]',
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
def channel_start_ts(protocol, host, port, user, pid, url):
    '''
    sdk start playing live channel with source "ts", request information
    :param protocol: http or https
    :param host:
    :param port: channel server port
    :param user: username
    :param pid: peer id
    :param url: rtmp url
    :return:
    '''

    url = "/startlivets?user=" + str(user) + "&pid=" + str(pid) + "&url=" + str(url)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_start_ts]',
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
def channel_start_m3u8(protocol, host, port, user, pid, url):
    '''
    sdk start playing live channel with source "m3u8", request information
    :param protocol: http or https
    :param host:
    :param port: channel server port
    :param user: username
    :param pid: peer id
    :param url: rtmp url
    :return:
    '''

    url = "/startlivem3u8?user=" + str(user) + "&pid=" + str(pid) + "&url=" + str(url)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_start_m3u8]',
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
def channel_ts_offset(protocol, host, port, file_id):
    """
    SDK get lastest_offset of ts
    :param hottporhttps:
    :param host:
    :param port:
    :param file_id:数据文件的file_id
    :return:
    """

    url = "/live/files/" + str(file_id) + "/latest_offset"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_ts_offset]',
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
def channel_m3u8_seg(protocol, host, port, file_id, user, pid, seq):
    """
    SDK get latest_seq of m3u8
    :param protocol:
    :param host:
    :param port:
    :param file_id:数据文件的file_id
    :param user:username
    :param pid:节点peer_id
    :param seq:sdk已经知晓的sequence
    :return:
    """
    url = "/live/files/" + str(file_id) + "segments?user=" + str(user) + "&pid=" + str(pid) + "&seq=" + str(seq)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[channel_m3u8_seg]',
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
def live_tag_lastest_tag(protocol, livetag_host, livetag_port, file_id, seq_header):
    """
    SDK get latest_tagpos of live_flv
    :param protocol:
    :param livetag_host:
    :param livetag_port:
    :param file_id:数据文件的file_id
    :param seq_header:是否需要seq_header信息, yes or no
    :return:
    """

    url = "/live/files/" + str(file_id) + "latest_tagpos?seq_header=" + str(seq_header)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    response = send_request(
        '[live_tag_lastest_tag]',
        protocol,
        GET,
        livetag_host,
        livetag_port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def channel_sdk_cache(protocol, host, port, pid, file_id, cppc, operation):
    """
    SDK cache report
    :param protocol:
    :param host:
    :param port:
    :param pid:汇报节点的pid
    :param file_id:数据文件的file_id
    :param cppc:每个chunk缓存的片数
    :param operation:对每个文件的操作，可以add | del
    :return:
    """
    url = "/cache_report?pid/" + str(pid)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    files = [{
        "file_id": file_id,
        "cppc": cppc,
        "op": operation
    }]

    body_data = {
        "files": files
    }

    response = send_request(
        '[channel_sdk_cache]',
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
def channel_create_live(protocol, host, port, action, client_id, ip, vhost, app, stream,
                      output_url, format):
    """
    记录用户频道信息
    :param protocol:
    :param host:
    :param port:
    :param action:
    :param client_id:int
    :param ip:
    :param vhost:
    :param app:
    :param stream:
    :param output_url:云熵服务器根据用户直播源视频流转换后的p2p url(频道启动后有值)
    :param format:视频输出格式(flv, ts or hls)
    :return:
    """
    url = "/live/channel/create"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    body_data = {
        "action": action,
        "client_id": int(client_id),
        "ip": ip,
        "vhost": vhost,
        "app": app,
        "stream": stream,
        "output_url": output_url,
        "format": format
    }

    response = send_request(
        '[channel_create_live]',
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
def channel_delete_live(protocol, host, port, action, client_id, ip, vhost, app, stream,
                      output_url):
    """
    记录用户频道信息
    :param protocol:
    :param host:
    :param port:
    :param action:
    :param client_id:int
    :param ip:
    :param vhost:
    :param app:
    :param stream:
    :param output_url:云熵服务器根据用户直播源视频流转换后的p2p url(频道启动后有值)
    :return:
    """
    url = "/live/channel/delete"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

    body_data = {
        "action": action,
        "client_id": int(client_id),
        "ip": ip,
        "vhost": vhost,
        "app": app,
        "stream": stream,
        "output_url": output_url
    }

    response = send_request(
        '[channel_delete_live]',
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
def channel_sdk_get_p2p(protocol, host, port, pid, *del_num):
    """
    SDK直播使用接口，服务扩展时，为用户节点分批添加p2p服务
    :param protocol:
    :param host:
    :param port:
    :param pid:
    :param del_num:
    :return:
    """
    field_list = ["pid"]

    url = "/sdk/peer/p2p"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body = {
        "pid": pid
    }
    for i in del_num:
        if i in range(len(field_list)):
            del body[field_list[i]]

    response = send_request(
        '[channel_sdk_get_p2p]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body
    )

    return response






