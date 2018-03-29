# _*_ coding: utf-8 _*_
import datetime
import bisect
from operator import add

from ssc.utils import *


# 全局变量
error_logs_type_monitor = {
    'p2p_errlogs_nginx_log': '',
}


class ErrorLogs(object):
    def __init__(self, opt, config, rdds, parse_data, sc):
        """
        :param opt:
        :param config:
        :param rdds:
        :param parse_data:
        """
        super(ErrorLogs, self).__init__()

        self.sc = sc
        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data

        self.es_index = "ssc-business_monitor_log-error_logs-{}"

    def main(self):
        """
        main函数,负责
        :return:
        """
        # 过滤；解析
        strategy_res = self.parse_data.filter(lambda info: info['type'] in error_logs_type_monitor).map(self.process_msg)
        # 生成汇总数据；汇总；解包
        strategy_count = strategy_res.flatMap(self.get_kv).reduceByKey(add).map(lambda x: [x[0], x[1]])

        def log_handle(rdd_time, rdd):
            data_list = rdd.collect()
            if data_list:
                # 生成数据
                datas = self.get_data(data_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "error_logs")

        self.rdds.append((strategy_count, log_handle))

        return self.rdds

    @staticmethod
    def process_msg(info):
        monitor = {'errors': []}
        try:
            # 格式化处理message
            message = info
            monitor['pubip'] = message['pubip']
            monitor['useragent'] = message['useragent']
            monitor['errors'] = message['body']['errors']

            # 可能没有
            monitor['user_id'] = message['body']['peer_id'][:8]
        except:
            pass
        return monitor

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info
        for mon in monitor.get('errors', []):
            kv_list.append((str(mon['type']) + '&' + str(monitor['useragent']) + '&' + str(monitor['user_id']), 1))
        return kv_list

    def pull_down(self, long_list):
        # 拆成 err_type, useragent, user_id, value
        types = long_list[0].split('&')
        return types[0], types[1], types[2], long_list[1]

    def get_data(self, data_list, rdd_time):
        rdd_time -= datetime.timedelta(hours=8)
        datas = []

        for data in data_list:
            err_type, useragent, user_id, count = self.pull_down(data)
            datas.append({
                'monitor': {
                    'err_type': err_type,
                    'useragent': useragent,
                    'user_id': user_id,
                    'count': count
                },
                '@timestamp': rdd_time,
                "@version": "1",
            })

        return datas

