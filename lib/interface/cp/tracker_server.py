# coding=utf-8
"""
ts相关服务器访问接口
ts.cloutropy.com, seeds.cloutropy.com, report.cloutropy.com

__author__ = 'zengwenye'

"""
import time
from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def peer_login(protocol, host, port, peer_id, version, nat_type, public_ip, public_port, private_ip, private_port,
               stun_ip=None, macs=None, device_info=None, del_key=None):
    """
    peer login，sdk -> ts.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param version:客户端SDK版本号，使用数字和小数点表示，例如1.0.2
    :param nat_type:NAT类型标识，0-6的正整数
    :param public_ip:客户端外网IP，使用String表示
    :param public_port:客户端端口号，使用UINT16表示
    :param private_ip:客户端内网地址，使用String表示
    :param private_port:客户端内网地址，使用UINT16表示
    :param stun_ip:sdk连接的stunIP（sdk版本在3.6.0及以上时，ts才会将stunIP写进PNIC）
    :param macs: 可选，设备macs，字符串格式
    :param device_info: 可选 设备信息，字符串格式
    :param del_key: 可选 删除body_data的键值
    :return:
    """
    url = "/session/peers/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    body_data = {
        "version": version,
        "natType": nat_type,
        "publicIP": public_ip,
        "publicPort": public_port,
        "privateIP": private_ip,
        "privatePort": private_port,
    }
    if stun_ip is not None:
        body_data["stunIP"] = stun_ip
    if macs is not None:
        body_data["macs"] = macs
    if device_info is not None:
        body_data["device_info"] = device_info
    if del_key is not None:
        if del_key in body_data.keys():
            del body_data[del_key]

    response = send_request(
        '[TsPeerLogin]',
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
def peer_logout(protocol, host, port, peer_id):
    """
    peer logout，sdk -> ts.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :return:
    """
    url = "/session/peers/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    response = send_request(
        '[TsPeerLogout]',
        protocol,
        DELETE,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def peer_heartbeat(protocol, host, port, peer_id):
    """
    peer heartbeat，sdk -> ts.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :return:
    """
    url = "/session/peers/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    response = send_request(
        '[TsPeerHeartbeat]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def peer_request_push_task(protocol, host, port, peer_id, lsm_free=""):
    """
    peer请求推送任务(老版本)
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param lsm_free:
    :return:

    """
    url = "/distribute/peers/" + str(peer_id) + "?lsmfree=" + str(lsm_free)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[TsPeerDistributeReqPush]',
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
def peer_get_seeds(protocol, host, port, peer_id, file_id, slice_id=""):
    """
    peer获取seed列表, 2.X以上SDK，sdk -> seeds.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param file_id:请求文件的file_id
    :param slice_id:0-63, Optional
    :return:
    """

    if slice_id in (None, ""):
        url = "/getseeds?pid=" + peer_id + "&fid=" + file_id
    else:
        url = "/getseeds?pid=" + peer_id + "&fid=" + file_id + "&sid=" + str(slice_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[TsPeerGetSeeds]',
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
def peer_get_live_seeds(protocol, host, port, peer_id, file_id, chunk_id=""):
    """
    peer获取直播seed列表，sdk -> seeds.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param file_id:请求文件的file_id
    :param chunk_id:Optional,sdk还会带上该字段, 但是服务器不做任何处理
    :return:
    """

    if chunk_id in (None, ""):
        url = "/live/" + file_id + "/seeds?pid=" + peer_id
    else:
        url = "/live/" + file_id + "/seeds?pid=" + peer_id + "&cid=" + str(chunk_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[TsPeerGetLiveSeeds]',
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
def peer_cache_report(protocol, host, port, peer_id, file_id, cppc, op):
    """
    peer cache_report，sdk -> report.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param file_id:128位UUID, 使用HEX编码
    :param cppc:该文件每个chunk被缓存的piece数(pieces per chunk),0表示该文件被删除
    :param op:对每个文件的操作，可以add | update (全量汇报) | del
    :return:
    """
    url = "/cache_report?pid=" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    files = [
        {
            "file_id": file_id,
            "cppc": int(cppc),
            "op": op
        }
    ]

    body_data = {"files": files}

    response = send_request(
        '[TsPeerCacheReport]',
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
def peer_lsm_report(protocol, host, port, peer_id, file_id, ppc, slice_map, lsm_size=None, universe=None):
    """
    peer汇报本地缓存，sdk -> report.cloutropy.com
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param peer_id:设备唯一标识符，128位UUID，使用HEX编码
    :param lsm_size:yunshang.so占用的本地磁盘容量
    :param file_id:128位UUID, 使用HEX编码
    :param ppc:该文件每个chunk被缓存的piece数(pieces per chunk),0表示该文件被删除
    :param slice_map:该文件有哪几个slices被成功缓存. 16字节的HEX编码
    :param universe:本次汇报是否包含LSM全集信息,default is false
    :return:
    """
    url = "/distribute/peers/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    files = [
        {
            "file_id": file_id,
            "ppc": int(ppc),
            "sliceMap": slice_map
        }
    ]

    body_data = {"files": files}

    if lsm_size is not None:
        body_data["lsmsize"] = int(lsm_size)
    if universe is not None:
        body_data["universe"] = universe

    response = send_request(
        '[TsPeerLsmReport]',
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
def peer_live_progress(protocol, host, port, file_id=None, peer_id=None, chunk_id=None, play_type=None, report_time=None):
    """
    sdk的直播进度汇报，由向seeds.cloutropy.com汇报迁移到report.cloutropy.com，适用SDK版本：>=3.0
    sdk -> report.cloutropy.com
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param peer_id:
    :param chunk_id: 直播当前进度(>0)
    :param play_type: 直播类型（live_flv, live_ts, live_m3u8)，该参数在body中为可选参数，目前ts-go不做处理
    :param report_time: 汇报进度的时间，默认body中该值为当前时间戳（该字段缺失时，服务器会以当前时间戳补上）
    :return:
    """
    url = "/live/" + str(file_id) + "/progress"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    nowtime = int(time.time()*1000)
    if report_time == "now_time":
        timestamp = nowtime
    else:
        timestamp = report_time

    body_data = {
        "timestamp": timestamp,
        "peer_id": str(peer_id),
        "chunk_id": chunk_id,
        "type": play_type
    }

    response = send_request(
        '[TsPeerLiveProgress]',
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


# @print_trace
# def TsPeerDistributeReqPush( http_or_https, ts_host, ts_port, peer_id, status, lsmFree = ""):
#     """
#     peer请求推送任务(新版本，暂未使用20160622)
#
#     """
#     if lsmFree in (None, ""):
#         url = "/gettasks/v1?peer_id=" + str(peer_id) + "&status=" + str(status)
#     else:
#         url = "/gettasks/v1?peer_id=" + str(peer_id) + "&lsmfree=" + str(lsmFree) + "&status=" + str(status)
#
#     headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()
#
#     print url
#
#     response = SendRequest(
#         '[TsPeerDistributeReqPush]',
#         http_or_https,
#         GET,
#         ts_host,
#         ts_port,
#         url,
#         headers,
#         None,
#         None
#     )
#     return response


@print_trace
def control_report_v1(protocol, host, port, peer_id, duration,
                      leifengs_file_id=None, cppc=None, download=None, provide=None, leifengs_op=None,
                      channels_file_id=None, playtype=None, chunk_id=None, cdn_bytes=None, p2p_bytes=None, p2penable=None, channels_op=None):
    """
    客户端LF直播频道汇报, 适用SDK版本: [3.7, latest]，sdk -> report.cloutropy.com
    :param protocol:
    :param host:
    :param port:
    :param peer_id: 设备唯一标识符，128位UUID，使用HEX编码
    :param duration: 采样间隔（秒）
    :param leifengs_file_id: 频道file_id
    :param cppc: Cached per chunk
    :param download: 从LivePushServer来的流量
    :param provide: 发送给需求方的量（包括Local）
    :param leifengs_op: 可选, "add"/"del" : 分别为新添加的频道和删除的频道；频道添加之后，删除之前汇报没有op字段
    :param channels_file_id: 频道file_id
    :param playtype: 播放类型,包括"download","live","vod"
    :param chunk_id: 直播必选, live_progress中的的chunk_id
    :param cdn_bytes:
    :param p2p_bytes:
    :param p2penable: 可选，"true"/"false" 默认为开
    :param channels_op: 可选，"add"/"del" 默认为add
    :return:
    """

    url = "/sdk/control_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    leifeng = {"file_id": leifengs_file_id,
               "cppc": cppc,
               "download": download,
               "provide": provide,
               "op": leifengs_op}
    if leifengs_op is None:
        del leifeng["op"]

    channel = {"file_id": channels_file_id,
               "type": playtype,
               "chunk_id": chunk_id,
               "cdn": cdn_bytes,
               "p2p": p2p_bytes,
               "p2penable": p2penable,
               "op": channels_op}
    if chunk_id is None:
        del channel["chunk_id"]
    if channels_op is None:
        del channel["op"]

    body_data = {"peer_id": peer_id,
                 "duration": duration,
                 "leifengs": [leifeng],
                 "channels": [channel]}
    if (type(leifengs_file_id) and type(cppc) and type(download) and type(provide) and type(leifengs_op)) == type(None):
        del body_data["leifengs"]
    if (type(channels_file_id) and type(playtype) and type(chunk_id) and type(cdn_bytes) and type(p2p_bytes) and type(p2penable) and type(channels_op)) == type(None):
        del body_data["channels"]

    response = send_request(
        '[TsControlReportV1]',
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


