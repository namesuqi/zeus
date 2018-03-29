# coding=utf-8
"""
__author__ = 'th'

"""
import urllib2

url1 = 'http://192.168.3.177:8001/httpdns?host=live-ch.cloutropy.com'
url2 = 'http://192.168.3.177:8002/httpdns?host=live-ch.cloutropy.com'
url3 = 'http://192.168.3.177:8003/httpdns?host=live-ch.cloutropy.com'
url4 = 'http://192.168.3.177:8004/httpdns?host=live-ch.cloutropy.com'
headers1 = {'X-Real-IP': '1.0.2.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Host': '192.168.3.177:8001'
            }
headers2 = {'X-Real-IP': '1.0.2.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Host': '192.168.3.177:8002'
            }
headers3 = {'X-Real-IP': '1.0.2.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Host': '192.168.3.177:8003'
            }
headers4 = {'X-Real-IP': '1.0.2.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Host': '192.168.3.177:8004'
            }

data = None
while True:
    req1 = urllib2.Request(url1, data, headers1)
    req2 = urllib2.Request(url2, data, headers2)
    req3 = urllib2.Request(url3, data, headers3)
    req4 = urllib2.Request(url4, data, headers4)
    response1 = urllib2.urlopen(req1)
    response2 = urllib2.urlopen(req2)
    html1 = response1.read()
    html2 = response2.read()
    print html1, html2
