import sys
import os
import random

import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyProvinceFilePlayCountDB.txt', 'r') as resultfile1:
        orglines1 = resultfile1.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyProvinceFilePlayCountDBWeek1.txt', 'w') as tempfile:
        for line in orglines1:
            tmpstr = line.split(',')[2]
            if int(tmpstr) % 2 == 0:
                newline = line.replace(',%s' % tmpstr, ',%s' % (int(tmpstr) + random.randint(0, 10)))
            else:
                newline = line.replace(',%s' % tmpstr, ',%s' % (int(tmpstr) - random.randint(0, 6)))
            tempfile.write(newline)

    pipeofodps.uploaddatatoodps(
        'output_daily_province_file_play_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyProvinceFilePlayCountDBWeek1.txt'),
        2)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyProvinceFilePlayCountDBWeek1.txt', 'r') as resultfile2:
        orglines2 = resultfile2.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist = {}

        for line in orglines1:
            province,username,playcount,_ = line.split(',')
            if province not in resultlist:
                resultlist[province] = {}
            if username not in resultlist[province]:
                resultlist[province][username] = int(playcount)
            else:
                resultlist[province][username] = resultlist[province][username] + int(playcount)

        for line in orglines2:
            province,username,playcount,_ = line.split(',')
            if province not in resultlist:
                resultlist[province] = {}
            if username not in resultlist[province]:
                resultlist[province][username] = int(playcount)
            else:
                resultlist[province][username] = resultlist[province][username] + int(playcount)

        for pro, value in resultlist.items():
            for user,count in value.items():
                expectedfile.write('%s,%s,%d\n' % (pro,user,count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]





