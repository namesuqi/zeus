# coding=utf-8
# author: zengyuetian

import time

def get_log_time():
    temp_timestamp = time.time()
    ret_str = time.strftime("%H:%M:%S", time.localtime(temp_timestamp))
    ret_str += str("%.3f" % temp_timestamp)[-4:]
    return int(temp_timestamp * 1000), ret_str


print get_log_time()
