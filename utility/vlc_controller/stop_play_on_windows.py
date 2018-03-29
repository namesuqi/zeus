# coding=utf-8
"""
stop play via killing vlc process

__author__ = 'zengyuetian'

"""

import os

if __name__ == "__main__":
    os.system("taskkill /IM vlc.exe /F")