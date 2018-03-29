import optparse
import os

import time

import sys

ttl = ['20', '50', '100', '200']
d = ['0.1', '1.5', '7.5', '15']
mode = ['udp']


def test():
    for i in ttl:
        for j in d:
            print "python lib/special/ue/peer_controller.py %s %s" % (i, j)
            os.system("python lib/special/ue/peer_controller.py %s %s" % (i, j))


def test_buffer(play_time):
    for i in ttl:
        for j in d:
            for m in mode:
                print "python lib/special/ue/custom_play.py -p %s -t %d --delay %s --loss %s" % (m, play_time, i, j)
                os.system("python lib/special/ue/custom_play.py -p %s  -t %d --delay %s --loss %s" % (m, play_time,
                                                                                                      i, j))


def test_buffer_join_lf(play_time, lf_num):
    for i in ttl:
        for j in d:
            for m in mode:
                print "python lib/special/ue/custom_play.py -p %s -t %d --delay %s --loss %s --lf %d" % (m, play_time,
                                                                                                         i, j, lf_num)
                os.system("python lib/special/ue/custom_play.py -p %s -t %d --delay %s --loss %s --lf %d" %
                          (m, play_time, i, j, lf_num))

if __name__ == '__main__':
    parser = optparse.OptionParser("Usage: python %prog -l <loop times> -t <play duration>")
    parser.add_option('-l', dest='loop_num', type='int', help='specify ue test loop times')
    parser.add_option('-t', dest='play_duration', type='int', help='specify play time [second]')
    parser.add_option('--lf', dest='lf_num', type='int', help='specify join LF number')

    (options, args) = parser.parse_args()
    loop_num = options.loop_num
    play_duration = options.play_duration
    lf_number = options.lf_num

    start_time = time.time()
    for k in range(loop_num):
        print "++++++++++++++++++++++++++++++++++++"
        print "++++++         %d         +++++" % k
        print "++++++++++++++++++++++++++++++++++++"
        if lf_number is None:
            test_buffer(play_duration)
        else:
            test_buffer_join_lf(play_duration, lf_number)

    print 'use time : %s' % (time.time() - start_time)
