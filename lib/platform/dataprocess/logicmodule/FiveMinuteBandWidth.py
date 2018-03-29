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
    # timestamp = long(get_timestamp_by_time(time_format)[:-3])
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
                    typelist[i][tmpusername]['all']['totaldown'] = typelist[i][tmpusername]['all'].setdefault('totaldown', 0) + long(cdndown) + long(p2pdown)
                    typelist[i][tmpusername]['all']['p2pdown'] = typelist[i][tmpusername]['all'].setdefault('p2pdown', 0) + long(p2pdown)
                    typelist[i][tmpusername]['all']['cdndown'] = typelist[i][tmpusername]['all'].setdefault('cdndown', 0) + long(cdndown)
                    if playtype.startswith('live'):
                        typelist[i][tmpusername]['live']['totaldown'] = typelist[i][tmpusername]['live'].setdefault('totaldown', 0) + \
                                                       long(cdndown) + long(p2pdown)
                        typelist[i][tmpusername]['live']['p2pdown'] = typelist[i][tmpusername]['live'].setdefault('p2pdown', 0) + long(p2pdown)
                        typelist[i][tmpusername]['live']['cdndown'] = typelist[i][tmpusername]['live'].setdefault('cdndown', 0) + long(cdndown)
                    else:
                        typelist[i][tmpusername]['vods']['totaldown'] = typelist[i][tmpusername]['vods'].setdefault('totaldown', 0) + \
                                                       long(cdndown) + long(p2pdown)
                        typelist[i][tmpusername]['vods']['p2pdown'] = typelist[i][tmpusername]['vods'].setdefault('p2pdown', 0) + long(p2pdown)
                        typelist[i][tmpusername]['vods']['cdndown'] = typelist[i][tmpusername]['vods'].setdefault('cdndown', 0) + long(cdndown)
                    resultlist[i][tmpusername][playtype]['totaldown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'totaldown', 0) + long(cdndown) + long(p2pdown)
                    resultlist[i][tmpusername][playtype]['p2pdown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'p2pdown', 0) + long(p2pdown)
                    resultlist[i][tmpusername][playtype]['cdndown'] = resultlist[i][tmpusername][playtype].setdefault(
                        'cdndown', 0) + long(cdndown)
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
            for index in (range(hour*12, (hour+1)*12)):
                for username, ptypes in resultlist[index].items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*index, username,
                                                          float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))
                for username, ptypes in typelist[index].items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*index, username,
                                                          float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))
                for username, ptypes in totallist[index].items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*index, username,
                                                                float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                                float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                                float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))
        else:
            for time, users in resultlist.items():
                for username, ptypes in users.items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*time, username,
                                                          float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))
            for time, users in typelist.items():
                for username, ptypes in users.items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*time, username,
                                                          float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                          float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))
            for time, users in totallist.items():
                for username, ptypes in users.items():
                    for ptype, values in ptypes.items():
                        expectedfile.write('%d,%s,%f,%f,%f,%s\n' % (timestamp + 300*1000*time, username,
                                                                float(float(values.setdefault('totaldown', 0))*8/1024/1024)/float(300),
                                                                float(float(values.setdefault('p2pdown', 0))*8/1024/1024)/float(300),
                                                                float(float(values.setdefault('cdndown', 0))*8/1024/1024)/float(300), ptype))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(23)

if __name__ == "__main__":
    main()
