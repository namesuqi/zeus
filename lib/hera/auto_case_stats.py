# coding=utf-8
# author: zengyuetian
# 用于获得当前自动化测试用数目的工具

from lib.utility.path import *
from collections import defaultdict
from lib.hera.const import *
import requests
import json


root_path = PathController.get_root_path()
tc_path = root_path + "/testsuite"
file_list = []
total = 0
auto_test_dict = defaultdict(int)


def handle_file(file_name):
    """
    统计带有指定tag的测试用例数目
    :param file_name:
    :return:
    """
    global total, auto_test_dict
    for line in open(file_name):
        line = line.strip()  # 去除两端空格
        words_list = line.split("  ")
        # print(words_list)
        for word in words_list:
            if word in AUTO_TEST_CASE_TAGS:
                total += 1
                auto_test_dict[word] += 1


def get_file_list(rootdir):
    """
    获得指定目录下所有的文件列表
    :param rootdir:
    :return:
    """
    for parent, dirnames, filenames in os.walk(rootdir):
        # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for dirname in dirnames: #输出文件夹信息
            # print "parent is:" + parent
            # print "dirname is" + dirname
        for filename in filenames:  # 输出文件信息
            # print "parent is" + parent
            # print "filename is:" + filename
            # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            full_name = os.path.join(parent, filename)
            # print file_name
            file_list.append(full_name)


def send_case_info():
    """
    send dailytest case info into hera management system
    :return:
    """
    get_file_list(tc_path)
    for fil in file_list:
        handle_file(fil)
    # print "Total auto case number is:{0}".format(total)
    auto_test_data = dict(auto_test_dict)
    response = requests.post(HERA_AUTO_TEST_URL, json=json.dumps(auto_test_data))
    if '200' in str(response):
        return True
    else:
        return False


if __name__ == "__main__":
    send_case_info()






