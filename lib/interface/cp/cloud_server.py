# coding=utf-8
"""
cloud related api

__author__ = 'zengyuetian'

"""

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *



@print_trace
def cloud_push(protocol, host, port, file_id, chunk_start, chunk_num, piece_num):
    """
    sdk向vod-push请求数据推送
    :param protocol:
    :param host:
    :param port:
    :param file_id:
    :param chunk_start:
    :param chunk_num:
    :param piece_num:
    :return:
    """
    # create url
    url = "/push/files/{0}/chunks/{1}_{2}/pieces/{3}".format(file_id, chunk_start, chunk_num, piece_num)

    # create header
    headers = HeaderData().ACCEPT('application/octet-stream').getRes()

    # send request
    response = send_request(
        '[cloud_push]', protocol,
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
def cloud_url(protocol, cloud_host, cloud_port, file_name, range_start, range_end, chunk_id=''):
    """
    源站服务器请求
    :param protocol:
    :param cloud_host:
    :param cloud_port:
    :param file_name:
    :param range_start:
    :param range_end:
    :param chunk_id:
    :return:
    """
    url = '/{0}'.format(file_name)
    range_str = 'bytes={0}-{1}'.format(str(range_start), str(range_end))
    if chunk_id != '':
        url = url + "?chunk={0}".format(chunk_id)
    print url

    headers = HeaderData().Range(range_str).getRes()

    response = send_request(
        '[cloud_url]', protocol,
        GET,
        cloud_host,
        cloud_port,
        url,
        headers,
        None,
        None
    )

    return response

