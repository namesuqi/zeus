# coding=utf-8
"""
p2pserver interfaces with shata

"""

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *
from lib.request.authentication import *

class Api_M3U8(object):

    @print_trace
    def Md5Token(self, str):
        """
        str to md5
        :param str:
        :return:
        """
        md5 = hashlib.md5()
        md5.update(str)
        return md5.hexdigest()

    @print_trace
    def CreateM3U8(self, fileid, m3u8_url):
        """
        通过该接口创建m3u8
        :param fileid:
        :param m3u8_url:
        :return:
        """

        url = "/createM3U8"

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

        body_data = {
            "username": "tester",
            "file_id": Api_M3U8().Md5Token(fileid),
            "m3u8_url": m3u8_url
        }

        response = send_request(
            '[CreateM3U8]',
            'HTTP',
            POST,
            '192.168.1.64',
            '9539',
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def DeleteM3U8(self, fileid):
        """
        通过该接口删除m3u8
        :param fileid:
        :param m3u8_url:
        :return:
        """

        url = "/deleteM3U8"

        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

        body_data = {
            "file_id": Api_M3U8().Md5Token(fileid)
        }

        response = send_request(
            '[DeleteM3U8]',
            'HTTP',
            POST,
            '192.168.1.64',
            '9539',
            url,
            headers,
            None,
            body_data
        )

        return response

if __name__ == "__main__":
    url = 'http://192.168.1.64:9999/home/admin/m3u8/test.m3u8'
    #Api_M3U8().CreateM3U8('yunshangtest', url)
    Api_M3U8().DeleteM3U8('yunshangtest')
    pass