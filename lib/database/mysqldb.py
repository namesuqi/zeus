# coding=utf-8
__author__ = 'zengyuetian'

'''
操作Mysql的底层库
'''


import MySQLdb
import time
from lib.constant.database import *
from lib.decorator.singleton import singleton

#@singleton
class MysqlDB(object):
    def __init__(self, host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_BOSS):
        start = time.time()
        print "Connect to mysql database by {0}, it should be only call one time!!!".format(user)
        self._db = MySQLdb.connect(host, user, password, database)
        self._cursor = self._db.cursor()
        end = time.time()
        print "Connection cost {0} seconds.".format(start - end)

    def __del__(self):
        self._db.close()

    def create_database(self, name):
        sql = "create database {0}".format(name)
        self._cursor.execute(sql)
        self._db.commit()

    def drop_database(self, name):
        sql = "drop database if exists {0}".format(name)
        self._cursor.execute(sql)
        self._db.commit()

    def drop_table(self, name):
        sql = "drop table if exists {0}".format(name)
        self._cursor.execute(sql)
        self._db.commit()

    def clear_table(self, name):
        sql = "delete from {0}".format(name)
        self._cursor.execute(sql)
        self._db.commit()

    def insert(self, table, **kwags):
        '''
        新增一行数据
        :param table:表
        :param kwags:
        :return:void
        '''
        values = [kwags[key] for key in kwags]
        keys = '('
        for key in kwags:
            keys += key
            keys += ','
        keys = keys[0:-1]  # remove "," from the end
        keys += ')'
        values_clause = str(tuple(values))

        # 如果只有一项，那么删除tuple函数自动加上的逗号
        if len(values) < 2:
            print "enter"
            values_clause = values_clause.replace(',', '')

        sql = 'INSERT INTO {0}{1} VALUES{2}'.format(table, keys, values_clause)
        print sql
        self._cursor.execute(sql)
        self._db.commit()

    def update(self, table, field, value_clause, **kwags):
        '''
        更新一条数据
        :param table:表
        :param kwags:
        :return:void
        '''
        sentence = ''

        if kwags:
            for key in kwags:
                value = '\'' + str(kwags[key]) + '\''
                sentence = '{0} {1}={2} AND'.format(sentence, key, value)
            sentence = sentence[0:-4]
            sql = 'UPDATE {0} SET {1} = {2} WHERE {3}'.format(table, field, value_clause, sentence)
        else:
            sql = 'UPDATE {0} SET {1} = {2}'.format(table, field, value_clause)

        print sql
        self._cursor.execute(sql)
        self._db.commit()

    def delete(self, table, **kwags):
        '''
        删除满足条件的数据
        :param table:表
        :param kwags:字典条件
        :return:void
        '''
        sentence = ''
        # create the "where" clause
        # 判断是否有参数，若有参数，则删除对应参数的数据，若无参数，则删除整张表
        if kwags:
            for key in kwags:
                value = '\'' + str(kwags[key]) + '\''
                sentence = '{0} {1}={2} AND'.format(sentence, key, value)
            sentence = sentence[0:-4]  # remove "AND" from end
            sql = 'DELETE FROM {0} WHERE {1}'.format(table, sentence)
        else:
            sql = 'DELETE FROM {0} '.format(table, sentence)
        print sql
        self._cursor.execute(sql)
        self._db.commit()

    def delete_except(self, table, **kwags):
        '''
        删除不满足条件的所有数据(慎重使用)
        :param table:表
        :param kwags:字典条件
        :return:void
        '''
        sentence = ''
        for key in kwags:
            value = '\'' + str(kwags[key]) + '\''
            sentence = '{0} {1}!={2} AND'.format(sentence, key, value)
        sentence = sentence[0:-4]  # remove "AND" from end
        sql = 'DELETE FROM {0} WHERE {1}'.format(table, sentence)
        print sql
        self._cursor.execute(sql)
        self._db.commit()

    def select(self, table, *args, **kwags):
        '''
        查询某些列的数据
        :param table: 表
        :param args: 列
        :param kwags: 条件
        :return:
        '''
        columns = ''
        for arg in args:
            columns = '{0}{1}{2}'.format(columns, arg, ',')
        columns = columns[0:-1]  # remove "," from the end
        sentence = ''
        for key in kwags:
            value = '\'' + str(kwags[key]) + '\''
            sentence = '{0} {1}={2} AND'.format(sentence, key, value)
        sentence = sentence[0:-4]
        if '' == sentence:
            sql = 'SELECT {0} FROM {1}'.format(columns, table)
        else:
            sql = 'SELECT {0} FROM {1} WHERE {2}'.format(columns, table, sentence)
        print sql
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def fuzzy_select(self, table, condition, *args):
        """
        for fuzzy query
        :param table:
        :param condition:
        :param args:
        :return:
        """
        columns = ''
        for arg in args:
            columns = '{0}{1}{2}'.format(columns, arg, ',')
        columns = columns[0:-1]  # remove "," from the end
        if '' == condition:
            sql = 'SELECT {0} FROM {1}'.format(columns, table)
        else:
            sql = 'SELECT {0} FROM {1} WHERE {2}'.format(columns, table, condition)
        print sql
        self._cursor.execute(sql)
        return self._cursor.fetchall()



if __name__ == "__main__":
    print MysqlDB.select("ppc_user_files", "*", file_id="F25A31CC371B43258EB8BCE084278B04")
    MysqlDB.insert("ppc_users", username="leigang1", password='leigang1', phoneNum="123456")
    #MysqlDB.delete("ppc_users", username='leigang1')









