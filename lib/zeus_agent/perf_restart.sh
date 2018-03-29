#!/usr/bin/env bash
# author: Zeng YueTian
# date: 2015/12/31

############################################
# kill perf_agent process and then start it
############################################


# kill previous process
ps aux | grep perf_agent |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9
ps aux | grep perf_start |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9

# start zeus_agent in background
echo agent starting
(
    python perf_start.py
)

# print process information
ps aux | grep perf |grep -v grep

