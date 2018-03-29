# coding=utf-8

"""

boss系统-计费模块 日活&在线相关的脚本

  1. add_peer_info/heartbeat/activity : 用于功能测试, 通过kafka-flume向kafka传入logs
  2. add_online : 直接将在线节点信息写入redis集群中
  * ts为timestamp的简称

__author__ = 'liwenxuan'
20170518

"""

import hashlib
import paramiko
from rediscluster import StrictRedisCluster
from lib.interface.boss.time_handler import get_date_to_int, get_millisecond_now, get_time_now, get_time_to_int

FLUME_PATH = "/home/admin/logs/funnel/report.log_test_boss"


def boss_add_heartbeat(start, end, ts_second, prefix="00000001", topic="boss_test_heartbeat",
                       flume_host="192.168.1.229", user="admin", password="admin", path=FLUME_PATH):
    # 向kafka传入heartbeat的logs, 设定peer_id后八位的范围[start, end)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flume_host, username=user, password=password)

    test_date = get_date_to_int()
    test_time = get_time_to_int()
    for i in range(start, end):
        peer_id = str(prefix).zfill(8) + "FFFF" + test_date + "FFFF" + str(i).zfill(8)
        # ssid = hashlib.md5(str(peer_id) + str(ts_second * 1000)).hexdigest()
        log = "topic={0}\x1fpeer_id={1}\x1ftimestamp={2}000\x1fsdk_version=3.9.0\x1fnat_type=1\x1fpublic_ip=10.6.3.6\
\x1fpublic_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fssid={3}"\
            .format(topic, peer_id, ts_second, test_time)
        ssh.exec_command('echo {0} >> {1}'.format(log, path))

    ssh.close()
    print "write", end-start, "heartbeat logs"
    return


def boss_add_peer_info(start, end, ts_second, prefix="00000001", net_change=False, topic="boss_test_peer_info",
                       flume_host="192.168.1.229", user="admin", password="admin", path=FLUME_PATH):
    # 向kafka传入peer_info的logs, 设定peer_id后八位的范围[start, end)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flume_host, username=user, password=password)

    test_date = get_date_to_int()
    test_time = get_time_to_int()
    for i in range(start, end):
        peer_id = str(prefix).zfill(8) + "FFFF" + test_date + "FFFF" + str(i).zfill(8)
        # ssid = hashlib.md5(str(peer_id) + str(ts_second * 1000)).hexdigest()
        log = "topic={0}\x1fpeer_id={1}\x1ftimestamp={2}000\x1fsdk_version=3.9.0\x1fnat_type=1\x1fpublic_ip=10.6.3.5\
\x1fpublic_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fssid={3}\x1fnet_change={4}"\
            .format(topic, peer_id, ts_second, test_time, net_change)
        ssh.exec_command('echo {0} >> {1}'.format(log, path))

    ssh.close()
    print "write", end-start, "peer_info logs"
    return


def boss_add_activity(peer_info_start, peer_info_end, heartbeat_start, heartbeat_end, ts_millisecond,
                      prefix="00000001", peer_info_topic="boss_test_peer_info", heartbeat_topic="boss_test_heartbeat",
                      flume_host="192.168.1.229", user="admin", password="admin", path=FLUME_PATH):
    # 向kafka传入peer_info和heartbeat的logs, 设定peer_id后八位的范围为[start, end), 及每条peer_info对应几条heartbeat

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flume_host, username=user, password=password)

    pi_timestamp = int(ts_millisecond)
    test_date = get_date_to_int()
    test_time = get_time_to_int()
    for i in range(int(peer_info_start), int(peer_info_end)):
        peer_id = str(prefix).zfill(8) + "FFFF" + test_date + "FFFF" + str(i).zfill(8)
        # ssid = hashlib.md5(str(peer_id) + str(pi_timestamp)).hexdigest()
        peer_info_log = "topic={0}\x1fpeer_id={1}\x1ftimestamp={2}\x1fsdk_version=3.9.0\x1fnat_type=1\x1fpublic_ip=\
10.6.3.5\x1fpublic_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fssid={3}\x1fnet_change=False"\
            .format(peer_info_topic, peer_id, pi_timestamp, test_time)
        ssh.exec_command('echo {0} >> {1}'.format(peer_info_log, path))
        for j in range(int(heartbeat_start), int(heartbeat_end)):
            hb_timestamp = pi_timestamp + (j + 1) * 10 * 60 * 1000
            heartbeat_log = "topic={0}\x1fpeer_id={1}\x1ftimestamp={2}\x1fsdk_version=3.9.0\x1fnat_type=1\x1fpublic_ip\
=10.6.3.6\x1fpublic_port=8080\x1fprivate_ip=192.168.1.1\x1fprivate_port=10000\x1fssid={3}"\
                .format(heartbeat_topic, peer_id, hb_timestamp, test_time)
            ssh.exec_command('echo {0} >> {1}'.format(heartbeat_log, path))

    ssh.close()
    return


def boss_add_online(start, end, prefix="00000001", ttl=1800, redis_host="192.168.1.205", port=6379):
    # 向redis写入节点登录信息

    startup_nodes = [{"host": redis_host, "port": port}]
    rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    for i in range(start, end):
        today = get_time_to_int()
        time = get_millisecond()
        peer_id = "{0}FFFF{1}FFFF{2}".format(str(prefix).zfill(8), today, str(i).zfill(8))
        ssid = hashlib.md5(str(peer_id) + str(time)).hexdigest()
        v = "{\"peer_id\":\"%s\",\"ssid\":\"%s\",\"version\":\"3.9.0\",\"natType\":1,\"publicIP\":\"0.0.0.0\",\
\"publicPort\":80,\"privateIP\":\"0.0.0.0\",\"privatePort\":8000,\"country\":\"CN\",\"province_id\":\"310000\",\
\"isp_id\":\"100017\",\"city_id\":\"310100\",\"stunIP\":\"0.0.0.0\"}" % (peer_id, ssid)
        k = "PNIC_" + str(peer_id)
        rc.setex(k, int(ttl), v)


if __name__ == "__main__":
    print "Now:", get_time_now(), get_millisecond_now()

    # boss_add_heartbeat(100000, 200001, timestamp_now)

    # 在线节点
    # boss_add_online(0, 20)
    # print "send 20 online to redis"

    # 日活
    # boss_add_activity(0, 20, 0, 10, timestamp_now*1000)
    # print "send 20 peer_info and 20*10 heartbeat to kafka"

    # a1 = boss_add_heartbeat(0, 300); time.sleep(1); print int(time.time())
    # a1 = boss_add_heartbeat(0, 3000); time.sleep(1); print int(time.time())
    # a2 = boss_add_heartbeat(3000, 6000); time.sleep(1); print int(time.time())
    # a3 = boss_add_heartbeat(6000, 9000); time.sleep(1); print int(time.time())
    # a4 = boss_add_heartbeat(9000, 12000); time.sleep(1); print int(time.time())
    # a5 = boss_add_heartbeat(12000, 15000); time.sleep(1); print int(time.time())



