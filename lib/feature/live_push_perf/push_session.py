# coding=utf-8
"""
mock multi lf push_session_req or hib or fin, lf => live-push server

__author__ = 'zsw'

"""
import json
import os
import string
import socket
import binascii
import time
import hashlib

from creator import PEER_ID_FILE
from conf_data import *


class PushSession(object):
    def push_session_req(self, interval=SLEEP, peer_start_num=1, peer_stop_num=2, file_id=FILE_ID, file_url=FILE_URL,
                         port=10000, peer_id_file=PEER_ID_FILE):
        with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_file, "r") as f:
            peer_ids = json.load(f)

        print "push_session_req"
        print "port:", port, "file_id:", file_id, "file_url:", file_url
        local_port = port + peer_start_num
        for m in range(int(peer_start_num), int(peer_stop_num)):

            peer_id = peer_ids[m]
            if local_port >= 60000:
                local_port = m - 50000

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(("", int(local_port)))
            session_id = "22"
            for index in range(len(file_id)):
                req_data = self.handle_req_data(peer_id, file_id[index], file_url[index], session_id)
                s.sendto(binascii.a2b_hex(req_data), (PUSH_HOST, PUSH_PORT))
                session_id = str(int(session_id) + 1)

            if m % 500 == 0:
                print m, peer_id, local_port
                time.sleep(0.2)

            s.close()
            local_port += 1
            time.sleep(float(interval))

    def push_session_hib(self, interval=SLEEP, peer_start_num=0, peer_stop_num=2, loop_times=3, file_id=FILE_ID,
                         port=10000, wait_time=0, peer_id_file=PEER_ID_FILE):
        with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_file, "r") as f:
            peer_ids = json.load(f)

        print "loop is ", loop_times

        # time.sleep(wait_time)  # follow req
        for i in range(int(loop_times)):
            print "Start loop ", i
            time.sleep(wait_time)
            local_port = port + peer_start_num
            for m in range(int(peer_start_num), int(peer_stop_num)):

                if local_port >= 60000:
                    local_port = m - 50000
                peer_id = peer_ids[m]
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.bind(("", int(local_port)))
                session_id = "22"
                for i in file_id:
                    hib_data = self.handle_hib_data(peer_id, i, session_id)
                    s.sendto(binascii.a2b_hex(hib_data), (PUSH_HOST, PUSH_PORT))
                    session_id = str(int(session_id) + 1)
                s.close()
                local_port += 1
                time.sleep(float(interval))

    def push_session_fin(self, peer_start_num=0, peer_stop_num=2, file_id=FILE_ID, lo_port=10000,
                         peer_id_file=PEER_ID_FILE):
        with open(os.path.abspath(os.path.dirname(__file__)) + peer_id_file, "r") as f:
            peer_ids = json.load(f)

        local_port = lo_port
        for m in range(int(peer_start_num), int(peer_stop_num)):
            if local_port >= 60000:
                local_port = m - 50000
            peer_id = peer_ids[m]
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(("", int(local_port)))
            for i in file_id:
                fin_data = PushSession.handle_fin_data(peer_id, i)
                s.sendto(binascii.a2b_hex(fin_data), (PUSH_HOST, PUSH_PORT))
            s.close()
            local_port += 1
            time.sleep(SLEEP)

    def handle_req_data(self, peer_id=PEER_ID, file_id=FILE_ID, file_url=FILE_URL, session_id="16", req_type="01",
                        cppc="0001", priority="00"):

        peer_id_hex = peer_id.lower()
        # file_id_hex = file_id.lower()
        url_md5 = hashlib.md5(str(file_url)).hexdigest()
        # print url_md5
        # url_md5_hex = binascii.b2a_hex(url_md5)
        file_url_hex = binascii.b2a_hex(file_url)
        file_url_fill = string.ljust(file_url_hex, 256 * 2, "0")

        req_data = "c1{0}{1}{2}{3}{4}{5}{6}".format(req_type, session_id, peer_id_hex, url_md5, file_url_fill,
                                                    cppc, priority)
        return req_data

    def handle_hib_data(self, peer_id=PEER_ID, file_id=FILE_ID, session_id="16", req_type="04"):
        peer_id_hex = peer_id.lower()
        file_id_hex = file_id.lower()

        hib_data = "c1{0}{1}{2}{3}".format(req_type, session_id, peer_id_hex, file_id_hex)
        return hib_data

    def handle_fin_data(self, peer_id=PEER_ID, file_id=FILE_ID, session_id="16", req_type="05", fin_reason="06"):

        peer_id_hex = peer_id.lower()
        file_id_hex = file_id.lower()

        fin_data = "c1{0}{1}{2}{3}{4}".format(req_type, session_id, peer_id_hex, file_id_hex, fin_reason)
        return fin_data

    def for_local(self, send, session_id, local_port):
        peer_id = "41435058313233343536D1CB9EECDB82"
        send_data = ""
        if send == "1":
            send_data = PushSession().handle_req_data(peer_id, FILE_ID, FILE_URL, session_id)
        if send == "4":
            send_data = PushSession().handle_hib_data(peer_id, FILE_ID, session_id)
        if send == "5":
            send_data = PushSession().handle_fin_data(peer_id, FILE_ID, session_id)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", int(63517)))
        s.sendto(binascii.a2b_hex(send_data), (PUSH_HOST, PUSH_PORT))
        s.close()


#
# def CreateThreads(peer_start_num=0, peer_stop_num=2, file_id=FILE_ID_LIST, file_url=FILE_URL_LIST):
#     threads = []
#
#     threads.append(threading.Thread(target=PushSession().PushSessionReq, args=(0.01,0, 25000, file_id, file_url,)))
#     threads.append(threading.Thread(target=PushSession().PushSessionHib, args=(0.01,0, 12500, 5, file_id, 10000, 5)))
#     threads.append(threading.Thread(target=PushSession().PushSessionHib, args=(1, 12500, 5, file_id, 10001, 30,)))
#     for t in threads:
#         t.start()
#     print time.time()
#     print threads
#     for t in threads:
#         t.join()
#
#     print "threads done"


if __name__ == '__main__':
    # python PushSession.py run 200 20
    # print time.time()
    # tag = sys.argv[1]
    # print struct.calcsize("2s")
    # PushSession().PushSessionReq(0, 100)
    # for i in range(10):
    i = 10
    # file_id = FILE_ID_LIST[i]
    # file_url = FILE_URL_LIST[i]
    print time.time()
    # PushSession().PushSessionHib(0.005, 0, 4, 1, FILE_ID_LIST)
    # F1 = PushSession().CreateFileList()[1]
    # print F1[0]
    # peer_id = "58594C41435047304643313331666666"
    # send_data = PushSession().HandleHibData(peer_id, FILE_ID, '22')
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind(("", 65000))
    # s.sendto(binascii.a2b_hex(send_data), (PUSH_HOST, PUSH_PORT))
    # s.close()
    print time.time()
    time.sleep(float("0.01"))
    print time.time()
    print "done"
