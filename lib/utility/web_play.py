# coding=utf-8
"""
play live channel via web page

http://www.ossrs.net/srs.release/trunk/research/players/osmf.html?vhost=players

__author__ = 'zengyuetian'

"""

from selenium import webdriver
from lib.utility.system import *
import time

PLAYER_URL = "http://www.ossrs.net/srs.release/trunk/research/players/osmf.html?vhost=players"


def PlayChannelViaSdk(channel_url):
    driver = webdriver.Chrome()
    driver.get(PLAYER_URL)
    driver.find_element_by_xpath('//*[@id="txt_url"]').clear()
    driver.find_element_by_xpath('//*[@id="txt_url"]').send_keys(channel_url)
    time.sleep(2)
    driver.find_element_by_id("btn_play").click()  # 使用多个class中的某个可以区分的class即可
    time.sleep(10)
    # GetProcessMemoryOnWindows('p2pclient')
    GetProcessMemoryOnLinux("192.168.1.151", "ubuntu-android", "123.com")
    driver.quit()


if __name__ == "__main__":
    KillSdkOnLinux("192.168.1.151", "ubuntu-android", "123.com")
    DeploySdkToLinux("192.168.1.151", "ubuntu-android", "123.com")
    StartSdkOnLinux("192.168.1.151", "ubuntu-android", "123.com")
    time.sleep(15)
    while True:
        # PlayChannelViaSdk('http://192.168.1.26:32717/live_flv/user/simshi?url=rtmp%3a%2f%2flive.hkstv.hk.lxdns.com%3A80%2Flive%2Fhks')
        PlayChannelViaSdk(
            'http://192.168.1.151:32717/live_flv/user/simshi?url=rtmp%3a%2f%2flive.hkstv.hk.lxdns.com%3A80%2Flive%2Fhks')



