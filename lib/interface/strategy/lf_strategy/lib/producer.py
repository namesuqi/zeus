# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170813

作用: 向kafka发送特定topic的logs

"""

from lib.interface.strategy.lf_strategy.lib.const import topics, basic_topics

from lib.interface.strategy.lf_strategy.lib.log_handler import log_logger
from lib.interface.strategy.lf_strategy.lib.kafka_handler import write_logs_to_kafka_with_schema
from lib.interface.strategy.lf_strategy.lib.utility import set_peer_id_list, set_ssid_list


# ---------------------------------------------------------------------------------------------------------------------


def fill_log_by_schema(input_log, basic_topic, schema):
    """
    用默认值填充必选字段和需要关注的可选字段, 并按topic的schema调整字段值的类型
    :param input_log: dict
    :param basic_topic: string, 该log的基础topic (非实际topic, 如 "ss_peer_info"的基础topic为"peer_info")
    :param schema: string, 该topic的schema (实际topic)
    :return:
    """
    output_log = dict(basic_topics[basic_topic], **input_log)

    # to_avro(input_log, schema)  # 按照avro格式调整各个字段的类型, 暂未实现

    log_logger.info("{0} -- {1}".format(basic_topic, output_log))

    return output_log


def send_logs(input_log_list, basic_topic, topic_schema, topic_schema_id):
    """
    向kafka发送logs
    :param input_log_list: [{}, {}, ...]
    :param basic_topic: string, logs的基础topic
    :param topic_schema:
    :param topic_schema_id:
    :return:
    """
    if not isinstance(input_log_list, list):
        input_log_list = [input_log_list]

    topic = topics[basic_topic]

    log_list = [fill_log_by_schema(input_log, basic_topic, topic_schema) for input_log in input_log_list]

    write_logs_to_kafka_with_schema(log_list, topic, topic_schema, topic_schema_id)

# ---------------------------------------------------------------------------------------------------------------------


# 向kafka发送一组peer_info或heartbeat的logs, peer_id与ssid的顺序必须一一对应
# def peer_online_log_list(**kwargs):
#
#     peer_id_list = kwargs.get("peer_id_list", None)
#     if peer_id_list is None:
#         peer_id_list = get_peer_id_list(kwargs["prefix_range"], kwargs["peer_index_range"], kwargs["peer_unique_id"])
#     if isinstance(peer_id_list, list):
#         peer_id_list = [peer_id_list]
#
#     ssid_list = kwargs.get("ssid_list", None)
#     if ssid_list is None:
#         ssid_list = get_ssid_list(kwargs["prefix_range"], kwargs["peer_index_range"], kwargs["ssid_unique_id"])
#     if isinstance(ssid_list, list):
#         ssid_list = [ssid_list]
#
#     input_log_list = [{"peer_id": peer_id, "ssid": ssid} for peer_id, ssid in zip(peer_id_list, ssid_list)]
#
#     return input_log_list

# ---------------------------------------------------------------------------------------------------------------------


def get_peer_id_list(**kwargs):
    peer_id_list = kwargs.get("peer_id_list", None)
    if peer_id_list is None:
        peer_id_list = set_peer_id_list(kwargs["prefix_range"], kwargs["peer_index_range"], kwargs["peer_unique_id"])
    if isinstance(peer_id_list, list):
        peer_id_list = [peer_id_list]
    return peer_id_list


def get_ssid_list(**kwargs):
    ssid_list = kwargs.get("ssid_list", None)
    if ssid_list is None:
        ssid_list = set_ssid_list(kwargs["prefix_range"], kwargs["peer_index_range"], kwargs["ssid_unique_id"])
    if isinstance(ssid_list, list):
        ssid_list = [ssid_list]
    return ssid_list







