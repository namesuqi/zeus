# coding=utf-8
"""
Main script to run multi-peer on IDC machine

"""

import paramiko
import time
import inspect
import ConfigParser
import os
import sys
import json
import requests
import tarfile
import commands
import re
from lib.utility.path import *
from lib.decorator.trace import *
from lib.decorator.log import *

file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
parent_path = os.path.dirname(file_path)
root_path = PathController.get_root_path()


REMOTE_SDK_PATH = '/home/admin/live'
REMOTE_PLAYER_PATH = '/home/admin/player'
SDK_FILE = 'liveclient_static'
REMOTE_SDK_FILE = '{0}/{1}'.format(REMOTE_SDK_PATH, SDK_FILE)   # /home/admin/live/liveclient_static

SDK_PORT_START = 60000
SDK_PORT_STEP = 10
SSH_PORT = 22
SCP_COPY = False
USERNAME = "admin"
PASSWORD = "yzhxc9!"

SDK_IP_LIST = []
SDK_NUM_LIST = []
SDK_USER_NAME_LIST = []
SDK_PASSWORD_LIST = []
CHANNEL_URL_LIST = []

LF_IP_LIST = []
LF_NUM_LIST = []
LF_USER_NAME_LIST = []
LF_PASSWORD_LIST = []
LF_CHANNEL_URL_LIST = []

SDK_FILE_PATH = "{0}/{1}".format(parent_path, SDK_FILE)

USE_LF_PREFIX = ""
USER_PREFIX = " -u 2 "


