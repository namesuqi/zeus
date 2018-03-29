import os


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r') as resultfile:
         orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        onlinetime = {}
        peeridlist = []
        for line in orglines:
            _, timesp, peerid, quarter, online, _, _ = line.split(',')
            if hour > -1:
                if int(online) == 1 and hour >= int(quarter)/4:
                    usernum = peerid[:8]
                    onlinetime[usernum] = onlinetime.setdefault(usernum, 0) + 900
                    if peerid not in peeridlist:
                        resultlist[usernum] = resultlist.setdefault(usernum, 0) + 1
                        peeridlist.append(peerid)
            else:
                if int(online) == 1:
                    usernum = peerid[:8]
                    onlinetime[usernum] = onlinetime.setdefault(usernum, 0) + 900
                    if peerid not in peeridlist:
                        resultlist[usernum] = resultlist.setdefault(usernum, 0) + 1
                        peeridlist.append(peerid)
        totalcount = 0
        totaltime = 0
        for usernum, count in resultlist.items():
            totalcount += count
            totaltime += onlinetime.setdefault(usernum, 0)
            expectedfile.write('%s,%f,%d\n' % (usernum, float(onlinetime[usernum])/float(count),count))
        expectedfile.write('%s,%f,%d\n' % ('99999999', float(totaltime)/float(totalcount),totalcount))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

