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

login_url = 'http://10.3.0.12:8080/zentao/user-login.html'
referer_url = "http://10.3.0.12:8080/zentao/bug-report-1-unclosed-0.html"

class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        '''登录网站'''
        # loginparams = {"account": "zengyuetian", "password": "123456", "keepLogin[]": "on", "referer": refererurl}
        login_params = "account=zengyuetian&password=123456&keepLogin%5B%5D=on&referer=http%3A%2F%2F10.3.0.12%3A8080%2Fzentao%2Fbug-report-1-unclosed-0.html"
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Accept': "text/html",
            # "Accept-Encoding": "gzip, deflate"

        }
        # req = urllib2.Request(loginurl, urllib.urlencode(loginparams), headers=headers)
        req = urllib2.Request(login_url, login_params, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

        query_params = "charts%5B%5D=openedBugsPerUser"
        req = urllib2.Request(referer_url, query_params, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage


if __name__ == '__main__':
    userlogin = Login()
    userlogin.login()

