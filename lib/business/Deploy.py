# coding=utf-8
"""
Deploy related functions and keywords

__author__ = 'zengyuetian'

"""

from lib.decorator.trace import *
from lib.constant.deploy import *
from lib.environment.node_controller_deploy import *


class Deploy(object):
    '''
    install and config on remote machines
    '''

    def __init__(self):
        self.node_num = None
        self.node_list = None


    @print_trace
    def InitNodeDeploy(self, node_num):
        '''
        init node list
        :param node_num: node machine number
        :return:void
        '''
        self.node_num = int(node_num)
        self.node_list = []
        for i in range(self.node_num):
            node = NodeControllerDeploy(DEPLOY_IP_LIST[i])
            self.node_list.append(node)

    @print_trace
    def UpdateAptget(self):
        for node in self.node_list:
            node.apt_update()

    @print_trace
    def InstallVlcOnUbuntu(self):
        for node in self.node_list:
            node.apt_install_vlc()

    @print_trace
    def InstallHtopOnUbuntu(self):
        for node in self.node_list:
            node.apt_install_htop()

    @print_trace
    def InstallIftopOnUbuntu(self):
        for node in self.node_list:
            node.apt_install_iftop()

    @print_trace
    def AddAdminOnUbuntu(self):
        for node in self.node_list:
            node.add_admin_on_ubuntu()

    @print_trace
    def AppendHosts(self, ip, host):
        for node in self.node_list:
            node.append_hosts(ip, host)

    @print_trace
    def InstallHtopOnCentos(self):
        for node in self.node_list:
            node.yum_install_htop()

    @print_trace
    def InstallIftopOnCentos(self):
        for node in self.node_list:
            node.yum_install_iftop()

    @print_trace
    def AddAdminOnCentos(self):
        for node in self.node_list:
            node.add_admin_on_centos()












