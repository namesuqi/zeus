# encoding: utf-8
import datetime
import re

from ssc.utils import *


# 全局变量
strategy_type_monitor = {
    'p2p_courier_monitor': ['receive_join_lf_count', 'sent_join_lf_count',
                            'receive_leave_lf_count', 'sent_leave_lf_count'],
    'p2p_stun_monitor': ['task_join_lf', 'sent_peer_join_lf', 'complete_peer_join_lf',
                         'task_leave_lf', 'sent_peer_leave_lf', 'complete_peer_leave_lf'],
    'p2p_tracker_go_monitor': ['lfReport'],
    'platform_kafka_flume_monitor': ['lf_report'],
    'p2p_strategy_monitor': ['topic_count', 'topic_count_timeout', 'lf_to_add',
                             'lf_to_delete', 'lf_added', 'lf_deleted'],
    'p2p_channel_monitor': ['lfCount'],
}

server_status_count = {'p2p_tracker_monitor': r'\d\d\d=\d+'}


class BOPSStrategy(object):
    def __init__(self, opt, config, rdds, parse_data):
        """
        strategy策略监控处理类
        注意:
            1.交给worker的程序不能包括python对象等，必须是常用变量，所以map、reduce handle是staticmethod
            2.driver负责处理返回的rdd数据集，进行二次处理后存储
        :param opt: 
        :param config: 
        :param rdds: 
        :param parse_data: 
        """
        super(BOPSStrategy, self).__init__()

        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data

        self.es_index = "ssc-business_monitor_log-strategy-{}"

        # 常用变量
        self.last_lf_online_count = 0

    def main_strategy(self):
        """
        main函数,负责
        :return: 
        """
        # 过滤；解析
        strategy_res = self.parse_data.filter(lambda info: info['type'] in strategy_type_monitor).map(self.process_msg)
        # 生成汇总数据；汇总；解包
        strategy_count = strategy_res.flatMap(self.get_kv).reduceByKey(self.handle_monitor).map(lambda x: [x[0], x[1]])

        def strategy_handle(rdd_time, rdd):
            strategy_list = rdd.collect()
            if strategy_list:
                # 生成数据
                datas = self.get_strategy_data(strategy_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "strategy")

        self.rdds.append((strategy_count, strategy_handle))

        return self.rdds

    @staticmethod
    def process_msg(info):
        # 格式化处理message
        message = info['message']
        monitor = {}
        for mes in message.split('\x1f'):
            key_value = mes.split('=')
            if key_value[0] in strategy_type_monitor['p2p_courier_monitor']:
                monitor[key_value[0]] = int(key_value[1])
            elif key_value[0] in strategy_type_monitor['p2p_stun_monitor']:
                monitor[key_value[0]] = int(key_value[1])
            elif key_value[0] in strategy_type_monitor['p2p_tracker_go_monitor']:
                monitor[key_value[0]] = int(key_value[1])
            elif key_value[0] in strategy_type_monitor['platform_kafka_flume_monitor']:
                monitor[key_value[0]] = int(key_value[1])
            elif key_value[0] in strategy_type_monitor['p2p_strategy_monitor']:
                monitor[key_value[0]] = int(key_value[1])
            elif key_value[0] in strategy_type_monitor['p2p_channel_monitor']:
                monitor[key_value[0]] = int(key_value[1])
        info['monitor'] = monitor
        return info

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info['monitor']
        for mon in monitor:
            kv_list.append(('{}&{}&{}'.format(info['type'], info.get('fields', {}).get('ip', 'no_ip'), mon),
                            {"type": info['type'],
                             'value': monitor[mon]}))
        return kv_list

    @staticmethod
    def handle_monitor(x, y):
        value = x['value'] + y['value']
        return {"type": x['type'], 'value': value}

    def pull_down(self, long_list):
        # 拆成 类型，hostip，指标和value
        types = long_list[0].split('&')
        return types[0], types[1], types[2], long_list[1]['value']

    def get_strategy_data(self, type_list, rdd_time):
        data = {}
        rdd_time -= datetime.timedelta(hours=8)
        for a_list in type_list:
            s_type, host_ip, index, val = self.pull_down(a_list)
            if s_type not in data:
                data[s_type] = {index: {'value': val, 'host_ip': {host_ip: val}}}
            elif index not in data[s_type]:
                data[s_type][index] = {'value': val, 'host_ip': {host_ip: val}}
            elif host_ip not in data[s_type][index]['host_ip']:
                data[s_type][index]['value'] += val
                data[s_type][index]['host_ip'][host_ip] = val
            else:
                data[s_type][index]['value'] += val
                data[s_type][index]['host_ip'][host_ip] += val

        # 补全信息
        for a_type in strategy_type_monitor:
            if a_type not in data:
                data[a_type] = {}
            for a_key in strategy_type_monitor[a_type]:
                if a_key not in data[a_type]:
                    data[a_type][a_key] = {"value": 0, "host_ip": {}}

        body = {
            'monitor': data,
            'monitor_value': {'lf_strategy_increment': data['p2p_strategy_monitor']['lf_to_add']['value'] +
                                                       data['p2p_channel_monitor']['lfCount']['value'] -
                                                       data['p2p_strategy_monitor']['lf_to_delete']['value'],
                              'lf_online_increment': data['p2p_strategy_monitor']['topic_count']['value'] - self.last_lf_online_count},
            '@timestamp': rdd_time,
            "@version": "1",
        }
        self.last_lf_online_count = data['p2p_strategy_monitor']['topic_count']['value']

        datas = [body]

        return datas


