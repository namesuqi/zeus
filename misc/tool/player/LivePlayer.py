# coding=utf-8
"""
模拟直播播放器播放m3u8文件

url是经过sdk播放的
限速根据播放的码率有所不同，直播在300K左右

调用方式：
python LivePlayer.py -u http://xxx.com/yyy.flv -s 300K
__author__ = 'zengyuetian'

"""

import optparse
from random import randint
from time import sleep
from time import ctime
from Queue import Queue
import os
import urllib2
import threading

class MyThread(threading.Thread):
    '''
    线程类
    '''
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print "starting", self.name, "at:", ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at:', ctime()


def writeQ(queue, url):
    '''
    将需要处理的url写入队列
    :param queue:
    :param url:
    :return:
    '''
    queue.put(url)
    print '--> Add url to Q, size now is', queue.qsize()

def readQ(queue):
    '''
    从队列中获得未处理的url
    :param queue:
    :return:
    '''
    i = 0
    while(queue.qsize() == 0):
        sleep(1)
        print "***** Queue is empty, wait"
        if i > 120:
            break
    url = queue.get()
    print '<-- Delete url from Q, size now is', queue.qsize()
    return url

def writer(queue, main_url):
    '''
    生产者
    :param queue: 队列
    :param main_url: 主url
    :return:void
    '''
    while True:
        url_list = get_url_list(main_url)
        for url in url_list:
            #sleep(randint(1, 3))
            if url_dict.get(url, None) is None:
                writeQ(queue, url)
                url_dict[url] = True


def reader(queue, speed):
    '''
    消费者
    :param queue:队列
    :param speed:限速G，M, K, B为单位
    :return:void
    '''
    while True:
        url = readQ(queue)
        #sleep(randint(2, 5))
        # 开始播放url对应的文件
        command = "curl --limit-rate {0} -O {1}".format(speed, url)
        print command
        os.system(command)


def get_url_list(main_url):
    '''
    从主url获得所有url链接
    :param main_url: 主url
    :return:列表
    '''
    response = urllib2.urlopen(main_url)
    html = response.read(response)
    line_list = html.split('\n')
    url_list = [line for line in line_list if line[0:7] == 'http://']
    return url_list

def parse_options():
    # -----------------------------------------------------------------------
    # 分析调用参数
    # usage 定义的是使用方法，%prog 表示脚本本身，version定义的是脚本名字和版本号
    # -u,--user 表示一个是短选项 一个是长选项
    # dest='user' 将该用户输入的参数保存到变量user中，可以通过options.user方式来获取该值
    # type=str，表示这个参数值的类型必须是str字符型，如果是其他类型那么将强制转换为str（可能会报错）
    # metavar='user'，当用户查看帮助信息，如果metavar没有设值，那么显示的帮助信息的参数后面默认带上dest所定义的变量名
    # help='Enter..',显示的帮助提示信息
    # default=3306，表示如果参数后面没有跟值，那么将默认为变量default的值
    # -----------------------------------------------------------------------
    parse = optparse.OptionParser(usage="python LivePlayer.py -u http://xxx.com/yyy.flv -s 100B")
    parse.add_option('-u', '--url', dest='url', action='store', type=str, metavar='url', help='Enter url')
    parse.add_option('-s', '--speed', dest='speed', action='store', type=str, metavar='speed',
                     help='Enter limited speed')

    options, args = parse.parse_args()

    print 'Options:', options
    print 'url is {0}, speed is {1}'.format(options.url, options.speed)
    return (options.url, options.speed)



# 存放所有获得的url，用于去重
url_dict = {}
# 生产者和消费者的线程
funcs = [writer, reader]
nfuncs = range(len(funcs))



def main():

    # 获得命令行参数，分析主url和限速参数
    (main_url, speed) = parse_options()

    #main_url = "http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lsmeSvostHYW3MuybV2NyHNYoRqS"
    q = Queue(1024)
    threads = []

    # 将writer加入
    t = MyThread(writer, (q, main_url), writer.__name__)
    threads.append(t)
    # 将reader加入
    t = MyThread(reader, (q, speed), reader.__name__)
    threads.append(t)

    # 启动两个线程
    for i in nfuncs:
        threads[i].start()

    # 等待线程停止
    for i in nfuncs:
        threads[i].join()

    print 'All done'


def test():
    print get_url_list('http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lsmeSvostHYW3MuybV2NyHNYoRqS')


if __name__ == "__main__":
    main()












    # 多线程，一个线程检查m3u8主文件，将新增的行加入queue
    # 一个线程运行curl将内容从网络上下载下来
    # 限速 curl --limit-rate 1000B -O http://www.gnu.org/software/gettext/manual/gettext.html




    pass



