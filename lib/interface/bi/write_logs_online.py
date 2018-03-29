# coding=utf-8

"""

BI-ETL 节点在线事务相关的脚本

__author__ = 'liwenxuan'
20170525

"""

import uuid
import paramiko
import hashlib
from random import choice
from lib.interface.boss.time_handler import get_date_to_int, get_millisecond_now, get_time_now

FLUME_PATH = "/home/admin/logs/funnel/report.log_test_bi"


# 由时间戳得到
def create_peer_id_by_time():
    return str(uuid.uuid1()).replace("-", "")


# 由伪随机数得到，有一定的重复概率。
def create_peer_id_by_random():
    return str(uuid.uuid4()).replace("-", "")


def bi_peer_info(peer_id, timestamp, ssid=None, sdk_version="3.11.7", nat_type=1, net_change=False,
                 public_ip="192.168.1.197", country="IANA", province_id=0, city_id=0, isp_id=0,
                 topic="bi_test_peer_info"):

    log = 'topic={0}\x1fpeer_id={1}\x1ftimestamp={2}\x1fsdk_version={3}\x1fnat_type={4}\x1fpublic_ip={5}\x1f\
public_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fcountry={6}\x1fprovince_id={7}\x1fcity_id={8}\x1f\
isp_id={9}'.format(topic, peer_id, timestamp, sdk_version, nat_type, public_ip, country, province_id, city_id, isp_id)

    if ssid is not None:
        log += "\x1fssid={0}".format(ssid)
    if net_change is not None:
        log += "\x1fnet_change={0}".format(net_change)

    print "peer_info log:", log

    return log


def bi_heartbeat(peer_id, timestamp, ssid=None, sdk_version="3.11.7", nat_type=1,
                 public_ip="192.168.1.197", country="IANA", province_id=0, city_id=0, isp_id=0,
                 topic="bi_test_heartbeat"):

    log = 'topic={0}\x1fpeer_id={1}\x1ftimestamp={2}\x1fsdk_version={3}\x1fnat_type={4}\x1fpublic_ip={5}\x1f\
public_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fcountry={6}\x1fprovince_id={7}\x1fcity_id={8}\x1f\
isp_id={9}'.format(topic, peer_id, timestamp, sdk_version, nat_type, public_ip, country, province_id, city_id, isp_id)

    if ssid is not None:
        log += "\x1fssid={0}".format(ssid)

    print "heartbeat log:", log

    return log


def write_logs(*logs):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.229", username='admin', password="admin")

    for log in logs:
        assert log.find("topic") != -1
        ssh.exec_command('echo {0} >> {1}'.format(log, FLUME_PATH))

    ssh.close()

    return


def online_param_random():
    sdk_version = choice(["3.9.0", "3.9.7", "3.9.15", "3.9.22", "3.9.24", "3.9.27", "3.11.7", "3.11.10", "3.11.13"])
    nat_type = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    net_change = choice([True, False])
    public_ip_segment = choice(range(0, 256))
    public_ip = "192.168.{0}.{1}".format(public_ip_segment, choice(range(0, 256)))
    param = {"sdk_version": sdk_version, "nat_type": nat_type, "net_change": net_change, "public_ip": public_ip}
    return param


