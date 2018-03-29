# coding=utf-8
"""
PYTHON SCRIPT TO DISPLAY LIVE 3.0 DELAY RELATED DATAS
Monitor delay data on SRS, PUSH, LF, SDK

***** user guide (please read it firstly) *****
0. make sure run "nohup python delay_server.py push &" on push server, otherwise set SHOW_PUSH_DATA = False
1. start sdk on 32717 port, if not use default port, please update SDK_PORT, SDK_IP
2. play live channel via sdk, set FILE_ID, make sure NUM_OF_INTEREST of chunks have already arrived SDK
3. start this script to get srs, push, sdk related delay data
4. if you want to display Leifeng related data, please pull leifeng firstly and update lf_nodes

__author__ = 'Zeng YueTian'
"""

import requests
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

# define global variables
# need to update following params
SHOW_PUSH_DATA = False

# list of LF ip and port
lf_nodes = list()

# IP and port of leifeng

FILE_ID = "2A56A52A6617F5942187555642BD849B"
# lf_nodes.append({"ip": "60.169.74.3", "port": "60002"})
SDK_IP, SDK_PORT = "127.0.0.1", "32719"    # sdk ip and dashboard port
PUSH_IP, PUSH_PORT = "10.5.100.22", "32720"  # push server ip and port

lf_data_collectors = list()  # object list of leifeng data
SAMPLE_NUM = 100       # how many items display on graph
NUM_OF_INTEREST = 20   # how many items get from http interface
INIT_Y_LIMIT = 1200    # init length of y-line
DEBUG_PRINT_INDEX = -11
SAFE_CHUNK_NUM = 5     # sometime the bigger chunk_id will firstly arrive sdk, so ignore the latest chunks

lf_ip_addresses = list()     # LF ip list
srs_pre_time_stamp = 0       # to save previous chunk time stamp

# ########################################################################################
# chunk_id, T0: chunk generated time, Tn: chunk left time , T0n=Tn-T0: chunk delay time
# ########################################################################################
xdata_srs_cid, ydata_srs_t0, ydata_srs_t1, ydata_srs_t01 = [], [], [], []  # SRS
xdata_push_cid, ydata_push_t0, ydata_push_t2, ydata_push_t02 = [], [], [], []  # PUSH
xdata_sdk_cid, ydata_sdk_t0, ydata_sdk_t4, ydata_sdk_t04 = [], [], [], []  # SDK
xdata_delay_cid, ydata_delay_t = [], []  # diff between SDK and PUSH

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

########################
# class to collect leifeng data
########################
class LfDataCollector(object):
    def __init__(self, lf_ip, lf_port):
        self.lf_ip = lf_ip
        self.lf_port = lf_port
        self.xdata_lf_cid = []
        self.ydata_lf_t0 = []
        self.ydata_lf_t3 = []
        self.ydata_lf_t03 = []

    def get_lf_data(self):
        lf_query_url = 'http://{0}:{1}/ajax/amplifier'.format(self.lf_ip, self.lf_port)
        r = requests.get(lf_query_url)
        data = json.loads(r.content)

        # parse for delay related data
        data = get_data_by_path(data, '/0/delay')

        data_dict = dict()
        for item in data:
            data_dict[str(item['chunk_id'])] = item

        # sort dictionary by chunk id
        data = sorted(data_dict.iteritems(), key=lambda d: long(d[0]), reverse=False)
        length = len(data)

        data = data[length - NUM_OF_INTEREST:]  # only keep some data

        for chunk_id, content_dict in data:
            if chunk_id == '0':
                continue

            # if it is a new chunk
            if long(content_dict['chunk_id']) not in self.xdata_lf_cid:
                # print chunk_id, time_stamp
                # add chunk id
                self.xdata_lf_cid.append(content_dict['chunk_id'])

                # add t0
                self.ydata_lf_t0.append(content_dict['base_time'])

                # add t1
                self.ydata_lf_t3.append(content_dict['get_time'])

                # add delay, delta = t1-t0,
                # print "{0}-{1}={2}".format(ydata_sdk_t4[-1], ydata_sdk_t0[-1], ydata_sdk_t4[-1] - ydata_sdk_t0[-1])
                self.ydata_lf_t03.append(self.ydata_lf_t3[-1] - self.ydata_lf_t0[-1])
            else:
                continue

