#!/usr/bin/env bash
# author: Zeng YueTian
# date: 2016/03/20

# kill previous process
ps aux | grep live_agent |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9
ps aux | grep live_start |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9

# start agent in background
echo agent starting
(
    python live_start.py
)

# print process information
ps aux | grep live_start |grep -v grep

