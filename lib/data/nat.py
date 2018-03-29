# coding=utf-8
"""
NAT网络类型相关数据逻辑

__author__ = 'zengyuetian'

"""

def GetExpectedConnectStatus(nat_type1, nat_type2):
    """
        0   1   2   3   4
    0   Y   Y   Y   Y   Y
    1   Y   Y   Y   Y   Y
    2   Y   Y   Y   Y   Y
    3   Y   Y   Y   Y   N
    4   Y   Y   Y   N   N

    """
    if int(nat_type1) + int(nat_type2) >= 7:
        return "connecting"
    else:
        return "connected"

def IsExpectedConnect(nat_type1, nat_type2):
    """
        0   1   2   3   4
    0   Y   Y   Y   Y   Y
    1   Y   Y   Y   Y   Y
    2   Y   Y   Y   Y   Y
    3   Y   Y   Y   Y   N
    4   Y   Y   Y   N   N

    """
    if int(nat_type1) + int(nat_type2) >= 7:
        return False
    else:
        return True
