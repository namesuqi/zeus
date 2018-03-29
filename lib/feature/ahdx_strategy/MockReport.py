# coding=utf-8
"""
SDK向ts和stats服务器汇报相关接口

"""
import time

from lib.constant.host import *
from lib.constant.request import *
from lib.feature.ahdx_strategy.CreatePeerData import CreatePeerData
from lib.feature.ahdx_strategy.file_data import *
from lib.request.HeaderAndData import *
from lib.request.HTTPRequest import *
from lib.decorator.trace import *

class MockReport(object):

    def __init__(self):
        self.response_login = []
        self.response_fod = []
        self.response_heartbeat = []
        self.response_distribute = []
        self.response_deldistribute = []
        self.response_flow = []

    @print_trace
    def NewPeerLogin(self, peer_num):
        """
        指定一定数量的peer login
        :param peer_num: 初始login的peer数量
        :return:
        """

        PEER_ID = CreatePeerData().ReadPeerInfo()[0]
        PEER_BODY = CreatePeerData().ReadPeerInfo()[1]
        # 调用随机生成的peer信息

        for i in range(0, int(peer_num)):
            peer_id = PEER_ID[i]
            peer_body = PEER_BODY[i]
            #login
            res = self.PeerLogin(HTTP, TS_HOST_AHDX, TS_PORT_AHDX, peer_id, peer_body)
            self.response_login = []
            self.response_login.append(res)

        return (self.response_login)

    @print_trace
    def OnlinePeerNum(self, peer_num):
        '''
        模拟peer的heartbeat
        :param peer_num: 汇报的peer数量
        :return:
        '''

        PEER_ID = CreatePeerData().ReadPeerInfo()[0]
        # 调用随机生成的peer信息

        for i in range(0, int(peer_num)):
            peer_id = PEER_ID[i]
            #heartbeat
            res = self.PeerHeartBeat(HTTP, TS_HOST_AHDX, TS_PORT_AHDX, peer_id)

            self.response_heartbeat = []
            self.response_heartbeat.append(res)

        return (self.response_heartbeat)

    @print_trace
    def SeedDistribute(self, file_start, file_end, seed_start, seed_end):
        """
        模拟seed进行本地文件缓存汇报(需要先login)
        :param file_start:起始文件序号
        :param file_end: 结束文件序号
        :param seed_start: seed起始序号
        :param seed_end: seed结束序号
        :return:
        """

        # 调用随机生成的peer信息
        PEER_ID = CreatePeerData().ReadPeerInfo()[0]

        for i in range(int(seed_start), int(seed_end)):
            peer_id = PEER_ID[i]
            res = self.PeerDistribute(HTTP, TS_HOST_AHDX, TS_PORT_AHDX, peer_id, FILE_ID[int(file_start): int(file_end)])

            self.response_distribute = []
            self.response_distribute.append(res)

        return (self.response_distribute)

    @print_trace
    def SeedDistributeDel(self, file_start, file_end, seed_start, seed_end):
        """
        模拟seed进行本地文件缓存删除汇报(需要先login)
        :param file_start: 文件起始序号
        :param file_end: 文件结束序号
        :param seed_start: seed起始序号
        :param seed_end: seed结束序号
        :return:
        """

        # 调用随机生成的peer信息
        PEER_ID = CreatePeerData().ReadPeerInfo()[0]

        for i in range(int(seed_start), int(seed_end)):
            peer_id = PEER_ID[i]
            res = self.PeerDistributeDel(HTTP, TS_HOST_AHDX, TS_PORT_AHDX, peer_id, FILE_ID[int(file_start): int(file_end)])

            self.response_deldistribute = []
            self.response_deldistribute.append(res)

        return (self.response_deldistribute)

    @print_trace
    def FodFile(self, file_start, file_end, peer_num):
        """
        模拟fod汇报(需要先login)
        :param file_start:起始文件序号
        :param file_end: 结束文件序号
        :param peer_num: 播放文件节点数
        :return:
        """

        # 调用随机生成的peer信息
        PEER_ID = CreatePeerData().ReadPeerInfo()[0]
        peer_start = 0
        peer_end = peer_start + int(peer_num)

        for i in range(int(file_start), int(file_end)):

            file_id = FILE_ID[i]
            fsize = FILE_SIZE[i]

            for j in range(int(peer_start), int(peer_end)):
                peer_id = PEER_ID[j]
                res = self.SdkFod(HTTP, STATS_HOST_AHDX, STATS_PORT_AHDX, FOD_ID, FILE_URL, file_id, peer_id, fsize)

                self.response_fod = []
                self.response_fod.append(res)
            peer_start = peer_end
            peer_end = peer_start + int(peer_num)

        return (self.response_fod)

    @print_trace
    def FodFileSingle(self, file_start, file_end, peer_start, peer_end):
        """
        单个文件模拟fod汇报(需要先login)
        :param file_start:起始文件序号
        :param file_end: 结束文件序号
        :param peer_start: peer起始序号
        :param peer_end: peer结束序号
        :return:
        """

        # 调用随机生成的peer信息
        PEER_ID = CreatePeerData().ReadPeerInfo()[0]

        for i in range(int(file_start), int(file_end)):

            file_id = FILE_ID[i]
            fsize = FILE_SIZE[i]

            for j in range(int(peer_start), int(peer_end)):
                peer_id = PEER_ID[j]
                res = self.SdkFod(HTTP, STATS_HOST_AHDX, STATS_PORT_AHDX, FOD_ID, FILE_URL, file_id, peer_id, fsize)

                self.response_fod = []
                self.response_fod.append(res)

        return (self.response_fod)

    @print_trace
    def DownloadFlow(self, file_start, file_end, peer_num):
        """
        模拟download_flow汇报(需要先fod汇报)
        :param file_start:起始文件序号
        :param file_end: 结束文件序号
        :param peer_num: 播放文件节点数
        :return:
        """

        # 调用随机生成的peer信息
        PEER_ID = CreatePeerData().ReadPeerInfo()[0]
        peer_start = 0
        peer_end = peer_start + int(peer_num)

        for i in range(int(file_start), int(file_end)):

            file_id = FILE_ID[i]
            fsize = FILE_SIZE[i]

            for j in range(int(peer_start), int(peer_end)):
                peer_id = PEER_ID[j]
                res = self.PeerFlow(HTTP, STATS_HOST_AHDX, STATS_PORT_AHDX, FLOW_ID, FILE_URL, file_id, peer_id, fsize)

                self.response_flow = []
                self.response_flow.append(res)
            peer_start = peer_end
            peer_end = peer_start + int(peer_num)

        return (self.response_flow)


    @print_trace
    def PeerLogin(self, httporhttps, ts_host, ts_port, peer_id, peer_info):
        """
        peer登录
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :param peer_info:
        :return:
        """
        url = "/session/peers/" + str(peer_id)

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        body_data = peer_info

        response = SendRequest(
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
    def PeerHeartBeat(self, httporhttps, ts_host, ts_port, peer_id):
        """
        peer心跳
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :return:
        """
        url = "/session/peers/" + str(peer_id)

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        response = SendRequest(
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
    def SdkFod(self, httporhttps, stats_host, stats_port, fod_id, file_url, file_id, peer_id, fsize):
        '''
        模拟sdk的fod汇报
        :param httporhttps:
        :param stats_host:
        :param stats_port:
        :param fod_id:
        :param file_url: 文件url
        :param file_id: 文件ID
        :param peer_id:
        :param fsize:s
        :return:
        '''

        url = "/sdk/fod/version/1"

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        body_data = {
            "id": fod_id,
            "timestamp": str(int(time.time())),
            "url": file_url,
            "file_id": str(file_id),
            "fsize": fsize,
            "peer_id": str(peer_id),
            "fod_type": str("vod")
        }

        response = SendRequest(
            '[SdkFod]',
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
    def PeerDistribute(self, httporhttps, ts_host, ts_port, peer_id, file_id):
        """
        模拟peer汇报本地缓存
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :param file_id:
        :return:
        """

        url = "/distribute/peers/" + str(peer_id)

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        #本地缓存文件信息
        file_data = []

        for i in range(0, len(file_id)):
            data = {
                "file_id": file_id[i],
                "ppc": 12,
                "sliceMap": 'FFFFFFFFFFFFFFFF'
            }
            file_data.append(data)

        body_data = {
            "lsmSize": "",
            "universe": "",
            "files": file_data,
        }

        response = SendRequest(
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
    def PeerDistributeDel(self, httporhttps, ts_host, ts_port, peer_id, file_id):
        """
        模拟peer汇报本地删除
        :param httporhttps:
        :param ts_host:
        :param ts_port:
        :param peer_id:
        :param file_id:
        :return:
        """

        url = "/distribute/peers/" + str(peer_id)

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        file_data = []
        for i in range(0, len(file_id)):
            data = {
                "file_id": file_id[i],
                "ppc": 0,
                "sliceMap": '0000000000000000'
            }
            file_data.append(data)

        body_data = {
            "lsmSize": "",
            "universe": "",
            "files": file_data,
        }

        response = SendRequest(
            '[PeerDistributeDelete]',
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
    def PeerFlow(self, httporhttps, stats_host, stats_port, flow_id, file_url, peer_id, file_id, fsize):
        """
        模拟peer汇报Flow信息
        :param httporthttps:
        :param stats_host:
        :param stats_port:
        :param flow_id:
        :param file_url:
        :param peer_id:
        :param file_id:
        :param fsize:
        :return:
        """

        url = "/sdk/flow/download/version/1"

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('allication/json').getRes()

        timestamp = str(int(time.time()))

        flow = [
            {
                "timestamp": timestamp,
                "duration": 60,
                "p2pDown": 0,
                "httpDown": 16547328
            }
        ]

        downloads = [
            {
                "url": file_url,
                "file_id": str(file_id),
                "fsize": fsize,
                "user_agent": "",
                "flow": flow
            }
        ]

        body_data = {
            "id": str(flow_id),
            "timestamp": timestamp,
            "type": "vod",
            "peer_id": str(peer_id),
            "downloads": downloads
        }

        response = SendRequest(
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


if __name__ == "__main__":
    MockReport().DownloadFlow(0, 1, 1)
    #pass
    #MockReport().FodFile(0, 1, 2)
    #MockReport().SeedDistributeDel(0, 2, 0, 2)
    #MockReport().NewPeerLogin(4)
    #MockReport().OnlinePeerNum(1)
    #MockReport().FodFile(0, 1, 1)
