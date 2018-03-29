# coding=utf-8
"""
通过ORM库操作mysql数据库

__author__ = 'zengyuetian'

"""

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DB_CONNECT_STRING = 'mysql+mysqldb://ppc:yunshang2014@10.5.0.55:3306/tbbox'

class User(Base):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __init__(self, id, name):
        self.id = id
        self.name = name

class User1(Base):
    __tablename__ = "user1"

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __init__(self, id, name):
        self.id = id
        self.name = name



class MysqlORM(object):
    def __init__(self):
        self.engine = create_engine(DB_CONNECT_STRING, echo=True)
        # create DBSession type
        self.DBSession = sessionmaker(bind=self.engine)


    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def add(self, name):
        self.session = self.DBSession()
        self.session.add(name)
        self.session.commit()
        self.session.close()








if __name__ == "__main__":
    new_user = User(id='15', name='bob')
    orm = MysqlORM()
    orm.create_tables()

