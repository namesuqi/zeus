import sys
import os

import constvars
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

time_format = constvars.recorddate + '000001'
timestamp = long(get_timestamp_by_time(time_format)[:-3])

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/FileOnDemandCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    resultlist={}
    peeridlist={}
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,peerid,timesp,_,_,publicip,_,_,_= line.split(',')
            for i in range(24):
                if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                    if i not in peeridlist:
                        peeridlist[i] = {}
                    if i not in resultlist:
                        resultlist[i] = {}
                    province = datavars.ip2isp[publicip].split(',')[0]
                    if province not in peeridlist[i]:
                        peeridlist[i][province] = []
                    if peerid not in peeridlist[i][province]:
                        userno = peerid[:8]
                        username = datavars.name_list[userno]
                        if province not in resultlist[i]:
                            resultlist[i][province] = {}
                        if username not in resultlist[i][province]:
                            resultlist[i][province][username] = 1
                        else:
                            resultlist[i][province][username] += 1
                    peeridlist[i][province].append(peerid)
                    break

        if hour > -1:
            for pro, value in resultlist[hour].items():
                totalcount = 0
                for username, count in value.items():
                    totalcount += count
                    expectedfile.write("%s,%s,%d\n" % (pro, username, count))
                expectedfile.write("%s,%s,%d\n" % (pro, 'all', totalcount))
        else:
            pass

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]





