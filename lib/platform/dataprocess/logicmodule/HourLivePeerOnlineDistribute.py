import sys
import os

import constvars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import testdata.datavars as datavars
from commonfunc import get_timestamp_by_time

time_format = constvars.recorddate + '000001'
timestamp = long(get_timestamp_by_time(time_format)[:-3])

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/LiveProgressCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    peeridlist=[]
    resultlist={}
    alllist={}
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,timesp,peerid,_,_,_,_,_= line.split(',')
            if (timestamp + 3600*(hour+1)) > long(timesp[:-3]) >= (timestamp + 3600*hour):
                if peerid not in peeridlist:
                    peeridlist.append(peerid)
                    username=datavars.name_list[peerid[:8]]
                    resultlist[username]=resultlist.setdefault(username, 0) + 1
                    alllist['all']=alllist.setdefault('all', 0)+1

        for username,count in resultlist.items():
            expectedfile.write(("%s,%s,%d\n")%(hour,username,count))
        expectedfile.write(("%s,%s,%d\n")%(hour,'all',alllist['all']))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]




