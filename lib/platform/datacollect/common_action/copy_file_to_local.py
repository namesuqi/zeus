from read_file import *
import time
import platform
from lib.platform.datacollect.global_vars.workpath import *
from lib.platform.datacollect.global_vars.constant import *
from sftp_client import *


def remote_copy_file(local_file_name):
    local_sys = platform.system()
    if local_sys == "Windows":
        # old way to copy file
        # command = os.path.dirname(__file__) + r'\tools\pscp.exe -pw yzhxc9! ' \
        #           r'%s:%s/report.log ' % (agent_account, funnel_report_path) \
        #           + os.path.dirname(__file__) + r'\..\data_file\temp_file\report.log'
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.download(funnel_report_path + r'/report.log', os.path.dirname(__file__) +
                             r'\..\data_file\temp_file\report.log')

    elif local_sys == "Linux":
        # old way to copy file
        # command = r'scp %s:%s/report.log ' % (agent_account, funnel_report_path) \
        #           + os.path.dirname(__file__) + r'/../data_file/temp_file/report.log'
        sftp_client = SFTPClient(agent_ip, agent_user, agent_pwd)
        sftp_client.download(funnel_report_path + r'/report.log', os.path.dirname(__file__) +
                             r'/../data_file/temp_file/report.log')
    else:
        raise Exception("System nonsupport!")
    # print command
    # os.system(command)

    '''
    make new file save that data we need compare
    '''

    time.sleep(0.05)
    output_file_lines = read_temp_file('report.log')
    temp_list = output_file_lines[-post_log_number:]
    file_name = os.path.abspath(os.path.dirname(__file__)) + "/../data_file/real_data_file/%s.log" % local_file_name
    test_file = open(file_name, 'w')
    test_file.writelines(temp_list)
    test_file.close()


if __name__ == '__main__':
    remote_copy_file("localfilename")
