# coding=utf-8
"""
性能测试节点机

__author__ = 'zengyuetian'

"""

import xmlrpclib
import time
from lib.utility.path import *
from lib.utility.times import *

RPC_PORT = "19527"

class PerfNode(object):
    ip = ""
    user = ""
    password = ""

    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password
        self.rpc_proxy = self.init_rpc_proxy()

    def init_rpc_proxy(self):
        '''
        初始化xpc服务器
        :return:void
        '''
        url = 'http://{0}:{1}'.format(self.ip, RPC_PORT)
        return xmlrpclib.ServerProxy(url)

    def start_collect_param(self):
        log_file = PathController.get_root_path() + "/log/perf.log"
        log = open(log_file, "a")
        memory_percent = self.rpc_proxy.get_memory_percent()
        cpu_idle_percent = self.rpc_proxy.get_cpu_idle_percent()
        log.write("TIME:{0}, IP:{1}, CPU IDLE:{2}%, MEM USER:{3}%\n".format(get_formated_time_sec_string(), self.ip, str(cpu_idle_percent), str(memory_percent)))
        log.close()

ROOT_USER = "root"
ROOT_PASSWORD = "Yunshang2014"
perf_nodes = []
perf_nodes.append(PerfNode("10.5.100.10", ROOT_USER, ROOT_PASSWORD))
perf_nodes.append(PerfNode("10.5.100.11", ROOT_USER, ROOT_PASSWORD))







