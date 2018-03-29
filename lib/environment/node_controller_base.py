# coding=utf-8
"""

__author__ = 'zengyuetian'

"""

import xmlrpclib

class NodeControllerBase(object):
    '''
    '''
    def __init__(self, ip):
        self._ip = ip
        self._rpc_proxy = self.init_rpc_proxy()


    def init_rpc_proxy(self):
        '''
        init rpc server
        :return:void
        '''
        url = 'http://{0}:{1}'.format(self._ip, "19527")
        return xmlrpclib.ServerProxy(url)













