# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

import socket
import time

one_k_data = "a"*200

def create_data(data_length):
    block = one_k_data*data_length
    return block


if __name__ == "__main__":
    HOST = '192.168.1.26'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data1 = create_data(512)
    data2 = create_data(256)
    data3 = create_data(128)
    data4 = create_data(64)
    data5 = create_data(32)
    data6 = create_data(32)

    data_list = [data1, data2, data3, data4, data5, data6]
    num = 0
    while 1:
        t1 = time.time()
        for i in range(6):
            s.send(data_list[i])
            time.sleep(0.05)
        t2 = time.time()
        delta_t = t2 - t1
        if 1-delta_t >= 0:
            time.sleep(1-delta_t)
        else:
            if 1-delta_t < -0.05:
                print "slow.......{0}".format(1-delta_t)
        num += 1
        print "Send {0}".format(num)
    s.close()