######################################################
# functions goes from here
######################################################

#####################################
# generate new data for each calling
#####################################
def data_gen():
    while True:
        # collect SRS related delay data
        t = threading.Thread(target=get_srs_data)
        t.start()

        # collect PUSH related delay data
        if SHOW_PUSH_DATA:
            t = threading.Thread(target=get_push_data, args=(FILE_ID,))
            t.start()

        # collect SDK related delay data
        t = threading.Thread(target=get_sdk_data)
        t.start()

        # collect LF related delay data
        for collector in lf_data_collectors:
            t = threading.Thread(target=collector.get_lf_data())
            t.start()

        # wait for thread done
        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()
        # calculate diff between PUSH and SDK

        for i in xdata_sdk_cid[:-1]:
            if (i not in xdata_delay_cid) and (i in xdata_srs_cid):
                xdata_delay_cid.append(i)
                j = xdata_sdk_cid.index(i)
                k = xdata_srs_cid.index(i)
                ydata_delay_t.append(ydata_sdk_t04[j] - ydata_srs_t01[k])
        yield 0

#####################################
# collect SRS related delay data
#####################################
def get_srs_data():
    global srs_pre_time_stamp

    r = requests.get("http://{0}:{1}/ajax/channeler".format(SDK_IP, SDK_PORT))
    data = json.loads(r.content)

    # parse for delay related data
    data = get_data_by_path(data, '/0/channel_stats/liveDelay')

    data_dict = dict()
    for item in data:
        data_dict[str(item['chunk_id'])] = item['base_time']

    # data = data_dict
    '''
    {"4484": "1463554053343", "4485": "1463554055848",
    "4479": "1463554034074", "4478": "1463554031824",
    "4486": "1463554059599", "4480": "1463554037956",
    "4481": "1463554042211", "4482": "1463554045583",
    "4483": "1463554049220"}
    '''
    # sort dictionary by chunk id
    data = sorted(data_dict.iteritems(), key=lambda d: long(d[0]), reverse=False)
    length = len(data)
    data = data[length - NUM_OF_INTEREST:]  # only keep some data
    for chunk_id, time_stamp in data[:-SAFE_CHUNK_NUM]:
        chunk_id_num = long(chunk_id)
        time_stamp_num = long(time_stamp)

        # if it is a new chunk
        if chunk_id_num not in xdata_srs_cid:
            # add chunk id
            xdata_srs_cid.append(chunk_id_num)

            # add t0
            ydata_srs_t0.append(time_stamp_num)

            # calculate delta t
            if len(ydata_srs_t01) == 0:
                ydata_srs_t01.append(0)  # add a place holder for index 0
            else:
                ydata_srs_t01[-1] = (time_stamp_num - srs_pre_time_stamp) # calculate delay for previous chunk
                ydata_srs_t01.append(0)   # add a place holder for current index
                # print "{0}-{1}={2}".format(time_stamp_num, pre_time_stamp, time_stamp_num - pre_time_stamp)
            srs_pre_time_stamp = time_stamp_num
        else:
            continue
    # to remove 0 from the last element


