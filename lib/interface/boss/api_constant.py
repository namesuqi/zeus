# coding=utf-8
"""

boss系统-API接口相关的常量

本地自动化环境与本地测试环境的CUSTOMER_1~5的数据不要随意变动

__author__ = 'liwenxuan'

"""


from random import randrange
from lib.interface.boss.time_handler import *
from lib.database.postgresql_db import PostgresqlDB
from lib.interface.boss.environment_constant import BOSS_CRM_HOST, BOSS_CRM_PORT


# -------------------------------------------------------------------------------------------------------

# common invalid
NUMBER = 100  # 正整数
ZERO = 0
NEGATIVE = -1  # 负数
DECIMAL = time.time()  # 小数
LETTER_A = "a"  # 字母-十六进制
LETTER_Z = "z"  # 字母-非十六进制
C_CHARACTER = "阿"  # 汉字
S_CHARACTER = "#"  # 特殊字符
STRING_NUMBER = "1"  # 字符串类型的数字
STRING_LIST = "[]"  # 字符串类型的列表
STRING_DICT = "{}"  # 字符串类型的字典
STRING_SPACE = " "  # 空格(一个字符)

SPECIAL_CHARACTER_LIST = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<',
                          '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', '-', '_']
COMMON_INVALID_LIST_N = [NUMBER, ZERO, NEGATIVE, DECIMAL]  # 不允许数字类型
COMMON_INVALID_LIST_S = [LETTER_A, LETTER_Z, C_CHARACTER, S_CHARACTER,
                         STRING_NUMBER, STRING_LIST, STRING_DICT, STRING_SPACE]  # 不允许字符类型
COMMON_INVALID_LIST = [NEGATIVE, DECIMAL, LETTER_A, LETTER_Z, C_CHARACTER, S_CHARACTER,
                       STRING_NUMBER, STRING_LIST, STRING_DICT, STRING_SPACE]  # 只能是非负整数

# -------------------------------------------------------------------------------------------------------

# empty-various type
EMPTY_STRING = ""
EMPTY_LIST = []
EMPTY_DICT = {}
EMPTY_TUPLE = ()
EMPTY_SET = ([])

# -------------------------------------------------------------------------------------------------------

# code码
"""
20170510
-100	"未知错误"
-101	"access_key 不正确"
-102	"sign 验证失败"
-103	"timestamp 错误"
-110	"customer_id 不存在"
-111	"prefix 不存在"
-112	"域名不存在"
-113	"blockinfo不存在"
-120	"参数错误"
-121	"step 格式错误"
-122	"时间区间过长"
-130	"客户未开启数据记录功能"
"""
CODE_UNKNOWN_ERROR = -100
CODE_ACCESS_KEY_ERROR = -101
CODE_SIGN_ERROR = -102
CODE_TIMESTAMP_ERROR = -103
CODE_CUSTOMER_NOT_EXIST = -110
CODE_PREFIX_NOT_EXIST = -111
CODE_DOMAIN_NOT_EXIST = -112
CODE_BLOCK_NOT_EXIST = -113
CODE_PARAMETER_ERROR = -120
CODE_STEP_ERROR = -121
CODE_INTERVAL_TOO_LONG = -122
CODE_RECORD_NOT_OPEN = -130

# -------------------------------------------------------------------------------------------------------

# customer_id & prefix 分配

CUSTOMER_ID_1 = "100000001"  # 上下游
CUSTOMER_ID_2 = "100000002"  # 上游
CUSTOMER_ID_3 = "100000003"  # 下游
CUSTOMER_ID_4 = "100000004"  # 不计费
CUSTOMER_ID_5 = "100000005"  # 无prefix
CUSTOMER_ID_LIST = [CUSTOMER_ID_1, CUSTOMER_ID_2, CUSTOMER_ID_3, CUSTOMER_ID_4, CUSTOMER_ID_5]

