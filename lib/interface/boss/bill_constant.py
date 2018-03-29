# coding=utf-8
"""

boss系统-计费模块相关的常量

正常计费 回溯计费 日常统计 再统计

__author__ = 'liwenxuan'

"""

import time
from lib.interface.boss.environment_constant import *
# from lib.interface.boss.api_constant import CUSTOMER_ID_1, PREFIX_01, PREFIX_02, CUSTOMER_1_DOMAIN_LIST
# CUSTOMER_ID = CUSTOMER_ID_1
# PREFIX_UPLOAD = PREFIX_01
# PREFIX_DOWNLOAD = PREFIX_02
# DOMAIN_LIST = CUSTOMER_1_DOMAIN_LIST


CUSTOMER_ID = "100000001"
PREFIX_UPLOAD = "00000001"
PREFIX_DOWNLOAD = "00000002"
DOMAIN_LIST = ["customer-1.domain-1", "customer-1.domain-2", "customer-1.domain-3"]

TOPIC_DOWNLOAD = "test_b_download_flow"
TOPIC_UPLOAD = "test_upload_flow"

CATEGORY_UPLOAD = "upload"
CATEGORY_DOWNLOAD = "download"

UNIT_GB = "GB"
UNIT_MB = "MB"
UNIT_KB = "KB"

TIMESTAMP_NORMAL = int(time.time())
TIMESTAMP_RECALL = TIMESTAMP_NORMAL - 3600
TIMESTAMP_REPORT = TIMESTAMP_NORMAL - 86400
TIMESTAMP_RE_REPORT = TIMESTAMP_NORMAL - 86400 * 2

BLOCK_COUNT = 1
LOGS_COUNT = 1500




