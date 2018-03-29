import os
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/RawVodPerformance.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    expectedformat = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        filterlist = []
        for line in orglines:
            id, timesp, duration, peerid, fileid, httpdown, p2pdown, url, username, useragent, type, startdelay, fwdseeks, bwdseeks, seekdelay, buffercnt, chunknum, chunkavgtime, chunkmaxtime, seedsnum, httpreqcnt, httpreqfailedcnt, httpreqavgtime, httpreqmaxtime, rqdecodecnt, rqdecodeavgtime, rqdecodemaxtime, seedreqnewcnt, seedreqsendcnt, seedreqlostcnt, seedreqacceptcnt, seedreqdeclinedcnt, seedreqcancnt, seedreqpieceexpcnt, seedreqpiecerecvcnt, seedreqpiecelostcnt, seedreqrecvfirstpiececnt, seedreqrecvfirstpieceavgtime, seedreqrecvfinishpiececnt, seedreqrecvfinishpieceavgtime, bufferdelay, intime, outtime = line.split(',')
            outtime = outtime.replace('\n','')
            if (id, peerid) not in filterlist:
                filterlist.append((id, peerid))
                expectedfile.write(expectedformat % (
                    id, timesp, duration, peerid, fileid, httpdown, p2pdown, url, username, useragent, type, startdelay, fwdseeks, bwdseeks, seekdelay, buffercnt, chunknum, chunkavgtime, chunkmaxtime, seedsnum, httpreqcnt, httpreqfailedcnt, httpreqavgtime, httpreqavgtime, httpreqmaxtime, rqdecodecnt, rqdecodeavgtime, rqdecodemaxtime, seedreqnewcnt, seedreqsendcnt, seedreqlostcnt, seedreqacceptcnt, seedreqdeclinedcnt, seedreqcancnt, seedreqpieceexpcnt, seedreqpiecerecvcnt, seedreqpiecelostcnt, seedreqrecvfirstpiececnt, seedreqrecvfirstpieceavgtime, seedreqrecvfirstpiececnt, seedreqrecvfirstpieceavgtime, bufferdelay, intime, outtime))
            else:
                continue

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
