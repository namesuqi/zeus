# coding=utf-8

import os
import logging
import demjson
from lib.decorator.trace import print_trace
from pykafka import KafkaClient
import avro.io
import avro.schema
import io
from pykafka.common import OffsetType
import re

from lib.platform.flume_test.flume_constant import *


class SimpleKafkaClient:

    def __init__(self, topic, hosts=KAFKA_HOST):
        self.client = KafkaClient(hosts=hosts)
        self.collect_topic = self.client.topics[topic]
        self._create_schema(topic)

    @print_trace
    def _create_schema(self, topic):
        schema = avro.schema.parse(open(os.path.abspath(os.path.dirname(__file__)) + "/../avro_schema/" + topic + ".avsc").read())
        self.avro_reader = avro.io.DatumReader(schema)

    @print_trace
    def show_topics(self):
        for topic in self.collect_topic:
            print topic

    @print_trace
    def consumer(self, consumer_group="flume_test_group"):
        simple_consumer = self.collect_topic.get_balanced_consumer(
            reset_offset_on_start=False,
            auto_commit_enable=True,
            auto_commit_interval_ms=1000,
            consumer_group=consumer_group,
            consumer_timeout_ms=10000,
            zookeeper_connect=ZOOKEEPER_HOST,
        )

        # simple_consumer = self.collect_topic.get_simple_consumer(
        #     reset_offset_on_start=False,
        #     auto_commit_enable=True,
        #     auto_commit_interval_ms=1000,
        #     consumer_group="flume_test_group",
        #     consumer_timeout_ms=1000,
        # )

        count = 0
        consumer = []
        for message in simple_consumer:
            # print 'offset: %s' % message.offset, 'data: ' + message.value
            bytes_msg = io.BytesIO(message.value[5:])
            decode_msg = avro.io.BinaryDecoder(bytes_msg)
            recode_msg = self.avro_reader.read(decode_msg)
            # print message.offset, recode_msg
            # simple_consumer.commit_offsets()
            consumer.append(recode_msg)
            count += 1
        print count
        return consumer

        # return count


if __name__ == '__main__':

    # logging.getLogger("pykafka").addHandler(logging.StreamHandler())
    # logging.getLogger("pykafka").setLevel(logging.DEBUG)
    # client = KafkaClient(hosts="192.168.1.230:9092,192.168.1.231:9092,192.168.1.232:9092")
    #
    # a = client.topics['heartbeat']
    # # a = client.topics
    #
    # # for topic in a:
    # #     # if topic == 'heartbeat':
    # #     #     b = topic
    # #     print topic
    #
    # consumer = a.get_simple_consumer(consumer_group='testgroup',
    #                                  auto_offset_reset=OffsetType.EARLIEST,
    #                                  reset_offset_on_start=True
    #                                  )
    # for message in consumer:
    #     if message is not None:
    #         print "----------------------------"
    #         print message.offset
    #         print message.value


    eg = SimpleKafkaClient('peer_info')
    print eg.consumer()

