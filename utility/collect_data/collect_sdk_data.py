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

REQUEST_TIMEOUT = 5
PORT_START = 60000
PORT_STEP = 10
SDK_NUM = 10
STREAM_TARGET = 32

# IP_LIST = ['221.131.105.19', '116.31.120.11', '113.107.207.241', '171.107.82.45', '218.6.154.172', '111.161.66.134', '202.111.173.115', '60.217.25.209', '221.204.173.207',
#            '120.52.28.214',
#            '124.232.148.103', '36.250.226.115', '122.188.107.253', '112.245.16.149', '58.222.48.19']

# IP_LIST = ['221.131.105.19', '116.31.120.11', '113.107.207.241', '171.107.82.45', '218.6.154.172',
#            '112.245.16.149', '202.111.173.115', '60.217.25.209', '221.204.173.207', '58.222.48.19',
#            '120.52.28.214', '124.232.148.103', '36.250.226.115', '122.188.107.253']

IP_LIST = ['222.222.12.12', '101.254.185.18', '124.68.11.169', '115.238.245.25',
           '103.246.152.47', '60.169.74.3', '221.203.235.2', '60.12.69.100']


def send_request(host_ip, host_port, url):
    url = "http://{0}:{1}{2}".format(host_ip, host_port, url)

    headers = dict()
    headers["accept"] = 'application/json'
    # if "60000" in url:
    #     print url

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

if __name__ == "__main__":
    mutex = threading.Lock()
    dash_board_port_list = []
    for i in range(SDK_NUM):
        dash_board_port_list.append(PORT_START + i * PORT_STEP)

    while True:

        try:
            time1 = time.time()
            # print dash_board_port_list

            p2p_list = []
            bad_p2p_list = []
            seed_num_list = []
            stream_num_list = []
            bad_stream_list = []
            download_rate_list =[]

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

            print
            print "********** {0} cost {1} seconds to get result **********".format(time_str, time2-time1)
            print "IP number is: ", len(IP_LIST), IP_LIST

            print "SDK number is: {0}".format(len(p2p_list))
            print "------------------------------------------"
            print "P2P List", p2p_list
            print "All sdk average p2p is: {0}%".format(sum(p2p_list) / len(p2p_list))
            print "Alive sdk average p2p is: {0}%".format(sum(non_zero_list) / len(non_zero_list))
            print "Max p2p is {0}%, Min p2p is {1}%".format(max(non_zero_list), min(non_zero_list))
            print "{0} SDKs with p2p >= 80%".format(len([i for i in non_zero_list if i >= 80]))
            print "{1}{0} SDKs with p2p 0%{1}".format(len(zero_list), "         @@@@@@@@@@@@         " if len(zero_list) > 0 else "")
            print "P2P 0 sdk info: ", bad_p2p_list
            print "------------------------------------------"
            # print "Seed List", seed_num_list
            print "{0} SDKs with seed < 32".format(len([i for i in seed_num_list if i < 32]))
            print "------------------------------------------"
            # print "Stream List", stream_num_list
            print "{0} SDKs with stream >= 32".format(len([i for i in stream_num_list if i >= 32]))
            print "{0} SDKs with stream < 32".format(len([i for i in stream_num_list if i < 32]))
            # print "Stream < 32 sdk info: ",  bad_stream_list
            print "------------------------------------------"
            # print "Download List", download_rate_list
            print "All sdk average download rate {0}".format(sum(download_rate_list)/len(download_rate_list))
            print "Alive sdk average download rate {0}".format(sum(download_rate_list)/len(non_zero_list))
            print "*******************************************************************************"
        except:
            pass

        time.sleep(15)