##############################
# collect PUSH related delay time
##############################
def get_push_data(file_id):
    r = requests.get("http://{0}:{1}/timestamp?fid={2}".format(PUSH_IP, PUSH_PORT, file_id))
    data = json.loads(r.content)
    '''
    {"90": {"base_time": 1463553793951, "local_time": 1463553798744, "chunk_id": 90},
     "91": {"base_time": 1463553798899, "local_time": 1463553802939, "chunk_id": 91},
     "92": {"base_time": 1463553802927, "local_time": 1463553806460, "chunk_id": 92},
     "93": {"base_time": 1463553806645, "local_time": 1463553810532, "chunk_id": 93},
     "94": {"base_time": 1463553810521, "local_time": 1463553813706, "chunk_id": 94}}
     '''
    # sort dictionary by chunk id
    data = sorted(data.iteritems(), key=lambda d: long(d[0]), reverse=False)
    length = len(data)
    data = data[length-NUM_OF_INTEREST:]  # only keep some data
    for chunk_id, content_dict in data:
        # if it is a new chunk
        if long(chunk_id) not in xdata_push_cid:
            # print chunk_id, time_stamp
            # add chunk id
            xdata_push_cid.append(long(chunk_id))

            # add t0
            ydata_push_t0.append(long(content_dict['base_time']))

            # add t1
            ydata_push_t2.append(long(content_dict['local_time']))

            # add delay, delta = t1-t0,
            # print "{0}-{1}={2}".format(ydata_srs_t1[-1], ydata_srs_t0[-1], ydata_srs_t1[-1] - ydata_srs_t0[-1])
            ydata_push_t02.append(ydata_push_t2[-1] - ydata_push_t0[-1])
        else:
            continue

##############################
# collect SDK related delay data
##############################
def get_sdk_data():
    r = requests.get("http://{0}:{1}/ajax/channeler".format(SDK_IP, SDK_PORT))
    data = json.loads(r.content)

    # parse for delay related data
    data = get_data_by_path(data, '/0/channel_stats/liveDelay')

    data_dict = dict()
    for item in data:
        data_dict[str(item['chunk_id'])] = item

    # sort dictionary by chunk id
    data = sorted(data_dict.iteritems(), key=lambda d: long(d[0]), reverse=False)
    length = len(data)

    data = data[length - NUM_OF_INTEREST:]  # only keep some data

    for chunk_id, content_dict in data[:-SAFE_CHUNK_NUM]:
        # if it is a new chunk
        if long(content_dict['chunk_id']) not in xdata_sdk_cid:
            # add chunk id
            xdata_sdk_cid.append(content_dict['chunk_id'])

            # add t0
            ydata_sdk_t0.append(content_dict['base_time'])

            # add t1
            ydata_sdk_t4.append(content_dict['get_time'])

            # add delay, delta = t1-t0,
            # print "{0}-{1}={2}".format(ydata_sdk_t4[-1], ydata_sdk_t0[-1], ydata_sdk_t4[-1] - ydata_sdk_t0[-1])
            ydata_sdk_t04.append(ydata_sdk_t4[-1] - ydata_sdk_t0[-1])
        else:
            continue

##############################
# get SDK's LF address (not use anymore)
##############################
def get_lf_ip_addresses(sdk_ip, sdk_is_lf=False):
    seeder_ip_list = list()
    if sdk_is_lf:
        seeder_ip_list.append(sdk_ip)

    # get seeder list from sdk dashboard
    seeder_url = 'http://{0}:32719/ajax/seeder'.format(sdk_ip)
    r = requests.get(seeder_url)
    data = json.loads(r.content)

    # parse for delay related data
    length = len(data)
    for i in range(length):
        ip_str = get_data_by_path(data, '/{0}/addr/pub_iport/ip'.format(i))
        if ip_str != "0.0.0.0" and ip_str != "192.168.1.42":
            seeder_ip_list.append(ip_str)

    return seeder_ip_list

##############################
# parse json data via path
##############################
def get_data_by_path(data, path):
    '''
    function to parse json data to get specified field value
    :param data:
    :param path: such as /0/fild_ids/1
    :return:
    '''

    # if start with /，remove /
    if path.startswith("/"):
        path = path[1:]
    key_list = path.split("/")
    num_list = [str(x) for x in range(100)]  # import to support index more than 10

    try:
        for key in key_list:
            if key in num_list:  # for number array
                index = int(key)
                data = data[index]
            else:  # for key
                data = data.get(key)
    except:
        data = None

    return data

