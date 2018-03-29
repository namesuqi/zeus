#!/usr/bin/python
import hashlib
from time import gmtime, strftime
import time

def get_data_md5(content):
    md5 = hashlib.md5(str(content))
    return md5.hexdigest()

def get_md5_with_date_offset(content, minoffset):
    gmt = strftime("%a, %d %b %Y %H:%M:%S GMT",
                             gmtime(time.time() - int(minoffset) * 60))
    md5 = hashlib.md5(str(content) + gmt)
    return md5.hexdigest(), gmt

def get_md5_with_date_offset_new(content):
    gmt = 'Mon, 20 Jul 2015 09:24:43 GMT'
    md5 = hashlib.md5(str(content) + gmt)
    return md5.hexdigest(), gmt
