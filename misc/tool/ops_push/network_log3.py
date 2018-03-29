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
    arg = sys.argv
    count = int(arg[1])
    for i in range(0, count):
        timestamp_now = int(time.time())
        net_name = ["net0", "net1", "net2"]
        name_now = random.choice(net_name)
        receive_num = random.randint(60000000, 100000000)
        transmit_num = random.randint(50000000, 60000000)
        d = str(random.randint(1, 300))
        ip_now1 = str(1) + "." + str(24) + "." + str(24) + "." + d
        ip_now2 = str(1) + "." + str(4) + "." + str(4) + "." + d
        ip_now3 = str(1) + "." + str(116) + "." + str(0) + "." + d
        ip_now4 = str(116) + "." + str(62) + "." + str(4) + "." + d
        ip_now5 = str(1) + "." + str(32) + "." + str(192) + "." + d
        ip_now6 = str(1) + "." + str(50) + "." + str(0) + "." + d
        ip_now7 = str(1) + "." + str(51) + "." + str(128) + "." + d
        ip_now8 = str(202) + "." + str(97) + "." + str(38) + "." + d
        ip_now9 = str(123) + "." + str(80) + "." + str(168) + "." + d
        ip_now10 = str(202) + "." + str(97) + "." + str(40) + "." + d
        ip_now11 = str(125) + "." + str(39) + "." + str(0) + "." + d
        ip_now12 = str(202) + "." + str(99) + "." + str(243) + "." + d
        ip_now13 = str(211) + "." + str(141) + "." + str(95) + "." + d
        ip_now14 = str(219) + "." + str(158) + "." + str(7) + "." + d
        ip_now15 = str(1) + "." + str(32) + "." + str(192) + "." + d
        ip_now16 = str(1) + "." + str(51) + "." + str(112) + "." + d
        ip_now17 = str(1) + "." + str(56) + "." + str(96) + "." + d
        ip_now18 = str(1) + "." + str(68) + "." + str(208) + "." + d
        ip_now19 = str(1) + "." + str(82) + "." + str(0) + "." + d
        ip_now20 = str(116) + "." + str(66) + "." + str(0) + "." + d
        ip_now21 = str(210) + "." + str(5) + "." + str(31) + "." + d
        ip_now22 = str(1) + "." + str(0) + "." + str(1) + "." + d
        ip_now23 = str(1) + "." + str(13) + "." + str(0) + "." + d
        ip_now24 = str(1) + "." + str(24) + "." + str(127) + "." + d
        ip_now25 = str(42) + "." + str(96) + "." + str(248) + "." + d
        host_id_now = timestamp_now
        # print ip_now
        # print receive_num
        # print sys.argv
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now1, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now2, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now3, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now4, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now5, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now6, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now7, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now8, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now9, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now10, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now11, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now12, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now13, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now14, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now15, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now16, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now17, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now18, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now19, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now20, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now21, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now22, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now23, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now24, host_id_now)
        lp_network(name_now, timestamp_now, receive_num, transmit_num, ip_now25, host_id_now)
