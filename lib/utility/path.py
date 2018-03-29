# coding=utf-8
__author__ = 'zengyuetian'

import inspect
import os
import sys

class PathController(object):
    """
    获得框架内的绝对路径信息
    """
    @classmethod
    def get_root_path(cls):
        """
        获得自动测试框架根目录
        :return:
        """
        file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
        parent_path = os.path.dirname(file_path)
        lib_path = os.path.dirname(parent_path)
        root_path = os.path.dirname(lib_path)
        return root_path

    @classmethod
    def get_root_parent_path(cls):
        """
        获得自动测试框架根目录的父目录
        :return:
        """
        root_parent_path = os.path.dirname(cls.get_root_path())
        return root_parent_path


    @classmethod
    def get_root_dir_name(cls):
        return os.path.basename(cls.get_root_path())

###############################
# 调试用
###############################
if __name__ == "__main__":
    print(PathController.get_root_path())
    print PathController.get_root_dir_name()



