#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import time
import os
import subprocess


def current_time():
    currenttime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return currenttime


def vlc_play_video(video_url):
    startvideo = "vlc --no-repeat --open=%s" % video_url
    newsub = subprocess.Popen(startvideo, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stopvlc = "taskkill /F /IM vlc.exe"
    time.sleep(20)  # start vlc and contiue 10 seconds
    #  newsub.kill()
    newsub.terminate()


def seek_video_in_vlc(video_url, seek_times):
    # --key-jump-extrashort <整型> 向后跳一很小的段
    # --key-jump+extrashort <整型> 向前跳一很小的段
    # --key-jump-short <整型>  向后跳一小段
    # --key-jump+short <整型>  向前跳一小段
    # --key-jump-medium <整型> 向后跳一中段
    # --key-jump+medium <整型> 向前跳一中段
    # --key-jump-long <整型>   向后跳一大段
    # --key-jump+long <整型>   向前跳一大段
    startvideo = "vlc --no-repeat --open=%s" % video_url
    newsub = subprocess.Popen(startvideo, stdin=subprocess.PIPE, close_fds=False)
    print "1"
    newsub.communicate(input="--key-fullscreen")
    print "2"

def change_channel_test(play_times, video_list):
    i = 0
    while i < play_times:
        for video in video_list:
            vlc_play_video(video)
        i += 1
    print "Finished Testing!Change channel %s times" % str(i * 3 - 1)

if __name__ == '__main__':
    VIDEO_1 = "http://192.168.1.90:32717/live_m3u8/user/leigang?url=http://hls.srs.cloutropy.com/wasu/86A3C9EB226F4E09BA6CAACB5EC2F8D8.m3u8"
    VIDEO_2 = "http://192.168.1.90:32717/live_m3u8/user/leigang?url=http://hls.srs.cloutropy.com/wasu/8D29BC7136354E0D8CE119881F5FE005.m3u8"
    VIDEO_3 = "http://192.168.1.63:32717/hls/user/ciwen?url=http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lpUd04T3JyXX0EpnpbgGCeyExTps"
    # VIDEO_2 = "http://192.168.1.63:32717/vod/user/thunder?url=http://cdn.cloutropy.com/thunder/phone_demo_ocean_8mbps.ts"
    # VIDEO_3 = "http://192.168.1.63:32717/vod/user/thunder?url=http://cdn.cloutropy.com/thunder/phone_demo_ocean_4mbps.ts"
    VIDEOURL = [VIDEO_1]


    # test change channel
    TIMES = 20
    change_channel_test(TIMES, VIDEOURL)
    # test seek video in vlc
    # seek_video_in_vlc(VIDEO_3, TIMES)

else:
    pass
