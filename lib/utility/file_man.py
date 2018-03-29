# coding=utf-8
"""
lib to download file via url

__author__ = 'zengyuetian'

"""

import requests
import os
from lib.constant.ci import *

def download_file(url, filename):
    # local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:   # filter out keep-alive new chunks
                fd.write(chunk)


def find_file_not_match(path, part_name):
    for root, dir, files in os.walk(path):
        for file in files:
            if file.find(part_name) < 0:
                return os.path.join(root, file)




if __name__ == "__main__":
    # download_file(DEVELOP_CENTOS_KIT_URL, "e:/archive.zip")
    find_file_not_match('E:/archive', "bundle")