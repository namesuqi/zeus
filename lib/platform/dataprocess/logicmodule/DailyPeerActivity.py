import os


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        peeridlist = []
        for line in orglines:
            _, timesp, peerid, quarter, online, _, _ = line.split(',')
            if hour > -1:
                if int(online) == 1 and hour >= int(quarter)/4 and peerid not in peeridlist:
                    usernum = peerid[:8]
                    resultlist[usernum] = resultlist.setdefault(usernum, 0) + 1
                    peeridlist.append(peerid)
            else:
                if online == 1 and peerid not in peeridlist:
                    usernum = peerid[:8]
                    resultlist[usernum] = resultlist.setdefault(usernum, 0) + 1
                    peeridlist.append(peerid)
        totalcount = 0
        for usernum, count in resultlist.items():
            totalcount += count
            expectedfile.write('%s,%d\n' % (usernum, count))
        expectedfile.write('%s,%d\n' % ('99999999', totalcount))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

