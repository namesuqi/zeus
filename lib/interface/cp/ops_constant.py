# coding=utf-8
"""
ops 相关参数

__author__ = 'zsw'

"""
STR_EMPTY = ""  # 空字符串
FILE_ID_0 = "4EB5897E90DA45ACAC38576EAD7786A5"  # 32位十六进制字符串
FILE_ID_LIST = [
    "4EB5897E90DA45ACAC38576EAD7786A5",
    "4EB5897E90DA45ACAC38576EAD7786A6",
    "4EB5897E90DA45ACAC38576EAD7786A7"
]
FILE_ID_INVALID_1 = "*--/"  # 无效参数
FILE_ID_INVALID_2 = "343855B7C23B4C349AFFED0D3B5EC73"  # 31位
FILE_ID_INVALID_3 = "343855B7C23B4C349AFFED0D3B5EC73DA"  # 33位
FILE_ID_INVALID_4 = "343855B7C23B4C349AFFED0D3B5EHZZG"  # 32位非十六进制
FILE_ID_INVALID_5 = "4EB5897E90DA45ACAC38576EAD7786A54EB5897E90DA45ACAC38576EAD7786A54EB5897E90DA45ACAC3857"
FILE_ID_INVALID_LIST = [FILE_ID_INVALID_1, FILE_ID_INVALID_2, FILE_ID_INVALID_3, FILE_ID_INVALID_4, FILE_ID_INVALID_5, STR_EMPTY]

USER_ID = "0000000"
USER_ID_0 = "343855B7"  # 8位十六进制字符串
USER_ID_LIST = [
    "00010001",
    "00010002",
    "00010003"
]
USER_ID_INVALID_1 = "*--/"  # 无效参数
USER_ID_INVALID_2 = "343855B"  # 7位
USER_ID_INVALID_3 = "343855B7C"  # 9位
USER_ID_INVALID_4 = "00ZFHG56"  # 8位非十六进制
USER_ID_INVALID_5 = "B7BBBBBBBBBBBBBBBBBBBBBBBBCAAAAAAADDDDDDDDdddddddddsssssssssssssssssssssssaaaaDDDDDDDD"
USER_ID_INVALID_LIST = [USER_ID_INVALID_1, USER_ID_INVALID_2, USER_ID_INVALID_3, USER_ID_INVALID_4, USER_ID_INVALID_5, STR_EMPTY]

# invalid
INVALID = "A"
DECIMAL = 5.5
NEGATIVE = -1
STRING_NUMBER = "10"

# httpdns
GROUPNAME = "test_group"
GROUPNAME_LONG = "test_groupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroupgroup"
GROUPNAME_2 = "test_group_test"

HOSTNAME = "test_host1"
HOSTNAME_LONG = "test_host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1host1"
HOSTNAME_2 = "test_host2"
HOSTNAME_3 = "test_host3"

TTL = 60
TTL_300 = 300

IPS = "ips"

DIVISION_DD = {"division": "default_default", "ips": ["192.168.1.200"]}
DIVISION_PD = {"division": "110000_default", "ips": ["192.168.1.200", "0.0.0.1"]}
DIVISION_DI = {"division": "default_100017", "ips": ["192.168.1.200", "255.255.255.254"]}
DIVISION_PI = {"division": "310000_100017", "ips": ["192.168.1.200", "0.0.0.1", "255.255.255.254"]}

DIVISION_P_WRONG = {"division": "200000_default", "ips": ["192.168.1.200"]}
DIVISION_P_EMPTY = {"division": "_default", "ips": ["192.168.1.200"]}

