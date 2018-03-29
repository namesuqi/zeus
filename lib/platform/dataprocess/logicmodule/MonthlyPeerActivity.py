import sys
import os
import pipeofodps
import random
import testdata.datavars as datavars

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

def makeexpecteddata(hour=-1):
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/MonthlyDistinctPeerIDDB.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        resultlist={}
        totallist={}

        for line in orglines:
            peerid,_ = line.split(',')
            resultlist[peerid[:8]]=resultlist.setdefault(peerid[:8],0)+1
            totallist['99999999']=totallist.setdefault('99999999',0)+1


        for prefix, count in resultlist.items():
            expectedfile.write('%s,%d,%s\n' % (prefix,count,''))
        expectedfile.write('%s,%d,%s\n' % ('99999999',totallist['99999999'],''))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]