##############################
# refresh graph
##############################
def run(data):
    # share data in functions
    global xdata_srs_cid, ydata_srs_t0, ydata_srs_t1, ydata_srs_t01
    global xdata_push_cid, ydata_push_t0, ydata_push_t2, ydata_push_t02
    global xdata_sdk_cid, ydata_sdk_t0, ydata_sdk_t4, ydata_sdk_t04
    global xdata_delay_cid, ydata_delay_t
    global lf_data_collectors
    dummy = data

    # update display range of canvas
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    max_cid = max(xdata_srs_cid)
    min_cid = min(xdata_srs_cid)
    y_max_srs = max(ydata_srs_t01)
    if SHOW_PUSH_DATA:
        y_max_push = max(ydata_push_t02)
    y_max_sdk = max(ydata_sdk_t04)

    # get ride of some incorrect data (for example if delay > 10s)
    if SHOW_PUSH_DATA:
        if max(y_max_srs, y_max_push, y_max_sdk) < 10*1000:
            max_delay = max(y_max_srs, y_max_push, y_max_sdk)
        else:
            print "ERROR: delay > 10s", max(y_max_srs, y_max_push, y_max_sdk)
            max_delay = y_max
    else:
        if max(y_max_srs, y_max_sdk) < 10 * 1000:
            max_delay = max(y_max_srs, y_max_sdk)
        else:
            print "ERROR: delay > 10s", max(y_max_srs, y_max_sdk)
            max_delay = y_max

    # update xlim
    if max_cid > x_max:
        ax.set_xlim(min_cid + 1, max_cid + 1)

    # update ylim
    if max_delay > y_max:
        ax.set_ylim(y_min, (max_delay/100+1) * 100)

    # if delay is decreased, decrease ylim
    if max_delay < y_max - 200:
        ax.set_ylim(y_min, y_max - 200)
    ax.figure.canvas.draw()

    # only keep SAMPLE_NUM samples in list to improve performance
    if len(xdata_srs_cid) > SAMPLE_NUM:
        xdata_srs_cid = xdata_srs_cid[len(xdata_srs_cid)-SAMPLE_NUM:]
        ydata_srs_t0 = ydata_srs_t0[len(ydata_srs_t0) - SAMPLE_NUM:]
        ydata_srs_t1 = ydata_srs_t1[len(ydata_srs_t1) - SAMPLE_NUM:]
        ydata_srs_t01 = ydata_srs_t01[len(ydata_srs_t01)-SAMPLE_NUM:]

    if SHOW_PUSH_DATA and len(xdata_push_cid) > SAMPLE_NUM:
        xdata_push_cid = xdata_push_cid[len(xdata_push_cid) - SAMPLE_NUM:]
        ydata_push_t0 = ydata_push_t0[len(ydata_push_t0) - SAMPLE_NUM:]
        ydata_push_t2 = ydata_push_t2[len(ydata_push_t2) - SAMPLE_NUM:]
        ydata_push_t02 = ydata_push_t02[len(ydata_push_t02) - SAMPLE_NUM:]

    if len(xdata_sdk_cid) > SAMPLE_NUM:
        xdata_sdk_cid = xdata_sdk_cid[len(xdata_sdk_cid) - SAMPLE_NUM:]
        ydata_sdk_t0 = ydata_sdk_t0[len(ydata_sdk_t0) - SAMPLE_NUM:]
        ydata_sdk_t4 = ydata_sdk_t4[len(ydata_sdk_t4) - SAMPLE_NUM:]
        ydata_sdk_t04 = ydata_sdk_t04[len(ydata_sdk_t04) - SAMPLE_NUM:]

    if len(xdata_delay_cid) > SAMPLE_NUM:
        xdata_delay_cid = xdata_delay_cid[len(xdata_delay_cid) - SAMPLE_NUM:]
        ydata_delay_t = ydata_delay_t[len(ydata_delay_t) - SAMPLE_NUM:]

    for collector in lf_data_collectors:
        if len(collector.xdata_lf_cid) > SAMPLE_NUM:
            collector.xdata_lf_cid = collector.xdata_lf_cid[len(collector.xdata_lf_cid) - SAMPLE_NUM:]
            collector.ydata_lf_t0 = collector.ydata_lf_t0[len(collector.ydata_lf_t0) - SAMPLE_NUM:]
            collector.ydata_lf_t3 = collector.ydata_lf_t3[len(collector.ydata_lf_t3) - SAMPLE_NUM:]
            collector.ydata_lf_t03 = collector.ydata_lf_t03[len(collector.ydata_lf_t03) - SAMPLE_NUM:]

    # seek the same position to display
    # make sure only lines display the data in same range
    # if some chunk only exists on srs，skip them
    for i in range(1, 20):
        chunk_id = xdata_srs_cid[i]
        print chunk_id

        if SHOW_PUSH_DATA:
            try:
                index_push = xdata_push_cid.index(chunk_id)
            except Exception:
                print "Error: Chunk id {0} can not be found in PUSH delay list.".format(chunk_id)
                continue

        try:
            index_sdk = xdata_sdk_cid.index(chunk_id)
        except Exception:
            print "Error: Chunk id {0} can not be found in SDK delay list.".format(chunk_id)
            print xdata_srs_cid
            print xdata_sdk_cid
            continue

        try:
            index_delay = xdata_delay_cid.index(chunk_id)
        except Exception:
            print "Error: Chunk id {0} can not be found in  Delay(sdk-source) list.".format(chunk_id)
            continue

        # if no error occurs, quit loop
        break

    idx = 0  # allocate color and marker
    for collector in lf_data_collectors:
        index_lf = collector.xdata_lf_cid.index(chunk_id)
        plt.scatter(collector.xdata_lf_cid[index_lf:], collector.ydata_lf_t03[index_lf:],
                    color=colors[idx], marker=markers[idx], alpha=0.3, edgecolors='yellow', label='lf')
        idx += 1

    # display delay data on SRS
    line_srs.set_data(xdata_srs_cid[i:-1], ydata_srs_t01[i:-1])

    # display delay data on PUSH
    if SHOW_PUSH_DATA:
        line_push.set_data(xdata_push_cid[index_push:], ydata_push_t02[index_push:])

    # display delay data on SDK
    line_sdk.set_data(xdata_sdk_cid[index_sdk:], ydata_sdk_t04[index_sdk:])

    # display delay(sdk-srs) data
    line_delay.set_data(xdata_delay_cid[index_delay:], ydata_delay_t[index_delay:])

    # ---------------    Debugging region start, DO NOT change    -------------------
    #
    #       only print latest 11 items
    #

    #     print srs data for debugging
    print ""
    print "SRS chunk_id:", xdata_srs_cid[DEBUG_PRINT_INDEX:]
    print "SRS base_time:", ydata_srs_t0[DEBUG_PRINT_INDEX:]
    print "SRS get_time:", ydata_srs_t1[DEBUG_PRINT_INDEX:]
    print "SRS delay_time:", ydata_srs_t01[DEBUG_PRINT_INDEX:]

    #     print push data for debugging
    if SHOW_PUSH_DATA:
        print "PUSH chunk_id:", xdata_push_cid[DEBUG_PRINT_INDEX:]
        print "PUSH base_time:", ydata_push_t0[DEBUG_PRINT_INDEX:]
        print "PUSH get_time:", ydata_push_t2[DEBUG_PRINT_INDEX:]
        print "PUSH delay_time:", ydata_push_t02[DEBUG_PRINT_INDEX:]

    #     print leifeng data for debugging
    for collector in lf_data_collectors:
        print "--------------"
        print "LF IP:", collector.lf_ip
        print "LF chunk_id:", collector.xdata_lf_cid[DEBUG_PRINT_INDEX:]
        print "LF base_time:", collector.ydata_lf_t0[DEBUG_PRINT_INDEX:]
        print "LF get_time:", collector.ydata_lf_t3[DEBUG_PRINT_INDEX:]
        print "LF delay_time:", collector.ydata_lf_t03[DEBUG_PRINT_INDEX:]

    #     print SDK data for debugging
    print "SDK chunk_id:", xdata_sdk_cid[DEBUG_PRINT_INDEX:]
    print "SDK base_time:", ydata_sdk_t0[DEBUG_PRINT_INDEX:]
    print "SDK get_time:", ydata_sdk_t4[DEBUG_PRINT_INDEX:]
    print "SDK delay_time:", ydata_sdk_t04[DEBUG_PRINT_INDEX:]

    # print Delay data for debugging
    print "Delay chunk_id:", xdata_delay_cid[DEBUG_PRINT_INDEX:]
    print "Delay delay_time:", ydata_delay_t[DEBUG_PRINT_INDEX:]
