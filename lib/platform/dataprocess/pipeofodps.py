import sys
import datetime
import constvars
from commonfunc import exec_odps_commands
from commonfunc import exec_odps_commands_notnull
import os
import MySQLdb
import platform
import xml.dom.minidom as minidom

class MysqlDbObj(object):

    dbconn = None

    def __init__(self):

        if platform.system() == "Windows":
            dom = minidom.parse('%s/misc/cnf/configure_win.xml' % os.path.abspath(os.path.dirname(__file__)))
        elif platform.system() == "Linux":
            dom = minidom.parse('%s/misc/cnf/configure_lin.xml' % os.path.abspath(os.path.dirname(__file__)))
        else:
            raise Exception("System nonsupport!")
        root = dom.documentElement
        bb = root.getElementsByTagName('host')
        host = bb[0].firstChild.data
        bb = root.getElementsByTagName('name')
        name = bb[0].firstChild.data
        bb = root.getElementsByTagName('username')
        username = bb[0].firstChild.data
        bb = root.getElementsByTagName('password')
        password = bb[0].firstChild.data
        self.hname = host
        self.user = username
        self.psword = password
        self.dbname = name
        print host, username, password, name
        try:
            if MysqlDbObj.dbconn is None:
                MysqlDbObj.dbconn = MySQLdb.connect(self.hname, self.user, self.psword, self.dbname)
        except MySQLdb.MySQLError:
            print 'connect mysql error, please check network or db status ...'
            MysqlDbObj.dbconn = None


    @classmethod
    def selectdatatofile(cls, selectsql, filepath):
        if cls.dbconn is not None:
            try:
                cursor = cls.dbconn.cursor()
                cursor.execute(selectsql)
                if filepath is not None:
                    datas = cursor.fetchall()
                    with open(filepath, 'w') as outputfile:
                        for data in datas:
                            outputfile.write(','.join([str(x) for x in data]) + '\n')
                return True
            except MySQLdb.MySQLError:
                print 'execute mysql query error, please check sql string...'
                return False

        else:
            return None

    @classmethod
    def executesql(cls, execsql):
        if cls.dbconn is not None:
            try:
                cursor = cls.dbconn.cursor()
                cursor.execute(execsql)
                cls.dbconn.commit()
                return True
            except MySQLdb.MySQLError:
                print 'execute mysql query error and db roll back, please check sql string...'
                cls.dbconn.rollback()
                return False
        else:
            return None


def uploaddatatoodps(tablename, filepathname, offsetbasedate=0, isnull= True):
#    droppartition = 'alter table %s drop if exists partition(recorddate=%s)' % (
#        tablename, str(int(constvars.recorddate) + int(offsetbasedate)))
    droppartition = 'alter table %s drop if exists partition(recorddate=%s)' % (
         tablename, (datetime.date(int(constvars.recorddate[0:4]),int(constvars.recorddate[4:6]),int(constvars.recorddate[6:])) + datetime.timedelta(days=int(offsetbasedate))).strftime('%Y%m%d'))
    print droppartition
    addpartition = 'alter table %s add partition(recorddate=%s)' % (
        tablename, (datetime.date(int(constvars.recorddate[0:4]),int(constvars.recorddate[4:6]),int(constvars.recorddate[6:])) + datetime.timedelta(days=int(offsetbasedate))).strftime('%Y%m%d'))
    print addpartition
    uploaddata = 'tunnel u %s %s/recorddate=%s' % (
        filepathname, tablename, (datetime.date(int(constvars.recorddate[0:4]),int(constvars.recorddate[4:6]),int(constvars.recorddate[6:])) + datetime.timedelta(days=int(offsetbasedate))).strftime('%Y%m%d'))
    commandlines = ';'.join((droppartition, addpartition, uploaddata))
    print uploaddata
    if isnull:
        exec_odps_commands('\"' + commandlines + '\"')
    else:
        exec_odps_commands_notnull('\"' + commandlines + '\"')


def downloaddatafromodps(tablename, filepathname, offsetbasedate=0, prefixfilepath='default'):
    if prefixfilepath == 'default':
        filepathname = os.path.dirname(__file__) + filepathname
    else:
        filepathname = prefixfilepath + filepathname
 #   downloaddata = 'tunnel d %s/recorddate=%s %s' % (tablename, str(int(constvars.recorddate) + int(offsetbasedate)), filepathname)
    downloaddata = 'tunnel d %s/recorddate=%s %s' % (tablename, (datetime.date(int(constvars.recorddate[0:4]),int(constvars.recorddate[4:6]),int(constvars.recorddate[6:])) + datetime.timedelta(days=int(offsetbasedate))).strftime('%Y%m%d'), filepathname)
    print downloaddata
    commandlines = ';'.join((downloaddata,))
    exec_odps_commands('\"' + commandlines + '\"')


def downloaddatafromodpsbypartten(tablename, filepathname, partitionpertten,  prefixfilepath='default'):
    if prefixfilepath == 'default':
        filepathname = os.path.dirname(__file__) + filepathname
    else:
        filepathname = prefixfilepath + filepathname
    downloaddata = 'tunnel d %s/%s %s' % (tablename, partitionpertten, filepathname)
    commandlines = ';'.join((downloaddata,))
    exec_odps_commands('\"' + commandlines + '\"')


def main():
    # tablename = sys.argv[1]
    # filepathname = sys.argv[2]
    tablename='input_vod_performance_cleaned'
    filepathname=r'DailyStartTimeCountDBWeek1.txt'
    uploaddatatoodps(tablename, filepathname,7)

if __name__ == "__main__":
    main()
