import os


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/HourPlayCountDB.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        for line in orglines:
            peerfix,_,count,_= line.split(',')
            resultlist[peerfix]=resultlist.setdefault(peerfix,0)+int(count)

        for peerfix, count in resultlist.items():
            expectedfile.write('%s,%d\n' % (peerfix, count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
