import sys
import os
import random

import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailySeekTimeCountDB.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailySeekTimeCountDBWeek1.txt', 'w') as tempfile1:
        for line in orglines:
            tmpstr = line.split(',')[1]
            tmpcount = line.split(',')[2]
            if int(tmpstr) > 3000:
                newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) + random.randint(0, 10)))
            else:
                newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) - random.randint(0, 6)))
            tempfile1.write(newline)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailySeekTimeCountDBWeek2.txt', 'w') as tempfile2:
        for line in orglines:
            tmpstr = line.split(',')[1]
            tmpcount = line.split(',')[2]
            if int(tmpstr) < 3000:
                newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) + random.randint(0, 10)))
            else:
                newline = line.replace(',%s' % tmpcount, ',%s' % (int(tmpcount) - random.randint(0, 6)))
            tempfile2.write(newline)

    pipeofodps.uploaddatatoodps(
        'output_daily_seek_time_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailySeekTimeCountDBWeek1.txt'),
        -7)

    pipeofodps.uploaddatatoodps(
        'output_daily_seek_time_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailySeekTimeCountDBWeek2.txt'),
        -20)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailySeekTimeCountDBWeek1.txt', 'r') as resultfile1:
        orglines1 = resultfile1.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailySeekTimeCountDBWeek2.txt', 'r') as resultfile2:
        orglines2 = resultfile2.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist={}

        for line in orglines:
            username,period,count,_ = line.split(',')
            if username not in resultlist:
                resultlist[username]={}
            if period not in resultlist[username]:
                resultlist[username][period]=int(count)
            else:
                resultlist[username][period]=resultlist[username][period]+int(count)

        for line in orglines1:
            username,period,count,_ = line.split(',')
            if username not in resultlist:
                resultlist[username]={}
            if period not in resultlist[username]:
                resultlist[username][period]=int(count)
            else:
                resultlist[username][period]=resultlist[username][period]+int(count)

        for line in orglines2:
            username,period,count,_ = line.split(',')
            if username not in resultlist:
                resultlist[username]={}
            if period not in resultlist[username]:
                resultlist[username][period]=int(count)
            else:
                resultlist[username][period]=resultlist[username][period]+int(count)

        for username, value in resultlist.items():
            for period, count in value.items():
                expectedfile.write('%s,%s,%d,%s\n' % (username,period,count,''))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]








