# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170811
__reference__ = "lib/database/pykafka_handler.py"

作用: 1.向kafka发送avro编码后的log(s)
     2.从kafka获取avro解码后的log(s)
说明: 针对lf调度策略系统的测试需要对原函数进行修改

"""

import io
import struct
import time

import avro
import requests
import avro.io
import avro.schema
from pykafka import KafkaClient

from lib.interface.strategy.lf_strategy.lib.const import KAFKA_HOSTS, SCHEMA_HOST, SCHEMA_PORT


# ---------------------------------------------------------------------------------------------------------------------

dis_id = "\r\r\r"  # dis-distinguish; 避免avro拆分log_list出错的标识

# ---------------------------------------------------------------------------------------------------------------------


def get_latest_schema_info(topic, schema_host=SCHEMA_HOST, schema_port=SCHEMA_PORT):
    # 获取topic最新的schema格式和schema_id
    r = requests.get("http://{0}:{1}/subjects/{2}-value/versions/latest".format(schema_host, schema_port, topic))
    if r.status_code == 200:
        rsp = r.json()
        return rsp["schema"], rsp["id"]
    else:
        raise ValueError(r.text)


def decode_by_avro(log_list, topic_schema, topic_schema_id):
    """
    对logs进行avro编码
    :param log_list: [{}, {}, ...]
    :param topic_schema:
    :param topic_schema_id:
    :return:
    """
    bytes_header = "\x00" + struct.pack('>L', topic_schema_id)
    schema = avro.schema.parse(topic_schema)
    datum_writer = avro.io.DatumWriter(schema)

    bytes_encode = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_encode)

    for log in log_list:
        encoder.write_bytes(bytes_header)
        datum_writer.write(log, encoder)
        encoder.write_bytes(dis_id)
    bytes_logs = bytes_encode.getvalue()
    bytes_encode.close()

    bytes_logs = bytes_logs[1:]  # 去掉开头的"\n"
    if len(dis_id) > 0:
        bytes_logs = bytes_logs[:-len(dis_id)]  # 去掉结尾的dis_id

    return bytes_logs

# ---------------------------------------------------------------------------------------------------------------------


# 向kafka传入log(s) - 需要传入schema信息 (避免重复获取schema)
def write_logs_to_kafka_with_schema(log_list, topic, topic_schema, topic_schema_id, kafka_hosts=KAFKA_HOSTS):
    if type(log_list) != list:
        log_list = [log_list]

    # 对logs进行avro编码
    bytes_logs = decode_by_avro(log_list, topic_schema, topic_schema_id)

    # 与kafka建立连接
    client = KafkaClient(hosts=kafka_hosts)
    kafka_topic = client.topics[topic]

    with kafka_topic.get_producer(max_queued_messages=10000, linger_ms=100) as producer:
        # 向kafka发送avro编码后的logs
        for bytes_log in bytes_logs.split(dis_id + "\n"):
            producer.produce(bytes_log)


# 向kafka传入log(s) - 不需要传入schema信息
def write_logs_to_kafka(log_list, topic, kafka_hosts=KAFKA_HOSTS, schema_host=SCHEMA_HOST, schema_port=SCHEMA_PORT):
    # 获取该topic最新的schema
    topic_schema, topic_schema_id = get_latest_schema_info(topic, schema_host=schema_host, schema_port=schema_port)

    # 向kafka发送avro编码后的logs
    start_ts = time.time()
    write_logs_to_kafka_with_schema(log_list, topic, topic_schema, topic_schema_id, kafka_hosts)
    end_ts = time.time()
    print "send", len(log_list), topic, "log(s) cost", end_ts - start_ts, "second(s)"

# ---------------------------------------------------------------------------------------------------------------------


# 从kafka消费数据
def read_logs_from_kafka(topic="sdk_directional_task_live", consumer_group="ss_test", kafka_hosts=KAFKA_HOSTS):
    # 获取该topic最新的schema
    topic_schema, topic_schema_id = get_latest_schema_info(topic)
    # 与kafka建立连接
    client = KafkaClient(hosts=kafka_hosts)
    kafka_topic = client.topics[topic]
    consumer = kafka_topic.get_simple_consumer(consumer_group=consumer_group,
                                               consumer_timeout_ms=5000,
                                               auto_commit_enable=True,
                                               auto_commit_interval_ms=1,
                                               consumer_id=consumer_group
                                               )
    # 存放消息记录的partition，offset，value
    collect_logs = []
    for message in consumer:
        if message is not None:
            msg_partition = message.partition.id
            msg_offset = message.offset
            # 对单条记录解码
            bytes_msg = io.BytesIO(message.value[5:])
            decode_msg = avro.io.BinaryDecoder(bytes_msg)
            recode_msg = avro.io.DatumReader(avro.schema.parse(topic_schema)).read(decode_msg)
            # 收集该log的partition，offset，value信息
            msg_collect = [msg_partition, msg_offset, recode_msg]
            collect_logs.append(msg_collect)
    # 按log的timestamp排序
    collect_logs.sort(key=lambda x: x[2]["timestamp"])
    # 打印消息记录的partition，offset，value
    print "+++++++Topic: %s+++++++" % topic
    print "logs count:", len(collect_logs)
    for index, log in enumerate(collect_logs):
        print index, log
    print "Successfully received."
    return collect_logs

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    pass

    # read_logs_from_kafka()

    # log_list = [{"user_id": str(i).zfill(8), "timestamp": i, "switch": False} for i in range(10)]
    # write_logs_to_kafka(log_list, "ss_user_strategy_switch")






