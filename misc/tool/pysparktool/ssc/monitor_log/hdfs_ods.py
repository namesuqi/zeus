# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2017/6/5 下午2:33
import datetime
import re

from ssc.utils import *


# 全局变量
hdfs_ods_type_monitor = {
    'platform_ods_monitor': '',
    'platform_kafka-hdfs_monitor': r'Number$'
}

# hdfs_ods_type_monitor = [
#     'platform_ods_monitor', 'platform_kafka-hdfs_monitor',
# ]


class HDFSOds(object):
    def __init__(self, opt, config, rdds, parse_data):
        """
        HDFS platform_ods_monitor监控
        注意:
        :param opt:
        :param config:
        :param rdds:
        :param parse_data:
        """
        super(HDFSOds, self).__init__()

        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data

        self.es_index = "ssc-business_monitor_log-hdfs_ods-{}"

    def main_ods(self):
        """
        main函数,负责
        :return:
        """
        # 过滤；解析
        ods_res = self.parse_data.filter(lambda info: info['type'] in hdfs_ods_type_monitor).map(self.process_msg)
        # 生成汇总数据；汇总；解包
        hdfs_ods = ods_res.flatMap(self.get_kv).reduceByKey(self.handle_monitor).map(lambda x: [x[0], x[1]])

        def ods_handle(rdd_time, rdd):
            ods_list = rdd.collect()
            if ods_list:
                # 生成数据
                datas = self.get_ods_data(ods_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "hdfs_ods")

        self.rdds.append((hdfs_ods, ods_handle))

        return self.rdds

    @staticmethod
    def process_msg(info):
        print info
        # 格式化处理message
        message = info['message']
        monitor = {}
        # 组合monitor
        for mes in message.split('\x1f'):
            key_value = mes.split('=')
            if info['type'] == 'platform_ods_monitor' and key_value[0] == 'total_records':
                monitor[key_value[0]] = int(key_value[1])
            elif info['type'] == 'platform_ods_monitor' and key_value[0] == 'table_name':
                monitor[key_value[0]] = key_value[1]
            elif info['type'] == 'platform_kafka-hdfs_monitor' and \
                    re.findall(hdfs_ods_type_monitor['platform_kafka-hdfs_monitor'], key_value[0]):
                monitor[key_value[0]] = int(key_value[1])

        info['monitor'] = monitor
        return info

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info['monitor']
        if info['type'] == 'platform_ods_monitor':
            kv_list.append(('{}&{}'.format(info['type'], monitor['table_name']),
                            {
                                'total': monitor['total_records'],
                            }))
        elif info['type'] == 'platform_kafka-hdfs_monitor':
            for mon in monitor:
                kv_list.append(('{}&{}'.format(info['type'], mon),
                                {
                                    'total': monitor[mon],
                                }))
        return kv_list

    @staticmethod
    def handle_monitor(x, y):
        total = x['total'] + y['total']
        return {'total': total}

    def pull_down(self, long_list):
        # 拆成 类型和value
        types = long_list[0].split('&')
        return types[0], types[1], long_list[1]['total']

    def get_ods_data(self, type_list, rdd_time):
        data = {}
        rdd_time -= datetime.timedelta(hours=8)
        for a_list in type_list:
            type_name, sec, total_records = self.pull_down(a_list)
            if type_name == 'platform_kafka-hdfs_monitor':
                if type_name not in data:
                    data[type_name] = {'total': total_records}
                else:
                    data[type_name]['total'] += total_records
            elif type_name == 'platform_ods_monitor':
                if type_name not in data:
                    data[type_name] = {
                        'total': total_records,
                        sec: total_records
                    }
                else:
                    data[type_name]['total'] += total_records
                    data[type_name][sec] = total_records

        body = {
            'monitor': data,
            '@timestamp': rdd_time,
            "@version": "1",
        }

        datas = [body]

        return datas
