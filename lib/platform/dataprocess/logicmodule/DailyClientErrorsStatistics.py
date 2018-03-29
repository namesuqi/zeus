import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/ClientExceptionCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    resultlist={}
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for line in orglines:
            _,_,peerid,_,_,_,_,_,_,_,_,_,_,_,op,_,_,_,_,_ = line.split(',')
            peerfix=peerid[:8]
            if peerfix not in resultlist:
                resultlist[peerfix]={}
            if op == 'OP_DOWNLOAD_FILE':
                resultlist[peerfix]['CDN']=resultlist[peerfix].setdefault('CDN',0)+1
            elif op == 'OP_START_HLS' or op == 'OP_START_CHANNEL':
                resultlist[peerfix]['START']=resultlist[peerfix].setdefault('START',0)+1
            else:
                resultlist[peerfix]['P2P']=resultlist[peerfix].setdefault('P2P',0)+1

        for peefix,value in resultlist.items():
            for err,count in value.items():
                expectedfile.write('%s,%s,%d,\n' % (peefix,err,count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]





