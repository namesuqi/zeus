import os

from lib.platform.dataprocess.spark_compute.commontool.ssh_client import SSHClient
from lib.platform.dataprocess.spark_compute.commontool.sftp_client import SFTPClient


class GetDataFromHbase(object):

    def __init__(self, ip, username, password):
        self.__ssh = SSHClient(ip, username, password)
        self.__sftp = SFTPClient(ip, username, password)

    def get_data_by_query(self, query_statement, output_file_name):

        command = 'echo "{0}" | hbase shell > /root/Testdata/{1}'.format(query_statement, output_file_name)
        print command
        self.__ssh.excute_command(command)
        self.__sftp.download('/root/Testdata/%s' % output_file_name,
                             os.path.abspath(os.path.dirname(__file__)) + '/../realfile/%s' % output_file_name)


if __name__ == '__main__':
    eg = GetDataFromHbase('10.5.100.46', 'root', 'Yunshang2014')
    eg.get_data_by_query("scan 'output_buffering_ratio'", 'play_fluency.txt')
    # eg.get_data_by_query("scan 'output_five_minute_startup_delay'", 'five_minute_average_startup_delay.txt')