class RemoteNode(object):
    def __init__(self, ip, sdk_nums, url, local_sdk, username, password):
        self.local_sdk = local_sdk
        self.sdk_nums = sdk_nums
        self.ip = ip
        self.url = url
        self.username = username
        self.password = password
        print [username, password]

    @print_trace
    @log_func_args
    def stop_play(self):
        print "Stop play for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 python")
        ssh.close()

    @print_trace
    @log_func_args
    def start_play(self):
        # start sdk on remote machines and remove folder
        print "Start play for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        for i in range(self.sdk_nums):
            port = i * SDK_PORT_STEP + SDK_PORT_START
            url = "http://127.0.0.1:{0}/{1}".format(port, self.url)
            command = "nohup python {0}/play.py {1} > /dev/null 2>&1 &".format(REMOTE_PLAYER_PATH, url)
            # command = "nohup python {0}/remote/play.py {1} > /dev/null 2>&1 &".format(REMOTE_PLAYER_PATH, url)
            print command
            time.sleep(2)
            ssh.exec_command(command)
        ssh.close()

    @print_trace
    @log_func_args
    def remove_files(self):
        print "remove files for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("rm -rf {0}".format(REMOTE_SDK_PATH))
        time.sleep(1)
        ssh.exec_command("rm -rf {0}".format(REMOTE_PLAYER_PATH))
        ssh.close()

    @print_trace
    @log_func_args
    def stop_sdk(self):
        # start sdk on remote machines and remove folder
        print "Stop sdk for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 {0}".format(SDK_FILE))
        ssh.close()

    @print_trace
    @log_func_args
    def start_sdk(self):
        # start sdk on remote machines and remove folder
        print "Start SDK for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("chmod +x {0}".format(REMOTE_SDK_FILE))
        for i in range(self.sdk_nums):
            port = i * SDK_PORT_STEP + SDK_PORT_START
            print "Start SDK for port {0}".format(port)
            ssh.exec_command("mkdir -p {0}/{1}".format(REMOTE_SDK_PATH, i))
            ssh.exec_command("cp {0} {1}/{2}/{3}".format(REMOTE_SDK_FILE, REMOTE_SDK_PATH, i, SDK_FILE))
            time.sleep(0.1)
            p2pclient = "ulimit -c 2000000 && cd {0}/{1} && nohup ./{2}".format(REMOTE_SDK_PATH, i, SDK_FILE)
            command = "{0} -p {1} {2} {3} > /dev/null 2>&1 &".format(p2pclient, port, USE_LF_PREFIX, USER_PREFIX)
            print "Command is: " + command
            ssh.exec_command(command)
        ssh.close()

    @print_trace
    @log_func_args
    def restart_sdk(self):
        # restart sdk on remote machines
        print "Start SDK for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("chmod +x {0}".format(REMOTE_SDK_FILE))
        for i in range(self.sdk_nums):
            port = i * SDK_PORT_STEP + SDK_PORT_START
            print "Restart SDK for port {0}".format(port)
            p2p_client = "ulimit -c 2000000 && cd {0}/{1} && nohup ./{2}".format(REMOTE_SDK_PATH, i, SDK_FILE)
            command = "{0} -p {1} {2} {3}> /dev/null 2>&1 &".format(p2p_client, port, USE_LF_PREFIX, USER_PREFIX)
            print "Command is: " + command
            ssh.exec_command(command)
        ssh.close()

    @print_trace
    @log_func_args
    def deploy_sdk(self):
        """
        mkdir in remote IDC machine.
        :return:
        """
        # delete sdk on remote machines
        print "Start Clean for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 {0}".format(SDK_FILE))
        time.sleep(2)
        ssh.exec_command("rm -rf {0} \n mkdir -p {1}".format(REMOTE_SDK_PATH, REMOTE_SDK_PATH))
        #time.sleep(2)
        #.exec_command("mkdir -p {0}".format(REMOTE_SDK_PATH))
        # ssh.exec_command("rm -rf {0}".format(REMOTE_SDK_PATH))
        time.sleep(1)
        ssh.close()

        # rsync_command = "rsync -avzP --delete  {0} {1}@{2}:{3}".format(self.local_sdk, self.username,
        #                                                                self.ip, REMOTE_SDK_PATH+"/liveclient_static")
        # print rsync_command
        # os.system(rsync_command)

        deployer = RemoteDeployer(self.ip, self.username, self.password)
        if SCP_COPY:
            deployer.copy_via_scp(self.local_sdk, REMOTE_SDK_PATH)
        else:
            deployer.copy_via_paramiko(self.local_sdk, REMOTE_SDK_FILE)

    @print_trace
    @log_func_args
    def deploy_player(self):
        # delete sdk on remote machines
        print "Start deploy player for {0}".format(self.ip)
        deployer = RemoteDeployer(self.ip, self.username, self.password)
        print "parent_path:", parent_path, "REMOTE_PLAYER_PATH:", REMOTE_PLAYER_PATH, "file_path:", file_path
        deployer.deploy_folder(parent_path, REMOTE_PLAYER_PATH, "python")

    @print_trace
    def find_core_dump(self, path=REMOTE_SDK_PATH):
        # start sdk on remote machines and remove folder
        print "Find core dump for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        # show timestamp for core dump files
        # find_command = "find {0} -name core.* ".format(path) + " -exec ls -l {} \;"
        find_command = "find {0} -name core.* ".format(path)
        # print find_command
        std_in, std_out, std_err = ssh.exec_command(find_command)
        output = std_out.read()
        print output
        ssh.close()
        return len(output.split())

    @print_trace
    def check_process(self, option):
        # check lf or peer sdk process
        print "check process for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        check_sdk_command = "ps aux | grep liveclient_static | wc"
        std_in, std_out, std_err = ssh.exec_command(check_sdk_command)
        sdk_process_number = std_out.read()
        pattern = "[0-9]+"
        match = re.search(pattern, sdk_process_number, flags=0)
        sdk_process_number = int(match.group())

        print sdk_process_number
        if "PEER" in option:
            check_python_commad = "ps aux | grep play.py | wc"
            std_in, std_out, std_err = ssh.exec_command(check_python_commad)
            python_process_number = std_out.read()
            match = re.search(pattern, python_process_number, flags=0)
            python_process_number = int(match.group())
        else:
            python_process_number = 0

        print "option:{0}".format(option)
        print "sdk_process_number:", sdk_process_number, "python_process_number:", python_process_number
        return sdk_process_number, python_process_number

    @print_trace
    def get_p2p_percent(self, port):
        try:
            url = "http://{0}:{1}{2}".format(self.ip, port, "/ajax/report")
            headers = dict()
            headers["accept"] = 'application/json'
            print url

            res = requests.get(url, headers=headers, timeout=3)
            return json.loads(res.content).get("p2p_percent", None)
        except:
            return 0

    @print_trace
    def check_md5(self):
        # delete files on remote machines
        print "Start Clean for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        std_in, std_out, std_err = ssh.exec_command("md5sum {0}".format(REMOTE_SDK_FILE))
        md5_str = std_out.read().split(" ")
        md5 = md5_str[0]
        ssh.close()
        return md5


