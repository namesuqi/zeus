# coding=utf-8
# const
# author = zengyuetian

from lib.utility.path import *
from lib.decorator.log import *

SDK_VERSION = "3.12.1"
LIVE_PUSH_VERSION = "1.4.7"

root_path = PathController.get_root_path()
SDK_PORT = 60000
ISO_TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# user and password to access remote machine
ROOT_USER = "root"
ROOT_PASSWD = "Yunshang2014"
ADMIN_USER = "admin"
ADMIN_PASSWD = "yzhxc9!"
LIVE_PUSH_USER = "admin"
LIVE_PUSH_ADMIN_PASSWD = "yzhxc9!"

SDK_FILE = "ys_service_static"
FLV_PARSER = "flv_parse.py"
PLAYER = "main.py"
PLAYER_LOG = "stat.log"

# sdk location on control machine
LOCAL_SDK = root_path + "/misc/bin/sdk/daily_ue/{0}".format(SDK_FILE)
LOCAL_FLV_PARSER = root_path + "/misc/tool/pyplayer/{0}".format(FLV_PARSER)
LOCAL_PLAYER = root_path + "/misc/tool/pyplayer/{0}".format(PLAYER)

RESULT_PATH = root_path + "/result/"

# sdk location on peer machine
REMOTE_UE_PATH = "/root/ue"
REMOTE_SDK_PATH = REMOTE_UE_PATH + "/sdk"
REMOTE_SDK = REMOTE_SDK_PATH + "/{0}".format(SDK_FILE)

# live push bin path
REMOTE_LIVE_PUSH_SUPP_PATH = "/home/admin/p2p_live_push/live-push-srv-supp"
LIVE_PUSH_FILE = "live-push-srv-1.4.7"

# player on peer machine
REMOTE_PLAYER_PATH = REMOTE_UE_PATH + "/pyplayer"
REMOTE_PLAYER = REMOTE_PLAYER_PATH + "/" + PLAYER
REMOTE_FLV_PARSER = REMOTE_PLAYER_PATH + "/" + FLV_PARSER
REMOTE_PLAYER_LOG = REMOTE_PLAYER_PATH + "/" + PLAYER_LOG

# channel url for udp and http
# YUNDUAN_URL = "live_flv/user/yunduan?url=http://live3.play.yunduan.cloutropy.com/live/test3.flv"
# BEIJING_URL = "live_flv/user/wasu?url=http://flv.srs.cloutropy.com/wasu/test.flv"
PLAY_URL = "live_flv/user/wasu?url="
# FILE_URL = "http://flv.srs.cloutropy.com/wasu/test.flv"
# FILE_ID = "23DA046BD3E2F06367C159534CE88A42"

FILE_URL = "http://flv.srs.cloutropy.com/wasu/time.flv"
FILE_ID = "3754346B73042A41DCF9DE9A355CC180"
BEIJING_URL = PLAY_URL + FILE_URL

# YUNDUAN_HTTP_FLV_URL = "http://live3.play.yunduan.cloutropy.com/live/test3.flv"
# BEIJING_HTTP_FLV_URL = "http://flv.srs.cloutropy.com/wasu/test.flv"
# BEIJING_HTTP_FLV_URL = "http://flv.srs.cloutropy.com:8080/wasu/test.flv"
BEIJING_HTTP_FLV_URL = "http://flv.srs.cloutropy.com:8080/wasu/time.flv"

# peer machine info
PEER_IP = "192.168.8.41"
PEER_ETH = "enp1s0"

# gateway machine info
PEER_PUSH_GW_IP = "192.168.8.42"
PEER_PUSH_GW_ETH = "enp1s0"

# gateway machine info
# PEER_PUSH_GW2_IP = "192.168.1.43"
# PEER_PUSH_GW2_ETH = "enp1s0"

# push server machine info
PUSH_NET = "192.168.8.40"
PUSH_NET_MASK = "255.255.255.255"
LIVE_PUSH_IP = "192.168.8.40"
LIVE_PUSH_DEV = "enp1s0"

# network params
ACTUAL_BAND_WIDTH = "2.5M"
BASIC_DELAY_TIME = 0

SAMPLE_NUM = 10
PLAY_DURATION = 30
LOGIN_DUATION = 3
REGULAR_TIME_PLAY_DURATION = 20
LAST_TIME_PLAY_DURATION = 300

DELAY_TIME_LIST = [200, 100, 50, 20]
# real_delay *= 2
LOSS_RATE_LIST = [15, 7.5, 1.5, 0.1]
MODE_LIST = ["first_image_time", "buffer_number"]

# NETWORK_CONGESTION_LIST = ["深队拥塞", "浅队拥塞", "突发延迟"]
# NETWORK_CONGESTION_LIST = ["deep", "shallow", "burst"]

MODE_UDP = "udp"
MODE_HTTP = "http"

UDP_LOG_NAME = "udp_stat.log"
HTTP_LOG_NAME = "http_stat.log"

MODE_FIRST_IMAGE_TIME = "first_image"
MODE_BUFFERING_NUM = "buffer_num"

RESULT_FILE = root_path + "/result/result.txt"

# csv params
CSV_HTTP_FILE = root_path + "/result/result_http_data.csv"
CSV_FILE = root_path + "/result/result_data.csv"
CSV_HEADER = [u"延迟", u"丢包", u"指标", u"播放次数", u"协议", u"平均值", u"中值", u"最大值", u"方差值",
              u"指标", u"播放时长", u"卡顿次数"]

CSV_DATABASE_HEADER = [u"延迟和丢包", u"版本", u"样本数", u"起播时间", u"卡顿次数",  u"p2p占比", u"版本", u"样本数",
                       u"起播时间", u"卡顿次数"]

CSV_DATABASE_TIME_HEADER = [u"延迟和丢包", u"版本", u"样本数", u"起播时间", u"卡顿次数"]


START_UP_TIME = u"启播时间"
BUFFERING_NUMBER = u"卡顿次数"


# live_push_srv version; the subsequent version should be add into this dict
# LIVE_PUSH_VERSION_DICT = {
#     "live push server 1.3.1": "3.6",
#     "live push server 1.4.1": "3.7",
#     "live push server 1.4.5": "3.7.1"
# }

# mysql database info
# MYSQL_HOST = "mysql.auto.cloutropy.com.cn"
# MYSQL_HOST = "192.168.8.43"
MYSQL_HOST = "192.168.1.61"
MYSQL_PORT = 3306
MYSQL_UE_USER = "ppc"
MYSQL_PASSWORD = "yunshang2014"
MYSQL_TABLE_NAME = "ue_performance"
MYSQL_DB_NAME = "user_experience"


STUN_THUNDER_IP = "192.168.8.43"
STUN_THUNDER_PORT = "8000"

LF_IP = "192.168.8.44"
LF_DEV = "enp3s0"
LF_PORT_START = 20000
LF_DEPLOY_PATH = "/home/admin/ue/lf_deploy"
LF_DEPLOY_SDK_PATH = LF_DEPLOY_PATH + "/sdk"
LF_SDK = LF_DEPLOY_PATH + "/sdk/%s" % SDK_FILE

