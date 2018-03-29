# coding=utf-8
"""
channel server related constant

__author__ = 'liwenxuan'

"""
import demjson as demjson
from lib.interface.cp.channel_server import *

# 提醒: 测试前请确认MYSQL和REDIS中相应的数据

# ALL
USER_THUNDER = "thunder" # user_not_match
USER_INVAILD = "INVAILD_USER"
PID = "0000000012345123451234512345ABCD"
PID_INVAILD = "INVAILD_PID"
URL_INVAILD = "INVAILD_URL"

# VOD
USER_VOD = "ciwen"
URL_FLV = "http://ciwen.cloutropy.com/v-1/s-1/l-cn/r-1280x720/5.flv"
URL_FLV_UNREG = "http://ciwen.cloutropy.com/v-1/s-1/l-en/r-1920x1080/52.flv"
URL_FLV_NOT_OURS = "http://flv.cntv.wscdns.com/live/flv/channel1.flv"
URL_M3U8 = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/ll8ekYfm0XXjYs4tkLv84iI2T7iA"
URL_M3U8_UNREG = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lqEfYNTpV7px5RAkIDOeZfr8BR0N"
URL_M3U8_NOT_OURS = "http%3a%2f%2fpl.youku.com%2fplaylist%2fm3u8%3fvid%3d230939657%26type%3dmp4%26ts%3d1427851438%26keyframe%3d0%26ep%3ddSaWHUGIV8oD7SLdjT8bZH3ncSFeXPwJ9haGiNRnB9QsT%252Bm7%26sid%3d7427851438125123a55fa%26token%3d8714%26ctype%3d12%26ev%3d1%26cip%3d3657590386"

# LIVE
USER_LIVE = "wasu"
URL_REDIS = "http://flv.srs.cloutropy.com/wasu/test11.flv"  # REDIS中存储的key
URL_REDIS_FILE_ID = "81B01A69331B95898C7EC8174246E41A"
URL_MYSQL = "http://flv.srs.cloutropy.com/live/test2222.flv"  # REDIS中未存储, 但MYSQL中有信息
URL_UNREG = "http://flv.srs.cloutropy.com/live/test233.flv"  # REDIS和MYSQL中都没有, 能注册
URL_NOT_OURS = "http://www.baidu.com/live/1.flv"  # 不是我们的客户, 不能注册

#EXERCISE CHANNEL-SRV PEER_P2P
ETCD_SDK_P2P_PATH = "/business/ops/sdk/p2p/users/"
USER_ID_222 = "22222222"
USER_ID_333 = "33333333"


# if __name__ == "__main__":
#     channel_start_channel(HTTP, "live-ch.cloutropy.com", 80,
#                           USER_VOD, PID, URL_INVAILD)
#     channel_start_hls(HTTP, "live-ch.cloutropy.com", 80,
#                       USER_VOD, PID, URL_INVAILD)
#     channel_start_live_flv(HTTP, "live-ch.cloutropy.com", 80,
#                            USER_LIVE, PID, URL_REDIS)
#     channel_start_live_flv(HTTP, "live-ch.cloutropy.com", 80,
#                            USER_LIVE, PID, URL_MYSQL)
#     r = requests.head("http://pl.youku.com/playlist/m3u8?vid=230939657&type=mp4&ts=1427851438&keyframe=0&ep=dSaWHUGIV8oD7SLdjT8bZH3ncSFeXPwJ9haGiNRnB9QsT%2Bm7&sid=7427851438125123a55fa&token=8714&ctype=12&ev=1&cip=3657590386",)
#     print r.headers
#     print demjson.encode(demjson.encode({"file_id":URL_REDIS_FILE_ID, "file_url":URL_REDIS, "tenant_name":USER_LIVE}))



