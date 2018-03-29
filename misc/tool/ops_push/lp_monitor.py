# coding=utf-8
"""
__author__ = 'th'

"""

import random
import time
import os
import sys


LOG_PATH = "/home/admin/logs/lp/lp_monitor.log"


def lp_monitor(timestamp, cpu_count, cpu_used_count, mem_used, host_id, channel_supp_transmit,
               channel_puff_transmit, channel_supp_nodes_cnt, channel_puff_nodes_cnt):
    log = "topic=livepush_monitor\x1ftimestamp={0}\x1fcpu_load_1m=0.5\x1fcpu_count={1}\x1fcpu_used_count={2}" \
          "\x1fcpu_used_percentage=85%\x1fmem_total=500704\x1fmem_used={3}\x1fmem_used_percentage=85%" \
          "\x1flivepush_version=1.1.0\x1fhost_id={4}\x1fchannel_supp_transmit={5}\x1fchannel_puff_transmit={6}" \
          "\x1fchannel_supp_nodes_cnt={7}\x1fchannel_puff_nodes_cnt={8}" \
          "\x1fsupp_nodes_ip_list=192.168.1\x1fdetail_info=test_info"\
            .format(timestamp, cpu_count, cpu_used_count, mem_used, host_id,channel_supp_transmit,
                    channel_puff_transmit, channel_supp_nodes_cnt, channel_puff_nodes_cnt)
    os.system('echo {0} >> {1}'.format(log, LOG_PATH))

    # ssh.close()
    print "write", "lp monitor logs"
    return


if __name__ == "__main__":
    timestamp_now = int(time.time())
    print "Now(s):", timestamp_now
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    cpu_count_now = random.randint(0, 8)
    cpu_used_count_now = round(random.uniform(0, 8), 2)
    # print cpu_used_count_now
    # print cpu_used_count_now
    # cpu_used_count_now = float(random.randint(0, 8))
    # print cpu_used_count_now
    # cpu_used_count_now = float(random.randint(0, 8))
    # print cpu_used_count_now
    # cpu_used_count_now = float(random.randint(0, 8))
    # print cpu_used_count_now
    mem_used_now = random.randint(60000000, 100000000)
    a = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    c = str(random.randint(0, 255))
    d = str(random.randint(0, 244))
    channel_supp_transmit_now = random.randint(60000000, 100000000)
    channel_puff_transmit_now = random.randint(60000000, 100000000)
    channel_supp_nodes_cnt_now = random.randint(0,50)
    host_id_now = a + "." + b + "." + c + "." + d
    arg = sys.argv
    count = int(arg[1])
    for i in range(0, count):
        lp_monitor(timestamp_now, cpu_count_now, cpu_used_count_now, mem_used_now, host_id_now,
                   channel_supp_transmit_now, channel_puff_transmit_now, channel_supp_nodes_cnt_now,
                   channel_supp_nodes_cnt_now)




