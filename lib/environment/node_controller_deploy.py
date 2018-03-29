# coding=utf-8
"""

__author__ = 'zengyuetian'

"""

from lib.environment.node_controller_base import *

class NodeControllerDeploy(NodeControllerBase):
    '''
    '''
    def __init__(self, ip):
        super(NodeControllerDeploy, self).__init__(ip)

    def append_hosts(self, ip, host):
        self._rpc_proxy.execute("echo {0} {1} >> /etc/hosts".format(ip, host))


    ##############
    # For ubuntu #
    ##############

    def apt_update(self):
        print self._rpc_proxy.execute("apt-get update")

    def apt_install_htop(self):
        self._rpc_proxy.execute("apt-get install htop -y")

    def apt_install_iftop(self):
        self._rpc_proxy.execute("apt-get install iftop -y")

    def apt_install_vlc(self):
        self._rpc_proxy.execute("apt-get install vlc -y")

    def add_admin_on_ubuntu(self):
        self._rpc_proxy.execute("groupadd admin")
        self._rpc_proxy.execute("useradd -g admin admin")
        self._rpc_proxy.execute("mkdir /home/admin")
        self._rpc_proxy.execute("chown admin /home/admin")
        self._rpc_proxy.execute("chgrp admin /home/admin")


    ##############
    # For centos #
    ##############
    def yum_install_htop (self):
        self._rpc_proxy.execute("yum install htop -y")

    def yum_install_iftop(self):
        self._rpc_proxy.execute("yum install iftop -y")

    def add_admin_on_centos(self):
        self._rpc_proxy.execute("groupadd admin")
        self._rpc_proxy.execute("useradd -g admin admin")
        self._rpc_proxy.execute("chown admin /home/admin")















