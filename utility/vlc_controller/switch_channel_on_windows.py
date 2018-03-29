# coding=utf-8
# author: zengyuetian

import time
import os
import subprocess

IS_RTMP = True
IP = "192.168.1.192"
if IS_RTMP:
    PORT = 32718
    PROTOCOL = "rtmp"
else:
    PORT = 32717
    PROTOCOL = "http"


channel_list = ["live_flv/user/wasu?url=http://test.live.cloutropy.com/live/test1",
                "live_flv/user/wasu?url=http://test.live.cloutropy.com/live/test2",
                "live_flv/user/wasu?url=http://test.live.cloutropy.com/live/test3"]


url_list = ["{0}://{1}:{2}/{3}".format(PROTOCOL, IP, PORT, channel) for channel in channel_list]

print url_list

while True:
    for url in url_list:
        os.system("taskkill /IM vlc.exe /F")
        command = "vlc --no-repeat --open={0}".format(url)
        subprocess.Popen(command, shell=True)
        time.sleep(0.5)



