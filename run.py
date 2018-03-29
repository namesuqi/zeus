#!/usr/bin/env python
# coding=utf-8
"""
Purpose:
The test entrance for System Testing

Precondition:
vi ~/.bashrc
export PYTHONPATH=.

then execute:
source ~/.bashrc

Usage：
******************************************************
python run.py type -i test_case_tag
    or
python run.py type test_case_tag
    or
python run.py type -t test_case_name
    or
python run.py type -s test_suite_name

for example:

python run.py server [regression|account|dir|...]
python run.py sdk [sdk|...]
python run.py system [...]
python run.py dummy [...]              # test pre-condition is empty

python run.py leifeng [start_leifeng|stop_leifeng|restart_leifeng]
python run.py idc [start_idc|stop_idc|restart_idc]
python run.py live [start_peer|stop_peer|restart_peer]
python run.py vod [start_vod|stop_vod|restart_vod]

******************************************************
__author__ = 'zengyuetian'

"""

from lib.framework.executor_factory import *

if __name__ == "__main__":
    # run robot framework test case via tag/test/suite
    # default is via tag
    robot_type = "tag"

    if len(sys.argv) > 1:
        executor_name = sys.argv[1]
        if len(sys.argv) > 2:
            tags = sys.argv[2:]
            # if the command is "python run.py server -t xxxx" or "python run.py server -s xxxx"
            if tags[0] == '-t':
                robot_type = 'case'
                tags = tags[1:]
            elif tags[0] == '-s':
                robot_type = 'suite'
                tags = tags[1:]
            elif tags[0] == '-i':
                robot_type = 'tag'
                tags = tags[1:]
        else:
            # default tag is "regression"
            tags = ["regression"]

        # Factory design pattern to create various executor
        test_executor = ExecutorFactory.make_executor(executor_name)

        print "Prepare Test Environment"
        test_executor.prepare_environment()

        # for vod, live, leifeng, idc
        if (isinstance(test_executor, ExecutorIdc) or isinstance(test_executor, ExecutorLeifeng)
            or isinstance(test_executor, ExecutorLive) or isinstance(test_executor, ExecutorVod)
            ) \
                and (tags[0] == "restart_idc" or tags[0] == "stop_idc" or tags[0] == "stop_some_idc"
                     or tags[0] == "restart_leifeng" or tags[0] == "stop_leifeng" or tags[0] == "stop_some_leifeng"
                     or tags[0] == "restart_peer" or tags[0] == "stop_peer"
                     or tags[0] == "restart_vod" or tags[0] == "stop_vod"
                     ):
            # don't deploy agent and sdk to save time
            pass
        else:
            test_executor.deploy_agent()
            test_executor.deploy_sdk()

        # start robot framework to run test cases
        test_executor.start_robot_framework(robot_type, tags)
        # copy test log to apache folder
        # test_executor.collect_result()
    else:
        print "Please specify at least one test type as following:"
        print "python run.py server"
