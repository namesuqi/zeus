# coding=utf-8
"""
SDK向ts和stats服务器汇报相关接口

__author__ = 'zsw'

"""
import time
import os
import socket
from random import Random
import struct
from lib.constant.request import *
from lib.feature.mock_sdk_report.file_data import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *

class SdkReport(object):


    @print_trace
    def peer_login(self, httporhttps, ts_host, ts_port, peer_id, peer_body):
        """
        peer login
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :param peer_info:
        :return:
        """
        url = "/session/peers/" + str(peer_id)

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

        body_data = peer_body

        response = send_request(
            '[PeerLogin]',
            httporhttps,
            POST,
            ts_host,
            ts_port,
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def peer_heartbeat(self, httporhttps, ts_host, ts_port, peer_id):
        """
        peer heartbeat
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :return:
        """
        url = "/session/peers/" + str(peer_id)

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

        response = send_request(
            '[PeerHeartBeat]',
            httporhttps,
            GET,
            ts_host,
            ts_port,
            url,
            headers,
            None,
            None
        )

        return response

    @print_trace
    def peer_fod(self, httporhttps, stats_host, stats_port, peer_id, file_id, file_url, fsize, fod_id, fod_type="vod"):
        '''
        fod report
        :param httporhttps:
        :param stats_host:
        :param stats_port:
        :param peer_id:
        :param file_id:
        :param file_url:
        :param fsize:
        :param fod_id:
        :param fod_type:
        :return:
        '''

        url = "/sdk/fod/version/1"

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

        body_data = {
            "id": fod_id,
            "timestamp": int(time.time()),
            "url": str(file_url),
            "file_id": str(file_id),
            "fsize": fsize,
            "peer_id": str(peer_id),
            "fod_type": str(fod_type)
        }

        response = send_request(
            '[PeerFod]',
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
    def peer_download_flow(self, httporhttps, stats_host, stats_port, file_id, file_url, fsize, peer_id, flow_id, p2p=0, flow_type="vod"):
        '''
        sdk download flow report, set httpdown=1000000, change p2pdown according to the p2p_percent
        :param stats_host:
        :param stats_port:
        :param file_url:
        :param fsize:
        :param flow_id:
        :param p2p: p2p_percent
        :param flow_type:
        :return:
        '''

        url = "/sdk/flow/download/version/1"

        headers = HeaderData().Content__Type('application/json').ACCEPT('allication/json').get_res()

        timestamp = time.time()
        all_flow = 100000000
        httpdown = all_flow*(1-float(p2p))
        p2pDown = all_flow*float(p2p)

        flow = [
            {
                "timestamp": int(timestamp),
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
            "timestamp": int(timestamp*1000),
            "type": str(flow_type),
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
    def peer_distribute(self, httporhttps, ts_host, ts_port, peer_id, file_id, isdel="del"):
        """
        lsm report
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :param file_id:
        :return:
        """

        url = "/distribute/peers/" + str(peer_id)

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

        # local file cache
        file_data = []
        if type(file_id) == list:
            len_file = len(file_id)
        else:
            len_file = 1

        if str(isdel) == "del":
            for i in range(0, len_file):
                data = {
                    "file_id": file_id,
                    "ppc": 0,
                    "sliceMap": '0000000000000000'
                }
                file_data.append(data)
        else:
            for i in range(0, len_file):
                data = {
                    "file_id": file_id,
                    "ppc": 12,
                    "sliceMap": 'FFFFFFFFFFFFFFFF'
                }
                file_data.append(data)

        body_data = {
            "lsmSize": "",
            "universe": "",
            "files": file_data,
        }

        response = send_request(
            '[PeerDistribute]',
            httporhttps,
            POST,
            ts_host,
            ts_port,
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def seed_get_task(self, httporhttps, ts_host, ts_port, seed_id, lsmFree="25600", onlyDel="0"):
        '''
        send request to ts, get download or delete task
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param seed_id:
        :param lsmFree:
        :param onlyDel:
        :return:
        '''

        url = "/distribute/peers/" + str(seed_id) + "?lsmFree=" + str(lsmFree) + "&onlyDel=" + onlyDel

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

        response = send_request(
            '[SeedGetTask]',
            httporhttps,
            GET,
            ts_host,
            ts_port,
            url,
            headers,
            None,
            None
        )
        return response

    @print_trace
    def read_peer_info(self, peer_id_file=PEER_ID_FILE, peer_body_file=PEER_BODY_FILE
                     , seed_id_file=SEED_ID_FILE, seed_body_file=SEED_BODY_FILE):
        '''
        peer_id, peer_body, seed_id, seed_body
        :param peer_id_file:
        :param peer_body_file:
        :param seed_id_file:
        :param seed_body_file:
        :return:
        '''

        with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_file, "r") as f:
            PEER_ID_LIST = json.load(f)
        with open(os.path.abspath(os.path.dirname(__file__)) + peer_body_file, "rb") as f1:
            PEER_BODY_LIST = json.load(f1)
        with open(os.path.abspath(os.path.dirname(__file__)) + seed_id_file, "r") as f2:
            SEED_ID_LIST = json.load(f2)
        with open(os.path.abspath(os.path.dirname(__file__)) + seed_body_file, "r") as f3:
            SEED_BODY_LIST = json.load(f3)

        return (PEER_ID_LIST, PEER_BODY_LIST, SEED_ID_LIST, SEED_BODY_LIST)

    @print_trace
    def create_peer_ids(self, peer_id_nums=5000, peer_id_file=PEER_ID_FILE):
        '''
        write many peerids into peer_id_file
        :param peer_id_nums:
        :param peer_id_file:
        :return:
        '''
        file1 = open(os.path.abspath(os.path.dirname(__file__)) + peer_id_file, "w")
        m = 1000000
        file1.write('[')
        for i in range(int(peer_id_nums)):
            file1.write('2222222222ABCDEABCDEABCDE{0}\n'.format(m))
            file1.flush()
            m += 1
        file1.write('"0"]')
        file1.close()

    @print_trace
    def create_peer_bodys(self, peer_nums=1000, peer_body_file=PEER_BODY_FILE):
        '''
        write many peer_body into peer_body_file (for "POST sdklogin")
        :param peer_nums:
        :return:
        '''

        # file1.write('[')
        peer_body_list = []
        for i in range(peer_nums):
            peer_ip = self.get_random_ip()
            peer_body = {'version': '3.1.0', 'natType': 0, 'publicIP': str(peer_ip), 'publicPort': 53200, 'privateIP': str(peer_ip), 'privatePort': 53200}
            peer_body_list.append(peer_body)
        with open(os.path.abspath(os.path.dirname(__file__)) + peer_body_file, "w") as f:
            json.dump(peer_body_list, f)


    @print_trace
    def get_random_ip(self):
        '''
        generate random IP
        :return:
        '''

        RANDOM_IP_POOL = ['192.168.10.222/0']
        random = Random()
        str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
        str_ip_addr = str_ip.split('/')[0]
        str_ip_mask = str_ip.split('/')[1]
        ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
        mask = 0x0
        for i in range(31, 31 - int(str_ip_mask), -1):
            mask = mask | ( 1 << i)
        ip_addr_min = ip_addr & (mask & 0xffffffff)
        ip_addr_max = ip_addr | (~mask & 0xffffffff)

        return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

    @print_trace
    def verify_task(self, response, file_key):
        '''
        check task from ts
        :param response: response of get_task
        :param file_key: file_id in response data (KEY-VALUE)
        :return:
        '''

        res_file_data = response.json().get("files", None)
        file_values = []
        if len(res_file_data) > 0:
            for i in range(len(res_file_data)):
                file_json_data = res_file_data[i]
                file_value = file_json_data[file_key]
                file_values.append(file_value)

        else:
            file_values = ""

        print file_values


if __name__ == "__main__":
    # SdkReport).CridseerBodys()
    # SdkReport().ReadPeerInfo()
    # SdkReport().PeerHeartBeat(HTTP, "ts.cloutropy.com", "80", "6666666666abcdeabcdeabcde100000# 0")

    pass


