# coding=utf-8
"""
Main script to run multi-peer on IDC machine
Enable multi-threading to improve performance.

how to use it:

python main.py start host.ini
python main.py restart host.ini
python main.py stop
python main.py p2p

python main.py restart jiluyou.ini

"""

import paramiko
import threading
import time
import inspect
import ConfigParser
import os
import sys
import requests
import json

# for yunshang IDC, set it to true
# for yunduan IDC, set it to false
SCP_COPY = False

REQUEST_TIMEOUT = 5
STREAM_TARGET = 32
THREAD_INTERVAL = 0.2  # seconds

file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
parent_path = os.path.dirname(file_path)

REMOTE_SDK_PATH = '/home/admin/live'
REMOTE_PLAYER_PATH = '/home/admin/player'
SDK_FILE = 'liveclient_static'
INI_FILE = 'host.ini'
REMOTE_SDK_FILE = '{0}/{1}'.format(REMOTE_SDK_PATH, SDK_FILE)

SDK_PORT_START = 60000
SDK_PORT_STEP = 10
SSH_PORT = 22
USERNAME = "admin"
PASSWORD = "yzhxc9!"

SDK_IP_LIST = []
SDK_NUM_LIST = []
SDK_USER_NAME_LIST = []
SDK_PASSWORD_LIST = []
CHANNEL_URL_LIST = []

SDK_FILE_PATH = "{0}/{1}".format(parent_path, SDK_FILE)
INI_FILE_PATH = "{0}/{1}".format(parent_path, INI_FILE)

USE_LF_PREFIX = ""
# USE_LF_PREFIX = " -x 00010047 "

# USER_PREFIX = ""
USER_PREFIX = " -u 2 "


def send_request(host_ip, host_port, url):
    url = "http://{0}:{1}{2}".format(host_ip, host_port, url)

    headers = dict()
    headers["accept"] = 'application/json'
    # if "60000" in url:
    #     print url

    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    return resp


def get_cid_data(host_ip, host_port):
    global cid_dict
    key = "{0}:{1}".format(host_ip, host_port)
    try:
        res = send_request(host_ip, host_port, "/ajax/scheduler")

        reading_cid = JsonParser.get_data_by_path(json.loads(res.content), "/0/reading_cid")
        # print reading_cid

        old_cid = cid_dict.get(key, None)

        if mutex.acquire(1):
            # if current == old, cid has problem
            if old_cid == reading_cid:
                bad_cid_list.append(key)
            cid_dict[key] = reading_cid  # save current cid

            mutex.release()
    except Exception as e:
        # print e
        if mutex.acquire(1):
            cid_dict[key] = None
            mutex.release()


def get_sdk_data(host_ip, host_port):
    global cid_dict
    try:
        res = send_request(host_ip, host_port, "/ajax/report")
        p2p_percent = json.loads(res.content).get("p2p_percent", None)
        seed_num = json.loads(res.content).get("seed_num", None)
        stream_num = json.loads(res.content).get("stream_num", None)
        download_rate = json.loads(res.content).get("download_rate", None)

        if mutex.acquire(1):
            p2p_list.append(p2p_percent)
            seed_num_list.append(seed_num)
            stream_num_list.append(stream_num)
            download_rate_list.append(download_rate)
            if stream_num < STREAM_TARGET:
                bad_stream_list.append("{0}:{1}".format(host_ip, host_port))

            mutex.release()
    except Exception as e:
        if mutex.acquire(1):
            p2p_list.append(0)
            seed_num_list.append(0)
            stream_num_list.append(0)
            download_rate_list.append(0)
            bad_p2p_list.append("{0}:{1}".format(host_ip, host_port))
            bad_stream_list.append("{0}:{1}".format(host_ip, host_port))
            mutex.release()


