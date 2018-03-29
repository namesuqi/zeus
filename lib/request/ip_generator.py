#!C:\Python27
import random
import pickle
import os
import socket
import struct

class IPGenerator(object):

    def __init__(self):
        self._resrc = open('./rely/ppc_ipinfo.dat', 'r')
        if os.path.exists('./rely/ipdata.dat'):
            ipdata = open('./rely/ipdata.dat', 'rb')
            self._lines = pickle.load(ipdata)
            ipdata.close()
        else:
            self._lines = []
            line_idx = [0]
            self._charnums = 0
            num = 0
            while True:
                char = self._resrc.read(1)
                if char == '':
                    output = open('./rely/ipdata.dat', 'wb')
                    pickle.dump(self._lines, output)
                    output.close()
                    break
                self._charnums += 1
                if char == ',':
                    line_idx.append(self._charnums)
                if char == '\n':
                    self._charnums += 1
                    num += 1
                    self._lines.append(line_idx)
                    line_idx = [self._charnums]
                
    def __del__(self):
        self._resrc.close()

    def _GetOneIPInfo(self):
        line = random.randrange(0, len(self._lines))
        print line
        self._resrc.seek(self._lines[line][2])
        str_ip_start = self._resrc.read(
            self._lines[line][3] - self._lines[line][2] - 1)
        self._resrc.seek(self._lines[line][3])
        str_ip_end = self._resrc.read(
            self._lines[line][4] - self._lines[line][3] - 1)
        int_ip_start = socket.ntohl(struct.unpack("I",socket.inet_aton(str_ip_start))[0])
        int_ip_end = socket.ntohl(struct.unpack("I",socket.inet_aton(str_ip_end))[0])
        self._resrc.seek(self._lines[line][8])
        province = self._resrc.read(
            self._lines[line][9] - self._lines[line][8] - 1)
        self._resrc.seek(self._lines[line][14])
        isp = self._resrc.read(
            self._lines[line][15] - self._lines[line][14] - 1)
        int_ip = random.randrange(int_ip_start,int_ip_end + 1)
        print int_ip
        return (int_ip,province,isp)

    def GetSomeIP(self, num):
        res = []
        for it in range(num):
            res.append(self._GetOneIPInfo())
        return res

IPGenerator().GetSomeIP(10)
