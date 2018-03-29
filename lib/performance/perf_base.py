# coding=utf-8
"""
性能测试基类

__author__ = 'zengyuetian'

"""

class BasePerformanceTest(object):
    def __init__(self):
        pass

    def prepare_environment(self):
        pass

    def prepare_test(self):
        pass

    def run_test(self):
        pass

    def stop_test(self):
        pass

    def collect_log(self):
        pass


    def parse_result(self):
        pass

    def archive_result(self):
        pass





