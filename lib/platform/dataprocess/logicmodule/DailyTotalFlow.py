import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/DownloadFlowCleaned.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/UploadFlowCleaned.txt', 'r') as resultfile:
        orguplines = resultfile.readlines()

    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        totallist = {}
        for line in orgdownlines:
            peerid, timesp, _, _, playtype, p2pdown, cdndown, _, _, _ = line.split(',')
            tmpusername = datavars.name_list[peerid[:8]]
            if tmpusername not in resultlist:
                resultlist[tmpusername] = {}
            if playtype not in resultlist[tmpusername]:
                resultlist[tmpusername][playtype] = {}
            if playtype not in totallist:
                totallist[playtype] = {}
            resultlist[tmpusername][playtype]['p2pdown'] = resultlist[tmpusername][playtype].setdefault('p2pdown', 0L) + long(p2pdown)
            resultlist[tmpusername][playtype]['cdndown'] = resultlist[tmpusername][playtype].setdefault('cdndown', 0L) + long(cdndown)
            resultlist[tmpusername][playtype]['totaldown'] = resultlist[tmpusername][playtype].setdefault('totaldown', 0L) + long(cdndown) + long(p2pdown)

            totallist[playtype]['p2pdown'] = totallist[playtype].setdefault('p2pdown', 0L) + long(p2pdown)
            totallist[playtype]['cdndown'] = totallist[playtype].setdefault('cdndown', 0L) + long(cdndown)
            totallist[playtype]['totaldown'] = totallist[playtype].setdefault('totaldown', 0L) + long(cdndown) + long(p2pdown)

        for line in orguplines:
            _, timesp, peerid, upload, _, _, _, playtype = line.split(',')
            playtype = playtype.replace('\n', '')
            tmpusername = datavars.name_list[peerid[:8]]
            if tmpusername not in resultlist:
                resultlist[tmpusername] = {}
            if playtype not in resultlist[tmpusername]:
                resultlist[tmpusername][playtype] = {}
            if playtype not in totallist:
                totallist[playtype] = {}
            resultlist[tmpusername][playtype]['upload'] = resultlist[tmpusername][playtype].setdefault('upload', 0L) + long(upload)
            totallist[playtype]['upload'] = totallist[playtype].setdefault('upload', 0L) + long(upload)

        for username, ptypes in resultlist.items():
            for ptype, values in ptypes.items():
                expectedfile.write('%s,%d,%d,%d,%d,%s\n' % (username, values.setdefault('cdndown', 0),
                                                        values.setdefault('p2pdown', 0), values.setdefault(
                    'totaldown', 0), values.setdefault('upload', 0), ptype))
        for ptype, values in totallist.items():
            expectedfile.write('all,%d,%d,%d,%d,%s\n' % (values.setdefault('cdndown', 0), values.setdefault(
                'p2pdown', 0), values.setdefault('totaldown', 0), values.setdefault('upload', 0), ptype))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata()

if __name__ == "__main__":
    main()
