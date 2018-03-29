# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170817

作用: 设定基本的日志格式

"""

start_statement = "\n\n\ntopic -- peer_info: {0[peer_info]} | heartbeat: {0[heartbeat]} | lf_report: {0[lf_report]} | \
live_report: {0[live_report]} | timestamp: {1}"  # .format(topics, get_millisecond_now())

# info
peer_online_info = "peer_info - info - peer_id: {0[peer_id]} \t ssid: {0[ssid]} \t ( province, isp ): \
( {0[province_id]}, {0[isp_id]} ) \t sdk_version: {0[sdk_version]} \t timestamp: {0[timestamp]}"  # .format(peer_log)

# send

# round

# ready & start & quit











