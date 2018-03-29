import os
import math

import pipeofodps


def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/TodayFilePlayCountDB.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/TodayFilePlayCountDBtmp.txt', 'w') as tempfile:
        for line in orgdownlines:
            tmpstr = line.split(',')[2]
            newline = line.replace(',%s' % tmpstr, ',%s,%s' % (tmpstr, tmpstr))
            tempfile.write(newline)

    pipeofodps.uploaddatatoodps(
        'output_daily_file_play_count',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/TodayFilePlayCountDBtmp.txt'),
        -1)

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        for line in orgdownlines:
            url, username, count, _ = line.split(',')
            if url not in resultlist:
                resultlist[url] = {}
            resultlist[url][username] = resultlist[url].setdefault(username, 0.0) + float(float(count)*(1.0 + math.exp(-1)))

        for url, users in resultlist.items():
            for user, count in users.items():
                expectedfile.write('%s,%s,%f,%s\n' % (url, user, count, ''))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata()

if __name__ == "__main__":
    main()