PREFIX_01 = "00000001"  # 客户1-上下游 上传计费&日活计费, 有合同
PREFIX_02 = "00000002"  # 客户1-上下游 下载计费&日活计费, 有合同
PREFIX_03 = "00000003"  # 客户2-上游   上传计费, 有合同
PREFIX_04 = "00000004"  # 客户2-上游   上传计费, 有合同
PREFIX_05 = "00000005"  # 客户3-下游   下载计费, 有合同
PREFIX_06 = "00000006"  # 客户3-下游   下载计费, 无合同; 日活计费, 有合同
PREFIX_07 = "00000007"  # 客户4-不计费 上传 上传下载不计费
PREFIX_08 = "00000008"  # 客户4-不计费 下载 上传下载不计费
PREFIX_LIST = [PREFIX_01, PREFIX_02, PREFIX_03, PREFIX_04, PREFIX_05, PREFIX_06, PREFIX_07, PREFIX_08]

# -------------------------------------------------------------------------------------------------------

# 会被计费的prefix
UPLOAD_PREFIX_LIST = [PREFIX_01, PREFIX_03, PREFIX_04]
DOWNLOAD_PREFIX_LIST = [PREFIX_02, PREFIX_05]

# 计费类别不为上传/下载的prefix
NOT_UPLOAD_PREFIX_LIST = [PREFIX_02, PREFIX_05, PREFIX_06, PREFIX_08]
NOT_DOWNLOAD_PREFIX_LIST = [PREFIX_01, PREFIX_03, PREFIX_06, PREFIX_07]

# 计费类别为上传/下载, 但没有分块信息
UPLOAD_NO_BLOCK_LIST = [PREFIX_07]
DOWNLOAD_NO_BLOCK_LIST = [PREFIX_04, PREFIX_08]

# -------------------------------------------------------------------------------------------------------

# 域名
# valid
CUSTOMER_1_DOMAIN_1 = "customer-1.domain-1"
CUSTOMER_1_DOMAIN_2 = "customer-1.domain-2"
CUSTOMER_1_DOMAIN_3 = "customer-1.domain-3"
CUSTOMER_1_DOMAIN_4 = "customer-1.domain-4"
CUSTOMER_1_DOMAIN_5 = "customer-1.domain-5"

CUSTOMER_1_DOMAIN_LIST = [CUSTOMER_1_DOMAIN_1, CUSTOMER_1_DOMAIN_2, CUSTOMER_1_DOMAIN_3, CUSTOMER_1_DOMAIN_4, CUSTOMER_1_DOMAIN_5]
CUSTOMER_2_DOMAIN_LIST = ["customer-2.domain-1", "customer-2.domain-2", "customer-2.domain-3"]
CUSTOMER_3_DOMAIN_LIST = ["customer-3.domain-1", "customer-3.domain-2"]
CUSTOMER_4_DOMAIN_LIST = ["customer-4.domain-1"]

# -------------------------------------------------------------------------------------------------------

pg_db = PostgresqlDB(host=BOSS_CRM_HOST)

# -------------------------------------------------------------------------------------------------------

# 鉴权参数
# internal
ACCESS_KEY_INTERNAL = pg_db.execute("select api_access_key from basic_sys_api_auth order by id limit 1").only_one()
SECRET_KEY_INTERNAL = pg_db.execute("select api_secret_key from basic_sys_api_auth order by id limit 1").only_one()

