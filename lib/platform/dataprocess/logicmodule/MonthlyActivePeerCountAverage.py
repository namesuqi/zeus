import sys
import os
import random

import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeerActivity.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek1.txt', 'w') as tempfile1:
        for line in orglines:
            randomnum = random.randint(150, 300)
            tmpcount = line.split(',')[1]

            newline = line.replace(',%s' % tmpcount, ',%s' % str(int(tmpcount) * randomnum))
            tmpstr1 = newline.split(',')[1]
            newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s\n' % (tmpstr1, 'NULL'))

            tempfile1.write(newline1)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek2.txt', 'w') as tempfile2:
        for line in orglines:
            randomnum = random.randint(150, 300)
            tmpcount = line.split(',')[1]

            newline = line.replace(',%s' % tmpcount, ',%s' % str(int(tmpcount) * randomnum))
            tmpstr1 = newline.split(',')[1]
            newline1 = newline.replace(',%s' % tmpstr1, ',%s,%s\n' % (tmpstr1, 'NULL'))

            tempfile2.write(newline1)

    pipeofodps.uploaddatatoodps(
        'output_daily_peer_activity',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyPeerActivityDBWeek1.txt'),
        3)

    pipeofodps.uploaddatatoodps(
        'output_daily_peer_activity',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyPeerActivityDBWeek2.txt'),
        7)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek1.txt', 'r') as resultfile1:
        orglines1 = resultfile1.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyPeerActivityDBWeek2.txt', 'r') as resultfile2:
        orglines2 = resultfile2.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        sumcount = {}

        for line in orglines:
            prefix, actcount = line.split(',')
            actcount = actcount.replace('\n', '')
            if prefix not in sumcount:
                sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)

        for line in orglines1:
            prefix, actcount, _ = line.split(',')
            if prefix not in sumcount:
                sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)
            else:
                sumcount[prefix] = sumcount[prefix] + int(actcount)

        for line in orglines2:
            prefix, actcount, _ = line.split(',')
            if prefix not in sumcount:
                sumcount[prefix] = sumcount.setdefault(prefix, 0) + int(actcount)
            else:
                sumcount[prefix] = sumcount[prefix] + int(actcount)

        for pre, count in sumcount.items():
            if (pre != '99999999'):
                expectedfile.write('%s,%d\n' % (pre, int(count/30)))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]







