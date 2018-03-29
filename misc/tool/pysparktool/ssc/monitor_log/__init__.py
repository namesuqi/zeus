# encoding: utf-8
from pyspark.streaming.kafka import KafkaUtils

from ssc.utils import *
from ssc.monitor_log.strategy import *
from ssc.monitor_log.hdfs_ods import *
from ssc.monitor_log.bi import *


def main(opt, config, sc, ssc, step_num):
    """
    monitor_log 主函数
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
        topics=['monitor_log'],
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
    parse_data = k_stream.map(json_parse)

    # rdd 及handles列表
    rdd_handles = []

    if step_num == 3*60:
        # 1.strategy策略监控
        bops_strategy = BOPSStrategy(opt, config, rdd_handles, parse_data)
        bops_strategy.main_strategy()

        # 2.服务HTTP Status 监控
        count_tab = CountTab(opt, config, rdd_handles, parse_data)
        count_tab.main_count()
    elif step_num == 60*60:
        # 1.HDFS ODS
        hdfs_ods = HDFSOds(opt, config, rdd_handles, parse_data)
        hdfs_ods.main_ods()

        # 2.BI
        bi = BI(opt, config, rdd_handles, parse_data)
        bi.main_bi()

    # rdd 处理
    for rdd, handle in rdd_handles:
        rdd.foreachRDD(handle)


