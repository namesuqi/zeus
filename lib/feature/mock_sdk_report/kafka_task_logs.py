# coding=UTF-8
"""
将task写入到funnel的report.log中，从而被采集写进到kafka的topic中
"""
import json
import os
import random
import time
import sys
from lib.feature.mock_sdk_report.kafka_data import *
import ConfigParser

log_file_path = "log_path.log"  # /home/admin/logs/funnel/report.log
FILE_ID = KAFKA_FILE_ID
PEER_ID = KAFKA_PEER_ID


def readconfig():
    config = ConfigParser.ConfigParser()
    config.readfp(open("config.ini"))
    section_list = config.sections()
    print section_list
    print config.get(section_list[0], "topic")
    config.set(section_list[0], "topic", "5")
    print config.get(section_list[0], "topic")


def sdk_directional_task_live(file_index, peer_index, operation="delete"):
    #  live_task
    file_start = file_index[0]
    file_end = file_index[1]
    peer_start = peer_index[0]
    peer_end = peer_index[1]
    f = open(log_file_path, 'a')
    f.write("\n")
    for m in range(int(file_end)-int(file_start)):
        file_id = FILE_ID[int(file_start)+m]
        for i in range(int(peer_end)-int(peer_start)):
            peer_id = PEER_ID[int(peer_start)+i]
            log = "timestamp={0}\37topic=sdk_directional_task_live\37file_id={1}\37peer_id={2}\37operation={3}".format(
                str(int(time.time()*1000)), str(file_id), str(peer_id), operation)
            f.write(log)
            f.write("\n")
            print log
    f.close()


def case_invalid():
    FILE_ID_LIST = ["2222222222ABCDEABCDEABCDE1000000", "D460BE98C5B062E0C458438117C6416E", "INVALID", ""]
    PEER_ID_LIST = ["6666666666ABCDEABCDEABCDE1000000", "INVALID", ""]
    OPE_LIST = ["download", "delete", "INVALID", ""]
    f = open(log_file_path, 'a')
    f.write("\n")
    for file_id in FILE_ID_LIST:
        for peer_id in PEER_ID_LIST:
            for ope in OPE_LIST:
                log = "timestamp={0}\37topic=sdk_directional_task_live\37file_id={1}\37peer_id={2}\37operation={3}".\
                    format(str(int(time.time()*1000)), str(file_id), str(peer_id), ope)
                f.write(log)
                f.write("\n")
                print log
    f.close()


def peer_info(peer_ids, sdk_version, nat_type, pub_ip, pub_port, pri_ip, pri_port, macs):
    # peer_id, sdk_version, nat_type, pub_ip, pub_port, pri_ip, pri_port, macs = args
    # python kafka_task_logs.py peer_info
    f = open(log_file_path, 'a')
    for peer_id in peer_ids:
        f.write("\n")
        log = "timestamp={0}\37topic=peer_info\37peer_id={1}\37sdk_version={2}\37nat_type={3}\37public_ip={4}" \
              "\37public_port={5}\37private_ip={6}\37private_port={7}\37macs={8}\37deviceInfo={9}"\
            .format(str(int(time.time()*1000)), str(peer_id), str(sdk_version), str(nat_type), str(pub_ip), str(pub_port),
                    str(pri_ip), str(pri_port), str(macs), "{}")
        f.write(log)
        print log
    f.write("\n")
    f.close()


def file_seed_change(peer_ids, file_ids, ope="delete", size_map="714", slice_percent=66.3536, cppc=1):
    # python kafka_task_logs.py lsm
    # operation = ["update", "delete"]
    sizes = size_map[0]
    size_lens = size_map[1:]
    size_str = sizes.ljust(int(size_lens), "F")
    s_map = size_str.rjust(16, "0")
    f = open(log_file_path, 'a')
    for file_id in file_ids:
        for peer_id in peer_ids:
            f.write("\n")
            log = "timestamp={0}\37topic=file_seed_change\37peer_id={1}\37file_id={2}\37operation={3}\37slice_map=" \
                  "{4}\37slice_percent={5}\37cppc={6}".format(str(int(time.time()*1000)), str(peer_id), str(file_id),
                                                                  str(ope), str(s_map), str(slice_percent), str(cppc))
            f.write(log)
            print log
    f.write("\n")
    f.close()

if __name__ == "__main__":
    # python .py [peer_id_nums] [file_id_nums] [loop_times]
    print sys.argv
    # if str(sys.argv[1]) == "peer_info":
    #     peer_info()
    # elif str(sys.argv[1]) == "lsm":
    #     file_seed_change()
    # elif str(sys.argv[1]) == "live_task":
    #     sdk_directional_task_live()
    # else:
    #     print "do nothing"
    PEER_END_NUM = sys.argv[1]
    FILE_END_NUM = sys.argv[2]
    PEER_INFO = ["3.5.0", "0", "123.123.123.123", "12345", "192.168.1.22", "12345"]
    PEER_MACS = [{"name": "win1", "addr": "18:CF:5E:01:D6:C8"}]

    SDK_VERSION, NAT_TYPE, PUB_IP, PUB_PORT, PRI_IP, PRI_PORT = PEER_INFO
    MACS = PEER_MACS
    # peer_info(peer_id, SDK_VERSION, NAT_TYPE, PUB_IP, PUB_PORT, PRI_IP, PRI_PORT, MACS)

    loop_times = int(sys.argv[3])
    for l in range(loop_times):
        file_seed_change(PEER_ID[0:int(PEER_END_NUM)], FILE_ID[0:int(FILE_END_NUM)], "")
        file_seed_change(PEER_ID[0:int(PEER_END_NUM)], FILE_ID[0:int(FILE_END_NUM)], "update", "F16", 100)
        file_seed_change(PEER_ID[0:int(PEER_END_NUM)], FILE_ID[0:int(FILE_END_NUM)], "delete")
        peer_info(PEER_ID[0:int(PEER_END_NUM)], SDK_VERSION, NAT_TYPE, PUB_IP, PUB_PORT, PRI_IP, PRI_PORT, MACS)
        time.sleep(0.1)



