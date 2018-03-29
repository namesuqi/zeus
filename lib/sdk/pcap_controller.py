# coding=utf-8
# author: zengyuetian
# capture package to a pcap file

from lib.decorator.trace import *
from lib.remote.remoter import *
from lib.sdk.const import *
import os


@print_trace
def stop_capture(ip=REMOTE_SDK_IP):
    """
    stop tcpdump process
    :param ip: sdk machine
    :return: None
    """
    cmd = "killall -9 tcpdump"
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)


@print_trace
def start_capture(ip=REMOTE_SDK_IP, dest=None):
    """
    start tcpdump to capture packages
    :param ip: remote machine ip to run sdk
    :param dest: domain or ip for server
    :return: None
    """

    # delete existing *.pcap file
    cmd = "rm -f {0}".format(REMOTE_PCAP)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)

    # start tcpdump command
    if dest is None:
        cmd = "nohup tcpdump -i {0} -w {1} > /dev/null 2>&1 &".format(REMOTE_ETH, REMOTE_PCAP)
    else:
        cmd = "nohup tcpdump -i {0} host {1} -w {2} > /dev/null 2>&1 &".format(REMOTE_ETH, dest, REMOTE_PCAP)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)


@print_trace
def transfer_pcap_file(ip=REMOTE_SDK_IP):
    """
    copy *.pcap file from remote machine to local machine
    :param ip: remote machine
    :return: None
    """
    copy_file_from(ip, ROOT_USER, ROOT_PASSWD, REMOTE_PCAP, LOCAL_PCAP)


@print_trace
def transfer_check_log_file(ip=REMOTE_SDK_IP):
    """
    copy *.pcap file from remote machine to local machine
    :param ip: remote machine
    :return: None
    """
    copy_file_from(ip, ROOT_USER, ROOT_PASSWD, REMOTE_LOG_FILE, LOCAL_LOG_FILE)


@print_trace
def transfer_exec_files(ip=REMOTE_SDK_IP):
    """
    copy *.pcap file from remote machine to local machine
    :param ip: remote machine
    :return: None
    """
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, os.path.join(os.path.dirname(__file__),
                                                          "api_format.py"), "/root/api_format.py")
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, os.path.join(os.path.dirname(__file__),
                                                          "sdk_request_check.py"), "/root/sdk_request_check.py")
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, os.path.join(os.path.dirname(__file__),
                                                          "tcpdump_filter.py"), "/root/tcpdump_filter.py")
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, os.path.join(root_path, "utility/yunduan_live_play/flv_parse.py"),
                 "/root/flv_parse.py")
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, os.path.join(root_path, "utility/yunduan_live_play/play.py"),
                 "/root/play.py")
