# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

from lib.database.redisdb import RedisDB

RedisDB.connect()
RedisDB.set("Hello", "world")
print RedisDB.get("Hello")
print RedisDB.get("test")

