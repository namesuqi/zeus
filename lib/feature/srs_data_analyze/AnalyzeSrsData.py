#!/usr/bin/python
# coding=utf-8

import binascii
import paramiko
import os
from lib.decorator.trace import print_trace
from lib.feature.srs_data_analyze.data import *

class AnalyzeSrsData(object):

    @print_trace
    def CreateFile(self,ip=IP,username=USERNAME,password=PASSWORD,file_path=FILE_PATH,file_name=FILE_NAME,file_id=FILE_ID):
        exec_device = paramiko.SSHClient()
        exec_device.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        exec_device.connect(ip,22,username,password)
        srs_data_save_file = file_path+file_name
        command = r" curl -o " + srs_data_save_file + " " +"\"http://flv.srs.cloutropy.com/wasu/"+file_id+".flv?active=stream"+"\""
        exec_device.exec_command(command)
        exec_device.close()

    @print_trace
    def DownloadFile(self,ip=IP,username=USERNAME,password=PASSWORD,file_path=FILE_PATH,file_name=FILE_NAME,localpath=LOCALPATH):
        remote_device = paramiko.Transport(ip,22)
        remote_device.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(remote_device)
        remotepath = file_path+file_name
        localpath=localpath
        sftp.get(remotepath,localpath)
        remote_device.close()

    @print_trace
    def AnalyzeFile(self,num=NUM,file_name=FILE_NAME):
        srs_data_file=os.path.abspath(os.path.dirname(__file__))+'\\'+file_name
        fp = open(srs_data_file,"rb")
        lines = fp.readlines()
        string = ""
        for line in lines:
            string = string+line
        strhex = binascii.b2a_hex(string)
        for i in range(1,num):
            offset = 0
            while(i):
                type_char = strhex[offset:2+offset]
                type_int = int(type_char,16)
                len_char = strhex[offset+2:8+offset]
                length = int(len_char,16)
                offset = offset+length*2+8
                i = i-1
            if type_int in [1,2,3,4,5]:
                print 'correct!'
                print type_int
                print length
                print '\n'
            else:
                print 'error!'
                print type_int
                print length
                print '\n'
        fp.close()

if __name__ == '__main__':
        #AnalyzeSrsData().DownloadFile()
        pass