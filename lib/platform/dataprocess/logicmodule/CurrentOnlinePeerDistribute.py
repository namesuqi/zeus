import sys
import os

import constvars
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

time_format = constvars.recorddate + '000001'
timestamp = long(get_timestamp_by_time(time_format)[:-3])

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    resultlist={}
    peeridlist={}
    totallist={}
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,timesp,peerid,quarter,online,_,_= line.split(',')
            if int(online) == 1:
                if (4 * (hour+1)) > int(quarter) >= (hour * 4):
                    if hour not in peeridlist:
                        peeridlist[hour] = []
                    if hour not in resultlist:
                        resultlist[hour]={}
                    if hour not in totallist:
                        totallist[hour]={}
                    if peerid not in peeridlist[hour]:
                        peeridlist[hour].append(peerid)
                        username=datavars.name_list[peerid[:8]]
                        resultlist[hour][username]=resultlist[hour].setdefault(username,0)+1
                        totallist[hour]['all']=totallist[hour].setdefault('all',0)+1

        if hour>-1:
            for username,count in resultlist[hour].items():
                expectedfile.write(("%s,%d,%s\n")%(username,count,None))
            expectedfile.write(("%s,%d,%s\n")%('all',totallist[hour]['all'],None))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]



