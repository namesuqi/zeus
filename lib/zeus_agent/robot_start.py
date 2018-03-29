# coding=utf-8
# child process start robot_agent and father process quit

import os

pid = os.fork()
if pid == 0:    # child
    os.system("python robot_agent.py >/dev/null 2>&1")
else:           # father
    exit()