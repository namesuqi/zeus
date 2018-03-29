#!/usr/bin/env bash
# author: Zeng YueTian
# date: 2015/12/31
# kill process and then start it

# kill previous process
ps aux | grep robot_agent |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9
ps aux | grep robot_start |grep -v grep |awk -F ' ' '{print $2}' | xargs kill -9

# start agent in background
echo agent starting
(
    python robot_start.py
)

# print process information
ps aux | grep robot_start |grep -v grep

