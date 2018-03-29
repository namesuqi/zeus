# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

import xmlrpclib
server = xmlrpclib.ServerProxy('http://10.6.111.1:19527')
server.StartAllVlcProcess(4, "http://", "admin")
#print server.execute("touch /root/1.txt1")