class RemoteDeployer(object):
    @print_trace
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        print [username, password]

    @print_trace
    @log_func_args
    def deploy_folder(self, local_dir, remote_dir, kill_proc=None):
        # delete files on remote machines
        print "Start Clean for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        if kill_proc is not None:
            ssh.exec_command("killall -9 {0}".format(kill_proc))
            print "kill process {0}".format(kill_proc)
        print "rm -rf {0}".format(remote_dir)
        ssh.exec_command("rm -rf {0} \n mkdir {1}".format(remote_dir, remote_dir))
        # ssh.exec_command("mkdir {0}".format(remote_dir))
        ssh.close()

        # rsync_command = "rsync -avzP --delete  {0} {1}@{2}:{3}".format(local_dir, self.username,
        #                                                                self.ip, remote_dir)
        # print rsync_command
        # os.system(rsync_command)

        if SCP_COPY:
            self.copy_via_scp(local_dir, remote_dir)
        else:
            self.copy_via_paramiko(local_dir, remote_dir)

    @print_trace
    @log_func_args
    def copy_via_paramiko(self, local_path, remote_path):
        t = paramiko.Transport(self.ip, SSH_PORT)
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print "local_path:{0}".format(local_path)
        print "remote_path:{0}".format(remote_path)
        if remote_path == REMOTE_PLAYER_PATH:
            sftp.put(local_path+"/play.py", remote_path+"/play.py")
            sftp.put(local_path+"/flv_parse.py", remote_path+"/flv_parse.py")
        else:
            sftp.put(local_path, remote_path)

        t.close()

    @print_trace
    @log_func_args
    def copy_via_scp(self, local_path, remote_path):
        # if "live" in remote_path:
        #     remote_path += "/liveclient_static"
        #     command = 'scp {0} {1}@{2}:{3}'.format(local_path, self.username, self.ip, remote_path)
        # else:
        # command = 'scp -rv {0} {1}@{2}:{3}'.format(local_path, self.username, self.ip, remote_path)
        command = 'scp -rv {0} {1}@{2}:{3}'.format(local_path, self.username, self.ip, remote_path)

        # search_command = "ls -l {0}".format(local_path)
        # print search_command
        # status, text = commands.getstatusoutput(search_command)
        # output = stdout.read()
        # print "file_exists: {0}".format(text)

        if remote_path in REMOTE_PLAYER_PATH:
            print "Start Deploy Player for {0}".format(self.ip)
        else:
            print "Start Deploy SDK for {0}".format(self.ip)
        print "remote_path:", remote_path
        print "command:{0}".format(command)
        os.system(command)
        print "End Deploy for {0}".format(self.ip)


