import os

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/VodPerCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1],"w") as expectedfile:
        resultlist = {}
        for line in orglines:
            _,_,_,peerid,_,_,_,_,_,_,type,_,_,_,seekdelay,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_ = line.split(',')
            username=peerid[:8]
            if username not in resultlist:
                resultlist[username]={}
            if 1000 > int(seekdelay) >= 0:
                resultlist[username][1000]=resultlist[username].setdefault(1000, 0) + 1
            elif 2000 > int(seekdelay) >= 1000:
                resultlist[username][2000]=resultlist[username].setdefault(2000, 0) + 1
            elif 3000 > int(seekdelay) >= 2000:
                resultlist[username][3000]=resultlist[username].setdefault(3000, 0) + 1
            elif 4000 > int(seekdelay) >= 3000:
                resultlist[username][4000]=resultlist[username].setdefault(4000, 0) + 1
            elif 5000> int(seekdelay)>= 4000:
                resultlist[username][5000]=resultlist[username].setdefault(5000, 0) + 1
            else:
                resultlist[username][0]=resultlist[username].setdefault(0, 0) + 1

        for user ,value in resultlist.items():
            for per ,count in value.items():
                expectedfile.write('%s,%d,%d\n' % (user, per, count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


