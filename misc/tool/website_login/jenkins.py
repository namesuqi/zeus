# coding=utf-8
# author: zengyuetian

import sys
import re
import urllib2
import urllib
import requests
import cookielib

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

loginurl = 'http://10.4.0.1:8080/login?from=%2F'



class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, username, password):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password


    def login(self):
        '''登录网站'''
        loginparams = {"j_username": "zengyuetian", "j_password": "vliQh3U2byob", "remember_me": False, "from": "/"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams), headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

        # pic_url = "http://10.4.0.1:8080/view/Auto-Test-DailyTest/"
        pic_url = "http://10.4.0.1:8080/static/42a4ec3a/images/headshot.png"
        # pic_url = "http://10.4.0.1:8080/view/Auto-Test-DailyTest/job/BJ-Auto-Test-Deploy_SDK_System_Start/292/robot/graph?zoomSignificant=true&failedOnly=false&criticalOnly=false&maxBuildsToShow=0&hd=true"
        req = urllib2.Request(pic_url, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        # print thePage
        f = file("pic.png", "wb")
        f.write(thePage)
        f.close()



    def get_pic(self):
        pic_url = "http://10.4.0.1:8080/view/Auto-Test-DailyTest/job/BJ-Auto-Test-Deploy_SDK_System_Start/292/robot/graph?zoomSignificant=true&failedOnly=false&criticalOnly=false&maxBuildsToShow=0&hd=true"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(pic_url, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        f = file("pic.png", "wb")
        f.write(thePage)
        f.close()


if __name__ == '__main__':
    userlogin = Login()
    username = 'zengyuetian'
    password = 'vliQh3U2byob'
    userlogin.setLoginInfo(username, password)
    userlogin.login()
    # userlogin.get_pic()
