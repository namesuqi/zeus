# coding=utf-8
"""
本文件用于rpc远程控制
现阶段只用于以下用例：
    1. 视频直播测试

__author__ = 'zengyuetian'

"""


from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import Binary
import datetime
import os



class RpcService:
    def execute(self, command):
        result = os.popen(command, 'r').read()
        return result

    def ping(self):
        return True

    def now(self):
        return datetime.datetime.now()

    def show_type(self, arg):
        return (str(arg), str(type(arg)), arg)

    def raises_exception(self, msg):
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        data = bin.data
        response = Binary(data)
        return response

if __name__ == "__main__":
    server = SimpleXMLRPCServer(('0.0.0.0', 19527),
                                logRequests=True,
                                allow_none=True)

    server.register_introspection_functions()
    server.register_multicall_functions()

    server.register_instance(RpcService())

    try:
        print 'use control-c to exit'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'exiting'




