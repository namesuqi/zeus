# coding=utf-8
"""
start multi-vlc to play channel on windows

__author__ = 'zengyuetian'

"""

import time
import os
import subprocess

channel_url = 'http://flv.srs.cloutropy.com/wasu/test.flv'
duration_to_start_new_vlc = 10
SDK_PORT_START = 60000
SDK_PORT_STEP = 10

def kill_all_vlc():
    os.system("taskkill /IM vlc.exe /F")


def start_vlc_to_play(ip, num, url):
    full_url = "http://{0}:{1}/live_flv/user/leigang?url={2}".format(ip, SDK_PORT_START+num*SDK_PORT_STEP, url)
    print full_url
    command = "vlc --no-repeat --open={0}".format(full_url)
    subprocess.Popen(command, shell=True)
    time.sleep(duration_to_start_new_vlc)



if __name__ == "__main__":
    # IDC_IP_LIST = ['122.228.207.106', '58.53.94.36', '61.164.110.152', '61.160.221.183', '61.191.61.133']
    IDC_IP_LIST = ['122.228.207.106', '58.53.94.36', '61.164.110.152']
    # IDC_IP_LIST = ['222.222.12.12', '101.254.185.18', '124.68.11.169']
    IDC_SDK_NUM_LIST = [2, 2, 2]

    # kill all vlc process
    kill_all_vlc()

    for index, ip in enumerate(IDC_IP_LIST):
        num = IDC_SDK_NUM_LIST[index]
        for i in range(num):
            start_vlc_to_play(ip, i, channel_url)

