import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import testdata.datavars as datavars

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/ClientExceptionCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,errtime,peerid,_,_,_,_,_,ip,_,_,_,mac1,mac2,optype,errcode,errmsg,_,_,type = line.split(',')
            type = type.replace('\n', '')
            mac1 = mac1[:-1]
            province=datavars.ip2isp[ip].split(',')[0]
            isp=datavars.ip2isp[ip].split(',')[1]
            expectedfile.write(("%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%s\n")%(peerid,errmsg,optype,errcode,errmsg,int(errtime),mac1,mac2,ip,province,isp,peerid[:8],type))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]


