# coding=utf-8
# control the player
# author: zengyuetian

import time
from lib.special.ue.const import *
from lib.remote.remoter import *
from lib.decorator.trace import *


@print_trace
@log_func_args
def player_deploy(ip):
    """
    deploy player interface
    :param ip:
    :return:
    """
    # kill previous processes
    kill_cmd = "killall -9 python"
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, kill_cmd)

    # create sdk dir
    mkdir_cmd = "mkdir -p {0}".format(REMOTE_PLAYER_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, mkdir_cmd)

    # copy file to remote sdk dir
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_PLAYER, REMOTE_PLAYER)
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_FLV_PARSER, REMOTE_FLV_PARSER)

    # make sdk executable
    chmod_cmd = "chmod +x {0}".format(REMOTE_PLAYER)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, chmod_cmd)


@print_trace
@log_func_args
def player_start(ip, url, log_file_name):
    """
    start player(python) interface
    :param log_file_name: first_image_time or buffering num
    :param ip:
    :param url:
    :return:
    """
    url = "http://127.0.0.1:{0}/{1}".format(SDK_PORT, url)
    play_cmd = "cd {0} && nohup python {1} {2} {3} > /dev/null 2>&1 &".format(REMOTE_PLAYER_PATH, REMOTE_PLAYER,
                                                                              url, log_file_name)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, play_cmd)


@print_trace
@log_func_args
def http_flv_player_start(ip, url, log_file_name):
    """
    start player(python) interface
    :param log_file_name: first_image_time or buffering num
    :param ip:
    :param url:
    :return:
    """
    play_cmd = "cd {0} && nohup python {1} {2} {3} > /dev/null 2>&1 &".format(REMOTE_PLAYER_PATH, REMOTE_PLAYER,
                                                                              url, log_file_name)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, play_cmd)


@print_trace
@log_func_args
def player_stop(ip):
    """
    :param ip:
    :param times: retention parameter
    :return:
    """
    kill_cmd = "killall -9 python"
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, kill_cmd)


@print_trace
@log_func_args
def player_wait(sec):
    time.sleep(sec)


@print_trace
@log_func_args
def player_first_image_time(ip, log_file_name):
    """
    parse log and get firstplaytime
    :param ip:
    :param log_file_name
    :return:
    """
    cmd = "head -5 {0}".format(log_file_name) + "|grep startup |awk -F ' ' '{print $5}'"
    # cmd = "head -5 {0}".format(REMOTE_PLAYER_LOG) + "|grep begin |awk -F ' ' '{print $1}'"
    cmd_result = remote_execute_result(ip, ROOT_USER, ROOT_PASSWD, cmd)

    if cmd_result.strip() in ['', None]:
        return 30

    try:
        first_image_time = float(cmd_result)
    except:
        first_image_time = -1

    return first_image_time


@print_trace
@log_func_args
def player_buffering_num(ip, log_file_name):
    """
    parse log and get buffering times
    :param ip:
    :param log_file_name
    :return:
    """
    cmd = "cat {0}".format(log_file_name) + "|grep buffering |wc -l"

    buffer_num = remote_execute_result(ip, ROOT_USER, ROOT_PASSWD, cmd)
    if buffer_num in ['', None]:
        return 0
    return int(buffer_num)