def heartbeats_per_peer_info(peer_info_start, peer_info_end, heartbeat_start, heartbeat_end, ts_millisecond, prefix,
                             hb_interval=10*60*1000, pi_param_random=False, hb_param_random=False):
    # 不同peer_id的在线情况
    assert isinstance(pi_param_random, bool) and isinstance(hb_param_random, bool)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.229", username='admin', password="admin")

    pi_timestamp = int(ts_millisecond)
    test_date = get_date_to_int()
    for i in range(int(peer_info_start), int(peer_info_end)):
        peer_id = str(prefix) + "FFFFFF" + test_date + "FFFFFF" + str(i).zfill(4)
        ssid = hashlib.md5(str(peer_id) + str(pi_timestamp)).hexdigest()
        if pi_param_random is True:
            d = online_param_random()
            peer_info_log = bi_peer_info(peer_id, pi_timestamp, ssid,
                                         d["sdk_version"], d["nat_type"], d["net_change"], d["public_ip"])
        else:
            peer_info_log = bi_peer_info(peer_id, pi_timestamp, ssid)
        ssh.exec_command('echo {0} >> {1}'.format(peer_info_log, FLUME_PATH))

        for j in range(int(heartbeat_start), int(heartbeat_end)):
            hb_timestamp = pi_timestamp + (j + 1) * hb_interval + choice(range(-1000, 1001))
            if pi_param_random is True and hb_param_random is False:
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid, d["sdk_version"], d["nat_type"], d["public_ip"])
            elif pi_param_random is False and hb_param_random is False:
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid)
            else:
                d = online_param_random()
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid, d["sdk_version"], d["nat_type"], d["public_ip"])
            ssh.exec_command('echo {0} >> {1}'.format(hb_log, FLUME_PATH))

    ssh.close()
    return


def sessions_per_peer_id(id, prefix, ts_millisecond, session_count, session_interval, pi_param_random=False,
                         hb_count=0, hb_interval=10*60*1000, hb_count_random=False, hb_param_random=False):
    # 同一个peer_id多次登录的情况
    assert isinstance(pi_param_random, bool) and isinstance(hb_param_random, bool)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.229", username='admin', password="admin")

    timestamp = int(ts_millisecond)
    test_date = get_date_to_int()
    peer_id = str(prefix) + "FFFFFF" + test_date + "FFFFFF" + str(id).zfill(4)
    for i in range(int(session_count)):
        pi_timestamp = timestamp + choice(range(-500, 501)) + i * int(session_interval)
        ssid = hashlib.md5(str(peer_id) + str(pi_timestamp)).hexdigest()
        if pi_param_random is True:
            d = online_param_random()
            peer_info_log = bi_peer_info(peer_id, pi_timestamp, ssid,
                                         d["sdk_version"], d["nat_type"], d["net_change"], d["public_ip"])
        else:
            peer_info_log = bi_peer_info(peer_id, pi_timestamp, ssid)
        ssh.exec_command('echo {0} >> {1}'.format(peer_info_log, FLUME_PATH))

        if hb_count_random is True:
            hb_count = choice(range(int(hb_count) + 1))
        else:
            hb_count = int(hb_count)
        for j in range(hb_count):
            hb_timestamp = pi_timestamp + (j + 1) * hb_interval + choice(range(-1000, 1001))
            if pi_param_random is True and hb_param_random is False:
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid, d["sdk_version"], d["nat_type"], d["public_ip"])
            elif pi_param_random is False and hb_param_random is False:
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid)
            else:
                d = online_param_random()
                hb_log = bi_heartbeat(peer_id, hb_timestamp, ssid, d["sdk_version"], d["nat_type"], d["public_ip"])
            ssh.exec_command('echo {0} >> {1}'.format(hb_log, FLUME_PATH))
        print hb_count, "heartbeat per peer_info"

    ssh.close()
    return


if __name__ == "__main__":
    pass
    print "Now:", get_time_now(), get_millisecond_now()

    # ts = timestamp_now - 86400000 * 7
    # heartbeats_per_peer_info(0, 15, 0, 6, 1493632800000, "00010013", pi_param_random=True, hb_interval=58*60*1000)

    # sessions_per_peer_id(02, "00010013", 1495380600000, 15, 300, True, 6, 5*60*1000, True)

    # peer_id = "075BCDC4BBBBBBBBBBBBBBBB05110076"
    # ssid = hashlib.md5(str(peer_id) + str(1494288600000)).hexdigest()
    # print "ssid:", ssid
    # ssid = "d5f16544ecce0793d23a16ff6de3b470"
    # log_1 = bi_peer_info(peer_id, 1494288600000, ssid=ssid)
    # write_logs(log_1)
    # log_2 = bi_heartbeat(peer_id, 1494288600000, ssid=ssid, public_ip="192.168.0.0")
    # write_logs(log_2)

