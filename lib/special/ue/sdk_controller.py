# coding=utf-8
# author = zengyuetian

from lib.special.ue.const import *
from lib.remote.remoter import *
from lib.special.ue.player_controller import *
import requests
import json


@log_func_args
def deploy_sdk(ip):
    # kill previous processes
    kill_cmd = "killall -9 {0}".format(SDK_FILE)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, kill_cmd)

    # create sdk dir
    mkdir_cmd = "mkdir -p {0}".format(REMOTE_SDK_PATH)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, mkdir_cmd)

    # copy file to remote sdk dir
    copy_file_to(ip, ROOT_USER, ROOT_PASSWD, LOCAL_SDK, REMOTE_SDK)

    # make sdk executable
    chmod_cmd = "chmod +x {0}".format(REMOTE_SDK)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, chmod_cmd)


@log_func_args
def start_sdk(ip, port=SDK_PORT):
    p2pclient = "ulimit -c 2000000 && cd {0} && nohup ./{1}".format(REMOTE_SDK_PATH, SDK_FILE)
    cmd = "{0} -p {1}  > /dev/null 2>&1 &".format(p2pclient, port)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)


@log_func_args
def stop_sdk(ip):
    kill_cmd = "killall -9 {0}".format(SDK_FILE)
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, kill_cmd)


@log_func_args
def get_sdk_version(ip, port=SDK_PORT):
    # try:
    #     url = "http://{0}:{1}{2}".format(ip, port, "/ajax/version")
    #     headers = dict()
    #     headers["accept"] = 'application/json'
    #     print url
    #
    #     res = requests.get(url, headers=headers, timeout=10)
    #     return json.loads(res.content).get("core", None)
    # except:
    #     return 0

    cmd = "curl http://{0}:{1}{2}".format(ip, port, "/ajax/version")
    result = remote_execute_result(ip, ROOT_USER, ROOT_PASSWD, cmd)
    return json.loads(result).get("core", None)


@log_func_args
def back_up_log(ip, time_stamp):
    cmd = "cp /root/ue/sdk/yunshang/yunshang.log /root/ue/sdk_log/yunshang_%s.log" % time_stamp
    remote_execute(ip, ROOT_USER, ROOT_PASSWD, cmd)


@log_func_args
def deploy_lf(ip, lf_num):
    # kill previous processes
    kill_cmd = "killall -9 {0}".format(SDK_FILE)
    remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, kill_cmd)

    # create sdk dir
    mkdir_cmd = "mkdir -p {0}".format(LF_DEPLOY_SDK_PATH)
    remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, mkdir_cmd)

    copy_file_to(ip, ADMIN_USER, ADMIN_PASSWD, LOCAL_SDK, LF_SDK)

    chmod_cmd = "chmod +x {0}".format(LF_SDK)
    remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, chmod_cmd)

    for i in range(lf_num):
        cmd = "cp -R {0} {1}/lf_{2}".format(LF_DEPLOY_SDK_PATH, LF_DEPLOY_PATH, i)
        remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, cmd)


@log_func_args
def deploy_lf_clean(ip):

    cmd1 = "rm -rf {0}/*".format(LF_DEPLOY_SDK_PATH)
    remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, cmd1)

    remove_lf_cmd = "rm -rf {0}/lf_*".format(LF_DEPLOY_PATH)
    remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, remove_lf_cmd)


def start_lf_sdk(ip, lf_num, port):

    count = 0
    for i in range(lf_num):
        lf_path = LF_DEPLOY_PATH + "/lf_{0}".format(i)
        p2p_client = "ulimit -c 2000000 && cd {0} && nohup ./{1}".format(lf_path, SDK_FILE)
        cmd = "{0} -p {1}  > /dev/null 2>&1 &".format(p2p_client, port + count)
        remote_execute(ip, ADMIN_USER, ADMIN_PASSWD, cmd)
        count += 3
