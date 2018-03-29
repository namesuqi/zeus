import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/FileOnDemandCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()
    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1],"w") as expectedfile:
        resultlist = {}
        for line in orglines:
            _,peerid,timesp,_,_,_,_,_,_= line.split(',')
            for i in range(24):
                if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                    if i not in resultlist:
                        resultlist[i] = {}
                    resultlist[i][peerid[:8]] = resultlist[i].setdefault(peerid[:8], 0) + 1
                    break
        if hour > -1:
            for peerfix, count in resultlist[hour].items():
                expectedfile.write('%s,%s,%d\n' % (peerfix, hour, count))
        else:
            for time, values in resultlist.items():
                for peerfix, count in values.items():
                    expectedfile.write('%s,%s,%d,%s\n' % (peerfix, time, count,''))
    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]