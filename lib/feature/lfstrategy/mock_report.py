# coding=utf-8
"""
SDK向ts和stats服务器汇报相关接口
__author__ = 'zsw'

"""
import json
import os
import time
from lib.constant.host import *
from lib.constant.request import *
from lib.feature.lfstrategy.peer_data import *
from lib.decorator.trace import *
from lib.request.header_data import HeaderData
from lib.request.http_request import send_request

response_login = []
response_fod = []
response_liveprogress = []
response_heartbeat = []


@print_trace
def range_peer_login(peer_id_path, peer_start_num, peer_stop_num):

    with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_path, "r") as f:
        PEER_IDS = json.load(f)

    for i in range(int(peer_start_num), int(peer_stop_num)):
        peer_id = PEER_IDS[i]
        peer_body = PEER_BODY1
        res1 = peer_login(HTTP, TS_HOST, TS_PORT, peer_id, peer_body)
        response_login.append(res1)

    return response_login


@print_trace
def range_live_progress(peer_id_path, peer_start_num, peer_stop_num, file_id, chunk_id, file_type="live_flv"):

    with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_path, "r") as f:
        PEER_IDS = json.load(f)

    for i in range(int(peer_start_num), int(peer_stop_num)):
        peer_id = PEER_IDS[i]
        res1 = peer_live_progress(HTTP, REPORT_HOST, REPORT_PORT, file_id, peer_id, chunk_id, file_type)
        response_login.append(res1)

    return response_login


@print_trace
def range_download_flow(peer_id_path, peer_start_num, peer_stop_num, file_id, file_url, p2p, fsize, flow_id, file_type):

    with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_path, "r") as f:
        PEER_IDS = json.load(f)

    for i in range(int(peer_start_num), int(peer_stop_num)):
        peer_id = PEER_IDS[i]
        res1 = peer_download_flow(HTTP, STATS_HOST, STATS_PORT, file_id, file_url, fsize, peer_id, flow_id, p2p, file_type)
        response_login.append(res1)

    return response_login


@print_trace
def range_cache_report(peer_id_path, peer_start_num, peer_stop_num, file_id, cppc, op):

    with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_path, "r") as f:
        PEER_IDS = json.load(f)

    for i in range(int(peer_start_num), int(peer_stop_num)):
        peer_id = PEER_IDS[i]
        res1 = peer_cache_report(HTTP, REPORT_HOST, REPORT_PORT, peer_id, file_id, cppc, op)
        response_login.append(res1)

    return response_login


@print_trace
def range_seed_flow(peer_id_path, peer_start_num, peer_stop_num, file_id, upload, download, upload_conn, accept_conn,
                    denied_conn, flow_id, file_type):

    with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_path, "r") as f:
        PEER_IDS = json.load(f)

    for i in range(int(peer_start_num), int(peer_stop_num)):
        peer_id = PEER_IDS[i]
        res1 = sdk_seed_flow(HTTP, STATS_HOST, STATS_PORT, file_id, peer_id, upload, download, upload_conn, accept_conn
                             , denied_conn, flow_id, file_type)
        response_login.append(res1)

    return response_login


