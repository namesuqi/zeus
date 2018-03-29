import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/LiveProgressCleaned.txt', 'r') as resultfile:
        liveprogresslines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/QosBufferingCleaned.txt', 'r') as resultfile:
        QosBufferinglines = resultfile.readlines()

    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:

        allpeerinfo = {}
        totalpeerinfo = {}
        bufferpeerinfo = {}
        totalbuffering = {}
        for line in liveprogresslines:
            _, timesp, peerid, _, _, _, _, _ = line.split(',')
            for i in range(288):
                if (timestamp + 300*(i+1)) > long(timesp[:-3]) >= (timestamp + 300*i):
                    if i not in allpeerinfo:
                        allpeerinfo[i] = {}
                    if i not in totalpeerinfo:
                        totalpeerinfo[i] = set()
                    tmpusernum = peerid[:8]
                    if tmpusernum not in allpeerinfo[i]:
                        allpeerinfo[i][tmpusernum] = set()
                    allpeerinfo[i][tmpusernum].add(peerid)
                    totalpeerinfo[i].add(peerid)

        for line in QosBufferinglines:
            _, timesp, peerid, _, _, _, _, _, _, _ = line.split(',')
            for i in range(288):
                if (timestamp + 300*(i+1)) > long(timesp[:-3]) >= (timestamp + 300*i):
                    if i not in bufferpeerinfo:
                        bufferpeerinfo[i] = {}
                    if i not in totalbuffering:
                        totalbuffering[i] = set()
                    tmpusernum = peerid[:8]
                    if tmpusernum not in bufferpeerinfo[i]:
                        bufferpeerinfo[i][tmpusernum] = set()
                    bufferpeerinfo[i][tmpusernum].add(peerid)
                    totalbuffering[i].add(peerid)

        if hour > -1:
            for index in range(hour*12, (hour+1)*12):
                if index in bufferpeerinfo:
                    buffernames = bufferpeerinfo[index].keys()
                    allnames = allpeerinfo[index].keys()
                    for bn in buffernames:
                        if bn not in allnames:
                            allpeerinfo[index][bn] = bufferpeerinfo[index][bn]
                for username, sets in allpeerinfo[index].items():
                    if index not in bufferpeerinfo:
                        tmpnum = 0
                    else:
                        if username not in bufferpeerinfo[index]:
                            tmpnum = 0
                        else:
                            tmpnum = len(bufferpeerinfo[index][username])
                    tmproughness = float(tmpnum)/float(len(sets))
                    expectedfile.write('%s,%f,%d,%s\n' % (username, tmproughness, index,' '))
                if index not in totalbuffering:
                    tmpnum = 0
                else:
                    tmpnum = len(totalbuffering[index])
                expectedfile.write('%s,%f,%d,%s\n' % ('99999999', float(tmpnum)/float(len(totalpeerinfo[index])), index,' '))
        else:
            for index in range(288):
                for username, sets in allpeerinfo[index].items():
                    if index not in bufferpeerinfo:
                        tmpnum = 0
                    else:
                        if username not in bufferpeerinfo[index]:
                            tmpnum = 0
                        else:
                            tmpnum = len(bufferpeerinfo[index][username])
                    tmproughness = float(tmpnum)/float(len(sets))
                    expectedfile.write('%s,%f,%d,%s\n' % (username, tmproughness, index,' '))
                if index not in totalbuffering:
                    tmpnum = 0
                else:
                    tmpnum = len(totalbuffering[index])
                expectedfile.write('%s,%f,%d,%s\n' % ('99999999', float(tmpnum)/float(len(totalpeerinfo[index])), index,' '))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

if __name__ == '__main__':
    makeexpecteddata(23)