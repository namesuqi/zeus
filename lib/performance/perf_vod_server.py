# coding=utf-8
"""
点播服务器性能测试主类

__author__ = 'zengyuetian'

"""

from lib.performance.perf_base import *
from lib.performance.perf_node import *
from lib.utility.path import *
import subprocess
import time

class VodServerPerformanceTest(BasePerformanceTest):
    def deploy_agent(self, perf_nodes):
        '''
        获得当前路径，然后将文件通过sshpass复制到远程机器，并且启动rpcserver
        :param perf_nodes:
        :return:
        '''
        root_path = PathController.get_root_path()

        command_list = []
        for node in perf_nodes:
            print "deploy_agent for {0}".format(node.ip)
            command_list.append(
                'sshpass -p {0} ssh -o StrictHostKeyChecking=no {1}@{2} "rm -rf ~/zeus_agent; mkdir ~/zeus_agent"'.format(
                    node.password, node.user, node.ip))
            command_list.append(
                'sshpass -p {0} scp -r {3}/lib/zeus_agent/perf_* {1}@{2}:~/zeus_agent'.format(node.password, node.user,
                                                                                              node.ip, root_path))
            command_list.append(
                'sshpass -p {0} ssh {1}@{2} "chmod -R 755 ~/zeus_agent; cd ~/zeus_agent; ./perf_restart.sh > /dev/null 2>&1"'.format(
                    node.password, node.user, node.ip))
            for command in command_list:
                p = subprocess.Popen(command, shell=True)
                p.wait()  # 等待进程结束，防止针对同一台机器的指令并发执行
                print command

    def prepare_environment(self):
        pass

    def prepare_test(self):
        # 控制性能测试机器
        while True:
            time.sleep(1)
            for node in perf_nodes:
                print "Start for {0}".format(node.ip)
                node.start_collect_param()



    def run_test(self):
        pass

    def stop_test(self):
        pass

    def collect_log(self):
        pass

    def parse_result(self):
        pass

    def archive_result(self):
        pass






if __name__ == "__main__":
    VodServerPerformanceTest().prepare_environment()
    # wait rpc service already get started
    time.sleep(1)
    VodServerPerformanceTest().prepare_test()


