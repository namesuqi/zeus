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

login_url = 'http://10.4.0.1:8080/j_acegi_security_check'
builds = ["p2pclient_ut", "p2pserver_ut"]
referer_url = "http://10.4.0.1:8080/view/Auto-Test-DailyTest/job/p2pclient_ut/lastCompletedBuild/testReport"


class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        '''登录网站'''

        login_params = {"j_username": "zengyuetian", "j_password": "vliQh3U2byob", "remember_me": False, "from": "/"}
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Accept': "text/html",
            # "Accept-Encoding": "gzip, deflate"

        }
        # req = urllib2.Request(loginurl, urllib.urlencode(loginparams), headers=headers)
        req = urllib2.Request(login_url, urllib.urlencode(login_params), headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

        req = urllib2.Request(referer_url, None, headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage




if __name__ == '__main__':
    userlogin = Login()
    userlogin.login()

