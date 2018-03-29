# coding=utf-8
"""
不停地将m3u8子片段写入文件
用于测试直播播放器的模拟器

__author__ = 'zengyuetian'

"""

from random import randint
import time
if __name__ == "__main__":
    for i in range(124):
        time.sleep(randint(1, 4))
        with open("zeus.m3u8", "a") as f:
            url = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lsmeSvostHYW3MuybV2NyHNYoRqS/seg{0}\n".format(str(i))
            f.write(url)
            f.flush()