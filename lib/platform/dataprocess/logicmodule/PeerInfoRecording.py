import os

import pipeofodps


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseODPS.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    pipeofodps.downloaddatafromodps(
        'output_peer_info', os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt', -1)
    oldpeeridlist = []
    if os.path.exists(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt'):
        tempfile = open(os.path.abspath(os.path.dirname(__file__)) + '/../outputdata/ISPProvinceParseDBtmp.txt', 'r')
        oldorglines = tempfile.readlines()
        tempfile.close()
        for oldline in oldorglines:
            oldpeeridlist.append(oldline.split(',')[0])
    else:
        oldorglines = []

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        for line in orglines:
            peerid,sdkversion,nat_type,pub_ip,pub_port,pri_ip,pri_port,macs,os_version,cpu,province,isp,_,_= line.split(',')
            if peerid not in oldpeeridlist:
                oldorglines.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                    peerid, sdkversion, nat_type, pub_ip, pub_port, pri_ip, pri_port, macs, os_version, cpu, province, isp))

        expectedfile.writelines(oldorglines)

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]
