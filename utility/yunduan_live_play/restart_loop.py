# coding=utf-8
# author: zengyuetian

# restart the player timely
# for server to collect start delay related data

import os
import time

if __name__ == "__main__":
    i = 0
    cmd = "python main.py restart qiboyanchi.ini"
    while True:
        i += 1
        print "Restart time ", i
        os.system(cmd)
        print "Done time ", i
        time.sleep(60*5)



