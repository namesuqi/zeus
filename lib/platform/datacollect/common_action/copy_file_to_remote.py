import os
import platform
from lib.platform.datacollect.global_vars.workpath import *
from lib.platform.datacollect.global_vars.constant import *
from sftp_client import *


def local_copy_file(file_name):
    local_sys = platform.system()
    if local_sys == "Windows":
        # old way to copy file
        # command = os.path.dirname(__file__) + r'/tools/pscp.exe -pw yzhxc9! ' \
        #     + os.path.dirname(__file__) + r'/../data_file/expect_data_file/%s.txt %s:%s/' \
        #                                   % (file_name, agent_account, agent_input_log_path)
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.upload(agent_input_log_path + r'/%s.txt' % file_name, os.path.dirname(__file__) +
                           r'/../data_file/expect_data_file/%s.txt'% file_name)
    elif local_sys == "Linux":
        # old way to copy file
        # command = 'scp ' + os.path.dirname(__file__) + r'/../data_file/expect_data_file/%s.txt %s:%s/' \
        #                                                % (file_name, agent_account, agent_input_log_path)
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.upload(agent_input_log_path + r'/%s.txt' % file_name, os.path.dirname(__file__) +
                           r'/../data_file/expect_data_file/%s.txt'% file_name)
    else:
        raise Exception("System nonsupport!")
    # print command
    # os.system(command)


def local_copy_execute_file():
    local_sys = platform.system()
    if local_sys == "Windows":
        # old way to copy execute file
        # command = os.path.dirname(__file__) + r'\tools\pscp.exe -pw yzhxc9! ' \
        #     + os.path.dirname(__file__) + r'/execute.py %s:%s/' % (agent_account, agent_input_log_path)
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.upload(agent_input_log_path + r'/execute.py', os.path.dirname(__file__) + r'/execute.py')
    elif local_sys == "Linux":
        # old way to copy execute file
        # command = 'scp ' + os.path.dirname(__file__) + r'/execute.py %s:%s/' % (agent_account, agent_input_log_path)
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.upload(agent_input_log_path + r'/execute.py', os.path.dirname(__file__) + r'/execute.py')
    else:
        raise Exception("System nonsupport!s")
    # print command
    # os.system(command)

if __name__ == '__main__':
    # local_copy_execute_file()
    local_copy_file('idc_peer_connection_report')
