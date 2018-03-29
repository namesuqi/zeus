# coding=utf-8
"""

boss系统-计费模块 自动化用例相关的脚本

__author__ = 'liwenxuan'
20170605

"""

import time
from random import choice
from lib.database.pykafka_handler import pykafka_producer, pykafka_consumer
from lib.interface.boss.time_handler import get_second_to_int
from lib.database.mysql_db_v2 import MysqlDB
from lib.interface.boss.environment_constant import BOSS_CRM_HOST


def send_billing_logs_to_kafka(kafka_hosts, schema_host, schema_port, topic, logs_list, consumer_group):
    """
    直接往kafka写入logs, 并确认可以从kafka消费到所有写入的logs
    :param kafka_hosts: kafka集群的host, 如 "192.168.1.230:9092,192.168.1.232:9092,192.168.1.191:9092,192.168.1.189:9092"
    :param schema_host: schema的host, 如 "192.168.1.230"
    :param schema_port: schema的port, 如 8081
    :param topic: logs的topic, 如 "test_b_download_flow"
    :param logs_list: 需要写入的logs, 如 [{k1: v1, k2: v2, ...}, ...]
    :param consumer_group: logs的消费组, 如 "boss_bill_daily_test"
    :return:
    """

    pykafka_consumer(kafka_hosts, schema_host, schema_port, topic, consumer_group)

    time.sleep(1)
    pykafka_producer(kafka_hosts, schema_host, schema_port, logs_list, topic, write_time=-7)
    time.sleep(5)

    actual_logs_count = len(pykafka_consumer(kafka_hosts, schema_host, schema_port, topic, consumer_group))
    if actual_logs_count == len(logs_list):
        return True
    else:
        print "total", len(logs_list), "logs, receive", actual_logs_count, "logs"
        return False


def create_download_logs_list(block_count, logs_count, prefix, ts_second, domain_list):
    """
    创建download的logs的list
    :param block_count: 将一堆logs记作一个block(块, 与boss的block概念不同), block的数量
    :param logs_count: 一个block中包含的logs的数量
    :param prefix: log的peer_id的prefix
    :param ts_second: log的时间戳(秒级)
    :param domain_list: log的url包含的域名的可选范围
    :return:
    """
    log_list = []

    for i in range(block_count):
        flow = 1000000 + i * 10240
        log_id_prefix = get_second_to_int()  # log的16位id标识的前八位, 表示发log的日期(天)及时间(时分秒)
        for j in range(logs_count):
            log_id = str(log_id_prefix) + str(j).rjust(8, "F")
            peer_id = str(prefix).zfill(8) + "FFFFFFFF" + log_id
            url = "http://{0}/".format(choice(domain_list))
            timestamp = (int(ts_second) - choice(range(0, 301))) * 1000 - choice(range(0, 1000))
            log = {"id": log_id, "timestamp": timestamp, "peer_id": peer_id, "url": url, "play_type": "live",
                   "vvid": "boss_daily_test", "duration": 60, "app": flow, "cdn": flow*3, "p2p": flow*4,
                   "public_ip": "192.168.0.0", "sdk_agent_name": "boss_daily_test", "sdk_agent_version": "3.11.0"}
            log_list.append(log)

    return log_list


def create_upload_logs_list(block_count, logs_count, prefix, ts_second):
    """
    创建upload的logs的list
    :param block_count: 将一堆logs记作一个block(块, 与boss的block概念不同), block的数量
    :param logs_count: 一个block中包含的logs的数量
    :param prefix: log的peer_id的prefix
    :param ts_second: log的时间戳(秒级)
    :return:
    """
    log_list = []

    for i in range(block_count):
        flow = 1000000 + i * 10240
        log_id_prefix = get_second_to_int()  # log的16位id标识的前八位, 表示发log的日期(天)及时间(时分秒)
        for j in range(logs_count):
            log_id = str(log_id_prefix) + str(j).rjust(8, "F")
            peer_id = str(prefix).zfill(8) + "FFFFFFFF" + log_id
            timestamp = (int(ts_second) - choice(range(0, 301))) * 1000 - choice(range(0, 1000))
            log = {"id": log_id, "timestamp": timestamp, "peer_id": peer_id, "play_type": "live", "duration": 60,
                   "upload": flow, "public_ip": "192.168.0.0"}
            log_list.append(log)

    return log_list


def compare_results_for_billing(block_count, logs_count, prefix, ts_second, category, price, unit):
    """
    比较预期结果与实际结果是否相符
    :param block_count: 将一堆logs记作一个block(块, 与boss的block概念不同), block的数量
    :param logs_count: 一个block中包含的logs的数量
    :param prefix: log的peer_id的prefix
    :param ts_second: log的时间戳(秒级)
    :param category: 计费类别, "download"/"upload"
    :param price: CRM中设定的计费单价
    :param unit: CRM中设定的计价单位, "KB"/"MB"/"GB"
    :return:
    """

    assert unit in ("KB", "MB", "GB")

    account = 0
    for i in range(logs_count):
        flow = 1000000 + i * 10240
        account += flow
    print "account one block:", account
    total_account = account * block_count
    print "account all block:", total_account

    total_money = total_account * price
    print "money (B):", total_money

    if unit == "KB":
        expect_account = float(total_account)/1024
        expect_money = float(total_money)/1024
    elif unit == "MB":
        expect_account = float(total_account)/1024/1024
        expect_money = float(total_money)/1024/1024
    else:
        expect_account = float(total_account)/1024/1024/1024
        expect_money = float(total_money)/1024/1024/1024

    timestamp_end = int(ts_second)
    timestamp_start = timestamp_end - 10 * 60

    sql = "select sum(account), sum(money) from {0}_billing where ts between {1} and {2} and prefix = '{3}'"\
        .format(category, timestamp_start, timestamp_end, prefix)
    mysql_db = MysqlDB(host=BOSS_CRM_HOST)
    actual_account, actual_money = mysql_db.execute(sql).one_by_one()
    del mysql_db

    if abs(actual_account - expect_account) <= 0.000001 and abs(actual_money - expect_money) <= 0.000001:
        return True
    else:
        print "account - expect:", expect_account, "; actual:", actual_account
        print "money - expect:", expect_money, "; actual:", actual_money
        return False


def clear_logs(customer_id, category):
    # 为避免自动化测试累积的数据占用boss自动化服务器的空间, 每次测试结束, 清空无效的数据(logs)
    ts_millisecond = (int(time.time()) - 86400 * 5) * 1000
    sql = "delete from {0}_log_{1} where timestamp <= {2}".format(category, customer_id, ts_millisecond)
    mysql_db = MysqlDB(host=BOSS_CRM_HOST)
    mysql_db.execute(sql)
    time.sleep(1)
    del mysql_db




