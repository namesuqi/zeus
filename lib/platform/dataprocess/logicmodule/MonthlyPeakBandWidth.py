import sys
import os

import lib.platform.dataprocess.pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidth.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek1.txt', 'w') as tempfile1:
        for line in orglines:
            temp = line.split(',')
            temp[1] = float(temp[1]) + 0.04
            temp[2] = float(temp[2]) + 0.02
            temp[3] = float(temp[3]) + 0.02
            line = ','.join(str(x) for x in temp)
            tempfile1.write(line)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek2.txt', 'w') as tempfile2:
        for line in orglines:
            temp = line.split(',')
            temp[1] = float(temp[1]) - 0.04
            temp[2] = float(temp[2]) - 0.02
            temp[3] = float(temp[3]) - 0.02
            line = ','.join(str(x) for x in temp)
            tempfile2.write(line)

    lib.platform.dataprocess.pipeofodps.uploaddatatoodps(
        'output_daily_peak_bandwidth',
        os.path.abspath(os.path.dirname(__file__) + '/../inputdata/DailyPeakBandWidthWeek1.txt'),
        -7)

    lib.platform.dataprocess.pipeofodps.uploaddatatoodps(
        'output_daily_peak_bandwidth',
        os.path.abspath(os.path.dirname(__file__) + '/../inputdata/DailyPeakBandWidthWeek2.txt'),
        7)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek1.txt', 'r') as resultfile1:
        orglines1 = resultfile1.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../inputdata/DailyPeakBandWidthWeek2.txt', 'r') as resultfile2:
        orglines2 = resultfile2.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist={}

        for line in orglines:
            username, totalpeakwidth, p2ppeakwidth, cdnpeakwidth, typ= line.split(',')
            typ=typ.replace('\n','')
            if username not in resultlist:
                resultlist[username] = {}
            if typ not in resultlist[username]:
                resultlist[username][typ] = {}
                resultlist[username][typ]['peak'] = {}
                resultlist[username][typ]['cdnpeak'] = {}
                resultlist[username][typ]['p2ppeak'] = {}
                resultlist[username][typ]['peak'] = float(totalpeakwidth)
                resultlist[username][typ]['cdnpeak'] = float(cdnpeakwidth)
                resultlist[username][typ]['p2ppeak'] = float(p2ppeakwidth)

        for line in orglines1:
            username, totalpeakwidth, p2ppeakwidth, cdnpeakwidth, typ= line.split(',')
            typ=typ.replace('\n','')
            # if username not in resultlist:
            #     resultlist[username] = {}
            # if typ not in resultlist[username]:
            #     resultlist[username][typ] = {}
            #     resultlist[username][typ]['peak'] = {}
            #     resultlist[username][typ]['cdnpeak'] = {}
            #     resultlist[username][typ]['p2ppeak'] = {}
            #     resultlist[username][typ]['peak'] = float(totalpeakwidth)
            #     resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
            #     resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)
            if float(totalpeakwidth) > resultlist[username][typ]['peak']:
                resultlist[username][typ]['peak'] = float(totalpeakwidth)
            if float(cdnpeakwidth) > resultlist[username][typ]['cdnpeak']:
                resultlist[username][typ]['cdnpeak'] = float(cdnpeakwidth)
            if float(p2ppeakwidth) > resultlist[username][typ]['p2ppeak']:
                resultlist[username][typ]['p2ppeak'] = float(p2ppeakwidth)

        for line in orglines2:
            username, totalpeakwidth, p2ppeakwidth, cdnpeakwidth, typ= line.split(',')
            typ=typ.replace('\n','')
            # if username not in resultlist:
            #     resultlist[username] = {}
            # if typ not in resultlist[username]:
            #     resultlist[username][typ] = {}
            #     resultlist[username][typ]['peak'] = {}
            #     resultlist[username][typ]['cdnpeak'] = {}
            #     resultlist[username][typ]['p2ppeak'] = {}
            #     resultlist[username][typ]['peak'] = float(totalpeakwidth)
            #     resultlist[username][typ]['cdnpeak'] = float(totalpeakwidth)
            #     resultlist[username][typ]['p2ppeak'] = float(totalpeakwidth)
            if float(totalpeakwidth) > resultlist[username][typ]['peak']:
                resultlist[username][typ]['peak'] = float(totalpeakwidth)
            if float(cdnpeakwidth) > resultlist[username][typ]['cdnpeak']:
                resultlist[username][typ]['cdnpeak'] = float(cdnpeakwidth)
            if float(p2ppeakwidth) > resultlist[username][typ]['p2ppeak']:
                resultlist[username][typ]['p2ppeak'] = float(p2ppeakwidth)

        for user, value1 in resultlist.items():
            for typeloc,peaks in value1.items():
                expectedfile.write('%s,%f,%f,%f,%s\n' % (user, peaks['peak'], peaks['cdnpeak'], peaks['p2ppeak'], typeloc))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]

if __name__ == '__main__':
    makeexpecteddata()