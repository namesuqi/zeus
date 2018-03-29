# coding=utf-8
"""
replace target machines host with local copy

__author__ = 'zengyuetian'

"""

import inspect
import os
import sys
import subprocess

if __name__ == "__main__":
    '''
    ip_list = ["10.5.101.8", "10.5.101.9", "10.5.101.10", "10.5.101.11", "10.5.101.12",
               "10.5.101.14", "10.5.101.15", "10.5.101.16", "10.5.101.17", "10.5.101.18",
               "10.5.101.19", "10.5.101.20", "10.5.101.21", "10.5.101.22", "10.5.101.23",
               "10.5.101.24", "10.5.101.25", "10.5.101.26", "10.5.101.27", "10.5.101.28"]
    '''
    ip_list = ["10.5.101.8", "10.5.101.9", "10.5.101.10", "10.5.101.11", "10.5.101.12",
               "10.5.101.14", "10.5.101.15", "10.5.101.16", "10.5.101.17", "10.5.101.18",
               "10.5.101.19", "10.5.101.20", "10.5.101.21", "10.5.101.22", "10.5.101.23"]

    user = "root"
    password = "Yunshang2014"

    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    parent_path = os.path.dirname(file_path)
    local_file = parent_path + '/hosts'
    print "Host file is ", local_file

    for ip in ip_list:
        commands = list()
        print "------------------------------------"
        print "deploy_hosts for {0}".format(ip)
        commands.append(
            'sshpass -p {0} ssh -o StrictHostKeyChecking=no {1}@{2} "rm -rf /etc/hosts"'
                .format(password, user, ip))
        commands.append(
            'sshpass -p {0} scp {3} {1}@{2}:/etc/hosts'
                .format(password, user, ip, local_file))
        for command in commands:
            p = subprocess.Popen(command, shell=True)
            p.wait()  # wait process finish to avoid parallel execution
            print command



