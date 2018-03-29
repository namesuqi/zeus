# coding=utf-8
"""
send multi peers' requests and report

__author__ = 'zsw'

"""

from lib.constant.host import *
from lib.constant.request import *
from lib.feature.mock_sdk_report.sdk_report import *
from lib.feature.mock_sdk_report.file_data import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


class SendSdkReqs(object):

    @print_trace
    def peers_login(self, peer_start_num=0, peer_end_num=10):
        '''
        get peer_id form peer_id_file, then send login request to ts
        :param peer_start_num:
        :param peer_end_num:
        :return:
        '''

        PEER_ID = SdkReport().read_peer_info()[0]
        print PEER_ID[0]
        PEER_BODY = SdkReport().read_peer_info()[1]

        response_login = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            peer_id = PEER_ID[i]
            peer_body = PEER_BODY[i]
            res = SdkReport().peer_login(HTTP, TS_HOST, TS_PORT, peer_id, peer_body)
            response_login.append(res)

        return response_login

    @print_trace
    def seeds_login(self, peer_start_num=0, peer_end_num=10):
        '''
        get seed_id form seed_id_file, then send login request to ts
        :param peer_start_num:
        :param peer_end_num:
        :return:
        '''

        SEED_ID = SdkReport().read_peer_info()[2]
        SEED_BODY = SdkReport().read_peer_info()[3]

        response_login = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            seed_id = SEED_ID[i]
            seed_body = SEED_BODY[i]
            res = SdkReport().peer_login(HTTP, TS_HOST, TS_PORT, seed_id, seed_body)
            response_login.append(res)

        return response_login

    @print_trace
    def peers_heartbeat(self, peer_start_num, peer_end_num):
        '''
        get peer_id form peer_id_file, then send heartbeat request to ts
        :param peer_start_num:
        :param peer_end_num:
        :return:
        '''

        PEER_ID = SdkReport().read_peer_info()[0]

        response_heartbeat = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            peer_id = PEER_ID[i]
            res = SdkReport().peer_heartbeat(HTTP, TS_HOST, TS_PORT, peer_id)
            response_heartbeat.append(res)

        return response_heartbeat

    @print_trace
    def seeds_heartbeat(self, peer_start_num, peer_end_num):
        '''
        get seed_id form seed_id_file, then send heartbeat request to ts
        :param peer_start_num:
        :param peer_end_num:
        :return:
        '''

        SEED_ID = SdkReport().read_peer_info()[2]

        response_heartbeat = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            seed_id = SEED_ID[i]
            res = SdkReport().peer_heartbeat(HTTP, TS_HOST, TS_PORT, seed_id)
            response_heartbeat.append(res)

        return response_heartbeat

    @print_trace
    def peers_fod(self, peer_start_num, peer_end_num, file_id=VOD_FILE1_ID, file_url=VOD_FILE1_URL, fsize=VOD_FILE1_SIZE):
        '''
       get peer_id form peer_id_file, send fod report
        :param peer_start_num:
        :param peer_end_num:
        :param file_id:
        :param file_url:
        :param fsize:
        :return:
        '''

        PEER_ID = SdkReport().read_peer_info()[0]
        print PEER_ID[0]
        response_fod = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            peer_id = PEER_ID[i]
            res = SdkReport().peer_fod(HTTP, STATS_HOST, STATS_PORT, peer_id, file_id, file_url, fsize, FOD_ID)
            response_fod.append(res)

        return response_fod

    @print_trace
    def peers_flow(self, peer_start_num, peer_end_num, p2p=0, file_id=VOD_FILE1_ID, file_url=VOD_FILE1_URL, fsize=VOD_FILE1_SIZE):
        '''
        sdk download flow，set httpdown=1000000, change p2pdown according to the p2p_percent
        :param peer_start_num:
        :param peer_end_num:
        :param file_id:
        :param file_url:
        :param fsize:
        :param p2p: p2p percent
        :return:
        '''

        PEER_ID = SdkReport().read_peer_info()[0]
        response_flow = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            peer_id = PEER_ID[i]
            res = SdkReport().peer_download_flow(HTTP, STATS_HOST, STATS_PORT, file_id, file_url, fsize, peer_id, FLOW_ID, p2p)
            response_flow.append(res)

        return response_flow

    @print_trace
    def peers_distribute(self, peer_start_num, peer_end_num, file_id=VOD_FILE1_ID, isdel="del"):
        '''
        get peer_id form peer_id_file, when isdel="del", slicemap=0000000000000000
        :param peer_start_num:
        :param peer_end_num:
        :param file_id:
        :param isdel:
        :return:
        '''

        PEER_ID = SdkReport().read_peer_info()[0]

        response_distribute = []

        for i in range(int(peer_start_num), int(peer_end_num)):
            seed_id = PEER_ID[i]
            res = SdkReport().peer_distribute(HTTP, TS_HOST, TS_PORT, seed_id, file_id, isdel)
            response_distribute.append(res)

        return response_distribute

    @print_trace
    def seeds_distribute(self, seed_start_num, seed_end_num, isdel="del", file_id=VOD_FILE1_ID):
        '''
        get seed_id form seed_id_file, when isdel="del", slicemap=0000000000000000
        :param seed_start_num:
        :param seed_end_num:
        :param file_id:
        :param isdel:
        :return:
        '''

        SEED_ID = SdkReport().read_peer_info()[2]

        response_distribute = []

        for i in range(int(seed_start_num), int(seed_end_num)):
            seed_id = SEED_ID[i]
            res = SdkReport().peer_distribute(HTTP, TS_HOST, TS_PORT, seed_id, file_id, isdel)
            response_distribute.append(res)

        return response_distribute

    @print_trace
    def seeds_get_task(self, seed_start_num, seed_end_num, file_id=VOD_FILE1_ID, seedorpeer="seed"):
        '''
        get seed_id from seed_id_file, send get_task to ts, analyse response
        :param seed_start_num:
        :param seed_end_num:
        :return:
        '''
        if seedorpeer == "seed":
            SEED_ID = SdkReport().read_peer_info()[2]
        else:
            SEED_ID = SdkReport().read_peer_info()[0]

        delete_task = 0
        download_task = 0
        for i in range(int(seed_start_num), int(seed_end_num)):
            seed_id = SEED_ID[i]
            res = SdkReport().seed_get_task(HTTP, TS_HOST, TS_PORT, seed_id)
            get_file_id = SdkReport().verify_task(res, "file_id")
            get_file_ope = SdkReport().verify_task(res, "operation")
            if str(file_id) in str(get_file_id) and str(get_file_ope) == "download":
                download_task += 1
                print seed_id, "get download task"
            elif str(get_file_id) == str(file_id) and str(get_file_ope) == "delete":
                delete_task += 1
                print seed_id, "get delete task"
            else:
                print seed_id, "didn't get ", file_id, "task"

        print "delete_task", delete_task
        print "download_task", download_task
        return (delete_task, download_task)


if __name__ == '__main__':
    # SendSdkReqs().peers_login(0, 60)
    # SendSdkReqs().peers_fod(0, 60, VOD_FILE1_ID, VOD_FILE1_URL, VOD_FILE1_SIZE)
    # SendSdkReqs().seeds_login(0, 200)
    # SendSdkReqs().seeds_distribute(0, 200, "no", VOD_FILE3_ID)
    print time.time()
    pass