# external
sql_external_api_access_key = "select api_access_key from crm_customer_info where number = '{}'"
sql_external_api_secret_key = "select api_secret_key from crm_customer_info where number = '{}'"
ACCESS_KEY_EXTERNAL_1 = pg_db.execute(sql_external_api_access_key.format(CUSTOMER_ID_1)).only_one()
SECRET_KEY_EXTERNAL_1 = pg_db.execute(sql_external_api_secret_key.format(CUSTOMER_ID_1)).only_one()
ACCESS_KEY_EXTERNAL_2 = pg_db.execute(sql_external_api_access_key.format(CUSTOMER_ID_2)).only_one()
SECRET_KEY_EXTERNAL_2 = pg_db.execute(sql_external_api_secret_key.format(CUSTOMER_ID_2)).only_one()
ACCESS_KEY_EXTERNAL_3 = pg_db.execute(sql_external_api_access_key.format(CUSTOMER_ID_3)).only_one()
SECRET_KEY_EXTERNAL_3 = pg_db.execute(sql_external_api_secret_key.format(CUSTOMER_ID_3)).only_one()
ACCESS_KEY_EXTERNAL_4 = pg_db.execute(sql_external_api_access_key.format(CUSTOMER_ID_4)).only_one()
SECRET_KEY_EXTERNAL_4 = pg_db.execute(sql_external_api_secret_key.format(CUSTOMER_ID_4)).only_one()
ACCESS_KEY_EXTERNAL_5 = pg_db.execute(sql_external_api_access_key.format(CUSTOMER_ID_5)).only_one()
SECRET_KEY_EXTERNAL_5 = pg_db.execute(sql_external_api_secret_key.format(CUSTOMER_ID_5)).only_one()

# timestamp
TIMESTAMP_NOW = int(time.time())

# sign-invalid
SIGN_LENGTH_INCORRECT_LIST = ["", LETTER_A * 31, LETTER_A * 33]
SIGN_INVALID_LIST = [LETTER_Z * 32, C_CHARACTER * 32, S_CHARACTER * 32]

# -------------------------------------------------------------------------------------------------------

del pg_db

# -------------------------------------------------------------------------------------------------------

# start & end 参数
# valid
START_DAY_NOW = second_to_millisecond("%Y-%m-%d", TIMESTAMP_NOW)  # 当天00:00:00
START_DAY_PAST = START_DAY_NOW - 86400000  # 昨天00:00:00
START_DAY_FUTURE = START_DAY_NOW + 86400000  # 明天00:00:00
START_HOUR_NOW = second_to_millisecond("%Y-%m-%d %H", TIMESTAMP_NOW)  # 当前小时段 ??:00:00
START_HOUR_PAST = START_HOUR_NOW - 3600000  # 上一个小时段
START_HOUR_FUTURE = START_HOUR_NOW + 3600000  # 下一个小时段
MILLISECOND_NOW = get_millisecond_now()
START_MINUTE_NOW = period_five_minutes(MILLISECOND_NOW)  # 当前5分钟段
START_MINUTE_PAST = START_MINUTE_NOW - 300000  # 上一个5分钟段
START_MINUTE_FUTURE = START_MINUTE_NOW + 300000  # 下一个5分钟段

END_DAY_PAST = START_DAY_NOW
END_DAY_NOW = START_DAY_FUTURE
END_DAY_FUTURE = START_DAY_FUTURE + 86400000
END_HOUR_PAST = START_HOUR_NOW
END_HOUR_NOW = START_HOUR_FUTURE
END_HOUR_FUTURE = START_HOUR_FUTURE + 86400000
END_MINUTE_PAST = START_MINUTE_NOW
END_MINUTE_NOW = START_MINUTE_FUTURE
END_MINUTE_FUTURE = START_MINUTE_FUTURE + 300000

START_DAY_LONG = END_DAY_PAST - 86400000 * 288
START_HOUR_LONG = END_HOUR_PAST - 3600000 * 288
START_MINUTE_LONG = END_MINUTE_PAST - 300000 * 288

START_RANDOM = (TIMESTAMP_NOW - 3600 - randrange(3600)) * 1000
END_RANDOM = (TIMESTAMP_NOW - randrange(3600)) * 1000  # 前一小时的随机时间

# invalid
START_DAY_TOO_LONG = END_DAY_PAST - 86400000 * 289
START_HOUR_TOO_LONG = END_HOUR_PAST - 3600000 * 289
START_MINUTE_TOO_LONG = END_MINUTE_PAST - 300000 * 289

