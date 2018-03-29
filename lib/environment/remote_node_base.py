# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

class RemoteNodeBase(object):
    ip = ""
    user = ""
    password = ""

    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

