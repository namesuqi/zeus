# coding=utf-8
"""
get sdk memory info

__author__ = 'zengyuetian'

"""


import psutil
import re

if __name__ == "__main__":
    for proc in psutil.process_iter():
        proc_name = str(proc)
        f = re.compile("p2pclient_static", re.I)
        if f.search(proc_name):
            # get private memory of the process
            print proc.memory_info().shared
            break