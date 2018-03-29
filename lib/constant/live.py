# coding=utf-8
"""
live automation test constant

__author__ = 'zengyuetian'

"""

# ip addresses for seed
SEED_IP_LIST = ["10.6.110.1", "10.6.110.2", "10.6.110.3", "10.6.110.4", "10.6.110.5",
                "10.6.110.6", "10.6.110.7", "10.6.110.8"]
# how many sdk will be started on seed
SEED_SDK_NUM_LIST = [5, 5, 5, 5, 5,
                     5, 5, 5]

# ip addresses for peer

PEER_IP_LIST = ["10.5.101.14", "10.5.101.15", "10.5.101.16", "10.5.101.17", "10.5.101.18",
                "10.5.101.19", "10.5.101.20", "10.5.101.21", "10.5.101.22", "10.5.101.23"]
'''
PEER_IP_LIST = ["10.5.101.8", "10.5.101.9", "10.5.101.10", "10.5.101.11", "10.5.101.12"]
'''
# how many sdk will will be started on peer

PEER_SDK_NUM_LIST = [10, 10, 10, 10, 10,
                     10, 10, 10, 10, 10]
'''
PEER_SDK_NUM_LIST = [10, 10, 10, 10, 10]
'''
PEER_USER = "root"
PEER_PASSWORD = "Yunshang2014"


# live channels
LIVE_CHANNEL_1 = "http%3a%2f%2f114.55.51.164%3a80%2fhls%2fpanda.m3u8"        # 300K
LIVE_CHANNEL_2 = "http%3a%2f%2f114.55.51.164%3a80%2fhls%2ffengjing.m3u8"     # 2M
LIVE_CHANNEL_3 = "http%3a%2f%2f10.5.100.28%3a80%2fhls%2focean2.m3u8"          # 4M
LIVE_CHANNEL_4 = "http%3a%2f%2fsrs.cloutropy.com%3a80%2fhls%2ffengjing.m3u8"        # 2M
CHANNEL_TS = "channel.ts"
CHANNEL_M3U8 = "channel.m3u8"
CHANNEL_FLV = "channel.flv"
CHANNEL_HLS = "channelhls"
CHANNEL_INVALID = "http%3a%2f%2test.com"
EMPTY = ""
OUTPUT_URL = ""

#live user
LIVE_USER = "test"
WRONG_USER = "userwrong"

#live peers
LIVE_PID = "00010026408B9F4AB0E85524E25043D3"

# remote control port for RPC
RPC_PORT = "19527"


