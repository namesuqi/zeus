# coding=utf-8
"""
The factory of Test Executor

__author__ = 'zengyuetian'

"""

from lib.framework.executor_server import *
from lib.framework.executor_sdk import *
from lib.framework.executor_system import *
from lib.framework.executor_idc import *
from lib.framework.executor_leifeng import *
from lib.framework.executor_live import *
from lib.framework.executor_vod import *
from lib.framework.executor_deploy import *


class ExecutorFactory(object):
    """
    create object according to param
    """
    @staticmethod
    def make_executor(name):
        """
        create executor
        :param name:
        :return:
        """
        if name == "server":
            return ExecutorServer()
        elif name == "sdk":
            return ExecutorSdk()
        elif name == "idc":
            return ExecutorIdc()
        elif name == "live":
            return ExecutorLive()
        elif name == "leifeng":
            return ExecutorLeifeng()
        elif name == "vod":
            return ExecutorVod()
        elif name == "deploy":
            return ExecutorDeploy()
        elif name == "system":
            return ExecutorSystem()
        elif name == "dummy":
            return ExecutorSystem()








