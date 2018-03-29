# coding=utf-8
# author: zengyuetian
# start sdk and player on local machine to avoid paramiko max connection number limitation

import os
import time

SDK_FILE = 'liveclient_static'
SDK_PORT_STEP = 10
SDK_PORT_START = 50000

USE_LF_PREFIX = ""
# USE_LF_PREFIX = " -x 00010047 "

# USER_PREFIX = ""
USER_PREFIX = " -u 2 "

SDK_START = 1001
SDK_END = 1100


def stop_player():
    print "stop player"
    os.system(" ps aux | grep play.py |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9")


def stop_sdk():
    print "stop sdk"
    os.system("killall -9 liveclient_static")


def create_folder(start=0, end=1000):
    print "create_folder for {0} to {1}".format(start, end)
    os.system("chmod +x ./{0}".format(SDK_FILE))
    for i in range(start, end+1):
        os.system("rm -rf ./{0}".format(i))
        os.system("mkdir -p ./{0}".format(i))
        os.system("cp ./{0}  ./{1}/".format(SDK_FILE, i))


def start_sdk(start=0, end=1000):
    print "start sdk for {0} to {1}".format(start, end)
    for i in range(start, end+1):
        port = i * SDK_PORT_STEP + SDK_PORT_START
        p2pclient = "ulimit -c 2000000 && cd {0} && nohup ./{1}".format(i, SDK_FILE)
        cmd = "{0} -p {1} {2} {3} > /dev/null 2>&1 &".format(p2pclient, port, USE_LF_PREFIX, USER_PREFIX)
        print cmd
        os.system(cmd)
        time.sleep(0.1)


def start_player(start=0, end=1000):
    print "start player for {0} to {1}".format(start, end)
    for i in range(start, end + 1):

        # 单频道多节点的代码部分 ***
        # index = ""
        # port = i * SDK_PORT_STEP + SDK_PORT_START
        # url = "http://127.0.0.1:{0}/live_flv/user/wasu?url=http://flv{1}.srs.cloutropy.com/wasu/test{2}.flv" \
        #     .format(port, 1, index)

        # 多频道多节点的代码部分 ***
        index = i % 10
        if index == 0:
            index = ""
        port = i * SDK_PORT_STEP + SDK_PORT_START
        url = "http://127.0.0.1:{0}/live_flv/user/wasu?url=http://flv{1}.srs.cloutropy.com/wasu/test{2}.flv" \
            .format(port, i, index)




        cmd = "nohup python play.py {0} > /dev/null 2>&1 &".format(url)
        print cmd
        os.system(cmd)
        time.sleep(0.1)


if __name__ == "__main__":

    # stop play
    # stop_player()
    # time.sleep(1)
    #
    # # stop sdk
    # stop_sdk()
    # time.sleep(1)

    # create folders
    create_folder(SDK_START, SDK_END)
    time.sleep(1)

    # start sdk
    start_sdk(SDK_START, SDK_END)
    time.sleep(1)

    start_player(SDK_START, SDK_END)



