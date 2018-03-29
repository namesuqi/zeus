# coding=utf-8
"""
create threads for hib

__author__ = 'zsw'

"""


import threading
import time
from creator import Creator
from push_session import PushSession


def create_1_g(all_nums=15000, sleep_t=3):
    # file_ids = Creator.create_file_list(1)[0]
    # file_urls = Creator.create_file_list(1)[1]

    threads = list()
    # threads.append(threading.Thread(target=PushSession().push_session_req, args=(0.001, 0, int(all_nums), file_ids, file_urls,)))
    # threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.001, 0, int(all_nums), 1000, file_ids, 10000, int(sleep_t),)))
    threads.append(threading.Thread(target=PushSession().push_session_req, args=(0.001, 0, int(all_nums))))
    threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.001, 0, int(all_nums), 1000)))
    t1 = time.time()
    print "start send packages"
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "end", time.time() - t1


# def create_5_g():
#     file_ids = Creator.create_file_list(5)[0]
#     file_urls = Creator.create_file_list(5)[1]
#     threads = list()
#     threads.append(threading.Thread(target=PushSession().push_session_req, args=(0.002, 0, 10000, file_ids, file_urls,)))
#     threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.001, 0, 5000, 1000, file_ids, 10000, 15,)))
#     threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.001, 5000, 10000, 1000, file_ids, 15000, 30,)))
#
#     print time.time()
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print "end", time.time()
#
#
# def create_10_g():
#     file_ids = Creator.create_file_list(10)[0]
#     file_urls = Creator.create_file_list(10)[1]
#     threads = list()
#     threads.append(threading.Thread(target=PushSession().push_session_req, args=(0.003, 0, 5000, file_ids, file_urls,)))
#     threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.003, 0, 2500, 10, file_ids, 10000, 15,)))
#     threads.append(threading.Thread(target=PushSession().push_session_hib, args=(0.003, 2500, 5000, 10, file_ids, 12500, 30,)))
#     # threads.append(threading.Thread(target=PushSession().PushSessionHib, args=(0.003, 5000, 7500, 10, FILE_ID_LIST, 15000, 45,)))
#
#     print time.time()
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print "end", time.time()


def create_flow_with_thread():
    """
    Create multi-thread to improve performance
    :return:
    """

    # send REQ to get ready receive data
    threads = list()
    start_peer = 1
    peer_interval = 45000
    t1 = time.time()
    print "start send req"
    for i in range(1):
        threads.append(threading.Thread(target=PushSession().push_session_req,
                                        args=(0.0005, start_peer, start_peer + peer_interval)))
        start_peer += peer_interval
        print "threads ", i, "peer ", start_peer, start_peer + peer_interval
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "end send req", time.time() - t1

    # send HIB to maintain online status
    threads = list()
    start_peer = 1
    print "start send hib"
    for i in range(1):
        threads.append(threading.Thread(target=PushSession().push_session_hib,
                                        args=(0.0001, start_peer, start_peer + peer_interval, 1000)))
        start_peer += peer_interval
        print "threads ", i, "peer ", start_peer, start_peer + peer_interval
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "end send hib"

    # print Total time
    print "total end", time.time() - t1


###################################
# Main Function
###################################
if __name__ == '__main__':
    create_1_g(100)