# -------------------------------------------------------------------------------------------------------

# start_day & end_day 参数
# valid
DATE_YESTERDAY = time.strftime("%Y-%m-%d", time.localtime(TIMESTAMP_NOW - 86400))
DATE_TODAY = time.strftime("%Y-%m-%d", time.localtime(TIMESTAMP_NOW))
DATE_TOMORROW = time.strftime("%Y-%m-%d", time.localtime(TIMESTAMP_NOW + 86400))
DATE_LONG_AGO = time.strftime("%Y-%m-%d", time.localtime(TIMESTAMP_NOW - 86400 * 31))

SPECIAL_DATE = "2016-02-29"
STATIC_DATE = "2017-03-01"  # 确认start_day或end_day中, 其中一个错误时就会报错(与无效情况一起使用)

DATE_SPECIAL_FORMAT_LIST = ["2017-3-01", "2017-03-1", "2017-3-1"]

# invalid
DATE_INVALID_LIST = ["", "20170301", "17-03-01", "017-03-01", "2017-003-01", "2017-03-001", "02017-03-01",
                     "2017-03", "0-0-0", "-100-01-01", "yyyy-mm-dd", "####-##-##", "2017.03.01"]
DATE_NOT_EXIST_LIST = ["2017-02-29", "2016-02-30", "2017-01-32", "2017-02-99", "2017-04-31", "2016-13-01"]
DATE_TOO_LONG_AGO = time.strftime("%Y-%m-%d", time.localtime(TIMESTAMP_NOW - 86400 * 32))

# -------------------------------------------------------------------------------------------------------

# step 参数
# valid
STEP_MINUTE = "minute"
STEP_HOUR = "hour"
STEP_DAY = "day"

# -------------------------------------------------------------------------------------------------------

# prefix 参数
# valid
PREFIX_ALL = "all"

# invalid
PREFIX_INVALID_LIST = ["0000000", "000000000", "BOSSBOSS"]
PREFIX_NOT_EXIST = "AAAAAAAA"

# -------------------------------------------------------------------------------------------------------

# category 参数
# valid
CATEGORY_UPLOAD = "upload"
CATEGORY_DOWNLOAD = "download"

CATEGORY_LIST = [CATEGORY_UPLOAD, CATEGORY_DOWNLOAD]

# -------------------------------------------------------------------------------------------------------

# customer_id 参数
# valid
CUSTOMER_ID_ALL = "all"
CUSTOMER_ID_LIST_AND_ALL = CUSTOMER_ID_LIST + [CUSTOMER_ID_ALL]

# invalid
CUSTOMER_ID_NOT_EXIST = "AAAAAAAA"

# -------------------------------------------------------------------------------------------------------

# domain 相关参数
UNDERLINE = "_"
HYPHEN = "-"
DOMAIN_START = "A."
DOMAIN_END = ".com"
DOMAINS_EMPTY_LIST = [EMPTY_STRING, EMPTY_DICT, EMPTY_TUPLE, EMPTY_SET]

# valid
CUSTOMER_2_DOMAIN_1 = CUSTOMER_2_DOMAIN_LIST[0]

DOMAIN_NAME_FILED = "domain_name"
DOMAIN_EXIST_1 = "test.api-domain-1"
DOMAIN_EXIST_2 = "test.api-domain-2"
DOMAIN_EXIST_3 = "test.api-domain-3"
DOMAINS_LIST = [DOMAIN_EXIST_1, DOMAIN_EXIST_2, DOMAIN_EXIST_3]

DOMAIN_NAME_LEVEL = "test.com"
DOMAIN_NAME_LENGTH_OK = "{0}.{1}".format(LETTER_A * 62, STRING_NUMBER * 62)
DOMAIN_NAME_LENGTH_MIX = "{0}{1}.com".format(LETTER_A * 31, STRING_NUMBER * 31)
DOMAIN_HYPHEN_NUMBER = "test.c{0}".format("-m" * 20)
DOMAIN_LEVEL_TRUE = "1{0}".format(".1" * 20)  # domain域级正好21

