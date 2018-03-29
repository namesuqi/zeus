# coding=utf-8

from lib.special.monitor_jenkins.robot_parser import *
from flask import Flask
import json
import threading
import time
import sys

app = Flask(__name__)

failed_build_dict = {}
cur_seq = 0


def init_data():
    """
    thread to get jenkins data for the display
    :return:
    """
    i = 0
    for i in range(10000):
        jenkins_handle = init_jenkins()
        global failed_build_dict
        failed_build_dict = get_failed_dateset(jenkins_handle)
        # body_data = {
        #     "p2pclient_ut": [
        #         {"build293": "1"},
        #         {"build292": "0"},
        #         {"build291": "2"},
        #         {"build290": "1"},
        #         {"build289": "2"},
        #         {"build288": "2"},
        #         {"build287": "1"},
        #         {"build286": "2"},
        #         {"build285": "2"}
        #     ]
        # }
        # if i % 2 == 0:
        #     failed_build_dict = body_data
        time.sleep(5)
        # if i >= 5:
        #     time.sleep(3)


@app.route("/jenkins_builds")
def hello():
    """
    json style:
    body_data = {
        "p2pclient_ut": [
            {"build293": "1"},
            {"build292": "0"},
            {"build291": "2"},
            {"build290": "1"},
            {"build289": "2"},
            {"build288": "2"},
            {"build287": "1"},
            {"build286": "2"},
            {"build285": "2"}
        ],
        "System_start": [
            {"build293": "1"},
            {"build292": "0"},
            {"build291": "2"},
            {"build290": "1"},
            {"build289": "2"}
        ],
        "System_check": [
            {"build293": "1"},
            {"build292": "0"}
        ]
    }
    :return:
    """
    global failed_build_dict
    # print "sequence:{0},list_len:{1}".format(cur_seq, len(failed_build_list))
    json_data = json.dumps(failed_build_dict)
    return json_data

if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=init_data)
    threads.append(t1)

    for t in threads:
        t.setDaemon(True)
        t.start()

    # time.sleep(5)
    app.run(port=5000, host='0.0.0.0', threaded=True)
