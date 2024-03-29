#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hive util with hive server2


import pyhs2

class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):
        """
        query
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetch()

    def close(self):
        """
        close connection
        """
        self.conn.close()


def main():
    """
    main process
    @rtype:
    @return:
    @note:

    """
    hive_client = HiveClient(db_host='192.168.1.197', port=9083, user='root', password='root',
                             database='defalut', authMechanism='PLAIN')
    result = hive_client.query('select * from t_test limit 10')
    print result
    hive_client.close()


if __name__ == '__main__':
    main()
