# coding=utf-8

"""

boss系统-计费模块 计费&统计相关的脚本

  1. add_downloads/uploads : 用于功能测试, 通过kafka-flume向kafka传入logs
  2. compare_result_for_normal_test : 与add_downloads/uploads结合使用, 验证Boss计费的结果是否正确
  3. stable : 用于稳定性测试, 通过kafka-flume向kafka传入大量logs, 根据id的前五位区分block, 后五位区分各个block中的第几条log
  4. compare_result_for_stable : 与stable结合使用, 在稳定性测试结束后, 根据block数进行流量的统计和计费, 验证Boss计费的结果是否正确
  * ts为timestamp的简称

__author__ = 'liwenxuan'
20170602

"""

import paramiko
import time
from random import choice
from lib.interface.boss.time_handler import get_time_to_int, get_date_to_int

FLUME_PATH = "/home/admin/logs/funnel/report.log_test_boss"

CUSTOMER_1_DOMAIN_LIST = ["customer-1.domain-1", "customer-1.domain-2", "customer-1.domain-3"]


def boss_prepare():
    pass
    # download = SimpleKafkaClient("test_b_download_flow")
    # download.consumer("billing_consumer")
    # upload = SimpleKafkaClient("test_upload_flow")
    # upload.consumer("billing_consumer")
    # block = SimpleKafkaClient("boss_task_block")
    # block.consumer("billing_consumer")


def boss_add_downloads(start, end, ts_second, prefix="00000002", url="http://customer-1.domain-1/",
                       topic="test_b_download_flow", flume_host="192.168.1.229",
                       user="admin", password="admin", path=FLUME_PATH):
    # 向kafka传入download的logs, 设定id的范围[start, end)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flume_host, username=user, password=password)

    test_date = get_date_to_int()
    test_time = get_time_to_int()
    total_flow = 0
    for i in range(start, end):
        id = str(i).zfill(8)
        flow = 100000 + i * 1024
        log = "topic={0}\x1fid={1}\x1ftimestamp={2}000\x1fpeer_id={3}FFFFFF{4}FFFFFF{1}\x1furl={5}\x1fplay_type={6}\
\x1fvvid={1}\x1fduration=60\x1fapp={7}\x1fcdn={8}\x1fp2p={9}\x1fpublic_ip=10.6.3.6\x1fsdk_agent_name=boss_test\x1f\
sdk_agent_version=3.9.0".format(topic, id, ts_second, prefix.zfill(8), test_date, url, test_time, flow, flow*3, flow*4)
        ssh.exec_command('echo {0} >> {1}'.format(log, path))
        total_flow += flow

    ssh.close()
    print "download from", start, "to", end, "sum:", total_flow, "Bytes"
    return total_flow


def boss_add_uploads(start, end, ts_second, prefix="00000001", topic="test_upload_flow",
                     flume_host="192.168.1.229", user="admin", password="admin", path=FLUME_PATH):
    # 向kafka传入upload的logs, 设定id的范围[start, end)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flume_host, username=user, password=password)

    test_date = get_date_to_int()
    test_time = get_time_to_int()
    total_flow = 0
    for i in range(start, end):
        id = str(i).zfill(8)
        flow = 100000 + i * 1024
        log = "topic={0}\x1fid={1}\x1ftimestamp={2}000\x1fpeer_id={3}FFFFFF{4}FFFFFF{1}\x1fplay_type={5}\x1fduration=\
60\x1fupload={6}\x1fpublic_ip=10.6.3.6".format(topic, id, ts_second, prefix.zfill(8), test_date, test_time, flow)

        ssh.exec_command('echo {0} >> {1}'.format(log, path))
        total_flow += flow

    ssh.close()
    print "upload from", start, "to", end, "sum:", total_flow, "Bytes"
    return total_flow


def compare_result_for_normal_test(price, billing_unit, *flows):
    # 与boss_add_downloads/uploads结合使用
    account = 0.0
    for flow in flows:
        account += float(flow)
    print "total account:", int(account)

    if billing_unit == "KB":
        billing_account = account / 1024
    elif billing_unit == "MB":
        billing_account = account / 1024 / 1024
    elif billing_unit == "GB":
        billing_account = account / 1024 / 1024 / 1024
    else:
        print billing_unit, "should be 'KB' or 'MB' or 'GB'"
        raise ValueError
    print "account by", billing_unit, ":", billing_account

    billing_money = round(price * billing_account, 6)
    print "total money:", billing_money

    return billing_money


