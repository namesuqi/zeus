import os

from lib.platform.dataprocess.commonfunc import get_timestamp_by_time
import constvars
import testdata.datavars as datavars


def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/RawLiveDelay.txt', 'r') as resultfile:
        orgdownlines = resultfile.readlines()

    time_format = constvars.recorddate + '000001'
    timestamp = long(get_timestamp_by_time(time_format)[:-3])

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1], "w") as expectedfile:
        resultlist = {}
        for line in orgdownlines:
            _, timesp, peerid, _, _, _, _, delaytime, _, _ = line.split(',')
            for i in range(288):
                if (timestamp + 300*(i+1)) > long(timesp[:-3]) >= (timestamp + 300*i):
                    if i not in resultlist:
                        resultlist[i] = {}
                    tmpusername = datavars.name_list[peerid[:8]]
                    if tmpusername not in resultlist[i]:
                        resultlist[i][tmpusername] = []
                    resultlist[i][tmpusername].append(int(delaytime))
                    break

        if hour > -1:
            for index in (range(0, (hour+1)*12)):   # for index in (range(hour*12, (hour+1)*12)):
                for username, values in resultlist[index].items():
                    if len(values) != 0:
                        average_delay = sum(values)/len(values)
                    else:
                        average_delay = 0
                    expectedfile.write('%s,%d,%d\n' % (username, index, average_delay))
        else:
            for index, users in resultlist.items():
                for username, values in users.items():
                    if len(values) != 0:
                        average_delay = sum(values)/len(values)
                    else:
                        average_delay = 0
                    expectedfile.write('%s,%d,%d\n' % (username, index, average_delay))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]


def main():
    makeexpecteddata(23)

if __name__ == "__main__":
    main()
