# coding=utf-8
"""
dir相关服务器访问接口

__author__ = 'zengyuetian'

modified by dh 2016.08.05

"""
import time
import urllib

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def dir_create_file(protocol, dir_host, dir_port, user_name, file_url, size, md5, file_id, source_url,
                    source_ext, source_type, public="", if_generate_dir=""):
    """
    create a new file
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param user_name:用户名
    :param file_url:文件URL (以根目录"/"开头的URL则表明是不携带前缀的(domain)相对URL,否则视为携带前缀的完整URL)
    :param size:文件大小
    :param md5:文件MD5
    :param file_id:文件的唯一标识 (可选标识，若不带该参数，则由服务器自行产生)
    :param source_url:数据来源(可选字段)
    :param source_ext:数据源的扩展信息(可选字段。仅作为附加信息携带)
    :param source_type:数据来源方式,如 "M3U8","CDN","OSS"
    :param public:控制文件是否公开,默认公开 (yes or no)
    :param if_generate_dir:控制是否生成目录 (true or false)
    :return:响应
    """
    url = "/user/files"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "username": user_name,
        "url": file_url,
        "size": int(size),
        "md5": md5,
        "file_id": file_id,
        "source_url": source_url,
        "source_ext": source_ext,
        "sourceType": source_type,
        "public": public,
    }
    if if_generate_dir in ("True", "true"):
        body_data["if_generate_dir"] = True
    elif if_generate_dir in ("False", "false"):
        body_data["if_generate_dir"] = False
    else:
        body_data["if_generate_dir"] = if_generate_dir

    response = send_request(
        '[DirCreateFile]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_search_by_url(protocol, dir_host, dir_port, url_prefix="", url_file_name=""):
    """
    根据URL查询文件信息
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param url_prefix:url前缀
    :param url_file_name: url文件名
    :return: 响应
    """
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if (url_prefix is not None) and (url_prefix != ""):
        if (url_file_name is not None) and (url_file_name != ""):
            url = "/user/files/url?url=" + url_prefix + url_file_name

        else:
            url = "/user/files/url?url=" + url_prefix

    else:
        if (url_file_name is not None) and (url_file_name != ""):
            url = "/user/files/url?url=" + url_file_name

        else:
            url = "/user/files/url?url="

    response = send_request(
        '[SearchByURL]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def dir_get_play_info(protocol, dir_host, dir_port, user_name, search_type, file_url=""):
    """
    根据URL(含义取决于$type)查询播放文件信息,并可支持未注册文件的自动注册
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param user_name:用户名
    :param search_type:指示查询方式,当前支持"video_url": 查询所用URL为视频文件URL;
                                "source_url": 查询所用URL为注册的源URL,如m3u8的URL
    :param file_url:
    :return:
    """

    url = "/user/files/start_channel?username=" + str(user_name) + "&type=" + str(search_type) + "&url=" + \
          str(file_url)

    headers = HeaderData().Content_Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[DirGetPlayInfo]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_search_by_file_id(protocol, dir_host, dir_port, file_id=''):
    """
    根据文件fileid查询文件信息
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param file_id: 文件id
    :return: 响应
    """
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    url = "/user/files/file_id?file_id=" + str(file_id)

    response = send_request(
        '[SearchByFileId]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def dir_search_by_md5(protocol, dir_host, dir_port, md5=''):
    """
    根据MD5获取文件信息
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param md5: 文件MD5
    :return: 响应
    """
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    url = "/user/files/md5?md5=" + md5

    response = send_request(
        '[SearchByMd5]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )

    return response


@print_trace
def dir_delete_file_path(protocol, dir_host, dir_port, user_id, file_path, source_type=""):
    """
    删除filepath对应的记录,如果没有其他URL再引用到同一文件，则服务器会通知响应的存储服务彻底删除对应文件
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param user_id:用户id
    :param file_path:指定文件的filepath
    :param source_type:数据源类型，可选参数，默认值“OSS”
    :return:响应
    """

    if source_type in (None, ""):
        url = "/user/files/" + str(user_id) + "?filepath=" + str(file_path)
    else:
        url = "/user/files/" + str(user_id) + "?filepath=" + str(file_path) + "&sourceType=" + str(source_type)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    response = send_request(
        '[DirDeleteFilePath]',
        protocol,
        DELETE,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_create_prefix(protocol, dir_host, dir_port, owner, prefix=None, source_type=""):
    """
    在指定用户下创建prefix
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param owner: 用户名
    :param prefix:prefix
    :param source_type:sourcetype
    :return:响应
    """
    url = '/user/prefix'

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "owner": owner,
        "sourceType": source_type
    }
    if (prefix is not None) and (prefix != ""):
        body_data["prefix"] = prefix

    response = send_request(
        '[DirCreatePrefix]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_delete_prefix(protocol, dir_host, dir_port, prefix=''):
    """
    删除指定prefix
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param prefix: 要删除的prefix
    :return: 响应
    """
    url = '/user/prefix?prefix=' + prefix

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    data = {
        "prefix": prefix
    }

    response = send_request(
        '[DeletePrefix]',
        protocol,
        DELETE,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        data
    )
    return response


@print_trace
def dir_get_folder(protocol, dir_host, dir_port, user_id="", directory="", source_type=""):
    """
    提取用户指定目录下的所有文件名和子目录名
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param user_id: 用户id
    :param directory: 查询目录
    :param source_type: 用户数据源的类型，可选参数，默认值“OSS"
    :return: 响应
    """

    if source_type in (None, ""):
        url = "/user/directory/" + str(user_id) + "?dir=" + str(directory)
    else:
        url = "/user/directory/" + str(user_id) + "?dir=" + str(directory) + "&sourceType=" + str(source_type)

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[DirGetFolder]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_check_file(protocol, dir_host, dir_port, user_id, file_path, source_type=""):
    """
    检测指定用户的指定文件是否存在
    :param protocol: 协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param user_id: 用户id
    :param file_path: 文件路径
    :param source_type: 用户的数据源的类型
    :return: 响应
    """

    if source_type in (None, ""):
        url = "/user/directory/" + str(user_id) + "/file_exist?filepath=" + file_path

    else:
        url = "/user/directory/" + str(user_id) + "/file_exist?filepath=" + file_path + "&sourceType=" + source_type

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[DirCheckFile]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_create_folder(protocol, dir_host, dir_port, user_id, current_folder=None, new_folder=None):
    """
    在指定路径下新建目录
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param user_id:用户id
    :param current_folder:当前目录
    :param new_folder:新建目录名称
    :return:响应
    """
    url = '/user/directory/' + str(user_id) + '/create_folder'

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}
    if (current_folder is not None) and (current_folder != ""):
        body_data["cwd"] = current_folder
    if (new_folder is not None) and (new_folder != ""):
        body_data["folder"] = new_folder

    response = send_request(
        '[DirCreateFolder]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_create_file_by_path(protocol, dir_host, dir_port, user_id, cwd, file_name, size, md5, file_id, public=""):
    """
    在指定路径下新建文件
    :param protocol:协议
    :param dir_host: 服务器
    :param dir_port: 端口
    :param user_id: 用户id
    :param cwd: 当前目录
    :param file_name: 新建文件名称
    :param size: 文件大小
    :param md5: 文件MD5
    :param file_id: 文件的唯一标识
    :param public: 控制文件是否公开，默认公开（yes or no)
    :return: 响应
    """
    url = "/user/directory/" + str(user_id) + "/create_file"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {
        "cwd": cwd,
        "filename": file_name,
        "size": int(size),
        "md5": md5,
        "file_id": file_id,
        "public": public,
        "createdTime": time.time()*1000
    }

    response = send_request(
        '[DirCreateFileByPath]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_delete_directory(protocol, dir_host, dir_port, user_id, directory=""):
    """
    删除指定目录
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param user_id:用户id
    :param directory: directory为全路径目录名
    :return:响应
    """
    url = "/user/directory/" + str(user_id) + "?directory=" + directory

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}

    response = send_request(
        '[DeleteDirectory]',
        protocol,
        DELETE,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_query_source_info(protocol, dir_host, dir_port, file_id=""):
    """
    根据指定的file_id查询其对应的源信息
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param file_id:file_id为本系统认定的文件标识
    :return:响应
    """
    url = "/user/files/source?file_id=" + file_id

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    response = send_request(
        '[DirQuerySourceInfo]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_add_blacklist(protocol, dir_host, dir_port, file_url=""):
    """
    添加一个文件到黑名单列表
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param file_url:
    :return:
    """
    url = "/user/files/blacklist"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}
    if (file_url is not None) and (file_url != ""):
        body_data["url"] = file_url

    response = send_request(
        '[AddBlacklist]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_delete_blacklist(protocol, dir_host, dir_port, file_url=""):
    """
    从黑名单列表中删除一个文件
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param file_url:
    :return:
    """
    url = "/user/files/blacklist?url=" + file_url

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = {}
    if (file_url is not None) and (file_url != ""):
        body_data["url"] = file_url

    response = send_request(
        '[DeleteBlacklist]',
        protocol,
        DELETE,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_get_source_files(protocol, dir_host, dir_port, user_id="", page_index="", page_count="", source_type=""):
    """
    获取用户OSS以外的其他源数据列表
    :param protocol:协议
    :param dir_host:服务器
    :param dir_port:端口
    :param user_id:用户id
    :param page_index:页码
    :param page_count:每页显示的条目数
    :param source_type:源类型
    :return:响应
    """
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    url = "/source_files?uid=" + str(user_id) + "&pageIndex=" + page_index + "&pageCount=" + page_count + \
             "&sourceType=" + source_type

    body_data = {
        "uid": user_id,
        "pageIndex": page_index,
        "pageCount": page_count,
        "sourceType": source_type
    }

    response = send_request(
        '[DirGetSourceFiles]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_get_url_info(protocol, dir_host, dir_port, file_url=""):
    """
    获取一个url的相关信息
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param file_url:url 文件的url，网络路径
    :return:
    """

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    url = "/file/url?url=" + str(file_url)

    response = send_request(
        '[DirGetUrlInfo]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_get_files_size(protocol, dir_host, dir_port, file_ids=""):
    """
    获取多个文件的大小
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param file_ids: 文件id列表
    :return:
    """

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    url = "/get/files/size"

    body_data = {
        "fileIds": file_ids
    }

    response = send_request(
        '[DirGetFilesSize]',
        protocol,
        POST,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        body_data
    )
    return response


@print_trace
def dir_sdk_start_play(protocol, dir_host, dir_port, user_name, peer_id, file_url="", version=""):
    """
    客户端SDK起播时，请求播放url的信息
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param user_name:用户名，必选
    :param peer_id:节点id，必选
    :param file_url:播放url，必选
    :param version:客户端版本信息，可选，旧版本的客户端没有此参数
    :return:
    """

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if (file_url is not None) and (file_url != ""):
        if file_url.startswith('http://'):
            file_url_encode = urllib.quote_plus(file_url.encode('UTF-8', 'replace'))
            # 对m3u8文件的url进行编码
        else:
            file_url_encode = file_url
    else:
        file_url_encode = ""

    if (version is not None) and (version != ""):
        url = "/startchannel?user=" + user_name + "&pid=" + peer_id + "&url=" + file_url_encode + "&version=" + version

    else:
        url = "/startchannel?user=" + user_name + "&pid=" + peer_id + "&url=" + file_url_encode

    response = send_request(
        '[DirSdkStartPlay]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def dir_sdk_start_m3u8(protocol, dir_host, dir_port, user_name, peer_id, file_url="", version=""):
    """
    客户端SDK起播M3U8文件时，请求播放url的信息
    :param protocol:
    :param dir_host:
    :param dir_port:
    :param user_name:用户名，必选
    :param peer_id:节点id，必选
    :param file_url:播放url，必选
    :param version:客户端版本信息，可选，旧版本的客户端没有此参数
    :return:
    """

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if (file_url is not None) and (file_url != ""):
        if file_url.startswith('http://'):
            file_url_encode = urllib.quote_plus(file_url.encode('UTF-8', 'replace'))
        # 对m3u8文件的url进行编码
        else:
            file_url_encode = file_url

    else:
        file_url_encode = ""

    if (version is not None) and (version != ""):
        url = "/starthls?user=" + user_name + "&pid=" + peer_id + "&url=" + file_url_encode + "&version=" + version

    else:
        url = "/starthls?user=" + user_name + "&pid=" + peer_id + "&url=" + file_url_encode

    response = send_request(
        '[DirSdkStartM3u8]',
        protocol,
        GET,
        dir_host,
        dir_port,
        url,
        headers,
        None,
        None
    )
    return response


