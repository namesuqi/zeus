import os

from lib.platform.dataprocess.spark_compute.commontool.get_data_from_hbase import GetDataFromHbase
from lib.platform.dataprocess.spark_compute.commontool.ssh_client import SSHClient
from lib.platform.dataprocess.spark_compute.commontool.sftp_client import SFTPClient
from lib.platform.dataprocess.spark_compute.test_data import *


def insert_datafile_to_hdfs(file_name):

    if os.path.isfile(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/' + file_name):
        sftp = SFTPClient(flume_ip, flume_username, flume_password)
        sftp.upload('/home/admin/TestInput/' + file_name,
                    os.path.abspath(os.path.dirname(__file__)) + '/../makedata/' + file_name)
        ssh = SSHClient(flume_ip, flume_username, flume_password)
        ssh.excute_command('cat /home/admin/TestInput/' + file_name + ' >> /home/admin/logs/funnel/report.log')
    else:
        raise Exception("data file %s is not created! please check it!" % file_name)

'''
    for robot framework call
'''


def excute_command(ip, username, password, command):
    ssh = SSHClient(ip, username, password)
    ssh.excute_command(command)

'''
    for robot framework call
'''


def get_data_from_hbase(query_statement, output_file_name):
    eg = GetDataFromHbase(hadoop_ip, hadoop_username, hadoop_password)
    eg.get_data_by_query(query_statement, output_file_name)
