# coding=utf-8
"""
p2pserver interfaces with shata

"""

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *
from lib.request.authentication import *

class Api_Shata(object):

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
    def ApiPurgeFiles(self, httporhttps, api_host, api_port, urls, access, secret):
        """
        通过该接口删除files
        :param httporhttps:
        :param api_host:
        :param api_port:
        :param urls:files的url，以\n结尾
        :param access:
        :param secret:
        :return:
        """

        url = "/api/purge/files"

        headers = HeaderData().Content__Type('text/plain').ACCEPT('application/json').getRes()

        url1 = secret + api_host + ":" + api_port + "/api/purge/files"
        print url1
        token = "token=" + access + ":" + Api_Shata().Md5Token(url1)
        url = url + "?" + token

        body_data = urls

        response = send_request_without_json(
            '[ApiPurgeFiles]',
            httporhttps,
            POST,
            api_host,
            api_port,
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def ApiPurgeFolders(self, httporhttps, api_host, api_port, urls, access, secret):
        """
        通过该接口删除folders
        :param httporhttps:
        :param api_host:
        :param api_port:
        :param urls:folders的url，以\n结尾
        :param access:
        :param secret:
        :return:
        """

        url = "/api/purge/folders"

        headers = HeaderData().Content__Type('text/plain').ACCEPT('application/json').getRes()

        url1 = secret + api_host + ":" + api_port + "/api/purge/folders"
        print url1
        token = "token=" + access + ":" + Api_Shata().Md5Token(url1)
        url = url + "?" + token

        body_data = urls

        response = send_request_without_json(
            '[ApiPurgeFolders]',
            httporhttps,
            POST,
            api_host,
            api_port,
            url,
            headers,
            None,
            body_data
        )

        return response

    @print_trace
    def ApiBandwidth(self, httporhttps, api_host, api_port, step, start, end, access, secret):
        """
        get bandwidth
        :param httporhttps:
        :param api_host:
        :param api_port:
        :param step:数据粒度，minute表示5分钟粒度（时间划分是以每天的零点为起点
        :param start:开始时间戳
        :param end:结束时间戳
        :param access:
        :param secret:
        :return:
        """

        url = "/api/bandwidth?step=" + step + "&start=" + start + "&end=" + end
        url1 = secret + api_host + ":" + api_port + "/api/bandwidth?step=" + step + "&start=" + start + "&end=" + end
        print url1
        token = "token=" + access + ":" + Api_Shata().Md5Token(url1)
        url = url + "&" + token
        print url
        headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').getRes()

        response = send_request(
            '[ApiBandwidth]',
            httporhttps,
            GET,
            api_host,
            api_port,
            url,
            headers,
            None,
            None
        )

        return response

if __name__ == "__main__":
    #MysqlHandler().RestoreTbbox()
    #Api_Shata().ApiPurgeFiles('http', '192.168.1.64', '8083', 'http://ciwen.cloutropy.com/v-21/s-16', '123456', '666666')
    #Api_Shata().ApiPurgeFolders('http', '192.168.1.64', '8083', 'http://ciwen.cloutropy.com/v-21/s-16', '123456', '666666')
    #Api_Shata().ApiBandwidth('http', '192.168.1.64', '8083', 'minute', '1451355600000', '1451752200000', '123456', '666666')
    #Api_Shata().ApiBandwidth('http', '192.168.1.64', '8083', 'day', '1451577600000', '1456761600000', '123456', '666666')
    #Api_Shata().ApiBandwidth('http', '192.168.1.64', '8083', 'hour', '1451365200000', '1451556000000', '123456', '666666')
    #Api_Shata().ApiBandwidth('http', '192.168.1.64', '8083', 'month', '1451491200000', '1459353600000', '123456', '666666')
    pass