def collect_p2p_test():
    while True:
        try:
            t1 = time.time()
            # print dash_board_port_list

            global p2p_list, bad_p2p_list, seed_num_list, stream_num_list, bad_stream_list, download_rate_list, bad_cid_list
            p2p_list = []
            bad_p2p_list = []
            seed_num_list = []
            stream_num_list = []
            bad_stream_list = []
            download_rate_list = []
            bad_cid_list = []

            print SDK_IP_LIST
            for index, ip in enumerate(SDK_IP_LIST):
                # print "start collect p2p for {0}".format(ip)
                # time.sleep(0.1)  # wait some time to start huge threads
                sdk_num = SDK_NUM_LIST[index]
                dash_board_port_list = []
                for i in range(sdk_num):
                    dash_board_port_list.append(SDK_PORT_START + i * SDK_PORT_STEP)
                # print dash_board_port_list

                for port in dash_board_port_list:
                    t = threading.Thread(target=get_sdk_data, args=(ip, port))
                    t.start()
                    # t = threading.Thread(target=get_cid_data, args=(ip, port))
                    # t.start()
            main_thread = threading.currentThread()
            for t in threading.enumerate():
                if t is not main_thread:
                    t.join()

            t2 = time.time()
            zero_list = [x for x in p2p_list if x == 0]
            non_zero_list = [x for x in p2p_list if x != 0]
            current = time.localtime()
            time_str = time.strftime("%Y/%m/%d %H:%M:%S", current)
            bad_p2p_list.sort()
            bad_stream_list.sort()

            print
            print "============================================= {0} cost {1} seconds to get result =============================================".format(
                time_str, t2 - t1)
            print "IP number is: ", len(SDK_IP_LIST), SDK_IP_LIST
            print "SDK number is: {0}".format(len(p2p_list))
            print "------------------------------------------"
            # print "P2P List", p2p_list
            print "          All sdk average p2p is: {0}%".format(sum(p2p_list) / len(p2p_list))
            print "          Alive sdk average p2p is: {0}%".format(sum(non_zero_list) / len(non_zero_list))
            print "          Max p2p is {0}%, Min p2p is {1}%".format(max(non_zero_list), min(non_zero_list))
            print "          {0} SDKs with p2p >= 80%".format(len([i for i in non_zero_list if i >= 80]))
            print "          {1}{0} SDKs with p2p 0%{1}".format(len(zero_list),
                                                                "  @@@@@@@@@@@@  " if len(zero_list) > 0 else "")
            print "          P2P 0 sdk info: ", bad_p2p_list
            print "------------------------------------------"
            # print "Seed List", seed_num_list
            print "{0} SDKs with seed < 32".format(len([i for i in seed_num_list if i < 32]))
            print "------------------------------------------"
            # print "Stream List", stream_num_list
            print "{0} SDKs with stream >= 32".format(len([i for i in stream_num_list if i >= 32]))
            print "{0} SDKs with stream < 32".format(len([i for i in stream_num_list if i < 32]))
            # print "Stream < 32 sdk info: ",  bad_stream_list
            print "------------------------------------------"
            # print "Download List", download_rate_list
            print "All sdk average download rate {0}".format(sum(download_rate_list) / len(download_rate_list))
            print "Alive sdk average download rate {0}".format(sum(download_rate_list) / len(non_zero_list))
            print "SDK reading cid has problem ", len(bad_cid_list), bad_cid_list
            print "=============================================================================================================================="
        except Exception as e:
            # print e
            pass

        time.sleep(15)


class JsonParser(object):
    @staticmethod
    def get_data_by_path(data, path):
        # if start with /，remove /
        if path.startswith("/"):
            path = path[1:]
        key_list = path.split("/")
        num_list = [str(x) for x in range(100)]  # import to support index more than 10

        try:
            for key in key_list:
                if key in num_list:  # for number array
                    index = int(key)
                    data = data[index]
                else:  # for key
                    data = data.get(key)
        except:
            data = None

        return data


