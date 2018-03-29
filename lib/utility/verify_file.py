# coding=utf-8
"""
验证文件信息

__author__ = 'zengyuetian'

"""

# if filesize presents number, return number
# else return str
def VerifyFileSize(size):
    if (size is None):
        return ""
    if size == "":
        return ""
    if all(c in "0123456789.+-" for c in size):
        if(size.find('.') > 0):
            return float(size)
        else:
            return int(size)
    else:
        return size



if __name__ == "__main__":
    str1 = "hello"
    str2 = "123"
    str3 = "100.3"
    print type(VerifyFileSize(str1))
    print type(VerifyFileSize(str2))
    print type(VerifyFileSize(str3))
    print str(str1)

