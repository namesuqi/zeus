# coding=utf-8
"""
操作MongoDB数据库的底层库

__author__ = 'zengyuetian'

"""

from pymongo import MongoClient
from lib.constant.database import *
from lib.decorator.singleton import singleton

@singleton
class MongoDB(object):

    def __init__(self, host=MONGODB_HOST, port=MONGODB_PORT):
        '''
        建立连接
        :param host:mongo服务器地址
        :param port:mongo服务器端口
        :return:void
        '''
        self.client = MongoClient(host, port)


    def get_all_collections(self, db):
        '''
        获得一个数据库中的所有集合名称
        :param db: 数据库
        :return:集合名称列表
        '''
        db = self.client[db]
        names = db.collection_names()
        return [str(name) for name in names]

    def get_one_doc(self, db, coll, condition=None):
        '''
        返回满足条件的一条记录
        :param db:数据库
        :param coll:集合
        :param condition:查询条件，dict
        :return:dict
        '''
        db = self.client[db]
        collection = db[coll]
        return collection.find_one(condition)

    def get_many_docs(self, db, coll, condition=None):
        '''
        将满足条件的记录都返回
        :param db:
        :param coll:
        :param condition:
        :return:列表
        '''
        db = self.client[db]
        collection = db[coll]
        result = []
        for item in collection.find(condition):
            result.append(item)
        return result


    def insert_one_doc(self, db, coll, doc):
        '''
        插入一个document
        :param db:数据库
        :param coll:集合
        :param doc:文档，一个dict
        :return:void
        '''
        # 选择库
        db = self.client[db]
        collection = db[coll]
        collection.insert_one(doc)

    def insert_multi_docs(self, db, coll, docs):
        '''
        批量插入documents,插入一个数组
        :param db:数据库
        :param coll:集合
        :param docs:文档集合，dict的列表
        :return:void
        '''
        db = self.client[db]
        collection = db[coll]
        collection.insert(docs)


    def clear_coll_datas(self, db, coll):
        '''
        清空一个集合中的所有数据
        :param db:数据库
        :param coll:集合
        :return:void
        '''
        db = self.client[db]
        collection = db[coll]
        collection.remove({})

    def delete_docs(self, db, coll, condition):
        '''
        清空满足条件的数据
        :param db:数据库
        :param coll:集合
        :condition:条件,dict
        :return:void
        '''
        db = self.client[db]
        collection = db[coll]
        collection.remove(condition)





######################################
# for unit testing
######################################
if __name__ == "__main__":

    data1 = {"peer_id": "0000000156BC45EE8F5AEA6A2866F111", "provinceId": 210000, "modifiedTime": "", "ip": "127.0.0.1", "version":"1.10.3", "lsmSize":1111}
    data2 = {"peer_id": "0000000156BC45EE8F5AEA6A2866F222", "provinceId": 210000, "modifiedTime": "", "ip": "127.0.0.1",
            "version": "1.10.3", "lsmSize": 1111}
    #MongoDB.insert_one_doc("cdn_peer", "cdn_peer", data1)
    #MongoDB.insert_multi_docs("cdn_peer", "cdn_peer", [data1, data2])
    #print MongoDB.get_all_collections("cdn_peer")

    # MongoDB.get_one_doc("cdn_peer", "cdn_peer", {"provinceId": 210000})
    print MongoDB.get_many_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})
    MongoDB.delete_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})
    print MongoDB.get_many_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})



