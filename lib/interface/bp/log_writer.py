#!/usr/bin/python
# -*-coding:UTF-8 -*-
"""
根据topic创建log

 __author__ = 'zsw'

"""
import os
import time
from random import choice
import paramiko


def live_report_log(peer_id, file_id, operation, cdn, p2p, chunk_id, version, country="ZZ", province_id="0",
                    city_id="0", isp_id="0", p2penable=True, timestamp=-9):
    """

    :param peer_id:
    :param file_id:
    :param operation:
    :param cdn:
    :param p2p:
    :param chunk_id:
    :param version:
    :param country:
    :param province_id:
    :param city_id:
    :param isp_id:
    :param p2penable:
    :param timestamp: log的timestamp值，为-9时按当前时间戳写入
    :return:
    """
    live_report = {
        "peer_id": str(peer_id),
        "file_id": str(file_id),
        "version": str(version),
        "operation": str(operation),
        "cdn": int(cdn),
        "p2p": int(p2p),
        "chunk_id": int(chunk_id),
        "country": str(country),
        "province_id": str(province_id),
        "city_id": str(city_id),
        "isp_id": str(isp_id),
        "p2penable": p2penable
    }
    if timestamp == -9:
        live_report["timestamp"] = int(time.time()*1000)
    else:
        live_report["timestamp"] = int(timestamp)
    return live_report


def lf_report_log(peer_id, file_id, operation, upload, download, version, cppc=1, country="ZZ", province_id="0",
                  city_id="0", isp_id="0", timestamp=-9):
    """

    :param peer_id:
    :param file_id:
    :param operation:
    :param upload:
    :param download:
    :param version:
    :param cppc:
    :param country:
    :param province_id:
    :param city_id:
    :param isp_id:
    :param timestamp: log的timestamp值，为-9时按当前时间戳写入
    :return:
    """
    lf_report = {
        "peer_id": str(peer_id),
        "version": str(version),
        "file_id": str(file_id),
        "operation": str(operation),
        "upload": int(upload),
        "download": int(download),
        "cppc": int(cppc),
        "country": str(country),
        "province_id": str(province_id),
        "city_id": str(city_id),
        "isp_id": str(isp_id)
    }
    if timestamp == -9:
        lf_report["timestamp"] = int(time.time()*1000)
    else:
        lf_report["timestamp"] = int(timestamp)
    return lf_report


def heartbeat_log(peer_id, sdk_version, nat_type, public_ip, public_port, private_ip, private_port, country="ZZ",
                  province_id="0", city_id="0", isp_id="0", timestamp=-9):
    """

    :param peer_id:
    :param sdk_version:
    :param nat_type:
    :param public_ip:
    :param public_port:
    :param private_ip:
    :param private_port:
    :param country:
    :param province_id:
    :param city_id:
    :param isp_id:
    :param timestamp: log的timestamp值，为-9时按当前时间戳写入
    :return:
    """
    heartbeat = {
        "peer_id": str(peer_id),
        "sdk_version": str(sdk_version),
        "nat_type": int(nat_type),
        "public_ip": str(public_ip),
        "public_port": int(public_port),
        "private_ip": str(private_ip),
        "private_port": int(private_port),
        "country": str(country),
        "province_id": str(province_id),
        "city_id": str(city_id),
        "isp_id": str(isp_id)
    }
    if timestamp == -9:
        heartbeat["timestamp"] = int(time.time()*1000)
    else:
        heartbeat["timestamp"] = int(timestamp)
    return heartbeat


def peer_info_log(peer_id, sdk_version, nat_type, public_ip, public_port, private_ip, private_port, country="ZZ",
                  province_id="0", city_id="0", isp_id="0", timestamp=-9):
    """

    :param peer_id:
    :param sdk_version:
    :param nat_type:
    :param public_ip:
    :param public_port:
    :param private_ip:
    :param private_port:
    :param country:
    :param province_id:
    :param city_id:
    :param isp_id:
    :param timestamp: log的timestamp值，为-9时按当前时间戳写入
    :return:
    """
    peer_info = {
        "peer_id": str(peer_id),
        "sdk_version": str(sdk_version),
        "nat_type": int(nat_type),
        "public_ip": str(public_ip),
        "public_port": int(public_port),
        "private_ip": str(private_ip),
        "private_port": int(private_port),
        "country": str(country),
        "province_id": str(province_id),
        "city_id": str(city_id),
        "isp_id": str(isp_id),
        "os_type": "",
        "macs": "",
        "os_version": "",
        "cpu": ""
    }
    if timestamp == -9:
        peer_info["timestamp"] = int(time.time()*1000)
    else:
        peer_info["timestamp"] = int(timestamp)
    return peer_info


def logs_creator(one_log, log_key, value_list):
    logs = []
    for index, v in enumerate(value_list):
        one_log[log_key] = v
        # print index, log_key, ":", v, one_log
        logs.append(one_log)
    return logs


def remote_write_logs(remote_host, remote_user, remote_passwd, remote_log_path, src_log_path, interval_time=1):
    """

    :param remote_host:
    :param remote_user:
    :param remote_passwd:
    :param remote_log_path:
    :param src_log_path:
    :param interval_time:
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host,  username=remote_user, password=remote_passwd)
    logs = []
    # 将topic_data中准备的log写入kafka
    f = open(os.path.abspath(os.path.dirname(__file__)) + src_log_path, 'r')
    for i in f.readlines():
        i = i.strip()
        ssh.exec_command('echo "{0}" >> {1}{2}'.format(i, remote_log_path, choice([1, 2, 3])))
        print i
        time.sleep(float(interval_time))
        log = i.split("\x1f")
        logs.append(log)

    f.close()
    ssh.close()

    return logs


if __name__ == "__main__":
    one = peer_info_log("00000002FA7C478F8E04749178FE62A5", "3.9.7", 1, "192.168.1.1", 22222, "192.168.1.1", 22222)
    # logs_creator(one, "peer_id", [1,2,3,4])
    remote_write_logs("192.168.4.229", "admin", "admin", "/home/admin/logs/funnel/report.log_test","\\topic_data\\ok_peer_info.log")
