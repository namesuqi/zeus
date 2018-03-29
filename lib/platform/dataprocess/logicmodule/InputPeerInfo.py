import os


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/RawPeerInfo.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    expectedformat = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        filterlist = []
        for line in orglines:
            id, timesp, peerid, ostype, osver, skdver, nattype, publicip, pubport, priip, priport, macs1, macs2, cpu, intime, outtime = line.split(',')
            if (id, peerid) not in filterlist:
                filterlist.append((id, peerid))
                expectedfile.write(expectedformat % (
                    id, timesp, peerid, ostype, osver, skdver, nattype, publicip, pubport, priip, priport, macs1, macs2, cpu, intime))
            else:
                continue

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
