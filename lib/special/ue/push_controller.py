# coding=utf-8

from lib.decorator.trace import *
from lib.special.ue.const import *
from lib.remote.remoter import *

__author__ = 'dh'


@print_trace
@log_func_args
def route_push(ip, command):
    """

    :param ip:
    :param command:
    :return:
    """
    pass


@log_func_args
@print_trace
def get_live_push_version(ip):
    cmd = "cd {0} && ./{1} -v".format(REMOTE_LIVE_PUSH_SUPP_PATH, LIVE_PUSH_FILE)
    print cmd
    version = remote_execute_stderr(ip, LIVE_PUSH_USER, LIVE_PUSH_ADMIN_PASSWD, cmd)
    # if version in LIVE_PUSH_VERSION_DICT.keys():
    #     return LIVE_PUSH_VERSION_DICT[version]
    # else:
    #     return LIVE_PUSH_VERSION
    return version.split(" ")[-1]

