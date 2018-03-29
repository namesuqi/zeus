import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/FileOnDemandCleaned.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        for line in orgdownlines:
            _, _, timesp, url, _, _, fileid, _, play_type = line.split(',')
            play_type = play_type.replace('\n', '')
            for i in range(24):
                if (timestamp + 3600*(i+1)) > long(timesp[:-3]) >= (timestamp + 3600*i):
                    if i not in resultlist:
                        resultlist[i] = {}
                    if url not in resultlist[i]:
                        resultlist[i][url] = {}
                    resultlist[i][url][play_type] = resultlist[i][url].setdefault(play_type, 0) + 1
                    break

        if hour > -1:
            for url, play_types in resultlist[hour].items():
                for play_type, count in play_types.items():
                    expectedfile.write('%s,%s,%d,%d,%s\n' % (url, datavars.url_username[url], count, hour, play_type))
        else:
            for time, urls in resultlist.items():
                for url, play_types in urls.items():
                    for play_type, count in play_types.items():
                        expectedfile.write('%s,%s,%d,%d,%s\n' % (url, datavars.url_username[url], count, time, play_type))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata()

if __name__ == "__main__":
    main()
