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
            peerid, timesp, url, _, playtype, p2pdown, cdndown, _, _, _ = line.split(',')
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
                    if url not in resultlist[i][tmpusername][playtype]:
                        resultlist[i][tmpusername][playtype][url] = {}
                    if playtype not in totallist[i]:
                        totallist[i][playtype] = {}
                    if url not in totallist[i][playtype]:
                        totallist[i][playtype][url] = {}
                    resultlist[i][tmpusername][playtype][url]['p2pdown'] = resultlist[i][tmpusername][playtype][url].setdefault(
                        'p2pdown', 0L) + long(p2pdown)
                    resultlist[i][tmpusername][playtype][url]['totaldown'] = resultlist[i][tmpusername][playtype][url].setdefault(
                        'totaldown', 0L) + long(cdndown) + long(p2pdown)

                    totallist[i][playtype][url]['p2pdown'] = totallist[i][playtype][url].setdefault(
                        'p2pdown', 0L) + long(p2pdown)
                    totallist[i][playtype][url]['totaldown'] = totallist[i][playtype][url].setdefault(
                        'totaldown', 0L) + long(cdndown) + long(p2pdown)
                    break

        if hour > -1:
            currentresultlist = {}
            currenttotallist = {}

            for index in range(hour+1):
                for username, ptypes in resultlist[index].items():
                    for ptype, urls in ptypes.items():
                        for url, values in urls.items():
                            if username not in currentresultlist:
                                currentresultlist[username] = {}
                            if ptype not in currentresultlist[username]:
                                currentresultlist[username][ptype] = {}
                            if url not in currentresultlist[username][ptype]:
                                currentresultlist[username][ptype][url] = {}
                            if ptype not in currenttotallist:
                                currenttotallist[ptype] = {}
                            if url not in currenttotallist[ptype]:
                                currenttotallist[ptype][url] = {}
                            currentresultlist[username][ptype][url]['p2pdown'] = currentresultlist[username][ptype][url].setdefault(
                                'p2pdown', 0L) + values.setdefault('p2pdown', 0L)
                            currentresultlist[username][ptype][url]['totaldown'] = currentresultlist[username][ptype][url].setdefault(
                                'totaldown', 0L) + values.setdefault('totaldown', 0L)
                            currenttotallist[ptype][url]['p2pdown'] = currenttotallist[ptype][url].setdefault(
                                'p2pdown', 0L) + values.setdefault('p2pdown', 0L)
                            currenttotallist[ptype][url]['totaldown'] = currenttotallist[ptype][url].setdefault(
                                'totaldown', 0L) + values.setdefault('totaldown', 0L)

            for username, ptypes in currentresultlist.items():
                for ptype, urls in ptypes.items():
                    for url, values in urls.items():
                        if values.setdefault('totaldown', 0) != 0:
                            expectedfile.write('%s,%s,%f,%s\n' % (username, url, float(values.setdefault('p2pdown', 0))/float(
                                values.setdefault('totaldown', 0)), ptype))
            for ptype, urls in currenttotallist.items():
                for url, values in currenttotallist.items():
                    if values.setdefault('totaldown', 0) != 0:
                        expectedfile.write('%s,%s,%f,%s\n' % ('all', url, float(values.setdefault('p2pdown', 0))/float(
                                values.setdefault('totaldown', 0)), ptype))
        else:
            pass
            # print('it should be an hour job not for all day!')
            # return

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(23)

if __name__ == "__main__":
    main()
