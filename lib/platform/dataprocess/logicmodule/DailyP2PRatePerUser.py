import os
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/DownloadFlowCleaned.txt', 'r') as resultfile:
         orgdownlines = resultfile.readlines()

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
            resultlist[tmpusername][playtype]['p2pdown'] = resultlist[tmpusername][playtype].setdefault(
                'p2pdown', 0L) + long(p2pdown)
            resultlist[tmpusername][playtype]['totaldown'] = resultlist[tmpusername][playtype].setdefault(
                'totaldown', 0L) + long(cdndown) + long(p2pdown)

            totallist[playtype]['p2pdown'] = totallist[playtype].setdefault('p2pdown', 0L) + long(p2pdown)
            totallist[playtype]['totaldown'] = totallist[playtype].setdefault('totaldown', 0L) + long(cdndown) + long(p2pdown)

        for username, ptypes in resultlist.items():
            for ptype, values in ptypes.items():
                expectedfile.write('%s,%f,%s\n' % (username, float(values.setdefault('p2pdown', 0))/float(
                    values.setdefault('totaldown', 0)), ptype))
        for ptype, values in totallist.items():
            expectedfile.write('%s,%f,%s\n' % ('99999999', float(values.setdefault('p2pdown', 0))/float(
                values.setdefault('totaldown', 0)), ptype))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(23)

if __name__ == "__main__":
    main()
