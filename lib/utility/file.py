# coding=utf-8
"""
文件对比，文件生成
__author__ = 'zengyuetian'

"""
import os
import hashlib




def WriteDataToFile(content, filename):
    """
    将内容字符串写成文件
    :param content: 内容字符串
    :param filename: file目录下的文件名
    :return: void
    """

    f = open(filename, "w")
    f.write(content)
    f.close()


def FilesAreEqual(file1, file2):
    """
    通过MD5判断两个文件内容是否相等
    :param file1: file目录下的文件名1
    :param file2: file目录下的文件名2
    :return: 相等True，不等False
    """

    str1 = GetFileMd5(file1)
    str2 = GetFileMd5(file2)
    print "MD5 for file1 is: ", str1
    print "MD5 for file2 is: ", str2
    return str1 == str2

def CreateFileBySize(file_name, ch, size):
    """
    以byte为单位创建特定大小的文件（对于大文件来说，速度较慢）
    :param file_name: 文件名
    :param ch:用于填充文件的字符
    :param size:多少byte
    :return:void
    """
    f = open(file_name, "w")
    i = 0
    while i < int(size):
        f.write(ch)
        i += 1
    f.close()


def CreateFileByKSize(file_name, ch, ksize):
    """
    快速以k byte为单位创建特定大小的文件
    :param file_name: 文件名
    :param ch:用于填充文件的字符
    :param ksize:多少k
    :return:void
    """

    f = open(file_name, "w")
    i = 0
    while i < int(ksize):
        f.write(ch * 1024)
        i += 1
    f.close()


def CreateFileByMSize (file_name, ch, msize):
    """
    快速以k byte为单位创建特定大小的文件
    :param file_name: 文件名
    :param ch:用于填充文件的字符
    :param msize:多少m
    :return:void
    """

    f = open(file_name, "w")
    i = 0
    while i < int(msize):
        f.write(ch * 1024 * 1024)
        i += 1
    f.close()


def GetFileMd5(filename):
    """
    获得大文件的MD5
    :param filename:大文件名
    :return:md5值
    """
    if not os.path.isfile(filename):
        print filename, "not exists"
        return
    myhash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def getHash(f):
    line = f.readline()
    hash = hashlib.md5()
    while(line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()


###############################
# 调试用
###############################
if __name__ == "__main__":
    print(FilesAreEqual("1024k.flv", "1023k.flv"))
    print(FilesAreEqual("1024k.flv", "1022k.flv"))