class Tester(object):
    @print_trace
    @log_func_args
    def start_play_test(self):
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i+1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH, SDK_USER_NAME_LIST[i],
                              SDK_PASSWORD_LIST[i])
            node.stop_play()

            node.stop_sdk()

            node.deploy_sdk()

            node.deploy_player()

            node.start_sdk()
            time.sleep(10)
            node.start_play()

    @print_trace
    @log_func_args
    def start_sdk_test(self, option):
        if "LF" == option:
            for i in range(len(LF_IP_LIST)):
                print "------------------------------------------------------------------------------------------------"
                print "Start for host {0}".format(i + 1)
                node = RemoteNode(LF_IP_LIST[i], LF_NUM_LIST[i], LF_CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                                  LF_USER_NAME_LIST[i], LF_PASSWORD_LIST[i])
                node.stop_sdk()
                node.deploy_sdk()
                node.start_sdk()
        else:
            for i in range(len(SDK_IP_LIST)):
                print "------------------------------------------------------------------------------------------------"
                print "Start for host {0}".format(i + 1)
                node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                                  SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
                node.stop_sdk()
                node.deploy_sdk()
                node.start_sdk()

    @print_trace
    @log_func_args
    def restart_play_test(self):
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH, SDK_USER_NAME_LIST[i],
                              SDK_PASSWORD_LIST[i])
            node.stop_play()
            node.stop_sdk()
            node.restart_sdk()
            node.start_play()

    @print_trace
    @log_func_args
    def restart_sdk_test(self):
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
            node.stop_sdk()
            node.start_sdk()

    @print_trace
    @log_func_args
    def stop_play_test(self):
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
            node.stop_play()
            node.stop_sdk()

    @print_trace
    @log_func_args
    def stop_sdk_test(self, option):
        if "LF" == option:
            for i in range(len(LF_IP_LIST)):
                print "------------------------------------------------------------------------------------------------"
                print "Start for host {0}".format(i + 1)
                node = RemoteNode(LF_IP_LIST[i], LF_NUM_LIST[i], LF_CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                                  LF_USER_NAME_LIST[i], LF_PASSWORD_LIST[i])
                node.stop_sdk()
        else:
            for i in range(len(SDK_IP_LIST)):
                print "------------------------------------------------------------------------------------------------"
                print "Start for host {0}".format(i + 1)
                node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                                  SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
                node.stop_sdk()

    @print_trace
    @log_func_args
    def clean_test(self):
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
            node.remove_files()

    @print_trace
    @log_func_args
    def core_test(self):
        core_dump_num = 0
        for i in range(len(SDK_IP_LIST)):
            print "------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
            core_dump_num += node.find_core_dump()

        print "Find {0} core dump files".format(core_dump_num)
        time.sleep(10)

        return core_dump_num

    @print_trace
    @log_func_args
    def process_leifeng_test(self):
        status = True
        for i in range(len(LF_IP_LIST)):
            print "------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(LF_IP_LIST[i], LF_NUM_LIST[i], LF_CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              LF_USER_NAME_LIST[i], LF_PASSWORD_LIST[i])
            sdk_number, python_number = node.check_process("LF")
            if sdk_number != LF_NUM_LIST[i] * 2 + 2:
                status = False
                print "LF_SDK:{0} error".format(LF_IP_LIST[i])

        return status

    @print_trace
    @log_func_args
    def process_peer_test(self):
        peer_sdk_status = True
        peer_player_status = True
        for i in range(len(SDK_IP_LIST)):
            print "------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
            sdk_number, python_number = node.check_process("PEER")
            if sdk_number != SDK_NUM_LIST[i] * 2 + 2:
                peer_sdk_status = False
                print "Peer_SDK:{0} error".format(SDK_IP_LIST[i])
            if python_number != SDK_NUM_LIST[i] + 2:
                peer_player_status = False
                print "Peer_Player:{0} error".format(SDK_IP_LIST[i])

        return peer_sdk_status, peer_player_status

    @print_trace
    @log_func_args
    def check_p2p(self):
        result_list = {}
        for i in range(len(SDK_IP_LIST)):
            print "----------------------------------------------------------------------------------------------------"
            print "Start check p2p for peer_host {0}".format(i + 1)
            node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                              SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])

            for j in range(SDK_NUM_LIST[i]):
                port = SDK_PORT_START + j * SDK_PORT_STEP + 0
                p2p = node.get_p2p_percent(port)
                result_key = "{0}:{1}".format(SDK_IP_LIST[i], port)
                result_list[result_key] = int(p2p)

        return result_list

    @print_trace
    @log_func_args
    def check_sdk_file_md5(self):
        print "----------------------------------------------------------------------------------------------------"
        print "Start check sdk file md5 for peer_host"
        node = RemoteNode(SDK_IP_LIST[0], SDK_NUM_LIST[0], CHANNEL_URL_LIST[0], SDK_FILE_PATH,
                          SDK_USER_NAME_LIST[0], SDK_PASSWORD_LIST[0])
        md5_value = node.check_md5()

        return md5_value

    @print_trace
    def print_help(self):
        print "Please use control type: [start] or [stop] or [restart]"


