# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2017/6/5 下午2:33
import datetime

from ssc.utils import *


# 全局变量
bi_type_monitor = [
    'platform_etl_monitor',
]


class BI(object):
    def __init__(self, opt, config, rdds, parse_data):
        """
        BI监控
        注意:
        :param opt:
        :param config:
        :param rdds:
        :param parse_data:
        """
        super(BI, self).__init__()

        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data

        self.es_index = "ssc-business_monitor_log-bi-{}"

    def main_bi(self):
        """
        main函数,负责
        :return:
        """
        # 过滤；解析
        ods_res = self.parse_data.filter(lambda info: info['type'] in bi_type_monitor).map(self.process_msg)
        # 生成汇总数据；汇总；解包
        hdfs_ods = ods_res.flatMap(self.get_kv).reduceByKey(self.handle_monitor).map(lambda x: [x[0], x[1]])

        def ods_handle(rdd_time, rdd):
            ods_list = rdd.collect()
            if ods_list:
                # 生成数据
                datas = self.get_bi_data(ods_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "bi")

        self.rdds.append((hdfs_ods, ods_handle))

        return self.rdds

    @staticmethod
    def process_msg(info):
        # 格式化处理message
        message = info['message']
        monitor = {}
        # 组合monitor
        for mes in message.split('\x1f'):
            key_value = mes.split('=')
            if key_value[0] == 'total_records':
                monitor[key_value[0]] = int(key_value[1])
            else:
                monitor[key_value[0]] = key_value[1]
        info['monitor'] = monitor
        return info

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info['monitor']
        kv_list.append(('{}&{}&{}'.format(info['type'], monitor['data_source'], monitor['table_name']),
                        {
                            'value': monitor['total_records']
                        }))

        return kv_list

    @staticmethod
    def handle_monitor(x, y):
        total = x['value'] + y['value']
        return {'value': total}

    def pull_down(self, long_list):
        # 拆成 类型和value
        types = long_list[0].split('&')
        return types[0], types[1], types[2], long_list[1]['value']

    def get_bi_data(self, type_list, rdd_time):
        data = {}
        rdd_time -= datetime.timedelta(hours=8)
        for a_list in type_list:
            type_name, data_source, table_name, total_records = self.pull_down(a_list)
            if type_name not in data:
                data[type_name] = {
                    data_source: {
                        'total': total_records,
                        table_name: total_records,
                    }
                }
            else:
                if data_source not in data[type_name]:
                    data[type_name][data_source] = {
                        'total': total_records,
                        table_name: total_records,
                    }
                else:
                    if table_name not in data[type_name][data_source]:
                        data[type_name][data_source]['total'] += total_records
                        data[type_name][data_source][table_name] = total_records
                    else:
                        data[type_name][data_source]['total'] += total_records
                        data[type_name][data_source][table_name] += total_records

        body = {
            'monitor': data,
            '@timestamp': rdd_time,
            "@version": "1",
            # 昨日0点时间戳
            '@occur_timestamp': int(int(time.mktime(datetime.datetime.now().timetuple()) * 1000) /
                                    86400000 - 1) * 86400000
        }

        datas = [body]

        return datas