def stable(block_start, block_end, logs_count, recall_time_start=0, recall_time_end=3600):
    # 用于稳定性测试(计费+回溯)
    while True:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("192.168.1.229", username="admin", password="admin")

            for i in range(block_start, block_end):
                pre = str(i).zfill(5)
                print int(time.time())
                print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

                for j in range(logs_count):
                    suf = str(j).zfill(5)
                    id = pre + suf
                    flow = 100000 + i * 1024
                    test_time = get_time_to_int()
                    timestamp = int(time.time()) - choice(range(recall_time_start, recall_time_end))

                    log_down = "topic=test_b_download_flow\x1fid={0}\x1ftimestamp={1}000\x1fpeer_id=00000002\
FFF{2}FFF{0}\x1furl=http://{3}/\x1fplay_type=live\x1fvvid={2}\x1fduration=60\x1fapp={4}\x1fcdn={5}\x1fp2p={6}\
\x1fpublic_ip=0.0.0.0\x1fsdk_agent_name=boss\x1fsdk_agent_version=3.11.0"\
                        .format(id, timestamp, test_time, choice(CUSTOMER_1_DOMAIN_LIST), flow, flow*3, flow*4)
                    ssh.exec_command('echo {0} >> {1}'.format(log_down, FLUME_PATH))
                    log_up = "topic=test_upload_flow\x1fid={0}\x1ftimestamp={1}000\x1fpeer_id=00000001FFF{2}FFF{0}\x1f\
play_type=live\x1fduration=60\x1fupload={3}\x1fpublic_ip=10.0.0.0".format(id, timestamp, test_time, flow)
                    ssh.exec_command('echo {0} >> {1}'.format(log_up, FLUME_PATH))

                time.sleep(5)
            ssh.close()
            break
        except:
            print "No.", i, "block"
            block_start = i


def compare_result_for_stable(block_count, logs_count, download_price, download_unit, upload_price, upload_unit):
    # 与stable结合使用, 允许0.00001以内的误差
    account = 0
    for i in range(logs_count):
        flow = 100000 + i * 1024
        account += flow
    print "account one block:", account
    total_account = account * block_count
    print "account all block:", total_account

    download_money = total_account * download_price
    upload_money = total_account * upload_price
    print "download money (B):", download_money
    print "upload money (B):", upload_money

    return [download_money, upload_money]


if __name__ == "__main__":
    timestamp_now = int(time.time())  # 当前时间戳, 单位为秒
    print timestamp_now
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # a1 = boss_add_downloads(0, 10, int(time.time()), prefix="00000002", url="http://customer-1.domain-1/")
    # a2 = boss_add_downloads(10, 30, int(time.time()), prefix="00000002", url="http://customer-1.domain-2/")
    # a3 = boss_add_downloads(30, 60, int(time.time()), prefix="00000002", url="http://customer-1.domain-3/")
    # b1 = boss_add_downloads(1000, 1010, int(time.time()-300), prefix="00000002", url="http://customer-1.domain-1/")
    # print "total:", a1 + a2 + a3
    # print "same domain:", a1 + b1

    # 回溯
    # a1 = boss_add_downloads(0, 990, int(time.time())-900); print a1; time.sleep(3)
    # a2 = boss_add_downloads(990, 1000, int(time.time())); print a2; time.sleep(3)
    # a3 = boss_add_downloads(1000, 1010, int(time.time())-900); print a3; time.sleep(3)

    # 计费
    # b1 = boss_add_downloads(1, 2001, "1483066200"); print b1; time.sleep(10)
    # b2 = boss_add_downloads(2001, 4001, "1483066500"); print b2; time.sleep(10)
    # b3 = boss_add_downloads(4001, 6001, "1483066800"); print b3; time.sleep(10)
    # b4 = boss_add_downloads(6001, 8001, "1483067100"); print b4; time.sleep(10)
    # b5 = boss_add_downloads(8001, 10001, "1483067400"); print b5; time.sleep(10)
    # b6 = boss_add_downloads(10001, 12001, "1483067400"); print b6; time.sleep(10)
    # b7 = boss_add_downloads(12001, 14001, "1483067400"); print b7; time.sleep(10)
    # b8 = boss_add_downloads(14001, 16001, "1483067400"); print b8; time.sleep(10)
    # b9 = boss_add_downloads(16001, 18001, "1483067400"); print b9; time.sleep(10)
    # b10 = boss_add_downloads(18001, 20001, "1483067400"); print b10; time.sleep(10)




