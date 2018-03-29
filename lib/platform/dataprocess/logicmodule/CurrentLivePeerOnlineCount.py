import sys
import os

import constvars
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

time_format = constvars.recorddate + '000001'
timestamp = long(get_timestamp_by_time(time_format)[:-3])

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/LiveProgressCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    resultlist={}
    peeridlist={}
    totallist={}
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,timesp,peerid,_,_,_,_,_= line.split(',')
            for i in range(24):
                if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                    if i not in peeridlist:
                        peeridlist[i] = []
                    if i not in resultlist:
                        resultlist[i]={}
                    if i not in totallist:
                        totallist[i]={}
                    if peerid not in peeridlist[i]:
                        peeridlist[i].append(peerid)
                        username=datavars.name_list[peerid[:8]]
                        resultlist[i][username]=resultlist[i].setdefault(username,0)+1
                        totallist[i]['all']=totallist[i].setdefault('all',0)+1
                    break

        if hour>-1:
            for username,count in resultlist[hour].items():
                expectedfile.write(("%s,%d\n")%(username,count))
            for all,count in totallist[hour].items():
                expectedfile.write(("%s,%d\n")%('all',count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]