@print_trace
def peer_login(protocol, host, port, peer_id, peer_body):

    url = "/session/peers/" + str(peer_id)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = peer_body

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
def peer_live_progress(httporhttps, report_host, report_port, file_id, peer_id, chunk_id, file_type):

    url = "/live/" + str(file_id) + "/progress"
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()
    body_data = {
        "timestamp": int(time.time()*1000),
        "peer_id": str(peer_id),
        "chunk_id": int(chunk_id),
        "type": str(file_type)
    }

    response = send_request(
        '[PeerLiveProgress]',
        httporhttps,
        POST,
        report_host,
        report_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def peer_download_flow(httporhttps, stats_host, stats_port, file_id, file_url, fsize, peer_id, flow_id, p2p=0,
                       file_type="live_flv"):

    url = "/sdk/flow/download/version/1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('allication/json').get_res()

    timestamp = time.time()
    all_flow = 100000000
    httpdown = all_flow*(1-float(p2p))
    p2pDown = all_flow*float(p2p)

    flow = [
        {
            "timestamp": int(timestamp*1000),
            "duration": 60,
            "p2pDown": int(p2pDown),
            "httpDown": int(httpdown)
        }
    ]

    downloads = [
        {
            "url": str(file_url),
            "file_id": str(file_id),
            "fsize": int(fsize),
            "user_agent": "",
            "flow": flow
        }
    ]

    body_data = {
        "id": str(flow_id),
        "timestamp": int(timestamp),
        "type": str(file_type),
        "peer_id": str(peer_id),
        "downloads": downloads
    }

    response = send_request(
        '[PeerDownloadFlow]',
        httporhttps,
        POST,
        stats_host,
        stats_port,
        url,
        headers,
        None,
        body_data
    )

    return response


@print_trace
def peer_cache_report(protocol, host, port, peer_id, file_id, cppc, op):

    url = "/sdk/cache_report/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    files = [
        {
            "file_id": file_id,
            "cppc": int(cppc),
            "op": op
        }
    ]

    body_data = {"peer_id": peer_id,
                 "files": files}

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
def sdk_seed_flow(httporhttps, stats_host, stats_port, file_id, peer_id, upload, download, upload_conn, accept_conn,
                  denied_conn, flow_id, file_type="live"):

    url = "/sdk/seed/v1"

    headers = HeaderData().Content__Type('application/json').ACCEPT('allication/json').get_res()

    timestamp = time.time()

    flow = [
        {
            "file_id": str(file_id),
            "file_type": str(file_type),
            "upload": int(upload),
            "download": int(download)
        }
    ]

    body_data = {
        "id": str(flow_id),
        "timestamp": int(timestamp),
        "peer_id": str(peer_id),
        "upload_connections": int(upload_conn),
        "accept_connections": int(accept_conn),
        "denied_connections": int(denied_conn),
        "flow": flow
    }

    response = send_request(
        '[SdkSeedFlow]',
        httporhttps,
        POST,
        stats_host,
        stats_port,
        url,
        headers,
        None,
        body_data
    )

    return response


def case(play_count, seeds_count, valid_seeds, p2p=0.0, upload=200, seed_op=OP_ADD, file_id=FILE_ID, file_url=FILE_URL):
    """
    针对直播雷锋策略，通过配置不同参数来模拟测试场景
    :param play_count: 播放节点数
    :param seeds_count: 雷锋节点数
    :param valid_seeds: 有流量汇报的雷锋节点数
    :param p2p: 播放节点p2p占比
    :param upload: 雷锋上传流量，用于放大比计算（download默认为1000）
    :param seed_op: 雷锋节点被拉入或被清退（add or del）
    :param file_id: 频道ID
    :param file_url: 频道url
    :return:
    """
    range_live_progress(PEER_ID_PATH, 0, play_count, file_id, CHUNK_ID, FILE_TYPE)
    range_download_flow(PEER_ID_PATH, 0, play_count, file_id, file_url, p2p, FILE_SIZE, VVID, FILE_TYPE)
    range_cache_report(SEED_ID_PATH, 0, seeds_count, file_id, CPPC, seed_op)
    range_seed_flow(SEED_ID_PATH, 0, valid_seeds, file_id, upload, 1000, upload_conn=0, accept_conn=0, denied_conn=0, flow_id=VVID, file_type=FILE_TYPE)

if __name__ == "__main__":

    print "test"

    # for i in range(10):
    #     time.sleep(120)
    #     case(60, 540, 540, 0.85, 200, OP_ADD, FID_LIST[0], FURL_LIST[0])
    # 针对某一个file，有60个播放节点，且播放p2p占比为85%，当前共有540个雷锋节点且都有流量汇报