class CountTab(object):
    def __init__(self, opt, config, rdds, parse_data):
        super(CountTab, self).__init__()

        self.opt = opt
        self.config = config
        self.rdds = rdds
        self.parse_data = parse_data
        self.es_index = "ssc-business_monitor_log-status_code-{}"

    def main_count(self):
        # 过滤；解析
        tab_res = self.parse_data.filter(lambda info: info['type'] in server_status_count).map(self.count_msg)
        # 生成汇总数据；汇总；解包
        tab_count = tab_res.flatMap(self.get_kv).reduceByKey(self.handle_monitor).map(lambda x: [x[0], x[1]])

        # tab_count

        def strategy_handle(rdd_time, rdd):
            strategy_list = rdd.collect()
            if strategy_list:
                # 生成数据
                datas = self.get_count_data(strategy_list, rdd_time)
                # 存到es中
                index = self.es_index.format(rdd_time.strftime("%Y.%m.%d"))
                send_es(self.config, index, datas, 'logs', "strategy")

        self.rdds.append((tab_count, strategy_handle))

        return self.rdds

    @staticmethod
    def count_msg(info):
        # 格式化处理message
        message = info['message']
        monitor = {}
        for codes in re.findall(server_status_count[info['type']], message):
            code = codes.split('=')
            if code[0] in monitor:
                monitor[code[0]] += int(code[1])
            else:
                monitor[code[0]] = int(code[1])
        info['monitor'] = monitor
        return info

    @staticmethod
    def get_kv(info):
        kv_list = []
        monitor = info['monitor']
        for mon in monitor:
            kv_list.append(('{}&{}&{}'.format(info['type'], info.get('fields', {}).get('ip', 'no_ip'), mon),
                            {"type": info['type'],
                             'value': monitor[mon]}))
        return kv_list

    @staticmethod
    def handle_monitor(x, y):
        value = x['value'] + y['value']
        return {"type": x['type'], 'value': value}

    def pull_down(self, long_list):
        # 拆成 类型，hostip，code和value
        types = long_list[0].split('&')
        return types[0], types[1], types[2], long_list[1]['value']

    def get_count_data(self, type_list, rdd_time):
        data = {}
        rdd_time -= datetime.timedelta(hours=8)
        for a_list in type_list:
            s_type, host_ip, code, val = self.pull_down(a_list)
            if s_type not in data:
                data[s_type] = {code: {'value': val, 'host_ip': {host_ip: val}}}
            elif code not in data[s_type]:
                data[s_type][code] = {'value': val, 'host_ip': {host_ip: val}}
            elif host_ip not in data[s_type][code]['host_ip']:
                data[s_type][code]['value'] += val
                data[s_type][code]['host_ip'][host_ip] = val
            else:
                data[s_type][code]['value'] += val
                data[s_type][code]['host_ip'][host_ip] += val
        datas = []
        for a_type in data:
            for a_code in data[a_type]:
                datas.append({
                    'monitor': {a_type: dict({'code': a_code}, **data[a_type][a_code])},
                    '@timestamp': rdd_time,
                    "@version": "1",
                })

        return datas

