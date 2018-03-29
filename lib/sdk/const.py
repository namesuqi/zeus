# coding=utf-8
# author: zengyuetian
# sdk api test related constant

import re
from lib.utility.path import *

root_path = PathController.get_root_path()
SDK_PORT = 32717

ROOT_USER = "root"
ROOT_PASSWD = "Yunshang2014"

SDK_FILE = "ys_service_static"
PCAP_FILE = "sdk.pcap"
LOG_FILE = "result_log.txt"


LOCAL_SDK = root_path + "/misc/bin/sdk/daily_sdk_api/{0}".format(SDK_FILE)
LOCAL_PCAP = root_path + "/misc/bin/sdk/daily_sdk_api/{0}".format(PCAP_FILE)
LOCAL_LOG_FILE = root_path + "/misc/bin/sdk/daily_sdk_api/{0}".format(LOG_FILE)
RESULT_PATH = root_path + "/result/"

REMOTE_ETH = "eth0"
REMOTE_ROOT_PATH = "/root"
REMOTE_CHECK_PYTHON_FILE = REMOTE_ROOT_PATH + "/sdk_request_check.py"
REMOTE_SDK_API_PATH = "/root/sdk_api"
REMOTE_SDK_PATH = REMOTE_SDK_API_PATH + "/sdk"
REMOTE_SDK = REMOTE_SDK_PATH + "/{0}".format(SDK_FILE)
REMOTE_PCAP = REMOTE_SDK_API_PATH + "/" + PCAP_FILE
REMOTE_LOG_FILE = REMOTE_ROOT_PATH + "/" + LOG_FILE

REMOTE_SDK_IP = "10.6.3.28"


LOGIN_REQUEST_PATTERN = re.compile('/session/peers/[0123456789ABCDEF]{32}$')
