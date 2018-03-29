import os

import testdata.datavars as datavars
import pipeofodps


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/PeerInfoCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    # prepare middle table data and upload to odps. middle data will be involved in making the expected data create
    peeridlist = []
    orglinestmp = []
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/%stmp.txt' % __name__.split('.')[-1], "w") as tmpfile:
        linecount = 0
        for line in orglines:
            _, _, peerid, _, _, _, _, public_ip, _, _, _, _, _, _, _ = line.split(',')
            if peerid not in peeridlist:
                if linecount % 100 == 0:
                    peerid = peerid[:-3] + 'xyz'
                username = datavars.name_list[peerid[:8]]
                ispinfo = datavars.ip2isp[public_ip].split(',')[1]
                proviceinfo = datavars.ip2isp[public_ip].split(',')[0]
                tmpstr = '%s,%s,%s,%s\n' % (peerid, ispinfo, proviceinfo, username)
                orglinestmp.append(tmpstr)
                tmpfile.write(tmpstr)
            linecount += 1
            peeridlist.append(peerid)
    pipeofodps.uploaddatatoodps('output_all_peer_isp_province_distribute',
                                os.path.abspath(os.path.dirname(__file__)) + '/../testdata/%stmp.txt' % __name__.split('.')[-1],
                                -1)

    ispresultlist = {}
    ispresultlist1 = {}
    proviceresultlist = {}
    proviceresultlist1 = {}

    for line in orglines:
        _, _, peerid, _, _, _, _, public_ip, _, _, _, _, _, _, _ = line.split(',')
        if peerid not in peeridlist:
            username = datavars.name_list[peerid[:8]]
            ispinfo = datavars.ip2isp[public_ip].split(',')[1]
            proviceinfo = datavars.ip2isp[public_ip].split(',')[0]
            tmpstr = '%s,%s,%s,%s\n' % (peerid, ispinfo, proviceinfo, username)
            orglinestmp.append(tmpstr)
            peeridlist.append(peerid)

    for tmpline in orglinestmp:
        peerid, ispinfo, proviceinfo, username = tmpline.split(',')
        username = username.replace('\n', '')
        if username not in ispresultlist:
            ispresultlist[username] = {}
        ispresultlist[username][ispinfo] = ispresultlist[username].setdefault(ispinfo, 0) + 1
        ispresultlist1[ispinfo] = ispresultlist1.setdefault(ispinfo, 0) + 1
        if username not in proviceresultlist:
            proviceresultlist[username] = {}
        proviceresultlist[username][proviceinfo] = proviceresultlist[username].setdefault(proviceinfo, 0) + 1
        proviceresultlist1[proviceinfo] = proviceresultlist1.setdefault(proviceinfo, 0) + 1

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%sISP.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for username, ipsinfos in ispresultlist.items():
            for ips, count in ipsinfos.items():
                 expectedfile.write('%s,%s,%d\n' % (username, ips, count))
        for ips, count in ispresultlist1.items():
            expectedfile.write('%s,%s,%d\n' % ('all', ips, count))

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%sProvince.txt"%__name__.split('.')[-1],"w") as expectedfile:
        for username, proviceinfos in proviceresultlist.items():
            for provice, count in proviceinfos.items():
                expectedfile.write('%s,%s,%d\n' % (username, provice, count))
        for provice, count in proviceresultlist1.items():
            expectedfile.write('%s,%s,%d\n' % ('all', provice, count))

    return (os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%sISP.txt"%__name__.split('.')[-1],
            os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%sProvince.txt"%__name__.split('.')[-1])