class RemoteNode(object):
    def __init__(self, ip, sdk_nums, url, local_sdk, username, password):
        self.local_sdk = local_sdk
        self.sdk_nums = sdk_nums
        self.ip = ip
        self.url = url
        self.username = username
        self.password = password
        print [username, password]

    def stop_play(self):
        print "Stop play for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 python")
        ssh.close()

    def remove_files(self):
        print "remove files for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("rm -rf {0}".format(REMOTE_SDK_PATH))
        time.sleep(1)
        ssh.exec_command("rm -rf {0}".format(REMOTE_PLAYER_PATH))
        ssh.close()

    def remove_core_dump(self, path=REMOTE_SDK_PATH):
        # start sdk on remote machines and remove folder
        print "Search core dump for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        # remove files
        find_command = "find {0} -name core.* ".format(path) + " -exec rm -f {} \;"
        # find_command = "find {0} -name core.* ".format(path)
        print find_command
        std_in, std_out, std_err = ssh.exec_command(find_command)
        output = std_out.read()
        print output
        ssh.close()

    def stop_sdk(self):
        # start sdk on remote machines and remove folder
        print "Stop sdk for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 {0}".format(SDK_FILE))
        ssh.close()

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
            print command
            time.sleep(0.5)
            ssh.exec_command(command)
        ssh.close()

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
            time.sleep(0.5)
            p2pclient = "ulimit -c 2000000 && cd {0}/{1} && nohup ./{2}".format(REMOTE_SDK_PATH, i, SDK_FILE)
            command = "{0} -p {1} {2} {3} > /dev/null 2>&1 &".format(p2pclient, port, USE_LF_PREFIX, USER_PREFIX)
            print "Command is: " + command
            ssh.exec_command(command)
        ssh.close()

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

    def deploy_sdk(self):
        # delete sdk on remote machines
        print "Start Clean for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        ssh.exec_command("killall -9 {0}".format(SDK_FILE))
        time.sleep(1)
        ssh.exec_command("rm -rf {0}/".format(REMOTE_SDK_PATH))
        ssh.exec_command("rm -rf {0}".format(REMOTE_SDK_PATH))
        time.sleep(0.5)
        ssh.exec_command("mkdir -p {0}".format(REMOTE_SDK_PATH))
        time.sleep(0.5)
        ssh.close()

        deployer = RemoteDeployer(self.ip, self.username, self.password)
        if SCP_COPY:
            deployer.copy_via_scp(self.local_sdk, REMOTE_SDK_PATH)
        else:
            deployer.copy_via_paramiko(self.local_sdk, REMOTE_SDK_FILE)

    def done(self):
        # delete sdk on remote machines
        print "Stop sdk and stop play for {0}".format(self.ip)
        command = 'sshpass -p {0} ssh -o StrictHostKeyChecking=no {1}@${2} "killall -9 liveclient_static"'.format(
            self.password, self.username, self.ip)
        print command
        os.system(command)




    def deploy_player(self):
        # delete sdk on remote machines
        print "Start deploy player for {0}".format(self.ip)
        deployer = RemoteDeployer(self.ip, self.username, self.password)
        deployer.deploy_folder(parent_path, REMOTE_PLAYER_PATH, "python")

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

        print "Host Memory usage: "
        memory_command = "free"
        std_in_mem, std_out_mem, std_err_mem = ssh.exec_command(memory_command)
        print std_out_mem.read()

        print "Python player number:"
        python_command = "ps aux|grep live|grep play.py|wc"
        std_in_py, std_out_py, std_err_py = ssh.exec_command(python_command)
        print std_out_py.read()

        ssh.close()
        return len(output.split())


class RemoteDeployer(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        print [username, password]

    def deploy_folder(self, local_dir, remote_dir, kill_proc=None):
        # delete files on remote machines
        print "Start Clean for {0}".format(self.ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, SSH_PORT, self.username, self.password)
        if kill_proc is not None:
            ssh.exec_command("killall -9 {0}".format(kill_proc))
            print "kill process {0}".format(kill_proc)
        ssh.exec_command("rm -rf {0}".format(remote_dir))
        ssh.exec_command("mkdir -p {0}".format(remote_dir))
        ssh.close()

        if SCP_COPY:
            self.copy_via_scp(local_dir, remote_dir)
        else:
            self.copy_via_paramiko(local_dir, remote_dir)

    def copy_via_paramiko(self, local_path, remote_path):
        t = paramiko.Transport(self.ip, SSH_PORT)
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print local_path
        print remote_path
        if remote_path == REMOTE_PLAYER_PATH:
            sftp.put(local_path + "/main.py", remote_path + "/main.py")
            sftp.put(local_path + "/play.py", remote_path + "/play.py")
            sftp.put(local_path + "/flv_parse.py", remote_path + "/flv_parse.py")
        else:
            sftp.put(local_path, remote_path)

        t.close()

    def copy_via_scp(self, local_path, remote_path):
        if SDK_FILE in local_path:
            command = 'scp -r {0} {1}@{2}:{3}'.format(local_path, self.username, self.ip, remote_path)
        else:
            command = 'scp -r {0}/* {1}@{2}:{3}'.format(local_path, self.username, self.ip, remote_path)
        print "Start Deploy SDK for {0}".format(self.ip)
        print command
        os.system(command)
        print "End Deploy SDK for {0}".format(self.ip)


class Tester(object):
    """
    test helper class
    """

    @staticmethod
    def start_play_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=start_play_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def start_sdk_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=start_sdk_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def restart_play_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=restart_play_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def restart_sdk_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=restart_sdk_thread, args=(i,))
            t.start()
            print "Thread name is", t.getName()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def stop_play_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=stop_play_thread, args=(i,))
            t.start()
            print "Thread name is", t.getName()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def stop_sdk_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=stop_sdk_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def done_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=done_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def clean_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}, {1}".format(i + 1, SDK_IP_LIST[i])
            t = threading.Thread(target=clean_thread, args=(i,))
            t.start()
            time.sleep(THREAD_INTERVAL)

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def core_test():
        while True:
            try:
                core_dump_num = 0
                for i in range(len(SDK_IP_LIST)):
                    print "-----------------------------------------"
                    print "Start for host {0}".format(i + 1)
                    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                                      SDK_USER_NAME_LIST[i],
                                      SDK_PASSWORD_LIST[i])
                    core_dump_num += node.find_core_dump()
                print "*********************************************"
                print "********************************************* Find {0} core dump files".format(core_dump_num)
                print "*********************************************"
            except:
                pass
            time.sleep(10)

    @staticmethod
    def remove_core_test():
        for i in range(len(SDK_IP_LIST)):
            print "---------------------------------------------------------------------------------------------------"
            print "Start for host {0}".format(i + 1)
            t = threading.Thread(target=remove_core_thread, args=(i,))
            t.start()

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

    @staticmethod
    def print_help():
        print "Please use control type: [start] or [stop] or [restart]"


