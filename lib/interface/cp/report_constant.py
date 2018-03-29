# coding=utf-8
"""
控制面httpdns接口测试相关信息

__author__ = 'liwenxuan'

"""

ISP_100017 = "100017"

# invalid
INVALID = "A"
DECIMAL = 5.5
NEGATIVE = -1
STRING_NUMBER = "10"

# control report

PEER_ID = "0000000012345123451234512345ABCD"
PEER_ID_INVALID = "0000000012345123451234512345ABCz"

DURATION = 300
DURATION_0 = 0

FILE_ID_1 = "ABCDABCD12345123451234512345ABCD"
FILE_ID_2 = "ABCD1234512345ABCD1234512345ABCD"

CPPC = 1
CPPC_0 = 0

BYTES_1 = 1000
BYTES_2 = 20000
BYTES_3 = 300000
BYTES_0 = 0

OP_ADD = "add"
OP_DEL = "del"

TYPE_LIVE = "live"
TYPE_VOD = "vod"
TYPE_DOWNLOAD = "download"

CHUNK_ID = 20000
CHUNK_ID_0 = 0

P2PENABLE_TRUE = True
P2PENABLE_FALSE = False


# cache report
FILE_ID = "272E603BA82C4B0E817A124960E1D1AD"
FILE_ID_INVALID = "invalid_file_id"


# live progress
TYPE_FLV = "live_flv"
TYPE_TS = "live_ts"
TYPE_M3U8 = "live_m3u8"

TIMESTAMP_NOW = "now_time"  # peer_live_progress函数参数report_time="now_time"时，会按当前时间戳重新赋值
TIMESTAMP_0 = 0
