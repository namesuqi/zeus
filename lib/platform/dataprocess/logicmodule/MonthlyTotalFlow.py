import sys
import os

import pipeofodps

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyTotalFlowDB.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyTotalFlowDBWeek1.txt', 'w') as tempfile1:
        for line in orglines:
            tempfile1.write(line)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyTotalFlowDBWeek2.txt', 'w') as tempfile2:
        for line in orglines:
            tempfile2.write(line)

    pipeofodps.uploaddatatoodps(
        'output_daily_total_flow',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyTotalFlowDBWeek1.txt'),
        -7,
        False)

    pipeofodps.uploaddatatoodps(
        'output_daily_total_flow',
        os.path.abspath(os.path.dirname(__file__) + '/../outputdata/DailyTotalFlowDBWeek2.txt'),
        7,
        False)

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyTotalFlowDBWeek1.txt', 'r') as resultfile1:
        orglines1 = resultfile1.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/DailyTotalFlowDBWeek2.txt', 'r') as resultfile2:
        orglines2 = resultfile2.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist={}

        for line in orglines:
            username,cdndown,p2pdown,totaldown,upload,typ = line.split(',')
            typ=typ.replace('\n','')
            if username not in resultlist:
                resultlist[username] = {}
            if typ not in resultlist[username]:
                resultlist[username][typ]={}
            resultlist[username][typ]['cdndown']=resultlist[username][typ].setdefault('cdndown',0)+int(cdndown)
            resultlist[username][typ]['p2pdown']=resultlist[username][typ].setdefault('p2pdown',0)+int(p2pdown)
            resultlist[username][typ]['totaldown']=resultlist[username][typ].setdefault('totaldown',0)+int(totaldown)
            resultlist[username][typ]['upload']=resultlist[username][typ].setdefault('upload',0)+int(upload)

        for line in orglines1:
            username,cdndown,p2pdown,totaldown,upload,typ = line.split(',')
            typ=typ.replace('\n','')
            if username not in resultlist:
                resultlist[username] = {}
            if typ not in resultlist[username]:
                resultlist[username][typ]={}
            resultlist[username][typ]['cdndown'] = resultlist[username][typ]['cdndown'] + int(cdndown)
            resultlist[username][typ]['p2pdown'] = resultlist[username][typ]['p2pdown'] + int(p2pdown)
            resultlist[username][typ]['totaldown'] = resultlist[username][typ]['totaldown'] + int(totaldown)
            resultlist[username][typ]['upload'] = resultlist[username][typ]['upload'] + int(upload)

        for line in orglines2:
            username,cdndown,p2pdown,totaldown,upload,typ = line.split(',')
            typ=typ.replace('\n','')
            if username not in resultlist:
                resultlist[username] = {}
            if typ not in resultlist[username]:
                resultlist[username][typ]={}
            resultlist[username][typ]['cdndown'] = resultlist[username][typ]['cdndown'] + int(cdndown)
            resultlist[username][typ]['p2pdown'] = resultlist[username][typ]['p2pdown'] + int(p2pdown)
            resultlist[username][typ]['totaldown'] = resultlist[username][typ]['totaldown'] + int(totaldown)
            resultlist[username][typ]['upload'] = resultlist[username][typ]['upload'] + int(upload)

        for user, value1 in resultlist.items():
            for typeloc,value2 in value1.items():
                expectedfile.write('%s,%d,%d,%d,%d,%s\n' % (user,resultlist[user][typeloc]['cdndown'],resultlist[user][typeloc]['p2pdown'],resultlist[user][typeloc]['totaldown'],resultlist[user][typeloc]['upload'],typeloc))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]








