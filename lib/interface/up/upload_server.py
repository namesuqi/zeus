# coding=utf-8
'''
upload相关服务器访问接口

'''

import hashlib
import time
from lib.constant.request import *
from lib.request.authentication import get_md5_with_date_offset
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *



@print_trace
def upload_url(protocol, host, port, username, password, file_url=None, file_size=None, file_md5=None, public='yes'):
    '''
    登记文件URL,引入外链文件，参与内部P2P系统
    :param protocol:协议
    :param host:服务器
    :param port:端口
    :param file_url:url
    :param file_size:文件大小
    :param file_md5:文件MD5
    :param public:是否公开
    :return:响应
    '''

    url = "/register_url"

    date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime(time.time()))

    md5 = hashlib.md5('POST' + '\n' + file_url + '\n' + file_size + '\n' + file_md5 + '\n' + public + '\n' + password + '\n' + date)
    signature = md5.hexdigest()

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').Authorization(
        username+":"+signature).Date(date).getRes()
    print date

    body_data = {
        "fileUrl": str(file_url),
        "fileSize": int(file_size),
        "fileMD5": str(file_md5),
        "public": str(public)
    }

    response = send_request(
        '[upload_url]',
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


if __name__ == "__main__":
     delay = 0
     date = get_md5_with_date_offset('sdf', int(delay))
     print date
     n1 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time()))
     n2 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime(time.time()))
     print n1, n2
     # print datetime.time()
     # print time.gmtime(time.time())
