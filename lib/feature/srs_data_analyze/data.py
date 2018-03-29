#!/usr/bin/python
# coding=utf-8
#运行代码时记得根据需要修改此处的参数

FILE_PATH = '/home/cxx/'#发送curl命令返回值保存的文件路径
FILE_NAME = 'srs_data.flv'#发送curl命令返回值保存的文件名称
FILE_ID = '7A97F4F87C194894B1A149AF19F1AB60'#curl命令向srs服务器请求的文件的file_id
LOCALPATH = './lib/feature/srs_data_analyze/srs_data.flv'#将curl命令返回值生成的文件拷到本机使用的路径及文件名
NUM = 31#分析多少个srs返回数据
IP = '192.168.187.131'#发送curl命令的机器ip
USERNAME = 'cxx'#发送curl命令的机器的用户名
PASSWORD = 'cxx123'#发送curl命令的机器的密码