import re
import os
from pipeofodps import MysqlDbObj

# basic compare result way for local odps compare or local mysql compare or odps-download compare(for those cases whose items in odps and mysql are different)
def compareresult(jobname):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        reline = reline.replace('\r', '')
        for dbline in dblines:
            if dbline.find(reline.replace('\n', '')) > -1:
                dblines.remove(dbline)
                findcount += 1
                break

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False



def compareresultmysql(jobname, selectsql, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile(selectsql, filepath):
        return compareresult(jobname)
    else:
        return False


def compareresultodps(jobname):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sODPS.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            if dbline.find(reline.replace('\n', '')) > -1:
                dblines.remove(dbline)
                findcount += 1
                break

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False

# compare result in pattern match way, including local odps way or local mysql way or odps-download way(for those cases whose items in odps and mysql are different)
def compareresultpatternmysql(jobname, selectsql, patternformat, index, cutlen, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile( selectsql, filepath):
        return compareresultpattern(jobname, patternformat, index, cutlen)
    else:
        return False


def compareresultpatternlistmysql(jobname, selectsql, patternformat, indexs, cutlens, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile( selectsql, filepath):
        return compareresultpatternlist(jobname, patternformat, indexs, cutlens)
    else:
        return False


def compareresultpatternodps(jobname, patternformat, index, cutlen):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sODPS.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            reline = reline.replace('\n', '')
            tmparray = reline.split(',')
            tmparray[index] = patternformat % tmparray[index][:cutlen]
            patternstr = ','.join(tmparray)
            m = re.match(patternstr, dbline)
            if m:
                dblines.remove(dbline)
                findcount += 1
                break
        else:
            print patternstr

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False


def compareresultpattern(jobname, patternformat, index, cutlen):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            reline = reline.replace('\n', '')
            tmparray = reline.split(',')
            tmparray[index] = patternformat % tmparray[index][:cutlen]
            patternstr = ','.join(tmparray)
            m = re.match(patternstr, dbline)
            if m:
                dblines.remove(dbline)
                findcount += 1
                break
        else:
            print patternstr

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False


def compareresultpatternlist(jobname, patternformat, indexs, cutlens):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            reline = reline.replace('\n', '')
            tmparray = reline.split(',')
            # tmparray[index] = patternformat % tmparray[index][:cutlen]
            for index in range(len(indexs)):
                tmparray[indexs[index]] = patternformat % tmparray[indexs[index]][:cutlens[index]]
            patternstr = ','.join(tmparray)
            m = re.match(patternstr, dbline)
            if m:
                dblines.remove(dbline)
                findcount += 1
                break
        else:
            print patternstr

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False

# compare result in abs pattern , including int and float error range
def compareresultabspatternmysql(jobname, selectsql, index, range, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile(selectsql, filepath):
        return compareresultabspattern(jobname, index, range)
    else:
        return False


def compareresultabspattern(jobname, index, range):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            reline = reline.replace('\n', '')
            if(abs(float(reline.split(',')[index])-float(dbline.split(',')[index]))<= range) :
                dblines.remove(dbline)
                findcount += 1
                break
        else:
            print abs(float(reline.split(',')[index])-float(dbline.split(',')[index]))

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False

# compare result in abs pattern list , including int and float error range
def compareresultabspatternlistmysql(jobname, selectsql, indexs, range, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile(selectsql, filepath):
        return compareresultabspatternlist(jobname, indexs, range)
    else:
        return False


# def compareresultabspatternlist(jobname, indexs, acprange):
#     with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
#         resultlines = resultfile.readlines()
#
#     with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
#         dblines = dbfile.readlines()
#
#     findcount = 0
#     count = 0
#     length = len(indexs)
#     for reline in resultlines:
#         reline = reline.replace('\n', '')
#         for dbline in dblines:
#             dbline = dbline.replace('\n', '')
#             for index in range(length):
#                 if(reline.split(',')[-1] == dbline.split(',')[-1] and reline.split(',')[-5] == dbline.split(',')[-5] and reline.split(',')[0] == dbline.split(',')[0]):
#                     if(abs(float(reline.split(',')[indexs[index]])-float(dbline.split(',')[indexs[index]]))<= acprange):
#                         count += 1
#                         continue
#                 if count == length:
#                     dbline = dbline + '\n'
#                     dblines.remove(dbline)
#                     count = 0
#                     findcount += 1
#                     break
#                 if index == length-1:
#                     count = 0
#                     break
#         else:
#             print reline
#
#     if findcount == len(resultlines):
#         print 'Job task %s compare result Pass' % jobname
#         return True
#     else:
#         print 'Job task %s compare result Failed' % jobname
#         return False

def compareresultabspatternlist(jobname, indexs, range):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for reline in resultlines:
        for dbline in dblines:
            reline = reline.replace('\n', '')
            dbline = dbline.replace('\n', '')
            if (reline.split(',')[-1] == dbline.split(',')[-1] and reline.split(',')[-5] == dbline.split(',')[-5] and reline.split(',')[0] == dbline.split(',')[0]):

                if(abs(float(reline.split(',')[indexs[0]])-float(dbline.split(',')[indexs[0]]))<= range and
                   abs(float(reline.split(',')[indexs[1]])-float(dbline.split(',')[indexs[1]]))<= range and
                   abs(float(reline.split(',')[indexs[2]])-float(dbline.split(',')[indexs[2]]))<= range) :
                    dbline += '\n'
                    dblines.remove(dbline)
                    findcount += 1
                    break
        else:
            print reline

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False


# compare result in line number way
def compareresultlinenumbermysql(jobname, selectsql, filepath='default'):
    if filepath == 'default':
        filepath = os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname)
    mysqldb = MysqlDbObj()
    if mysqldb.selectdatatofile( selectsql, filepath):
        return compareresultlinenumber(jobname)
    else:
        return False


def compareresultlinenumber(jobname):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/%s.txt' % jobname), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/%sDB.txt' % jobname), 'r') as dbfile:
        dblines = dbfile.readlines()

    if len(resultlines) == len(dblines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False



def main():
    compareresult()

if __name__ == "__main__":
    main()
