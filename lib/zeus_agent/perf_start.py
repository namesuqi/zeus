#!/usr/bin/python
#coding=utf-8
# child process start rpc server and father process quit


import os

pid = os.fork()
if pid == 0:    # child
    os.system("python perf_agent.py >/dev/null 2>&1")
else:           # father
    exit()