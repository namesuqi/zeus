import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerOnlineTimeCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    peeridlist = []
    if os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/MonthlyDistinctPeerID.txt'):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/MonthlyDistinctPeerID.txt', 'r') as resultfile1:
            orglines1 = resultfile1.readlines()
    else:
        orglines1 = []

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:

        for line in orglines1:
            peerid,_ = line.split(',')
            if peerid not in peeridlist:
                peeridlist.append(peerid)
                expectedfile.write('%s,%s\n' % (peerid,''))
            else:
                continue

        for line in orglines:
            _,_,peerid,_,_,_,_ = line.split(',')
            if peerid not in peeridlist:
                peeridlist.append(peerid)
                expectedfile.write('%s,%s\n' % (peerid,''))
            else:
                continue

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]








