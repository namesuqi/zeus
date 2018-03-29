# coding=utf-8
"""
idc control constant

__author__ = 'zengyuetian'

"""

# for seed node deploying
RPC_PORT = "19527"      # remote control port for RPC
IDC_USER = "admin"
IDC_PASSWORD = ""

# low_delay, high_delay, vod
# IDC_TYPE = "low_delay"
IDC_TYPE = "high_delay"
# IDC_TYPE = "vod"

if IDC_TYPE == "low_delay":
    IDC_IP_LIST = ['122.228.207.106', '115.238.245.25', '103.246.152.47', '112.54.205.251', "60.12.69.100"]
    IDC_SDK_NUM_LIST = [10, 10, 10]
elif IDC_TYPE == "high_delay":
    # IDC_IP_LIST = ['61.164.110.152', '123.157.28.160']
    # IDC_SDK_NUM_LIST = [10, 10]

    IDC_IP_LIST = ['60.169.74.3', '222.222.12.12', '101.254.185.18', '61.160.221.183', '61.191.61.133']
    IDC_SDK_NUM_LIST = [20, 30, 30, 10, 10]
elif IDC_TYPE == "vod":
    IDC_IP_LIST = ['122.226.181.111', '61.164.110.152', '123.157.28.160']
    IDC_SDK_NUM_LIST = [10, 10, 10, 10]


IDC_SDK_NUM_TO_KILL = [0, 0, 0, 0]