def start_play_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH, SDK_USER_NAME_LIST[i],
                      SDK_PASSWORD_LIST[i])
    node.stop_play()
    node.deploy_player()
    node.stop_sdk()
    node.deploy_sdk()
    node.start_sdk()
    node.start_play()


def start_sdk_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
    node.stop_sdk()
    node.deploy_sdk()
    node.start_sdk()


def restart_play_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH, SDK_USER_NAME_LIST[i],
                      SDK_PASSWORD_LIST[i])
    node.stop_play()
    node.stop_sdk()
    node.restart_sdk()
    node.start_play()


def restart_sdk_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
    node.stop_sdk()
    node.start_sdk()


def stop_play_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
    node.stop_play()
    node.stop_sdk()


def stop_sdk_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i], SDK_PASSWORD_LIST[i])
    node.stop_sdk()


def clean_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i],
                      SDK_PASSWORD_LIST[i])
    node.remove_files()

def done_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i],
                      SDK_PASSWORD_LIST[i])
    node.done()


def remove_core_thread(i):
    node = RemoteNode(SDK_IP_LIST[i], SDK_NUM_LIST[i], CHANNEL_URL_LIST[i], SDK_FILE_PATH,
                      SDK_USER_NAME_LIST[i],
                      SDK_PASSWORD_LIST[i])
    node.remove_core_dump()


def read_ini():
    config = ConfigParser.ConfigParser()
    config.readfp(open(INI_FILE_PATH))
    section_list = config.sections()
    for i in section_list:
        if config.has_section(i):
            SDK_IP_LIST.append(config.get(i, "IP"))
            SDK_USER_NAME_LIST.append(config.get(i, "Username"))
            SDK_PASSWORD_LIST.append(config.get(i, "Password"))
            SDK_NUM_LIST.append(int(config.get(i, "SDK_Number")))
            CHANNEL_URL_LIST.append(config.get(i, "Channel_URL"))
        else:
            break

            # print SDK_IP_LIST
            # print SDK_USER_NAME_LIST
            # print SDK_PASSWORD_LIST
            # print SDK_NUM_LIST
            # print CHANNEL_URL_LIST


###############################
# Main Function
###############################
if __name__ == "__main__":
    mutex = threading.Lock()
    p2p_list = []
    bad_p2p_list = []
    seed_num_list = []
    stream_num_list = []
    bad_stream_list = []
    download_rate_list = []
    bad_cid_list = []
    cid_dict = dict()

    time1 = time.time()
    tester = Tester()

    if len(sys.argv) < 2:
        tester.print_help()
    else:
        if len(sys.argv) == 3:
            INI_FILE = sys.argv[2]

        else:
            INI_FILE = "host.ini"
        INI_FILE_PATH = "{0}/{1}".format(parent_path, INI_FILE)

        read_ini()
        if sys.argv[1] == "start":
            tester.start_play_test()
        elif sys.argv[1] == "restart":
            tester.restart_play_test()
        elif sys.argv[1] == "stop":  # stop sdk, stop play
            tester.stop_play_test()
        elif sys.argv[1] == "start_sdk":  # only deploy and start sdk
            tester.start_sdk_test()
        elif sys.argv[1] == "restart_sdk":  # only stop, start sdk
            tester.restart_sdk_test()
        elif sys.argv[1] == "stop_sdk":  # only stop sdk
            tester.stop_sdk_test()
        elif sys.argv[1] == "clean":  # delete live and player files
            tester.clean_test()
        elif sys.argv[1] == "core":  # find core dump file for sdk
            tester.core_test()
        elif sys.argv[1] == "remove_core":  # find core dump file for sdk
            tester.remove_core_test()
        elif sys.argv[1] == "p2p":  # collect p2p data for sdks
            collect_p2p_test()
        elif sys.argv[1] == "done":  # collect p2p data for sdks
            tester.done_test()
        else:
            tester.print_help()

    time2 = time.time()
    print "********** Cost {0} seconds **********".format(time2 - time1)
