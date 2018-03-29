# coding=utf-8
# author: Pan Pan

from remote_commander import RemoteCommand
import time
import json
import re
import os
from lib.constant.pene import *


def check_peer_login(timeout, ip_list):
    """
    检查SDK是否已经登录
    :param timeout:
    :param ip_list:
    :return:
    """
    login_val = False
    count = 0
    while count < timeout and not login_val:
        check_dict = get_peer_login_info(ip_list)
        for key in check_dict.keys():
            if not check_dict[key][0].find('"status": "E_OK"') > -1:
                login_val = False
                break
        else:
            login_val = True
        time.sleep(1)
        count += 1
    return login_val


def get_peer_login_info(ip_list):
    """
    获得ajax/login页的数据
    :param ip_list:
    :return:
    """
    re_com = RemoteCommand()
    re_com.set_remote_ips(ip_list)
    ret_values = re_com.exec_command('curl %s' % SDK_LOGIN_URL, "admin")
    return ret_values


def get_peer_id_info(remoteip):
    """
    获得Peer节点的PeerID
    :param remoteip:
    :return:
    """
    re_com = RemoteCommand()
    re_com.set_remote_ips([remoteip])
    ret_values = re_com.exec_command("cat %s" % SDK_CONF_FILE, "admin")
    try:
        tmp_obj = json.loads(ret_values[remoteip][0])
        return tmp_obj["peer_id"]
    except:
        return None


def get_peer_version_info(remoteip):
    """
    获得SDK版本信息
    :param remoteip:
    :return:
    """
    re_com = RemoteCommand()
    re_com.set_remote_ips([remoteip])
    ret_values = re_com.exec_command("curl %s" % SDK_VERSION_URL, "admin")
    try:
        tmp_obj = json.loads(ret_values[remoteip][0])
        return tmp_obj["core"]
    except:
        return None


def generate_ts_mock_response(peerver, peerid, pinfobj):
    """
    将期望的ts响应写入jsontext.text
    :param peerver:
    :param peerid:
    :param pinfobj:
    :return:
    """
    ret_str_format = '{"seeds":[{"stunIP":"%s","version":"%s","natType":%s,"publicIP":"%s","publicPort":%s,"privateIP":"%s",' \
                     '"privatePort":%s,"isp_id":"100017","peer_id":"%s","cppc":1}]}'
    mock_ts_file = r"/home/admin/mock_ts/jsontext.txt"
    ret_str = ret_str_format % (pinfobj["stunIP"], peerver, pinfobj["natType"], pinfobj["publicIP"], pinfobj["publicPort"],
                                pinfobj["privateIP"], pinfobj["privatePort"], peerid)
    re_com = RemoteCommand()
    re_com.set_remote_ips([MOCK_TS_IP])
    ret_values = re_com.exec_command("> %s; echo '%s' > %s" % (mock_ts_file, ret_str, mock_ts_file), "admin")
    if len(ret_values[MOCK_TS_IP][1]) > 0:
        return False
    else:
        return True


def check_penetrator_log(remoteip, penetype, needREVER=False):

    if check_penetrator_pattern_log(remoteip, penetype, needREVER):
        if check_penetrator_simple_log(remoteip):
            return True
        else:
            return False
    else:
        return False


def check_penetrator_pattern_log(remoteip, penetype, needREVER=False):
    log_file_path = PENETRATE_LOG_PATH
    re_com = RemoteCommand()
    re_com.set_remote_ips([remoteip])
    ret_values = re_com.exec_command("cat %s" % log_file_path, "root")
    lines = ret_values[remoteip][0].split("\n")
    if penetype:
        if not needREVER:
            log_pattern = ([".*OUTside.*packet: a103.*", False], [".*INside.*packet: a104.*", False],
                           [".*OUTside.*packet: a105.*", False])
        else:
            log_pattern = ([".*OUTside.*packet: a106.*", False], [".*INside.*packet: a103.*", False],
                           [".*OUTside.*packet: a104.*", False], [".*INside.*packet: a105.*", False])
    else:
        if not needREVER:
            log_pattern = ([".*INside.*packet: a103.*", False], [".*OUTside.*packet: a104.*", False],
                           [".*INside.*packet: a105.*", False])
        else:
            log_pattern = ([".*INside.*packet: a106.*", False], [".*OUTside.*packet: a103.*", False],
                           [".*INside.*packet: a104.*", False], [".*OUTside.*packet: a105.*", False])
    for line in lines:
        for index, item in enumerate(log_pattern):
            if not item[1]:
                if re.match(item[0], line):
                    log_pattern[index][1] = True
                break
    for temp_item in log_pattern:
        if not temp_item[1]:
            return False
    return True


def check_penetrator_simple_log(remoteip):
    log_file_path = PENETRATE_LOG_PATH
    re_com = RemoteCommand()
    re_com.set_remote_ips([remoteip])
    ret_values = re_com.exec_command("cat %s" % log_file_path, "root")
    lines = ret_values[remoteip][0].split("\n")
    for line in lines:
        if line.find("packet: d1") > -1:
            return True
    return False


def collect_nat_log(remoteip, folder, filesuffix):
    root_folder = "./natLogs"
    if not os.path.isdir(root_folder):
        os.mkdir(root_folder)
    full_folder = os.path.join(root_folder, folder)
    if not os.path.isdir(full_folder):
        os.mkdir(full_folder)
    re_com = RemoteCommand()
    re_com.set_remote_ips([remoteip])
    ret_values = re_com.exec_command("ls /home/admin/dummy_nat/log/ -tl |grep forward_ |head -n 1|awk '{print $9}'",
                                     "root")
    file_name = ret_values[remoteip][0].replace("\n", "")
    if len(file_name) == 0:
        print "get collect log name failed ..."
    else:
        remote_file = "/home/admin/dummy_nat/log/%s" % file_name
        local_file = os.path.join(full_folder, file_name + filesuffix)
        re_com.copy_from_remote(remote_file, local_file, "root")
