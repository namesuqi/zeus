# coding=utf-8
"""
本文件用于rpc远程控制
运行在远程的节点机器上

现阶段只用于以下用例：
    1. 性能测试

__author__ = 'zengyuetian'

"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import logging
import logging.config
import logging.handlers
import inspect
import sys
import time
import psutil

RPC_PORT = 19527
logger = None

def get_current_dir():
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    parent_path = os.path.dirname(file_path)
    return parent_path


class RpcService(object):
    def get_memory_used(self):
        '''
        获得使用的内存大小(M)
        :return:
        '''
        mem = psutil.virtual_memory()
        logger.info("get_memory_used: {0}".format(mem.used))
        return mem.used / (1024 * 1024)

    def get_memory_percent(self):
        '''
        获得使用的内存百分比
        :return:
        '''
        mem = psutil.virtual_memory()
        logger.info("get_memory_percent: {0}".format(mem.percent))
        return mem.percent


    def get_cpu_idle_percent(self):
        '''
        获得使用的内存百分比
        :return:
        '''
        cpu_time_percent = psutil.cpu_times_percent()
        logger.info("get_cpu_idle_percent: {0}".format(cpu_time_percent.idle))
        return cpu_time_percent.idle


if __name__ == "__main__":
    # logging for debugging
    log_path = get_current_dir() + "/log"
    BRIEF_LENGTH = 1024
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = log_path + "/perf_test.log"
    handler = logging.handlers.RotatingFileHandler \
        (log_file, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
    fmt = '%(asctime)s - %(message)s'
    formatter = logging.Formatter(fmt)  # 实例化formatter
    handler.setFormatter(formatter)  # 为handler添加formatter
    logger = logging.getLogger('ta')  # 获取名为tst的logger
    logger.addHandler(handler)  # 为logger添加handler
    logger.setLevel(logging.INFO)
    logger.info("================================")
    logger.info("***** Performance Test *****")
    logger.info("================================")

    # start service, keep ip address as 0.0.0.0 to monitor all networking interface
    server = SimpleXMLRPCServer(('0.0.0.0', RPC_PORT),
                                logRequests=True,
                                allow_none=True)

    server.register_introspection_functions()
    server.register_multicall_functions()
    server.register_instance(RpcService())

    try:
        print 'use control-c to exit'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'exiting'




