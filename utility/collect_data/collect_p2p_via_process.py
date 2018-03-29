# coding=utf-8
"""
TODO: collect p2p data according to rules

__author__ = 'zengyuetian'

"""

import requests
import json
import time


def send_request(ip, port, url):
    url = "http://{0}:{1}{2}".format(ip, port, url)

    headers = dict()
    headers["accept"] = 'application/json'
    print url

    resp = requests.get(url, headers=headers, timeout=3)
    return resp


def get_p2p_percent(ip, port):
    try:
        res = send_request(ip, port, "/ajax/report")
        return json.loads(res.content).get("p2p_percent", None)
    except:
        return 0


if __name__ == "__main__":
    time1 = time.time()

    # IDC_IP_LIST = ['60.169.74.3', '222.222.12.12', '101.254.185.18']
    IDC_IP_LIST = ['111.161.66.134']
    IDC_SDK_NUM_LIST = [10]
    # IDC_IP_LIST = ['221.131.105.19', '116.31.120.11', '113.107.207.241', '171.107.82.45', '218.6.154.172'
    #                                                                                   '61.183.52.32', '111.161.66.134',
    #            '202.111.173.115', '60.217.25.209', '221.204.173.207']
    #

    port_start = 60000
    port_step = 10


    result_list = []


    for index, ip in enumerate(IDC_IP_LIST):
        num = IDC_SDK_NUM_LIST[index]
        for i in range(num):
            port = port_start + i*port_step + 0
            p2p = get_p2p_percent(ip, port)
            result_list.append(p2p)



    print
    print "***********************************************************"
    zero_list = [x for x in result_list if x == 0]
    non_zero_list = [x for x in result_list if x != 0]
    time2 = time.time()
    print "Cost {0} seconds to collect result".format(time2 - time1)
    print "Total SDKs number is {0}".format(len(result_list))
    print "Result List", result_list
    print "Total average p2p percentage is: {0}%".format(sum(result_list) / len(result_list))
    print "Alive average p2p percentage is: {0}%".format(sum(non_zero_list) / len(non_zero_list))
    print "Max p2p percentage is {0}%".format(max(non_zero_list))
    print "Min p2p percentage is {0}%".format(min(non_zero_list))
    print "{0} SDKs with p2p percentage 0%".format(len(zero_list))
    print "***********************************************************"
