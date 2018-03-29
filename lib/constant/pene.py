# coding=utf-8
"""

Those constant variable for SDK penetrate case

__author__ = 'panpan'

"""
from lib.utility.path import PathController

root_path = PathController.get_root_path()

DUMMY_NAT_FILE_PATH = r"/home/admin/dummy_nat/dummynat.py"
PENETRATE_LOG_PATH = "/home/admin/dummy_nat/log/penetrator.log"
SDK_FOLDER_PATH = r"/home/admin/yssdk/"
# PENETRATE_SDK_FILE_PATH = r"/home/jenkins/zeus/misc/bin/sdk/daily_penetrate/ys_service_static"
PENETRATE_SDK_FILE_PATH = root_path + r"/misc/bin/sdk/daily_penetrate/ys_service_static"
SDK_FILE_PATH = r"/home/admin/yssdk/ys_service_static"
# SEND_NAT_IP = "10.6.5.1"
# RECEIVE_NAT_IP = "10.6.4.1"
# SEND_SDK_IP = "10.6.5.2"
# RECEIVE_SDK_IP = "10.6.4.2"
SEND_NAT_IP = "192.168.4.196"
RECEIVE_NAT_IP = "192.168.4.197"
SEND_SDK_IP = "192.168.201.3"
RECEIVE_SDK_IP = "192.168.202.3"
MOCK_TS_IP = SEND_NAT_IP

# START_VOD_COMMAND = r'nohup curl  --header "Range: bytes=0-335928740" -o vod.file "http://127.0.0.1:32717/vod?url=' \
#                     'http://ciwen.cloutropy.com/v-1/s-1/l-en/r-1280x720/2.flv&user=ciwen" > /dev/null 2>&1 &'
START_VOD_COMMAND = r'nohup curl  --header "Range: bytes=0-335928740" -o vod.file "http://127.0.0.1:32717' \
                    r'/live_flv/user/wasu?url=http://flv.srs.cloutropy.com/wasu/test.flv" > /dev/null 2>&1 &'
STOP_SDK_COMMAND = r"ps aux | grep ys_service_static |grep -v grep |awk -F  ' ' '{print $2}' | xargs kill -9"
STOP_DUMMY_NAT_COMMAND = r"python /home/admin/dummy_nat/natoperator.py"
START_SDK_COMMAND = "nohup " + SDK_FILE_PATH + " > /dev/null 2>&1 &"
START_DUMMY_NAT_COMMAND = "cd /home/admin/dummy_nat/" + ";nohup python " + DUMMY_NAT_FILE_PATH + \
                          " %s > /dev/null 2>&1 &"

SDK_LOGIN_URL = r"http://127.0.0.1:32719/ajax/login"
SDK_CONF_FILE = r"/home/admin/yunshang/yunshang.conf"
SDK_VERSION_URL = r"http://127.0.0.1:32717/ajax/version"