@print_trace
def get_centos_sdk(file_name, des_dir):
    """
    used to get_cent_os_sdk
    :param file_name:
    :param des_dir:
    :return:
    """
    if "*.tar.gz" in file_name:
        file_handle = tarfile.open(file_name)
        file_handle.extractall(path=des_dir)
    elif "ys" in file_name:
        commands_string = "mv {0} {1}".format(file_name, "liveclient_static")
        status, text = commands.getstatusoutput(commands_string)
        if not status:
            return False

    return True


@print_trace
def init_leifeng_parameter(copy_method, lf_info, user=USERNAME):
    print "init some parameters:", user, copy_method
    root_path = PathController.get_root_path()
    global SCP_COPY, LF_IP_LIST, LF_NUM_LIST, LF_USER_NAME_LIST, LF_PASSWORD_LIST, LF_CHANNEL_URL_LIST, SDK_FILE_PATH
    if copy_method or copy_method == "True":
        SCP_COPY = True
    else:
        SCP_COPY = False
    SDK_FILE_PATH = "{0}/misc/bin/sdk/daily_system/liveclient_static".format(root_path)
    for i in lf_info:
        LF_IP_LIST.append(i.get("IP"))
        LF_NUM_LIST.append(i.get("SDK_Number"))
        LF_USER_NAME_LIST.append(i.get("Username"))
        LF_PASSWORD_LIST.append(i.get("Password"))
        LF_CHANNEL_URL_LIST.append(i.get("Channel_URL"))


@print_trace
def init_peer_parameter(copy_method, peer_info, user=USERNAME):
    print "init some parameters:", user, copy_method
    root_path = PathController.get_root_path()
    global SCP_COPY, LF_IP_LIST, LF_NUM_LIST, LF_USER_NAME_LIST, LF_PASSWORD_LIST, LF_CHANNEL_URL_LIST, SDK_FILE_PATH
    if copy_method or copy_method == "True":
        SCP_COPY = True
    else:
        SCP_COPY = False
    SDK_FILE_PATH = "{0}/misc/bin/sdk/daily_system/liveclient_static".format(root_path)
    for i in peer_info:
        SDK_IP_LIST.append(i.get("IP"))
        SDK_NUM_LIST.append(i.get("SDK_Number"))
        SDK_USER_NAME_LIST.append(i.get("Username"))
        SDK_PASSWORD_LIST.append(i.get("Password"))
        CHANNEL_URL_LIST.append(i.get("Channel_URL"))


@print_trace
def start_leifeng():
    """
    start_leifeng for the testsuite case

    :return:
    """
    time1 = time.time()
    tester = Tester()
    tester.start_sdk_test("LF")
    time2 = time.time()
    print "********** Cost {0} seconds **********".format(time2 - time1)
    return True


@print_trace
def check_leifeng_process(lf_info=None):
    get_lei_feng(lf_info)
    tester = Tester()
    return tester.process_leifeng_test()


@print_trace
def check_peer_process(peer_info=None):
    get_peer_info(peer_info)
    tester = Tester()
    sdk_status, player_status = tester.process_peer_test()
    if sdk_status and player_status:
        return True
    else:
        return False

@print_trace
def get_lei_feng(lf_info=None):
    if lf_info is not None and len(LF_IP_LIST) == 0:
        for i in lf_info:
            LF_IP_LIST.append(i.get("IP"))
            LF_NUM_LIST.append(i.get("SDK_Number"))
            LF_USER_NAME_LIST.append(i.get("Username"))
            LF_PASSWORD_LIST.append(i.get("Password"))
            LF_CHANNEL_URL_LIST.append(i.get("Channel_URL"))

