# coding=utf-8
# __author__ = 'Zeng YueTian'

"""
分析响应的核心库
modified by dh 2016.08.10
"""
from lib.decorator.trace import *


@print_trace
def get_field_value(response, field):
    """
    获得响应的返回值
    :param response:响应体
    :param field:感兴趣的域
    :return:void
    """
    try:
        value = response.json().get(field, None)
    except Exception as err:
        print err.message
        value = None

    return value


@print_trace
def get_cookies_value(response):
    """
    获得响应的返回值
    :param response:响应体
    :param field:感兴趣的域
    :return:void
    """
    cookies_info = response.headers.get("set-cookie")
    # sid = cookies_info[4:40]
    # sid_use = sid.replace("-", "")
    s_use = "{0}".format(cookies_info)
    print s_use
    return s_use


@print_trace
def get_response_data(response):
    data = response.text
    return data


@print_trace
def get_value_by_keys(res_data, *args):
    """
    取出多重字典结构下的value， {"d1": {"d2":{"d3": Value}}}
    :param res_data:
    :param args:
    :return:
    """

    for arg in args:
        # print res_data.get(arg)
        res_data = res_data.get(arg, None)
    return res_data


@print_trace
def get_response_data_by_path(response, path=None):
    """
    通过path来解析测试框架发送给mock服务器的数据项
    :param response: 发送的api数据列表
    :param path: 路径，通过/分割，数字表示数组中的项
    :return:path指定的数据内容
    """
    # 判断response的内容和path是否为空
    if len(response.content):
        data = response.json()
        if path is not None:
            # 如果是/开头，去掉/；如果path为空，直接返回response中内容
            if path.startswith("/"):
                path = path[1:]
            key_list = path.split("/")

            for key in key_list:
                if key.isdigit():   # 是数组
                    index = int(key)
                    if len(data) != 0:
                        data = data[index]
                    else:
                        data = ""  # 空数组
                else:  # 是key
                    data = data.get(key)
    else:
        data = response.content

    return data


@print_trace
def parse_stun_rsp_data(rsp_data):
    """
    通过UDP协议解析stun返回的rsp包
    :param rsp_data:
    :return:
    """
    if rsp_data in (None, ""):
        print "Rsp_data is None"
        return None
    elif rsp_data.startswith("8102"):
        step = int(rsp_data[4:6], 16)
        pub_ip_hex = rsp_data[6:14]
        pub_ip = '.'.join([str(int(pub_ip_hex[i:i+2], 16)) for i in xrange(0, len(pub_ip_hex), 2)])
        pub_port = int(rsp_data[14:18], 16)
        return step, pub_port
    elif rsp_data.startswith("8104"):
        rsp_code = int(rsp_data[4:6], 16)
        timestamp = int(rsp_data[6:22], 16)
        return rsp_code
    elif rsp_data.startswith("a102"):
        peer_id = str(rsp_data[4:36]).upper()
        default_str = rsp_data[36:-4]  # default str is contains NAT_TYPE=6, PUBLIC_IP=0.0.0.0, PUBLIC_PORT=0, PRIVATE_IP=0.0.0.0,PRIVATE_PORT=0
        check_sum = rsp_data[-4:]
        return peer_id, default_str, check_sum
    else:
        print "Cannot parse rsp_data : {0}".format(rsp_data)
        return False


def parse_supp_rsp_data(rsp_data):
    """
    解析supp协议的回复
    :param rsp_data:
    :return:
    """
    if rsp_data in (None, ""):
        print "Rsp_data is None"
        return None
    elif rsp_data.startswith("b102"):
        channel_id = int(rsp_data[4:8], 16)
        sequence = int(rsp_data[8:12], 16)
        code = int(rsp_data[12:14], 16)
        print channel_id, sequence, code
    elif rsp_data.startswith("b104"):
        channel_id = int(rsp_data[4:8], 16)
        sequence = int(rsp_data[8:12], 16)
        code = int(rsp_data[12:14], 16)
        return channel_id, sequence, code
    elif rsp_data.startswith("b106"):
        channel_id = int(rsp_data[4:8], 16)
        chunk_id = int(rsp_data[8:16], 16)
        code = int(rsp_data[16:18], 16)
        return channel_id, chunk_id, code
    else:
        pass


def get_code_of_supp_start(response_list):
    """
    获取start response的code参数
    :param response_list:
    :return:
    """
    code = 'not found'
    for response in response_list:
        if response[0:4] == 'b102':
            code = response[12:14]
            break
    return code


if __name__ == "__main__":
    pass
    # data = [{"username":"leigang","phoneNum":"13512345678","emailAddress":"leigang@cloutropy.com",
    # "groups":["admin","downstream","upstream"]},{"username":"ciwen","phoneNum":"80000000001",
    # "emailAddress":"@","groups":["downstream"]},{"username":"icntv","phoneNum":"80000000023",
    # "emailAddress":"@","groups":["downstream","upstream"]}]
    # print GetApiDataByPath(data, "/0/username")
    a = "a1026666666666abcdeabcdeabcde1000000060000000000000000000000008323"

    if a.startswith("a102"):
        peer_id = a[4:36]
        default_str = a[36:-4]  # default str is contains NAT_TYPE=6, PUBLIC_IP=0.0.0.0, PUBLIC_PORT=0, PRIVATE_IP=0.0.0.0,PRIVATE_PORT=0
        check_sum = a[-4:]
        print peer_id, default_str, check_sum









