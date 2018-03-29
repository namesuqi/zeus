# coding=utf-8
"""
控制面httpdns接口测试相关信息

__author__ = 'liwenxuan'

"""

# host
from lib.constant.various import PROVINCE_LIST

HOST_TS = "ts.cloutropy.com"
HOST_SEEDS = "seeds.cloutropy.com"
HOST_REPORT = "report.cloutropy.com"
HOST_ERRLOGS = "errlogs.cloutropy.com"
HOST_STATS = "stats.cloutropy.com"
HOST_UPGRADEV2 = "upgradev2.cloutropy.com"
HOST_STUN2 = "stun2.cloutropy.com"
HOST_PUSH = "push.cloutropy.com"
HOST_CHANNEL = "channel.cloutropy.com"
HOST_DEBUG = "debug.cloutropy.com"
HOST_GROUP = "cloutropy.com"
HOST_NOT_EXIST_LIST = ["HOST_NOT_EXIST", 0, -1, 1, "*"]
AUTO_TEST_HOST = "www.test.com"

# ip
IP_DEFAULT = "192.168.2.0"
IP_SH_TELECOM = "116.231.56.252"  # province_isp: 310000_100017
INVALID_IP_LIST = ["INVALID_IP", -1, 0, "255.255.255.256"]

# group
GROUP = "cloutropy.com"
GROUP_INVAILD = "INVALID_GROUP"
AUTP_TEST_GROUP = "test.com"

HTTPDNS_MASTER_PATH = "/business/httpdns/v2/"  # etcd中httpdns配置主目录

# etcd set_value
AREA_DEFAULT = {"ip_group": "default"}
AREA_NORTH = {"province_group": "north_group", "keep_alive": True, "ip_group": "beijing"}
AREA_SOUTH = {"province_group": "south_group", "keep_alive": True, "ip_group": "hangzhou"}

# 域名组
GROUP_CLOUTROPY = "cloutropy.com"
GROUP_DOMAINS_CLOUTROPY = [
    "ts.cloutropy.com",
    "seeds.cloutropy.com",
    "report.cloutropy.com",
    "live-ch.cloutropy.com",
    "channel.cloutropy.com",
    "stun2.cloutropy.com",
    "stats.cloutropy.com",
    "hls.cloutropy.com",
    "errlogs.cloutropy.com",
    "upgradev2.cloutropy.com",
    "push.cloutropy.com",
    "debug.cloutropy.com",
    "opt.cloutropy.com",
    "test.live.cloutropy.com",
    "yunduan.live.cloutropy.com",
    "zeng.cloutropy.com",
    "demo.live.cloutropy.com"
    ]
PART_DOMAIN_CLOUTROPY = GROUP_DOMAINS_CLOUTROPY[0:7]
DEFAULT_DOMAIN_CLOUTROPY = GROUP_DOMAINS_CLOUTROPY[7:]

# 省份分区
NORTH_PROVINCE = PROVINCE_LIST[0:17]
SOUTH_PROVINCE = PROVINCE_LIST[17:-5]
GUANGXI_PROVINCE = PROVINCE_LIST[-5:-4]
DEFAULT_PROVINCE = PROVINCE_LIST[-4:]

# 域名IP_MAP配置
IP_MAP_DEFAULT = {
    "ips": {
        "default": ["0.0.1.0", "0.0.1.1", "0.0.1.2", "0.0.1.3", "0.0.1.4"]
    },
    "ttl": 3600
}
IP_MAP_NORTH = {
    "ips": {
        "default": ["1.1.0.0", "1.1.0.1", "1.1.0.2", "1.1.0.3"],
        "100017": ["1.1.7.0", "1.1.7.1", "1.1.7.2", "1.1.7.3"],
        "100026": ["1.1.6.0", "1.1.6.1", "1.1.6.2", "1.1.6.3"]
    },
    "ttl": 1000
}
IP_MAP_SOUTH = {
    "ips": {
        "default": ["2.2.0.0", "2.2.0.1", "2.2.0.2", "2.2.0.3", "2.2.0.4", "2.2.0.5"],
        "100017": ["2.2.7.0", "2.2.7.1", "2.2.7.2", "2.2.7.3", "2.2.7.4", "2.2.7.5"]
    },
    "ttl": 2000
}
IP_MAP_GUANGXI = {
    "ips": {
        "default": ["3.3.0.0", "3.3.0.1"],
        "100017": ["3.3.7.0", "3.3.7.1"],
        "100026": ["3.3.6.0", "3.3.6.1"]
    },
    "ttl": 3000
}