@print_trace
def get_peer_info(peer_info=None):
    if peer_info is not None and len(SDK_IP_LIST) == 0:
        for i in peer_info:
            SDK_IP_LIST.append(i.get("IP"))
            SDK_NUM_LIST.append(i.get("SDK_Number"))
            SDK_USER_NAME_LIST.append(i.get("Username"))
            SDK_PASSWORD_LIST.append(i.get("Password"))
            CHANNEL_URL_LIST.append(i.get("Channel_URL"))


@print_trace
def start_play():
    # read_ini(PEER_INI_FILE_PATH)
    time1 = time.time()
    tester = Tester()
    tester.start_play_test()
    time2 = time.time()
    print "********** Cost {0} seconds **********".format(time2 - time1)
    return True

@print_trace
def check_md5_status(peer_info=None):
    root_path = PathController.get_root_path()
    command = "md5sum {0}/misc/bin/sdk/daily_system/liveclient_static".format(root_path)
    print command
    std_out = commands.getoutput(command)
    print std_out
    md5_str = std_out.split(" ")
    md5 = md5_str[0]
    get_peer_info(peer_info)
    tester = Tester()
    md5_peer = tester.check_sdk_file_md5()
    print "md5:{0} md5_peer:{1}".format(md5, md5_peer)
    if md5 != md5_peer:
        status = False
    else:
        status = True

    return status

@print_trace
def get_core_dump_number(peer_info=None):
    get_peer_info(peer_info)
    tester = Tester()
    core_dump_number = tester.core_test()
    return core_dump_number


@print_trace
def get_p2p_average_value(peer_info=None):
    get_peer_info(peer_info)
    time1 = time.time()
    tester = Tester()
    result_hash = tester.check_p2p()

    if len(result_hash) == 0:
        return 0

    print "***********************************************************"
    zero_list = [x for x in result_hash.values() if x == 0]
    non_zero_list = [x for x in result_hash.values() if x != 0]
    time2 = time.time()

    if len(non_zero_list) == 0:
        return 0

    print "Cost {0} seconds to collect result".format(time2 - time1)
    print "Total SDKs number is {0}".format(len(result_hash))
    print "Result List", result_hash
    print "Total average p2p percentage is: {0}%".format(sum(result_hash.values()) / len(result_hash))
    print "Alive average p2p percentage is: {0}%".format(sum(non_zero_list) / len(non_zero_list))
    print "Max p2p percentage is {0}%".format(max(non_zero_list))
    print "Min p2p percentage is {0}%".format(min(non_zero_list))
    print "{0} SDKs with p2p percentage 0%".format(len(zero_list))
    print "***********************************************************"

    live_p2p_percentage = sum(non_zero_list) / len(non_zero_list)
    return live_p2p_percentage

###############################
# Main Function
###############################
if __name__ == "__main__":
    time1 = time.time()
    tester = Tester()

    if len(sys.argv) != 2:
        tester.print_help()
    else:
        # read_ini(PEER_INI_FILE_PATH)
        if sys.argv[1] == "start":
            tester.start_play_test()
        elif sys.argv[1] == "restart":
            tester.restart_play_test()
        elif sys.argv[1] == "stop":    # stop sdk, stop play
            tester.stop_play_test()
        elif sys.argv[1] == "start_sdk":  # only deploy and start sdk
            tester.start_sdk_test("PEER")
        elif sys.argv[1] == "restart_sdk":  # only stop, start sdk
            tester.restart_sdk_test()
        elif sys.argv[1] == "stop_sdk":  # only stop sdk
            tester.stop_sdk_test("PEER")
        elif sys.argv[1] == "clean":   # delete live and player files
            tester.clean_test()
        elif sys.argv[1] == "core":  # find core dump file for sdk
            tester.core_test()
        else:
            tester.print_help()

    time2 = time.time()
    print "********** Cost {0} seconds **********".format(time2 - time1)