# invalid
DOMAIN_NAME_FILED_INCORRECT = "domain"
DOMAIN_HYPHEN_ALONE = "-.com"
DOMAIN_HYPHEN_START = "-test.com"  # 以"-"开头
DOMAIN_HYPHEN_END = "test-.com"    # 以"-"结尾
DOMAIN_HYPHEN_REPEAT = "domain.de--com"   # 连续使用"-"
DOMAIN_NOT_EXIST = "AAAAAAAAAAAAAAAA.com"
DOMAIN_CASE_SENSITIVE = "test.Api-domain-1"  # 区分大小写
DOMAIN_LEVEL_ERROR = "1{0}".format(".1" * 21)  # domain域级超过21
DOMAIN_NAME_LENGTH_ERROR = "{0}.{1}".format(LETTER_A * 63, STRING_NUMBER * 62)
DOMAIN_HYPHEN_ERROR = "test.c{0}".format("-m" * 21)

DOMAIN_INVALID_LIST = SPECIAL_CHARACTER_LIST + [C_CHARACTER, STRING_SPACE]
DOMAINS_INVALID_LIST = COMMON_INVALID_LIST_N + COMMON_INVALID_LIST_S

# -------------------------------------------------------------------------------------------------------

# invalid
# DOMAIN_SPECIAL_CHARACTER_LIST = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<',
#                                  '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', ' ']

# -------------------------------------------------------------------------------------------------------


