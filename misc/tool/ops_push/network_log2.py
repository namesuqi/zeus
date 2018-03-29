import random
import time
import os
import sys


LOG_PATH = "/home/admin/logs/lp_network.log"


def lp_network(name, timestamp, receive, transmit, ip, host_id):
    log = "topic=network_card_flow\x1fname={0}\x1ftimestamp={1}\x1freceive={2}\x1ftransmit={3}\x1fip={4}\
\x1fhost_id={5}\x1fdetail_info=test"\
            .format(name, timestamp, receive, transmit, ip, host_id)
    os.system('echo {0} >> {1}'.format(log, LOG_PATH))

    # ssh.close()
    print "write", "lp network logs"
    return


if __name__ == "__main__":

    # print "Now(s):", timestamp_now
    # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    timestamp_now = int(time.time())
    net_name = ["net0", "net1", "net2"]
    name_now = random.choice(net_name)
    receive_num = random.randint(60000000, 100000000)
    transmit_num = random.randint(50000000, 60000000)
    a = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    c = str(random.randint(0, 255))
    d = str(random.randint(0, 244))
    ip_now = a + "." + b + "." + c + "." + d
    host_id_now = a + "." + b + "." + c + "." + d
    th = True
    while th:
        # print ip_now
        # print receive_num
        # print sys.argv
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now, host_id_now)