DIVISION_I_WRONG = {"division": "default_100011", "ips": ["192.168.1.200"]}
DIVISION_I_EMPTY = {"division": "default_", "ips": ["192.168.1.200"]}
DIVISION_WRONG = {"division": "111111_100111", "ips": ["192.168.1.200"]}
DIVISION_IPS_EMPTY_1 = {"division": "default_default", "ips": []}
DIVISION_IPS_EMPTY_2 = {"division": "default_default", "ips": [""]}
DIVISION_IP_EMPTY_1 = {"division": "default_default", "ips": ["192.168.1.200", None, "1.1.1.1"]}
DIVISION_IP_EMPTY_2 = {"division": "default_default", "ips": ["192.168.1.200", "", "1.1.1.1"]}
DIVISION_IP_INVALID_1 = {"division": "default_default", "ips": ["192.168.1.200", "256.256.256.256"]}
DIVISION_IP_INVALID_2 = {"division": "default_default", "ips": ["192.168.1.200", "A"]}
DIVISION_IP_INVALID_3 = {"division": "default_default", "ips": ["192.168.1.200", "0.0.0.0"]}
DIVISION_IP_INVALID_4 = {"division": "default_default", "ips": ["192.168.1.200", "255.255.255.255"]}
DIVISION_IP_SAME = {"division": "default_default", "ips": ["192.168.1.200", "192.168.1.200"]}


# etcd key_path
DOMAIN_NAME_GROUP = "/httpdns/domain_name_group/"
DOMAIN_NAME_IP_MAP = "/httpdns/domain_name_ip_map/"

# join/leave LF
PEER_ID = "0000000012345123451234512345ABCD"
PEER_ID9 = "0000000012345123451234512345DDDD"
PEER_ID1 = "0000000012345123451234512345ABBD"
PEER_ID2 = "0000000012345123451234512345ABAD"
PEER_ID3 = "0000000012345123451234512345ABCE"
PEER_ID4 = "0000000012345123451234512345ABCF"
PEER_ID5 = "0000000012345123451234512345ABCA"
PEER_ID6 = "0000000012345123451234512345ABCB"
PEER_ID7 = "0000000012345123451234512345ABCC"
PEER_ID8 = "0000000012345123451234512345ADCA"
PEER_LIST = [PEER_ID1, PEER_ID2, PEER_ID3, PEER_ID4, PEER_ID5, PEER_ID6, PEER_ID7, PEER_ID8]
PEER_ID_INVALID = "0000000012345123451234512345ABCz"
PEER_LIST_MIX = [PEER_ID1, PEER_ID_INVALID, PEER_ID5, PEER_ID6, PEER_ID7,PEER_ID8]

FILE_URL_NOT_EXIST = "cdn.cloutropy.com/leigang_cdn/testcreatenewfile.flv"
FILE_URL_INVALID = -1
FILE_URL_ALL_ZERO = "0000000000000000000000000000000000000000000000000"
FILE_ID = "23DA046BD3E2F06367C159534CE88A42"
FILE_URL = "http://flv.srs.cloutropy.com/wasu/test.flv"

OPS_USER_NAME = "root"
OPS_PASSWORD = "Yunshang2014"
CMD_DROP_CHAN = "iptables -A INPUT -s chn-mgr.ys-internal.com -j DROP"
CMD_DROP_STUN_IN = "iptables -A INPUT -s stun-hub.cloutropy.com -j DROP"
CMD_DROP_STUN_OUT = "iptables -A OUTPUT -s stun-hub.cloutropy.com -j DROP"
CMD_F = "iptables -F"

EMPTY = ""

ISP_100017 = "100017"  # 电信
ISP_100026 = "100026"  # 联通
ISP_000000 = "000000"  # 其他
ISP_INVALID_1 = "00000A"
ISP_INVALID_2 = "!@$!@#"
ISP_INVALID_3 = "asdqweasdqweasdgasdzxasrdasdaqweasdasdqr"

PUBLIC_IP_100017 = "116.231.167.180"  # isp: 100017
STUN_IP1 = "123.56.30.51"

USER_ID_CORRECT = "00000000"
JSON_NEED_JOIN = "need_to_join_count"
JSON_NEED_LEAVE = "need_to_leave_count"
JSON_USEABLE = "useable_peer_count"

COUNT = 6
COUNT_INVALID_1 = "@%!@%!@$#^&&"
COUNT_INVALID_2 = "112AC"
COUNT_INVALID_3 = -6
WATER_MARK = 2
WATER_MARK_INVALID_1 = "!@$!%^!#@"
WATER_MARK_INVALID_2 = "4425BD"
WATER_MARK_INVALID_3 = -2

TOPIC_CHANNEL_SWITCH = "channel_strategy_switch"
TOPIC_USER_SWITCH = "user_strategy_switch"