#
    # ---------------    debugging region end, DO NOT modify-------------------

    return line_srs, line_push, line_sdk

def list_append(list1, list2):
    '''
    Only append new element to an existing list
    :param list1: existing list
    :param list2: new list
    :return: None
    '''
    for element in list2:
        if element not in list1:
            list1.append(element)

# ****************************************
#       *******************************
#
#        Main Function Goes From Here
#
#       *******************************
# ****************************************
if __name__ == "__main__":
    # get LF address via SDK dashboard
    # lf_ip_addresses = get_lf_ip_addresses(SDK_IP, sdk_is_lf=True)
    # for ip in lf_ip_addresses:
    #     lf_nodes.append({"ip" : ip, "port" : "32719"})

    # configure by rules
    # for i in range(40):
    #     lf_nodes.append({"ip": "192.168.1.115", "port": str(60002+i*10)})
    # exit(0)

    # generate line and color
    colors = dictcolors()
    markers = dictmarkers()

    # init leifeng nodes
    for node in lf_nodes:
        data_collector = LfDataCollector(node["ip"], node["port"])
        lf_data_collectors.append(data_collector)
        print data_collector.lf_ip

    # init canvas
    data_gen.t = 0

    # fig, ax = plt.subplots()
    fig = plt.figure(figsize=(8, 6), dpi=72, facecolor="white")
    ax = plt.subplot()
    fig.canvas.set_window_title("LIVE DELAY：" + ("HKS" if HKS_CHANNEL else "OTHER"))

    # define lines for srs, push, sdk
    line_srs, = ax.plot([], [], lw=2, color='y', label="source", linestyle='-')  # yellow line
    line_push, = ax.plot([], [], lw=1, color='g', label="push", linestyle='-')  # green line
    line_sdk, = ax.plot([], [], lw=1, color='b', label="sdk", linestyle='-', marker='*')    # blue line
    line_delay, = ax.plot([], [], lw=1, color='r', label="delay(sdk-source)", linestyle='-')  # red line

    ax.set_ylim(0, INIT_Y_LIMIT)
    ax.set_xlim(0, SAMPLE_NUM)
    ax.grid(color='y', linestyle='--', linewidth=1)
    plt.xlabel('x= chunk id')
    plt.ylabel('y= delay time (ms)')

    # allocate color and marker
    idx = 0
    for collector in lf_data_collectors:
        plt.scatter(collector.xdata_lf_cid, collector.ydata_lf_t03,
                    color=colors[idx], marker=markers[idx], alpha=0.3, edgecolors='yellow', label='leifeng')
        idx += 1

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)

    # every second call run, run's param is function data_gen
    ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=1000, repeat=False)
    plt.show()