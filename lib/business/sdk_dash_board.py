# coding=utf-8
"""
通过SDK的dashboard获得SDK相关信息

__author__ = 'zengyuetian'

"""

from lib.request.http_request import *
from lib.constant.sdk import *
import time


send_from = "SdkDashBoard"
host = SDK1_IP
port = SDK1_DASH_BOARD_PORT

max_try = 5

login_url = "/ajax/login"
version_url = "/ajax/version"
index_url = "/dashboard/index"
httpd_url = "/ajax/httpd"
vod_core_url = "/ajax/vod_core"
chunk_buffer_url = "/dashboard/chunk_buffer"
chunk_pool_url = "/ajax/chunk_pool"
distribute_url = "/ajax/distribute"
meminfo_url = "/dashboard/meminfo"
profiling_url = "/ajax/profiling"
timer_url = "/dashboard/timer"
sched_url = "/dashboard/sched"
seeds_url = "/ajax/seeder"
offer_url = "/ajax/offer"
peers_url = "/dashboard/peers"
dccp_url = "/dashboard/dccp"
lsm_url = "/ajax/lsm"
help_url = "/ajax/help"
report_url = "/ajax/report"

    
def get_login():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, login_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_version():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, version_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_httpd():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, httpd_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_vod_core():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, vod_core_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_chunk_buffer():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, chunk_buffer_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_chunk_pool():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, chunk_pool_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_distribute():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, distribute_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_meminfo():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, meminfo_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_profiling():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, profiling_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_timer():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, timer_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_sched():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, sched_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_seeds():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, seeds_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_offer():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, offer_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_peers():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, peers_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_dccp():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, dccp_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_lsm():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, lsm_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_help():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, help_url)
            break
        except:
            time.sleep(0.1)
    return response.content


def get_report():
    response = None
    for i in range(max_try):
        try:
            response = send_request(send_from, 'HTTP', 'GET', host, port, report_url)
            break
        except:
            time.sleep(0.1)
    return response.content







###############################
# 调试用
###############################
if __name__ == "__main__":
    pass





