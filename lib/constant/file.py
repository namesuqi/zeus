# coding=utf-8
"""
播放文件，文件信息

__author__ = 'zengyuetian'

"""
BYTE_DISTRICT = "0-2392068"
NEW_FILE_NAME = "testcreatefile.flv"
NEW_FILE_M3U8_URL = "cdn.cloutropy.com/leigang_cdn/new/sUWPWh5odxh9vtorJ2tsEue__hQ=/ln0M3zSmpCKVWlWkjC3D5vZQoOUl"
NEW_FILE_URL = "cdn.cloutropy.com/leigang_cdn/testcreatenewfile.flv"
NEW_FILE_MD5 = "abcdeabcdeabcdeabcdeabcdeabcde00"
NEW_FILE1_URL = "cdn.cloutropy.com/leigang_cdn/new/testcreatenewfile.flv"
NEW_FILE1_MD5 = "abcdeabcdeabcdeabcdeabcdeabcde01"
NEW_FILE_SIZE = 223333
NEW_FILE_ID = "00000000000000000000000000000001"
NEW_FILE_SOURCE_URL = "cdn.cloutropy.com/testcreatenewfile.flv"
NEW_FILE_SOURCE_EXT = "ext"
INVALID_FILE_URL = "invalidprefix.com/testcreatenewfile.flv"

CNTV_FILE_ID = "E0EAB8F85B724A448E7D9861F80EC93C"
CNTV_PREFIX = "t027.vod05.icntvcdn.com"
CNTV_RELATIVE_URL = "/media/new/2013/icntv2/media/2016/01/13/HD1M7c4f735caf7f47ce8ae32f4f5f7d3506.ts"
CNTV_FILE1_MD5 = "00000000000000000000000000000000"

CIWEN_FILE_ID = "A455140091584518B606D9DF651A7902"
CIWEN_PREFIX = "ciwen.cloutropy.com"
CIWEN_RELATIVE_URL = "/v-1/s-1/l-cn/r-1280x720/7.flv"

INVALID_PREFIX = "invalidprefix.com"
INVALID_RELATIVE_URL = "/___invalidfile.ts"
INVALID_FILE_ID = "00000000000000000000000000000000"

UNREGISTERED_TS_URL = \
    "http://t027.vod05.icntvcdn.com/media/new/2013/icntv2/media/2015/12/02/HD1M1285d86ace6d438b8123211fc815f71d.ts"
UNREGISTERED_FLV_URL = "http://ciwen.cloutropy.com/v-1/s-1/l-en/r-1920x1080/52.flv"
UNREGISTERED_M3U8_URL = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/ln0M3zSmpCKVWlWkjC3D5vZQoOUl"
CIWEN_FLV_URL = "http://ciwen.cloutropy.com/v-1/s-1/l-cn/r-1280x720/7.flv"
CIWEN_M3U8_URL = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lsznRlfC1JDFwwZphcOWSdaAjrwQ"
ICNTV_TS_URL = "http://m.icntvcdn.com/media/new/2011/09/15/sd_dsj_hwdd01_201109115.ts"
ICNTV_CDN_URL = "http://m.icntvcdn.com/media/new/2011/09/15/sd_dsj_hwdd01_201109115.ts"
INVALID_M3U8_URL = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lqcYgaAx99ioZucCAg6e5nmK9BZwNoEXIST"
INVALID_TS_URL = "http://m.icntvcdn.com/media/new/2011/09/15/sd_dsj_hwdd01_201109115NoEXIST.ts"
INVALID_FLV_URL = "http://ciwen.cloutropy.com/NoEXIST2.flv"
INVALID_PREFIX_URL = "http://invalidprefix.com/HD1M7c4f735caf7f47ce8ae32f4f5f7d3506.ts"

NEW_CREATE_PREFIX = "leigang.cloutropy.com"
COMMON_PREFIX = "commonprefix.cloutropy.com"
NEW_CREATE_PREFIX2 = "leigang.cloutropy.com/cntv_cdn"
NEW_CREATE_PREFIX3 = "cdn.cloutropy.com/leigang_test"

FILE_IDS = ["8346C4FB7BE947C7A04953AD5EA49A43", "A455140091584518B606D9DF651A7902", "74DA6014794F4C7184E52D1B84D7317B"]
FILE_ID1 = ["8346C4FB7BE947C7A04953AD5EA49A43"]
INVALID_FILE_IDS = ["INVALID_FILE_ID", "A455140091584518B606D9DF651A7902", "00000000*"]
INCORRECT_FILE_IDS = ["8346C4FB7BE947C7A04953AD5EA49A43", "00000000000000000000000000000000", "A455140091584518B606D9DF651A7902"]

PEER_ID1 = "00010026408B9F4AB0E85524E25043D3"

SOURCE_TYPE_CDN = "CDN"
SOURCE_TYPE_M3U8 = "M3U8"
SOURCE_TYPE_OSS = "OSS"