# 默认测试配置
CONF_TEST_V1 = {
    "domain_group/cloutropy.com": GROUP_DOMAINS_CLOUTROPY,
    "domain_ip_map/beijing": {
        "ts.cloutropy.com": IP_MAP_NORTH,
        "seeds.cloutropy.com": IP_MAP_NORTH,
        "report.cloutropy.com": IP_MAP_NORTH,
        "live-ch.cloutropy.com": IP_MAP_NORTH,
        "channel.cloutropy.com": IP_MAP_NORTH,
        "stun2.cloutropy.com": IP_MAP_NORTH,
        "stats.cloutropy.com": IP_MAP_NORTH,
    },
    "domain_ip_map/hangzhou": {
        "ts.cloutropy.com": IP_MAP_SOUTH,
        "seeds.cloutropy.com": IP_MAP_SOUTH,
        "report.cloutropy.com": IP_MAP_SOUTH,
        "live-ch.cloutropy.com": IP_MAP_SOUTH,
        "channel.cloutropy.com": IP_MAP_SOUTH,
        "stun2.cloutropy.com": IP_MAP_SOUTH,
        "stats.cloutropy.com": IP_MAP_SOUTH,
    },
    "domain_ip_map/guangxi": {
        "ts.cloutropy.com": IP_MAP_GUANGXI,
        "seeds.cloutropy.com": IP_MAP_GUANGXI,
        "report.cloutropy.com": IP_MAP_GUANGXI,
        "live-ch.cloutropy.com": IP_MAP_GUANGXI,
        "channel.cloutropy.com": IP_MAP_GUANGXI,
        "stun2.cloutropy.com": IP_MAP_GUANGXI,
        "stats.cloutropy.com": IP_MAP_GUANGXI,
    },
    "domain_ip_map/default": {
        "ts.cloutropy.com": IP_MAP_DEFAULT,
        "seeds.cloutropy.com": IP_MAP_DEFAULT,
        "report.cloutropy.com": IP_MAP_DEFAULT,
        "live-ch.cloutropy.com": IP_MAP_DEFAULT,
        "channel.cloutropy.com": IP_MAP_DEFAULT,
        "stun2.cloutropy.com": IP_MAP_DEFAULT,
        "stats.cloutropy.com": IP_MAP_DEFAULT,

        "hls.cloutropy.com": IP_MAP_DEFAULT,
        "errlogs.cloutropy.com": IP_MAP_DEFAULT,
        "upgradev2.cloutropy.com": IP_MAP_DEFAULT,
        "push.cloutropy.com": IP_MAP_DEFAULT,
        "debug.cloutropy.com": IP_MAP_DEFAULT,
        "opt.cloutropy.com": IP_MAP_DEFAULT,
        "test.live.cloutropy.com": IP_MAP_DEFAULT,
        "yunduan.live.cloutropy.com": IP_MAP_DEFAULT,
        "zeng.cloutropy.com": IP_MAP_DEFAULT,
        "demo.live.cloutropy.com": IP_MAP_DEFAULT
    },
    "province_group/north_group": NORTH_PROVINCE,
    "province_group/south_group": SOUTH_PROVINCE,
    "province_group/guangxi_group": GUANGXI_PROVINCE,
    "province_group/false_group": DEFAULT_PROVINCE,
    "areas/false": {
        "keep_alive": False,
        "province_group": "false_group",
        "ip_group": "beijing"
    },
    "areas/north": {
        "keep_alive": True,
        "province_group": "north_group",
        "ip_group": "beijing"
    },
    "areas/south": {
        "keep_alive": True,
        "province_group": "south_group",
        "ip_group": "hangzhou"
    },
    "areas/guangxi": {
        "keep_alive": True,
        "province_group": "guangxi_group",
        "ip_group": "guangxi"
    },
    "areas/default": {
        "ip_group": "default"
    }
}

# 所有分区使用DEFAULT
CONFIG_PARTITION_ALL_SWITCH_TO_DEFAULT = {
    "areas/false": {
        "keep_alive": False,
        "province_group": "false_group",
        "ip_group": "beijing"
    },
    "areas/north": {
        "keep_alive": False,
        "province_group": "north_group",
        "ip_group": "beijing"
    },
    "areas/south": {
        "keep_alive": False,
        "province_group": "south_group",
        "ip_group": "hangzhou"
    },
    "areas/guangxi": {
        "keep_alive": False,
        "province_group": "guangxi_group",
        "ip_group": "guangxi"
    },
    "areas/default": {
        "ip_group": "default"
    }
}
# 将SOUTH分区切到beijing
CONFIG_PARTITION_SOUTH_SWITCH_TO_BEIJING = {
    "areas/false": {
        "keep_alive": False,
        "province_group": "false_group",
        "ip_group": "beijing"
    },
    "areas/north": {
        "keep_alive": True,
        "province_group": "north_group",
        "ip_group": "beijing"
    },
    "areas/south": {
        "keep_alive": True,
        "province_group": "south_group",
        "ip_group": "beijing"
    },
    "areas/guangxi": {
        "keep_alive": True,
        "province_group": "guangxi_group",
        "ip_group": "guangxi"
    },
    "areas/default": {
        "ip_group": "default"
    }
}

