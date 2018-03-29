import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/MonthlyDistinctPeerID.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    expectedfile = open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w")
    peeridprefix={}

    for line in orglines:
        peerid,_ = line.split(',')
        if peerid[:8] not in peeridprefix:
            peeridprefix[peerid[:8]] = 1
        else:
            peeridprefix[peerid[:8]] = peeridprefix[peerid[:8]] + 1

    for prefix,count in peeridprefix.items():
        expectedfile.write('%s,%d,%s\n' % (prefix,count,''))

    expectedfile.close()

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]








