# coding=utf-8
"""
通过接口设置push-hub
"""
__author__ = 'ys_tester'

from lib.decorator.trace import *
from lib.request.HeaderAndData import *
from lib.request.HTTPRequest import *
from lib.feature.multi_host.push_data import *
from lib.constant.request import *



class Pushhub(object):

    @print_trace
    def IP_Map(self, ip_map_body):
        """
        更改ip_map映射表
        :return:
        """
        res = self.UpdateIpMap(HTTP, PUSH_HUB_HOST, PUSH_HUB_PORT, ip_map_body)

        return res

    @print_trace
    def UpdateIpMap(self, httporhttps, push_hub_host, push_hub_port, ip_map_body):
        '''
        管理员更改live-push-srv的ip与省份（province）和供应商（isp）之间的映射表
        :param httporhttps:
        :param push_hub_host:
        :param push_hub_port:
        :param ip_map_body:
        :return:
        '''

        headers = HeaderAndData().Content__Type('application/json').ACCEPT('application/json').getRes()

        url = "/admin/ip_map?all=1"

        body = ip_map_body

        response = SendRequest(
            '[UpdateIpMap]',
            httporhttps,
            POST,
            push_hub_host,
            push_hub_port,
            url,
            headers,
            None,
            body
        )

        return response

if __name__ == "__main__":
    #Pushhub().IP_Map(IP_MAP_BODY);
    pass