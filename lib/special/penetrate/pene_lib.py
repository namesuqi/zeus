# coding=utf-8
# author: Pan Pan
from lib.special.penetrate.remote_commander import RemoteCommand
from lib.special.penetrate import pene_util
import time
import json
from lib.constant.pene import *


def start_dummy_nat(remoteip, natype):
    """
    启动NAT模拟器
    :param remoteip:
    :param natype:
    :return:
    """
    try:
        re_comm = RemoteCommand()
        re_comm.set_remote_ips([remoteip])
        re_comm.exec_command(START_DUMMY_NAT_COMMAND % natype, "root")
        return True
    except:
        return False


def start_sdk(remoteip):
    """
    启动SDK
    :param remoteip:
    :return:
    """
    try:
        re_comm = RemoteCommand()
        re_comm.set_remote_ips([remoteip])
        re_comm.exec_command(START_SDK_COMMAND, "admin")
        return True
    except:
        return False


def check_sdk_login(remoteip):
    """
    验证SDK是否登录成功
    :param remoteip:
    :return:
    """
    try:
        return pene_util.check_peer_login(3, [remoteip])
    except:
        return False


def check_sdk_nat_type(remoteip, natype):
    """
    验证NAT类型
    :param remoteip:
    :param natype:
    :return:
    """
    if natype == "2":
        natype = "1"
    try:
        ret_values = pene_util.get_peer_login_info([remoteip])
        out_str, err_str = ret_values[remoteip]
        tmp_obj = json.loads(out_str)
        if str(tmp_obj["natType"]) != natype:
            return False
        else:
            return True
    except:
        return False


def mock_ts_info(remoteip):
    """
    mock ts 的返回值
    :param remoteip:
    :return:
    """
    try:
        peer_id = pene_util.get_peer_id_info(remoteip)
        sdk_version = pene_util.get_peer_version_info(remoteip)
        if peer_id and sdk_version:
            ret_values = pene_util.get_peer_login_info([remoteip])
            out_str, err_str = ret_values[remoteip]
            tmp_obj = json.loads(out_str)
            if pene_util.generate_ts_mock_response(sdk_version, peer_id, tmp_obj):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


def start_sdk_vod(remoteip):
    """
    点播起播
    :param remoteip:
    :return:
    """
    try:
        re_comm = RemoteCommand()
        re_comm.set_remote_ips([remoteip])
        re_comm.exec_command(START_VOD_COMMAND, "admin")
        time.sleep(15)
        return True
    except:
        return False


def check_pene_log_steps(sendremoteip, receiveremoteip, sendnatype):
    """
    验证log里面的穿透步骤是否正确
    :param sendremoteip:
    :param receiveremoteip:
    :param sendnatype:
    :return:
    """
    ret_val = True
    need_rever = False
    if sendnatype == "4":
        need_rever = True
    if pene_util.check_penetrator_log(sendremoteip, True, needREVER=need_rever):
        print "check penetrate log PASS in ip: %s" % sendremoteip
        ret_val = ret_val and True
    else:
        print "check penetrate log FAILED in ip: %s" % sendremoteip
        ret_val = ret_val and False
    if pene_util.check_penetrator_log(receiveremoteip, False, needREVER=need_rever):
        print "check penetrate log PASS in ip: %s" % receiveremoteip
        ret_val = ret_val and True
    else:
        print "check penetrate log FAILED in ip: %s" % receiveremoteip
        ret_val = ret_val and False
    return ret_val


def stop_sdk_running(*remoteips):
    """
    停止SDK
    :param remoteips:
    :return:
    """
    ip_list = list(remoteips)
    re_comm = RemoteCommand()
    re_comm.set_remote_ips(ip_list)
    re_comm.exec_command(STOP_SDK_COMMAND, "root")


def stop_dummy_nat_running(*remoteips):
    """
    停止NAT模拟器
    :param remoteips:
    :return:
    """
    ip_list = list(remoteips)
    re_comm = RemoteCommand()
    re_comm.set_remote_ips(ip_list)
    re_comm.exec_command(STOP_DUMMY_NAT_COMMAND, "root")


def collect_original_nat_log(remoteip, foldername, filesuffix):
    """
    收集NAT日志
    :param remoteip:
    :param foldername:
    :param filesuffix:
    :return:
    """
    pene_util.collect_nat_log(remoteip, foldername, filesuffix)


def deploy_penetrate_sdk(*remoteips):
    """
    部署SDK到remote机器
    :param remoteips:
    :return:
    """
    ip_list = list(remoteips)
    re_comm = RemoteCommand()
    re_comm.set_remote_ips(ip_list)
    re_comm.exec_command("rm -r %s* /home/admin/yunshang/" % SDK_FOLDER_PATH, "admin")
    re_comm.copy_to_remote(SDK_FILE_PATH, PENETRATE_SDK_FILE_PATH, "admin")
    re_comm.exec_command("chmod +x %s" % SDK_FILE_PATH, "admin")
