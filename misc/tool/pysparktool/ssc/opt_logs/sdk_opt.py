# _*_ coding: utf-8 _*_
import datetime
import bisect
from operator import add

from pyspark import SparkFiles

from ssc.utils import *
from ssc.variables import *
geo_db_path = 'GeoLite2-City.mmdb'
cfg = None

# 全局变量
sdk_opt_type_monitor = {
    'sdk_optlogs': '',
}
rtt_level_list = [0, 500, 1000, 2000, 10000]
rtt_level_map = {
    1: "0~499",
    2: "500~999",
    3: "1000~1999",
    4: "2000~9999",
    5: "10000~1000000",
}


class SDKOpt(object):
    def __init__(self, opt, config, rdds, parse_data, sc):
        """
        :param opt:
        :param config:
        :param rdds:
        :param parse_data:
        """
        super(SDKOpt, self).__init__()

        self.sc = sc
        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data

        self.es_index = "ssc-business_monitor_log-sdk_opt-{}"
        global cfg
        cfg = self.config

    def main_sdk_opt(self):
        """
        main函数,负责
        :return:
        """
        # 过滤；解析
        strategy_res = self.parse_data.filter(lambda info: info['type'] in sdk_opt_type_monitor).map(self.process_msg)
        # 生成汇总数据；汇总；解包
        strategy_count = strategy_res.mapPartitions(self.partition_handle).flatMap(self.get_kv).reduceByKey(add).map(lambda x: [x[0], x[1]])

        def sdk_handle(rdd_time, rdd):
            data_list = rdd.collect()
            if data_list:
                # 生成数据
                datas = self.get_data(data_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "strategy")

        self.rdds.append((strategy_count, sdk_handle))

        return self.rdds

    @staticmethod
    def process_msg(info):
        monitor = {"req_rtt": []}
        try:
            # 格式化处理message
            message = info
            monitor['req_rtt'] = message['body']['req_rtt'] or []
            monitor['pubip'] = message['pubip']
        except:
            pass
        return monitor

    @staticmethod
    def partition_handle(mons):
        from geoip2 import database

        etcd_key = get_etcd_key(cfg)

        def ip2subdivision(monitor):
            try:
                province_name = reader.city(monitor['pubip']).subdivisions.most_specific.name
                monitor['province'] = province_name or 'None'
                identity_code = IDENTITY_CODE.get(province_name)
                # 获取地区分组类别
                monitor['group'] = etcd_key.get(identity_code, 'default')
            except:
                monitor['province'] = 'None'
                monitor['group'] = 'default'
            return monitor

        def rtt2level(monitor):
            for info in monitor.get('req_rtt', []):
                info['rtt_level'] = rtt_level_map.get(bisect.bisect_right(rtt_level_list, info['rtt']), rtt_level_map[1])
            return monitor

        reader = database.Reader(SparkFiles.get(geo_db_path))

        ip_res = [ip2subdivision(mon) for mon in mons]
        rtt_level_res = [rtt2level(mon) for mon in ip_res]
        return rtt_level_res

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info
        for mon in monitor['req_rtt']:
            key = str(mon['domain']) + '&' + str(mon['rtt_level']) + '&' + monitor['province'].encode('utf-8') + '&' +\
                  monitor['group'].encode('utf-8')
            kv_list.append((key, 1))
        return kv_list

    def pull_down(self, long_list):
        # 拆成 类型，hostip，指标和value
        types = long_list[0].split('&')
        return types[0], types[1], types[2], types[3], long_list[1]

    def get_data(self, data_list, rdd_time):
        rdd_time -= datetime.timedelta(hours=8)
        datas = []

        for data in data_list:
            domain, rtt_level, province, group, count = self.pull_down(data)
            datas.append({
                'monitor': {
                    'domain': domain,
                    'rtt_level': rtt_level,
                    'province': province,
                    'count': count,
                    'group': group,
                },
                '@timestamp': rdd_time,
                "@version": "1",
            })

        return datas



