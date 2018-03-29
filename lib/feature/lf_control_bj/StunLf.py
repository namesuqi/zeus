# coding=utf-8
"""
join leifeng and leave leifeng through ts -> stun

__author__ = 'zsw'

"""
from struct import pack

from lib.constant.request import *
from lib.feature.lf_control_bj.GetLfFile import GetLfFile
from lib.feature.lf_control_bj.lf_data import *
from lib.request.HeaderAndData import *
from lib.request.HTTPRequest import *
from lib.decorator.trace import *

class StunLf(object):

    def __init__(self):
        self.response_join = []
        self.response_leave = []

    @print_trace
    def JoinLfNum(self, lf_start_num, lf_stop_num, cppc=1, file_info=HKS_FILE_INFO):

        LF_ID_LIST = GetLfFile().GetPeerID(int(lf_stop_num))
        LF_IDS = LF_ID_LIST[int(lf_start_num):int(lf_stop_num)]

        response = self.LfJoin(HTTP, STUN_IP, STUN_PORT, LF_IDS, cppc, file_info)
        return response

    @print_trace
    def LeaveLfNum(self, lf_start_num, lf_stop_num, file_info=HKS_FILE_INFO):

        LF_ID_LIST = GetLfFile().GetPeerID(int(lf_stop_num))
        LF_IDS = LF_ID_LIST[int(lf_start_num):int(lf_stop_num)]

        response = self.LfLeave(HTTP, STUN_IP, STUN_PORT, LF_IDS, file_info)

        return response

    @print_trace
    def LfJoin(self, httporhttps, stun_ip, stun_port, lf_id="", cppc=1, file_info=HKS_FILE_INFO):

        url = "/rrpc/join_leifeng"

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        if type(lf_id) != list:
            lf_ids = [lf_id]
            # change lf_id type, str => list
        else:
            lf_ids = lf_id

        # lf_ids = ["00000000D80F7C46BD3245480F93DBB1", "000000043F0D46CC8ABC18DB8B7A95D3"]

        file_id = file_info[0]
        file_url = file_info[1]
        file_ppc = file_info[2]

        body_data = {
            "file_id": file_id,
            "file_url": file_url,
            "peer_ids": lf_ids,
            "psize": int(864),
            "ppc": int(file_ppc),
            "cppc": int(cppc),
            "push_server": LIVE_PUSH_ARGS
        }

        response = SendRequest(
            '[LfJoin]',
            httporhttps,
            POST,
            stun_ip,
            stun_port,
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def LfLeave(self, httporhttps, stun_ip, stun_port, lf_id="", file_info=HKS_FILE_INFO):

        url = "/rrpc/leave_leifeng"

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        if type(lf_id) != list:
            lf_ids = [lf_id]
            # change lf_id type, str => list
        else:
            lf_ids = lf_id

        # lf_ids = ["00000000D80F7C46BD3245480F93DBB1", "000000043F0D46CC8ABC18DB8B7A95D3"]
        file_id = file_info[0]

        body_data = {
            "file_id": file_id,
            "peer_ids": lf_ids,
        }

        response = SendRequest(
            '[LfLeave]',
            httporhttps,
            POST,
            stun_ip,
            stun_port,
            url,
            headers,
            None,
            body_data
        )

        return response

if __name__ == '__main__':
    # StunLf().LfJoin('http', 'stun.cloutropy.com', '80','00000004C69A4B8992F73716D89F78B0')
    pass