# encoding: utf-8
from pyspark.streaming.kafka import KafkaUtils

from ssc.utils import *
from ssc.opt_logs.sdk_opt import *


def main(opt, config, sc, ssc, step_num):
    """
    sdk_optlogs 主函数
    :param sc: 
    :param step_num:
    :param opt:
    :param config:
    :param ssc:
    :return:
    """
    # 连接kafka
    k_stream = KafkaUtils.createDirectStream(
        ssc=ssc,
        topics=['opt_logs'],
        kafkaParams={
            "group.id": config.CONSUMER_GROUP,
            "auto.offset.reset": "largest",
            "metadata.broker.list": config.KAFKA_HOSTS
        })

    # 连接zookeeper
    # zookeeper = "192.168.4.199:2181"                                            # 打开一个TCP socket 地址 和 端口号
    # topic = {"monitor_log": 0, "monitor_log": 1, "monitor_log": 2}              # 要列举出分区
    # group_id = "business_ops"                                                   # group id
    # k_stream = KafkaUtils.createStream(ssc, zookeeper, group_id, topic)

    # 获取处理后的原始log数据
    parse_data = k_stream.map(json_parse).cache()

    # rdd 及handles列表
    rdd_handles = []

    if step_num == 3*60:
        # 1.sdk_optlogs
        sdk_opt = SDKOpt(opt, config, rdd_handles, parse_data, sc)
        sdk_opt.main_sdk_opt()

    # rdd 处理
    for rdd, handle in rdd_handles:
        rdd.foreachRDD(handle)


