# coding=utf-8

"""
生成不断刷新的m3u8文件
"""

import time
from random import Random, random
import os

class CreateM3u8(object):

    def CreateHttp(self):
        CreateM3u8().CreateNormal('http://192.168.1.64:9999/home/admin/m3u8/')

    def CreateHttpCase(self):
        CreateM3u8().CreateNormal('HTTP://192.168.1.64:9999/home/admin/m3u8/http')

    def CreateDir(self):
        CreateM3u8().CreateNormal('/admin/m3u8/')

    def CreateDirNoSlash(self):
        CreateM3u8().CreateNormal('admin/m3u8/')

    def CreateFilename(self):
        CreateM3u8().CreateNormal()

    def CreateWithTimestamp(self):
        CreateM3u8().CreateWithTime()

    def CreateNormal(self, url=''):
        """
        生成不断刷新的m3u8
        :param url:segment的url格式（不需要包括文件名）
        :return:
        """
        duration = 5
        seq = 0
        seq1 = 0
        ts_name = 10
        BODY = []
        for i in range(0, 9999):
            if seq > 9:
                seq1 = seq - 9
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq1) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    body = '#EXTINF:' + str(time1) + ',\n' + str(url) + str(ts_name) + '.ts\n'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        f.write(BODY[j])
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        body = '#EXTINF:' + str(time1) + ',\n' + str(url) + str(ts_name) + '.ts\n'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.flush()
                        time.sleep(int(time1))

            f.close()

    def CreateWithTime(self):
        """
        生成不断刷新的m3u8, url带有时间戳
        :return:
        """
        duration = 5
        seq = 0
        seq1 = 0
        ts_name = 10
        BODY = []
        url = 'http://192.168.1.64:9999/home/admin/m3u8/'
        for i in range(0, 9999):
            if seq > 9:
                seq1 = seq - 9
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq1) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    timestamp = str(int(time.time()))
                    body = '#EXTINF:' + str(time1) + ',\n' + str(url) + str(ts_name) + '.ts'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.write('?timestamp=' + timestamp + '\n')
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        timestamp = str(int(time.time()))
                        f.write(BODY[j])
                        f.write('?timestamp=' + timestamp + '\n')
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        timestamp = str(int(time.time()))
                        body = '#EXTINF:' + str(time1) + ',\n' + str(url) + str(ts_name) + '.ts'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.write('?timestamp=' + timestamp + '\n')
                        f.flush()
                        time.sleep(int(time1))

            f.close()


    def CreateSeqTo0(self):
        """
        生成不断刷新的m3u8, 在某一个时间点seq归0
        :return:
        """
        duration = 5
        seq = 0
        seq1 = 0
        ts_name = 10
        BODY = []
        for i in range(0, 100):
            if seq > 9:
                seq1 = seq - 9
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq1) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        f.write(BODY[j])
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.flush()
                        time.sleep(int(time1))
            f.close()

        seq = 0

        for i in range(0, 999):
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        f.write(BODY[j])
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.flush()
                        time.sleep(int(time1))
            f.close()

    def CreateSeqFluctuation(self):
        """
        生成不断刷新的m3u8, 在某一个时间点seq波动
        :return:
        """
        duration = 5
        seq = 0
        seq1 = 0
        ts_name = 10
        BODY = []
        for i in range(0, 100):
            if seq > 9:
                seq1 = seq - 9
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq1) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        f.write(BODY[j])
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.flush()
                        time.sleep(int(time1))
            f.close()
        seq = seq - 11
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
        f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
        f.flush()

        for j in range(0, 10):

            if j < 9:
                BODY[j] = BODY[j+1]
                f.write(BODY[j])
                f.flush()
            else:
                time1 = round(Random().uniform(3, 5), 2)
                body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                #print j
                #print body
                ts_name += 1
                seq += 2
                BODY[j] = body
                f.write(BODY[j])
                f.flush()
                time.sleep(int(time1))
        f.close()

        for i in range(0, 999):
            f = open(os.path.abspath(os.path.dirname(__file__)) + "/test.m3u8", "w")
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:' + str(seq) +
                    '\n#EXT-X-TARGETDURATION:' + str(duration) + '\n')
            f.flush()

            if len(BODY) < 10:
                for j in range(0, 10):
                    time1 = round(Random().uniform(3, 5), 2)
                    body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                    BODY.append(body)
                    ts_name += 1
                    seq += 1
                    f.write(BODY[j])
                    f.flush()
                time.sleep(int(time1))
            else:
                for j in range(0, 10):

                    if j < 9:
                        BODY[j] = BODY[j+1]
                        f.write(BODY[j])
                        f.flush()
                    else:
                        time1 = round(Random().uniform(3, 5), 2)
                        body = '#EXTINF:' + str(time1) + ',\n' + str(ts_name) + '.ts\n'
                        #print j
                        #print body
                        ts_name += 1
                        seq += 1
                        BODY[j] = body
                        f.write(BODY[j])
                        f.flush()
                        time.sleep(int(time1))
            f.close()

if __name__ == "__main__":
    type = raw_input("Please enter type:1-8\n")
    type = int(type)
    if type == 1:
        CreateM3u8().CreateHttp()
    elif type == 2:
        CreateM3u8().CreateHttpCase()
    elif type == 3:
        CreateM3u8().CreateDir()
    elif type == 4:
        CreateM3u8().CreateDirNoSlash()
    elif type == 5:
        CreateM3u8().CreateFilename()
    elif type == 6:
        CreateM3u8().CreateWithTimestamp()
    elif type == 7:
        CreateM3u8().CreateSeqTo0()
    elif type == 8:
        CreateM3u8().CreateSeqFluctuation()
    else:
        print "输入错误"
