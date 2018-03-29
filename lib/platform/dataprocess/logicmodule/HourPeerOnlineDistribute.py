import sys
import os
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1],"w") as expectedfile:
        resultlist = {}
        peeridlist= {}
        totallist={}

        for line in orglines:
            _,timesp,peerid,quarter,online,_,_= line.split(',')
            if int(online)==1:
                username=datavars.name_list[peerid[:8]]
                if (4 * (hour+1)) > int(quarter) >= (hour * 4):
                    if hour not in peeridlist:
                        peeridlist[hour] = []
                    if hour not in resultlist:
                        resultlist[hour] = {}
                    if hour not in totallist:
                            totallist[hour]={}
                    if peerid not in peeridlist[hour]:
                        peeridlist[hour].append(peerid)
                        resultlist[hour][username] = resultlist[hour].setdefault(username, 0) + 1
                        totallist[hour]['all']=totallist[hour].setdefault('all', 0) + 1

        if hour > -1:
            for username, count in resultlist[hour].items():
                expectedfile.write('%s,%s,%d\n' % (hour,username,count))
            for all, count in totallist[hour].items():
                expectedfile.write('%s,%s,%d\n' % (hour,'all',count))
        else:
            for hour, values in resultlist.items():
                for username, count in values.items():
                    expectedfile.write('%s,%s,%d\n' % (hour,username,count))

            for hour,count in totallist.items():
                expectedfile.write('%s,%s,%d\n' % (hour,'all',count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

