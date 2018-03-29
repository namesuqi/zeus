# coding=utf-8
"""
push_hub汇报相关信息

"""

PUSH_HUB_HOST = "push-hub.ys-internal.com"
PUSH_HUB_PORT = "9558"

ISP = ["电信", "移动", "联通", "其他"]

PROVINCE_LIST = [
    {"province": "北京市", "isp": ISP},
    {"province": "天津市", "isp": ISP},
    {"province": "上海市", "isp": ISP},
    {"province": "重庆市", "isp": ISP},
    {"province": "河北省", "isp": ISP},
    {"province": "河南省", "isp": ISP},
    {"province": "云南省", "isp": ISP},
    {"province": "辽宁省", "isp": ISP},
    {"province": "黑龙江省", "isp": ISP},
    {"province": "湖南省", "isp": ISP},
    {"province": "湖北省", "isp": ISP},
    {"province": "安徽省", "isp": ISP},
    {"province": "山东省", "isp": ISP},
    {"province": "新疆维吾尔自治区", "isp": ISP},
    {"province": "江苏省", "isp": ISP},
    {"province": "浙江省", "isp": ISP},
    {"province": "江西省", "isp": ISP},
    {"province": "广西壮族自治区", "isp": ISP},
    {"province": "甘肃省", "isp": ISP},
    {"province": "山西省", "isp": ISP},
    {"province": "内蒙古", "isp": ISP},
    {"province": "陕西省", "isp": ISP},
    {"province": "吉林省", "isp": ISP},
    {"province": "福建省", "isp": ISP},
    {"province": "贵州省", "isp": ISP},
    {"province": "广东省", "isp": ISP},
    {"province": "青海省", "isp": ISP},
    {"province": "西藏自治区", "isp": ISP},
    {"province": "四川省", "isp": ISP},
    {"province": "宁夏回族自治区", "isp": ISP},
    {"province": "海南省", "isp": ISP},
    {"province": "台湾省", "isp": ISP},
    {"province": "香港特别行政区", "isp": ISP},
    {"province": "澳门特别行政区", "isp": ISP}
]

IP_MAP_BODY = {
    "live-push1.cloutropy.com": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    },

    "live-push2.cloutropy.com": {
        "10.5.101.26": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.26"]
        }
    },

    "live-push3.cloutropy.com": {
        "10.5.101.27": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.27"]
        }
    }
}

IP_REPEAT = {
    "live-push1.cloutropy.com": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    },

    "live-push2.cloutropy.com": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    }
}

HOST_INVALID = {
    "live-push1.cloutropy": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    },

    "live-push2.cloutropy": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    }
}

HOST_REPEAT = {
    "live-push1.cloutropy.com": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "10.5.101.26": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    },

    "live-push2.cloutropy.com": {
        "10.5.101.25": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "10.5.101.26": {
            "comment": "",
            "province_list": PROVINCE_LIST
        },
        "default": {
            "comment": "",
            "default_push_ip": ["10.5.101.25"]
        }
    }

}



