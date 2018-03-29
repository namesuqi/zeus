import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
import constvars
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/DownloadFlowCleaned.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    time_format = constvars.recorddate + '000000'
    timestamp = long(get_timestamp_by_time(time_format)[:-3]+'000')

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        totallist = {}
        typelist = {}
        for line in orgdownlines:
            peerid, timesp, _, _, playtype, p2pdown, cdndown, _, _, _ = line.split(',')
            if playtype == '':
                playtype = 'vod'
            for i in range(288):
                if (timestamp + 300*1000*(i+1)) > long(timesp) >= (timestamp + 300*1000*i):
                    if i not in resultlist:
                        resultlist[i] = {}
                    if i not in totallist:
                        totallist[i] = {}
                        totallist[i]['all'] = {}
                        totallist[i]['all']['live'] = {}
                        totallist[i]['all']['vods'] = {}
                        totallist[i]['all']['all'] = {}
                    if i not in typelist:
                        typelist[i] = {}
                    tmpusername = datavars.name_list[peerid[:8]]
                    if tmpusername not in resultlist[i]:
                        resultlist[i][tmpusername] = {}
                    if tmpusername not in typelist[i]:
                        typelist[i][tmpusername] = {}
                        typelist[i][tmpusername]['live'] = {}
                        typelist[i][tmpusername]['vods'] = {}
                        typelist[i][tmpusername]['all'] = {}
                    if playtype not in resultlist[i][tmpusername]:
                        resultlist[i][tmpusername][playtype] = {}
                    if playtype not in totallist[i]['all']:
                        totallist[i]['all'][playtype] = {}
                    typelist[i][tmpusername]['all']['totaldown'] = typelist[i][tmpusername]['all'].setdefault('totaldown', 0) + int(cdndown) + int(p2pdown)
                    typelist[i][tmpusername]['all']['p2pdown'] = typelist[i][tmpusername]['all'].setdefault('p2pdown', 0) + int(p2pdown)
                    typelist[i][tmpusername]['all']['cdndown'] = typelist[i][tmpusername]['all'].setdefault('cdndown', 0) + int(cdndown)
                    if playtype.startswith('live'):
                        typelist[i][tmpusername]['live']['totaldown'] = typelist[i][tmpusername]['live'].setdefault('totaldown', 0) + \
                                                           int(cdndown) + int(p2pdown)
                        typelist[i][tmpusername]['live']['p2pdown'] = typelist[i][tmpusername]['live'].setdefault('p2pdown', 0) + int(p2pdown)
                        typelist[i][tmpusername]['live']['cdndown'] = typelist[i][tmpusername]['live'].setdefault('cdndown', 0) + int(cdndown)
                    else:
                        typelist[i][tmpusername]['vods']['totaldown'] = typelist[i][tmpusername]['vods'].setdefault('totaldown', 0) + \
                                                           int(cdndown) + int(p2pdown)
                        typelist[i][tmpusername]['vods']['p2pdown'] = typelist[i][tmpusername]['vods'].setdefault('p2pdown', 0) + int(p2pdown)
                        typelist[i][tmpusername]['vods']['cdndown'] = typelist[i][tmpusername]['vods'].setdefault('cdndown', 0) + int(cdndown)
                    resultlist[i][tmpusername][playtype]['totaldown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'totaldown', 0) + long(cdndown) + long(p2pdown)
                    resultlist[i][tmpusername][playtype]['cdndown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'cdndown', 0) + long(cdndown)
                    resultlist[i][tmpusername][playtype]['p2pdown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'p2pdown', 0) + long(p2pdown)
                    totallist[i]['all'][playtype]['totaldown'] = totallist[i]['all'][playtype].setdefault('totaldown', 0) + long(cdndown) + long(p2pdown)
                    totallist[i]['all'][playtype]['p2pdown'] = totallist[i]['all'][playtype].setdefault('p2pdown', 0) + long(p2pdown)
                    totallist[i]['all'][playtype]['cdndown'] = totallist[i]['all'][playtype].setdefault('cdndown', 0) + long(cdndown)
                    totallist[i]['all']['all']['totaldown'] = totallist[i]['all']['all'].setdefault('totaldown', 0) + long(cdndown) + long(p2pdown)
                    totallist[i]['all']['all']['p2pdown'] = totallist[i]['all']['all'].setdefault('p2pdown', 0) + long(p2pdown)
                    totallist[i]['all']['all']['cdndown'] = totallist[i]['all']['all'].setdefault('cdndown', 0) + long(cdndown)
                    if playtype.startswith('live'):
                        totallist[i]['all']['live']['totaldown'] = totallist[i]['all']['live'].setdefault('totaldown', 0) + long(cdndown) + long(p2pdown)
                        totallist[i]['all']['live']['p2pdown'] = totallist[i]['all']['live'].setdefault('p2pdown', 0) + long(p2pdown)
                        totallist[i]['all']['live']['cdndown'] = totallist[i]['all']['live'].setdefault('cdndown', 0) + long(cdndown)
                    else:
                        totallist[i]['all']['vods']['totaldown'] = totallist[i]['all']['vods'].setdefault('totaldown', 0) + long(cdndown) + long(p2pdown)
                        totallist[i]['all']['vods']['p2pdown'] = totallist[i]['all']['vods'].setdefault('p2pdown', 0) + long(p2pdown)
                        totallist[i]['all']['vods']['cdndown'] = totallist[i]['all']['vods'].setdefault('cdndown', 0) + long(cdndown)
                    break
        if hour > -1:
            outputlist = {}
            outputtotallist = {}
            outputtypelist = {}
            for index in (range(hour*12, (hour+1)*12)):
                for username, ptypes in resultlist[index].items():
                    for ptype, values in ptypes.items():
                        if username not in outputlist:
                            outputlist[username] = {}
                        if ptype not in outputlist[username]:
                            outputlist[username][ptype] = {}
                        tmpvalue = float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300)
                        tmpvalue2 = float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300)
                        tmpvalue3 = float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300)

                        if tmpvalue > outputlist[username][ptype].setdefault('peak', 0.0):
                            outputlist[username][ptype]['peak'] = tmpvalue
                        if tmpvalue2 > outputlist[username][ptype].setdefault('cdnpeak', 0.0):
                            outputlist[username][ptype]['cdnpeak'] = tmpvalue2
                        if tmpvalue3 > outputlist[username][ptype].setdefault('p2ppeak', 0.0):
                            outputlist[username][ptype]['p2ppeak'] = tmpvalue3
                for username, ptypes in typelist[index].items():
                    for ptype, values in ptypes.items():
                        if username not in outputtypelist:
                            outputtypelist[username] = {}
                        if ptype not in outputtypelist[username]:
                            outputtypelist[username][ptype] = {}
                        tmpvalue = float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300)
                        tmpvalue2 = float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300)
                        tmpvalue3 = float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300)

                        if tmpvalue > outputtypelist[username][ptype].setdefault('peak', 0.0):
                            outputtypelist[username][ptype]['peak'] = tmpvalue
                        if tmpvalue2 > outputtypelist[username][ptype].setdefault('cdnpeak', 0.0):
                            outputtypelist[username][ptype]['cdnpeak'] = tmpvalue2
                        if tmpvalue3 > outputtypelist[username][ptype].setdefault('p2ppeak', 0.0):
                            outputtypelist[username][ptype]['p2ppeak'] = tmpvalue3
                for username, ptypes in totallist[index].items():
                    for ptype, values in ptypes.items():
                        if username not in outputtotallist:
                            outputtotallist[username] = {}
                        if ptype not in outputtotallist[username]:
                            outputtotallist[username][ptype] = {}
                        tmpvalue = float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300)
                        tmpvalue2 = float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300)
                        tmpvalue3 = float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300)

                        if tmpvalue > outputtotallist[username][ptype].setdefault('peak', 0.0):
                            outputtotallist[username][ptype]['peak'] = tmpvalue
                        if tmpvalue2 > outputtotallist[username][ptype].setdefault('cdnpeak', 0.0):
                            outputtotallist[username][ptype]['cdnpeak'] = tmpvalue2
                        if tmpvalue3 > outputtotallist[username][ptype].setdefault('p2ppeak', 0.0):
                            outputtotallist[username][ptype]['p2ppeak'] = tmpvalue3
            # outputtotallist['vods'] = {}
            # outputtotallist['live'] = {}
            # outputtotallist['all'] = {}
            # outputtotallist['vods']['peak'] = outputtotallist['vod']['peak'] + outputtotallist['hls']['peak']
            # outputtotallist['vods']['cdnpeak'] = outputtotallist['vod']['cdnpeak'] + outputtotallist['hls']['cdnpeak']
            # outputtotallist['vods']['p2ppeak'] = outputtotallist['vod']['p2ppeak'] + outputtotallist['hls']['p2ppeak']
            # outputtotallist['live']['peak'] = outputtotallist['live_flv']['peak'] + outputtotallist['live_ts']['peak'] + outputtotallist['live_m3u8']['peak']
            # outputtotallist['live']['cdnpeak'] = outputtotallist['live_flv']['cdnpeak'] + outputtotallist['live_ts']['cdnpeak'] + outputtotallist['live_m3u8']['cdnpeak']
            # outputtotallist['live']['p2ppeak'] = outputtotallist['live_flv']['p2ppeak'] + outputtotallist['live_ts']['p2ppeak'] + outputtotallist['live_m3u8']['p2ppeak']
            # outputtotallist['all']['peak'] = outputtotallist['vods']['peak'] + outputtotallist['live']['peak']
            # outputtotallist['all']['cdnpeak'] = outputtotallist['vods']['cdnpeak'] + outputtotallist['live']['cdnpeak']
            # outputtotallist['all']['p2ppeak'] = outputtotallist['vods']['p2ppeak'] + outputtotallist['live']['p2ppeak']

            for username, ptypes in outputlist.items():
                for ptype, values in ptypes.items():
                    expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*hour*12, username, values.setdefault('peak', 0.0),
                                            values.setdefault('cdnpeak', 0.0), values.setdefault('p2ppeak', 0.0), ptype))
            for username, ptypes in outputtypelist.items():
                for ptype, values in ptypes.items():
                    expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*hour*12, username, values.setdefault('peak', 0.0),
                                            values.setdefault('cdnpeak', 0.0), values.setdefault('p2ppeak', 0.0), ptype))
            for username, ptypes in outputtotallist.items():
                for ptype, values in ptypes.items():
                    expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*hour*12, username, values.setdefault('peak', 0.0),
                                                values.setdefault('cdnpeak', 0.0), values.setdefault('p2ppeak', 0.0), ptype))
        else:
            raise

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(0)

if __name__ == "__main__":
    main()
