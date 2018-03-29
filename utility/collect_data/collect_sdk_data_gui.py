# coding=utf-8
"""
collect p2p data according to rules
use multi threading to improve performance

__author__ = 'zengyuetian'

"""

import requests
import json
import time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation


REQUEST_TIMEOUT = 5
PORT_START = 60000
PORT_STEP = 10
SDK_NUM = 70
STREAM_TARGET = 32
INIT_Y_LIMIT = 200
SAMPLE_NUM = 20

# IP_LIST = ['120.52.28.214', '124.232.148.103']

IP_LIST = ['221.131.105.19', '116.31.120.11', '113.107.207.241', '171.107.82.45', '218.6.154.172',
           '61.183.52.32', '111.161.66.134', '202.111.173.115', '60.217.25.209', '221.204.173.207',
           '120.52.28.214',
           '124.232.148.103', '36.250.226.115', '122.188.107.253', '112.245.16.149', '58.222.48.19']

p2p_list = []
bad_p2p_list = []
seed_num_list = []
stream_num_list = []
bad_stream_list = []
download_rate_list = []

num = 0

xdata_p2p, ydata_p2p = [], []
xdata_bad, ydata_bad = [], []
xdata_stream, ydata_stream = [], []
xdata_seed, ydata_seed = [], []


#######################
# CLASS goes from here
#######################
class dictseq():
    def __init__(self, l):
        self.seq = l
        self.dict = {}

    def __getitem__(self, name):
        if name in self.dict:
            return self.dict[name]
        idx = len(self.dict) % len(self.seq)
        self.dict[name] = self.seq[idx]
        return self.dict[name]

    def __str__(self):
        return "seq:%d dicts:%d keys:%s" % (len(self.seq), len(self.dict), ",".join(self.dict.keys()))

