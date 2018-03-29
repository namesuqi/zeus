import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/DownloadFlowCleaned.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        totallist = {}
        for line in orgdownlines:
            peerid, timesp, _, _, playtype, p2pdown, cdndown, _, _, _ = line.split(',')
            for i in range(24):
                if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                    if i not in resultlist:
                        resultlist[i] = {}
                    if i not in totallist:
                        totallist[i] = {}
                    tmpusername = datavars.name_list[peerid[:8]]
                    if tmpusername not in resultlist[i]:
                        resultlist[i][tmpusername] = {}
                    if playtype not in resultlist[i][tmpusername]:
                        resultlist[i][tmpusername][playtype] = {}
                    if playtype not in totallist[i]:
                        totallist[i][playtype] = {}
                    resultlist[i][tmpusername][playtype]['p2pdown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'p2pdown', 0L) + long(p2pdown)
                    resultlist[i][tmpusername][playtype]['totaldown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'totaldown', 0L) + long(cdndown) + long(p2pdown)

                    totallist[i][playtype]['p2pdown'] = totallist[i][playtype].setdefault('p2pdown', 0L) + long(p2pdown)
                    totallist[i][playtype]['totaldown'] = totallist[i][playtype].setdefault('totaldown', 0L) + long(cdndown) + long(p2pdown)
                    break

        if hour > -1:
            for username, ptypes in resultlist[hour].items():
                for ptype, values in ptypes.items():
                    expectedfile.write('%s,%d,%f,%s\n' % (username, hour, float(values.setdefault('p2pdown', 0))/float(
                        values.setdefault('totaldown', 0)), ptype))
            for ptype, values in totallist[hour].items():
                expectedfile.write('%s,%d,%f,%s\n' % ('all', hour, float(values.setdefault('p2pdown', 0))/float(
                        values.setdefault('totaldown', 0)), ptype))
        else:
            for time, users in resultlist.items():
                for username, ptypes in users.items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%s,%d,%f,%s\n' % (username, hour, float(values.setdefault('p2pdown', 0))/float(
                            values.setdefault('totaldown', 0)), ptype))
            for time, ptypes in totallist.items():
                for ptype, values in ptypes.items():
                    expectedfile.write('%s,%d,%f,%s\n' % ('all', hour, float(values.setdefault('p2pdown', 0))/float(
                        values.setdefault('totaldown', 0)), ptype))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(23)

if __name__ == "__main__":
    main()
