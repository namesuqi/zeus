import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import testdata.datavars as datavars

def makeexpecteddata(hour=-1 ):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerInfoCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    peeridlist = []
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,timesp,peerid,ostype,osver,sdkver,nattype,publicip,pubport,priip,priport,_,macs,cpu,inputtime=line.split(',')
            if peerid not in peeridlist:
                peeridlist.append(peerid)
                macs = macs.split('":"')[1][:-3]
                province=datavars.ip2isp[publicip].split(',')[0]
                isp=datavars.ip2isp[publicip].split(',')[1]
                expectedfile.write('%s,%s,%d,%s,%d,%s,%d,%s,%s,%s,%s,%s,%d,%s\n' % (peerid,sdkver,int(nattype),publicip,int(pubport),priip,int(priport),macs,osver,cpu,province,isp,int(timesp),ostype))
            else:
                continue

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]