# 域名IP_MAP配置
CONFIG_TEST_DOMAIN_DEFAULT = {
    "domain_ip_map/default": {
        "ts.cloutropy.com": IP_MAP_DEFAULT,
        "seeds.cloutropy.com": IP_MAP_DEFAULT,
        "report.cloutropy.com": IP_MAP_DEFAULT,
        "live-ch.cloutropy.com": IP_MAP_DEFAULT,
        "channel.cloutropy.com": IP_MAP_DEFAULT,
        "stun2.cloutropy.com": IP_MAP_DEFAULT,
        "stats.cloutropy.com": IP_MAP_DEFAULT,

        "hls.cloutropy.com": IP_MAP_DEFAULT,
        "errlogs.cloutropy.com": IP_MAP_DEFAULT,
        "upgradev2.cloutropy.com": IP_MAP_DEFAULT,
        "push.cloutropy.com": IP_MAP_DEFAULT,
        "debug.cloutropy.com": IP_MAP_DEFAULT,
        "opt.cloutropy.com": IP_MAP_DEFAULT,
        "test.live.cloutropy.com": IP_MAP_DEFAULT,
        "yunduan.live.cloutropy.com": IP_MAP_DEFAULT,
        "zeng.cloutropy.com": IP_MAP_DEFAULT,
        "demo.live.cloutropy.com": IP_MAP_DEFAULT
    }
}

CONFIG_TEST_DOMAIN_BEIJING = {
    "domain_ip_map/beijing": {
        "ts.cloutropy.com": IP_MAP_NORTH,
        "seeds.cloutropy.com": IP_MAP_NORTH,
        "report.cloutropy.com": IP_MAP_NORTH,
        "live-ch.cloutropy.com": IP_MAP_NORTH,
        "channel.cloutropy.com": IP_MAP_NORTH,
        "stun2.cloutropy.com": IP_MAP_NORTH,
        "stats.cloutropy.com": IP_MAP_NORTH,
    }
}
# 无效IP_MAP
IP_MAP_INVALID_LIST = [
        {},
        "",
        [],
        {"ttl": 10},
        {"ips": {"default": ["6.6.6.6"]}},
        {"ttl": -1, "ips": {"default": ["6.6.6.6"]}},
        {"ttl": 0, "ips": {"default": ["6.6.6.6"]}},
        {"ttl": "0", "ips": {"default": ["6.6.6.6"]}},
        {"ttl": "INVALID", "ips": {"default": ["6.6.6.6"]}},
        {"ttl": 66, "ips": {}},
        {"ttl": 66, "ips": {"default": ""}},
        {"ttl": 66, "ips": {"default": []}},
        {"ttl": 66, "ips": {"default": [""]}},
        {"ttl": 66, "ips": {"default": [0]}},
        {"ttl": 66, "ips": {"default": ["INVALID"]}},
        {"ttl": 66, "ips": {"default": ["1.1.1"]}},
        {"ttl": 66, "ips": {"default": ["1.1.1.-1"]}},
        {"ttl": 66, "ips": {"default": ["255.255.255.256"]}},
        # {"ttl": 66, "ips": {"default": ["255.255.255.255"]}},
        # {"ttl": 66, "ips": {"default": ["0.0.0.0"]}},
        {"ttl": 66, "ips": {"default": ["192.168.1.200", "255.255.255.256"]}},
        # {"ttl": 66, "ips": {"default": ["192.168.1.200", "0.0.0.0"]}},
        {"ttl": 66, "ips": {"default_default": ["6.6.6.6"]}},
        {"ttl": 66, "ips": {"invalid": ["6.6.6.6"]}},
        {"ttl": 66, "ips": {100017: ["6.6.6.6"]}},
]
CONFIG_TEST_OFFICE = {
    "/business/httpdns/v2/domain_group/cloutropy.com": [
        "ts.cloutropy.com",
        "seeds.cloutropy.com",
        "hls.cloutropy.com",
        "report.cloutropy.com",
        "errlogs.cloutropy.com",
        "stats.cloutropy.com",
        "live-ch.cloutropy.com",
        "upgradev2.cloutropy.com",
        "push.cloutropy.com",
        "channel.cloutropy.com",
        "debug.cloutropy.com",
        "stun2.cloutropy.com",
        "opt.cloutropy.com",
        "test.live.cloutropy.com",
        "yunduan.live.cloutropy.com",
        "zeng.cloutropy.com",
        "demo.live.cloutropy.com"
    ],
    "/business/httpdns/v2/domain_ip_map/default": {
        "ts.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "seeds.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "report.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "live-ch.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "channel.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "stun2.cloutropy.com": {"ips": {"default": ["192.168.1.202", "192.168.1.195"]}, "ttl": 3600},
        "stats.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "hls.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "errlogs.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "upgradev2.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "push.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "debug.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
        "opt.cloutropy.com": {"ips": {"default": ["192.168.1.200"]}, "ttl": 3600},
    },
    "/business/httpdns/v2/areas/default": {
        "ip_group": "default"
    },
}