class dictcolors(dictseq):

    def __init__(self):
        dictseq.__init__(self, ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                                "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

class dictmarkers(dictseq):

    def __init__(self):
        dictseq.__init__(self, ['o', 's', '^', '*', 'D', 'H'])


def send_request(host_ip, host_port, url):
    url = "http://{0}:{1}{2}".format(host_ip, host_port, url)

    headers = dict()
    headers["accept"] = 'application/json'

    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    return resp

def get_sdk_data(host_ip, host_port):
    try:
        res = send_request(host_ip, host_port, "/ajax/report")
        p2p_percent = json.loads(res.content).get("p2p_percent", None)
        seed_num = json.loads(res.content).get("seed_num", None)
        stream_num = json.loads(res.content).get("stream_num", None)
        download_rate = json.loads(res.content).get("download_rate", None)
        if mutex.acquire(1):
            p2p_list.append(p2p_percent)
            seed_num_list.append(seed_num)
            stream_num_list.append(stream_num)
            download_rate_list.append(download_rate)
            if stream_num < STREAM_TARGET:
                bad_stream_list.append("{0}:{1}".format(host_ip, host_port))
            mutex.release()
    except:
        if mutex.acquire(1):
            p2p_list.append(0)
            seed_num_list.append(0)
            stream_num_list.append(0)
            download_rate_list.append(0)
            bad_p2p_list.append("{0}:{1}".format(host_ip, host_port))
            bad_stream_list.append("{0}:{1}".format(host_ip, host_port))
            mutex.release()


def data_gen():
    global xdata_p2p, ydata_p2p
    global xdata_bad, ydata_bad
    global xdata_stream, ydata_stream
    global xdata_seed, ydata_seed

    while True:
        global p2p_list, bad_p2p_list, seed_num_list, stream_num_list, bad_stream_list, download_rate_list
        p2p_list = []
        bad_p2p_list = []
        seed_num_list = []
        stream_num_list = []
        bad_stream_list = []
        download_rate_list = []

        time1 = time.time()
        for ip in IP_LIST:
            time.sleep(0.1)  # wait some time to start huge threads
            for port in dash_board_port_list:
                t = threading.Thread(target=get_sdk_data, args=(ip, port))
                t.start()

        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

        time2 = time.time()
        zero_list = [x for x in p2p_list if x == 0]
        non_zero_list = [x for x in p2p_list if x != 0]
        current = time.localtime()
        time_str = time.strftime("%Y/%m/%d %H:%M:%S", current)
        bad_p2p_list.sort()
        bad_stream_list.sort()
        ydata_p2p.append(sum(non_zero_list) / len(non_zero_list))
        ydata_bad.append(len(bad_p2p_list))
        ydata_seed.append(len([i for i in seed_num_list if i < 32]))
        ydata_stream.append(len([i for i in stream_num_list if i < 32]))


        print
        print "********** {0} cost {1} seconds to get result **********".format(time_str, time2 - time1)
        print "IP number is: ", len(IP_LIST), IP_LIST

        print "SDK number is: {0}".format(len(p2p_list))
        print "------------------------------------------"
        print "P2P List", p2p_list
        print "All sdk average p2p is: {0}%".format(sum(p2p_list) / len(p2p_list))
        print "Alive sdk average p2p is: {0}%".format(sum(non_zero_list) / len(non_zero_list))
        print "Max p2p is {0}%, Min p2p is {1}%".format(max(non_zero_list), min(non_zero_list))
        print "{0} SDKs with p2p >= 80%".format(len([i for i in non_zero_list if i >= 80]))
        print "{1}{0} SDKs with p2p 0%{1}".format(len(zero_list),
                                                  "         @@@@@@@@@@@@         " if len(zero_list) > 0 else "")
        print "P2P 0 sdk info: ", bad_p2p_list
        print "------------------------------------------"
        print "Seed List", seed_num_list
        print "{0} SDKs with seed < 32".format(len([i for i in seed_num_list if i < 32]))
        print "------------------------------------------"
        print "Stream List", stream_num_list
        print "{0} SDKs with stream >= 32".format(len([i for i in stream_num_list if i >= 32]))
        print "{0} SDKs with stream < 32".format(len([i for i in stream_num_list if i < 32]))
        print "Stream < 32 sdk info: ", bad_stream_list
        print "------------------------------------------"
        print "Download List", download_rate_list
        print "All sdk average download rate {0}".format(sum(download_rate_list) / len(download_rate_list))
        print "Alive sdk average download rate {0}".format(sum(download_rate_list) / len(non_zero_list))
        print "*******************************************************************************"

        yield 0

def run(data):
    # share data in functions
    global num
    global xdata_p2p, ydata_p2p
    global xdata_bad, ydata_bad
    global xdata_stream, ydata_stream
    global xdata_seed, ydata_seed
    num = num + 1
    xdata_stream.append(num)
    xdata_seed.append(num)
    xdata_p2p.append(num)
    xdata_bad.append(num)

    dummy = data

    # update display range of canvas
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    max_p2p = max(ydata_p2p)
    max_busy = max(ydata_bad)
    max_stream = max(ydata_stream)
    max_seed = max(ydata_seed)
    max_y_value = max(max_p2p, max_busy, max_seed, max_stream)


    # update xlim
    if num > x_max:
        ax.set_xlim(x_min + 10, x_max + 10)

    # update ylim
    if max_y_value > y_max:
        ax.set_ylim(y_min, max_y_value + 10)

    ax.figure.canvas.draw()


    # only keep SAMPLE_NUM samples in list to improve performance
    if len(ydata_p2p) > SAMPLE_NUM:
        ydata_p2p = ydata_p2p[len(ydata_p2p)-SAMPLE_NUM:]
        xdata_p2p = xdata_p2p[len(xdata_p2p) - SAMPLE_NUM:]

    if len(ydata_bad) > SAMPLE_NUM:
        ydata_bad = ydata_bad[len(ydata_bad) - SAMPLE_NUM:]
        xdata_bad = xdata_bad[len(xdata_bad) - SAMPLE_NUM:]

    if len(ydata_seed) > SAMPLE_NUM:
        ydata_seed = ydata_seed[len(ydata_seed) - SAMPLE_NUM:]
        xdata_seed = xdata_seed[len(xdata_seed) - SAMPLE_NUM:]

    if len(ydata_stream) > SAMPLE_NUM:
        ydata_stream = ydata_stream[len(ydata_stream) - SAMPLE_NUM:]
        xdata_stream = xdata_stream[len(xdata_stream) - SAMPLE_NUM:]


    # display delay data on SRS
    line_p2p.set_data(xdata_p2p, ydata_p2p)
    line_busy.set_data(xdata_bad, ydata_bad)
    line_low_seed.set_data(xdata_seed, ydata_seed)
    line_low_stream.set_data(xdata_stream, ydata_stream)

    return line_p2p, line_busy, line_low_seed, line_low_stream


if __name__ == "__main__":
    colors = dictcolors()
    markers = dictmarkers()
    mutex = threading.Lock()

    dash_board_port_list = []
    for i in range(SDK_NUM):
        dash_board_port_list.append(PORT_START + i * PORT_STEP)
    # print dash_board_port_list

    # init canvas
    data_gen.t = 0

    # fig, ax = plt.subplots()
    fig = plt.figure(figsize=(12, 9), dpi=72, facecolor="white")
    ax = plt.subplot()
    fig.canvas.set_window_title("LIVE DATA：")

    # define lines for srs, push, sdk
    line_p2p, = ax.plot([], [], lw=2, color='y', label="p2p", linestyle='-')  # yellow line
    line_busy, = ax.plot([], [], lw=1, color='g', label="busy", linestyle='-')  # green line
    line_low_stream, = ax.plot([], [], lw=1, color='b', label="low_stream", linestyle='-', marker='*')    # blue line
    line_low_seed, = ax.plot([], [], lw=1, color='r', label="low_seed", linestyle='-')  # red line

    ax.set_ylim(0, INIT_Y_LIMIT)
    ax.set_xlim(0, SAMPLE_NUM)
    ax.grid(color='y', linestyle='--', linewidth=1)

    # allocate color and marker
    idx = 0

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)

    # every second call run, run's param is function data_gen
    ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=1000, repeat=False)
    plt.show()





