# coding=utf-8
# author: zengyuetian


def get_target(filename, target):
    try:
        fi = open(filename, 'r')
        line = fi.readline().strip()
        print line
        fi.close()
    except:

        print "           File not exist", filename
        pass




protocols = ['http', 'udp']
# delays = ["20", "50", "100", "200"]
delays = ["50", "80", "130", "230"]
losts = ["0.1", "1.5", "7.5", "15"]
targets = ["first_image_time", "buffer_num"]

for protocol in protocols:
    for delay in delays:
        for lost in losts:
            for target in targets:
                filename = "e:/git/zeus/result/"+"{0}_{1}_{2}_{3}.txt".format(protocol, delay, lost, target)
                # print "{0}_{1}_{2}_{3}.txt".format(protocol, delay, lost, target)
                get_target(filename, "")







