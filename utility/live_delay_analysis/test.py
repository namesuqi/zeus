# coding=utf-8
"""
create a multi-line txt file

__author__ = 'zengyuetian'

"""

import time

if __name__ == "__main__":
    file1 = file("654321.cts", mode='w')
    for i in range(100000):

        time.sleep(1)
        file1.write("{0},{1}\n".format(i+900000, time.time()+i))
        file1.flush()
    file1.close()


