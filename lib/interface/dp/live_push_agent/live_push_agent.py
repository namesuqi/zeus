# coding=utf-8
# author: zengyuetian

from lib.constant.request import *
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *
from lib.interface.live_push_agent.const import *
import threading
import time


@print_trace
def get_live_push_status(protocol, host, port, file_url=None, time_out=None):

    url = "/api/livepush/status"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = dict()
    if time_out is not None:
        body_data["TimeOut"] = time_out
    if file_url is not None:
        body_data["FileURL"] = file_url

    response = send_request(
        '[LivePushAgent]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data

    )
    return response


@print_trace
def get_live_push_status(protocol, host, port, file_url=None, time_out=None):

    global failed_code, failed_puff, failed_supp
    url = "/api/livepush/status"

    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    body_data = dict()
    if time_out is not None and time_out is not "":
        try:
            body_data["TimeOut"] = int(time_out)
        except:
            try:
                body_data["TimeOut"] = float(time_out)
            except:
                body_data["TimeOut"] = time_out
    if file_url is not None:
        body_data["FileURL"] = file_url

    response = send_request(
        '[LivePushAgent]',
        protocol,
        POST,
        host,
        port,
        url,
        headers,
        None,
        body_data

    )
    if response.status_code != 200 or response.json().get("PuffStatus") == 254 or response.json().get("SuppStatus") == 254:
        if mutex.acquire(1):
            if response.status_code != 200:
                failed_code += 1
            if response.json().get("PuffStatus", 254) == 254:
                failed_puff += 1
            if response.json().get("SuppStatus", 254) == 254:
                failed_supp += 1
            mutex.release()
    return response

if __name__ == "__main__":
    start = time.time()
    mutex = threading.Lock()
    failed_code = 0
    failed_puff = 0
    failed_supp = 0

    for i in range(0, 2000):
        t = threading.Thread(target=get_live_push_status, args=("HTTP", "192.168.1.216", 9003, URL_CORRECT, 15))
        t.start()
        time.sleep(0.01)
        # t = threading.Thread(target=get_cid_data, args=(ip, port))
        # t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    print "code error {0}, puff error {1}, supp error {2}".format(failed_code, failed_puff, failed_supp)
    print (time.time()-start)
