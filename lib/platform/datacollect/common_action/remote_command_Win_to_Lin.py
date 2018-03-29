import os
import platform
from lib.platform.datacollect.global_vars.workpath import *
from lib.platform.datacollect.global_vars.constant import *
from ssh_client import *


def execute_command(command):
    os.system(command)


def start_write_log(file_name):
    ssh_client = SSHClient(agent_ip, agent_user, agent_pwd)
    ssh_client.execute_command("python %s/execute.py %s/%s" % (agent_input_log_path, agent_input_log_path, file_name))

if __name__ == '__main__':
    start_write_log('server_peer_info')
