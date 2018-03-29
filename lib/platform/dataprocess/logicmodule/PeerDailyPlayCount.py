import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/PeerHourPlayCountDB.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist = {}
        for line in orglines:
            peerid,_,count,_ = line.split(',')
            resultlist[peerid]=resultlist.setdefault(peerid,0)+int(count)

        for peerid, count in resultlist.items():
            expectedfile.write('%s,%d\n' % (peerid,count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]