"""
# domain_names 参数 (e.g. [{"domain_name": "domain1"}, ...])
# 添加域名接口
DOMAIN_NAME_CASE1 = "A.COM"
DOMAIN_NAME_CASE2 = "A.com"                             # 不区分大小写
DOMAINS_TRUE = "abcd.com"                               # domains字段添加成功
DOMAIN_NAME_START_ERROR = "-cd.com"                     # domain_name以"-"开头
DOMAIN_NAME_COTENT_ERROR = "domainnamesayhallo!!"       # domain_name中单级域名中有特殊字符
DOMAIN_LEVEL_COTENT_ERROR1 = "abcd.com.-abcd"           # domain_name多级域名以"-"开头
DOMAIN_LEVEL_COTENT_ERROR2 = "ab!cd.com"                # domain_name多级域名中含特殊字符
DOMAIN_NAME_START_TRUE = "_abcd.com"                    # domain_name以"_"开头(在(0,20]内且有效)
DOMAIN_NAME_LENGTH_ERROR = "domainnamesayhallopython"   # domain_name中单级域名超过20个字符
DOMAIN_LEVEL_ERROR = "1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"  # domain域级超过21
DOMAINS_LENGTH_ERROR = "{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}.{0}".format("".ljust(20, 's'))  # 长度大于255


# DOMAIN_NAME_MISSING = [{"domain_name": ""}]
# DOMAIN_NAME_NUMBER = [{"domain_name": NUMBER}]
# DOMAIN_NAME_DECIMAL = [{"domain_name": DECIMAL}]
# DOMAIN_NAME_EMPTY_DICT = [{"domain_name": EMPTY_DICT}]
# DOMAIN_NAME_EMPTY_LIST = [{"domain_name": EMPTY_LIST}]

# DOMAIN_NAMES_EXIST = [{"domain_name": "a.com"}, {"domain_name": "b.com"}]
# DOMAIN_NAMES_VALID = [{"domain_name": "a.com"}, {"domain_name": "b.com"}]

# DOMAIN_NAMES_NOT_EXIST = [{'domain_name': 'testdel999'}, {'domain_name': 'testdel888'}]  # 无效域名
# DOMAIN_NAMES_REPEAT = [{'domain_name': 'a.com'}, {'domain_name': 'a.com'}]  # 重复域名
# DOMAIN_NAMES_CONTENT_ERROR = [{"domain_name": "a.com"}, {"domain_name": "WREGGD.SDE"}]  # 有效域名+无效域名
# DOMAIN_CONTENT_ERROR_LIST = [DOMAIN_NAMES_REPEAT, DOMAIN_NAMES_NOT_EXIST, DOMAIN_NAMES_CONTENT_ERROR]



# DOMAINS_PART_INVALID = [{"domain_name": "abcd.com"}, {"domain_name": "ab!cd.com"}]  # 多个域名时,部分域名无效
# OMAINS_REPEAT_TRUE = [{"domain_name": "abcde.com"}, {"domain_name": "abcde.com"}]  # 多个域名时,部分域名重复


# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------

# 域名-增删改查接口

# EMPTY_LIST = []
# EMPTY_DICT = {}
#
# DOMAIN_NAMES_EXIST = [{"domain_name": "a.com"}, {"domain_name": "b.com"}]
# DOMAIN_NAMES_VALID = [{"domain_name": "a.com"}, {"domain_name": "b.com"}]
# DOMAIN_NAME_NUMBER = [{"domain_name": NUMBER}]
# DOMAIN_NAME_DECIMAL = [{"domain_name": DECIMAL}]
# DOMAIN_NAME_EMPTY_LIST = [{"domain_name": EMPTY_LIST}]
# DOMAIN_NAME_NONE = [{"domain_name": None}]
# DOMAIN_NAME_EMPTY_DICT = [{"domain_name": EMPTY_DICT}]
#
# DOMAIN_NAME_INVALID_LIST = [
#                             DOMAIN_NAME_NUMBER,
#                             DOMAIN_NAME_DECIMAL,
#                             DOMAIN_NAME_EMPTY_LIST,
#                             DOMAIN_NAME_NONE,
#                             DOMAIN_NAME_EMPTY_DICT
#                             ]
#
# ACCESS_KEY_WRONG = "d86676b78cc41faabc52a58123481a91d0a27906"
#
# ACCESS_KEY_TEST1 = "d86676b78cc41fa4a452a589f0f81a91d0a27906"
# SECRET_KEY_TEST1 = "d8239c930c5f4bb5e6f828f498eb7ee8"
#
# ACCESS_KEY_TEST2 = '133633ea472ad6dc4dc8ff631e11c5c98a32a260'
# SECRET_KEY_TEST2 = '2e260e031af88a5118800d3f584915aa'
#
# ACCESS_KEY_TEST3 = '65a4f96ef6bb0e46418fff0c72df048c2f0fd452'
# SECRET_KEY_TEST3 = '302c980c6e6d68e84e790041454df8be'
#
# DOMAIN_NAMES_TEST2 = "[{u'domain': u'test.domainname1.com'}, {u'domain': u'test.domainname2.com'}]"
# DOMAIN_NAMES_TEST2_DICT = [{'domain_name': 'test.domainname1.com'}, {'domain_name': 'test.domainname2.com'}]
# ACCESS_KEY_TEST4 = '648fee73c16fc22a88c2395f9f6e859f3f9b523a'
# SECRET_KEY_TEST4 = 'c66b00e61e50bd33b2cce8b87bdebf3c'
# DOMAIN_NAMES_TO_DEL = [{'domain_name': 'testdel1'}, {'domain_name': 'testdel2'}]
# DOMAIN_NAMES_NOT_EXIST = [{'domain_name': 'testdel999'}, {'domain_name': 'testdel888'}]
# DOMAIN_NAMES_MIX = [{'domain_name': 'testdel1'}, {'domain_name': 'test.domainname1.com'}]
# DOMAIN_NAMES_EMPTY_DICT = [{}, {}]
# DOMAIN_NAMES_REPEAT = [{'domain_name': 'testdel1'}, {'domain_name': 'testdel1'}]

# -------------------------------------------------------------------------------------------------------

"""


