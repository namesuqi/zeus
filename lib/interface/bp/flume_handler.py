# coding=utf-8
"""

将log写入服务器中, kafka-flume采集后传入kafka, 对kafka中的数据进行校验
__author__ = 'liwenxuan'

"""

import paramiko
import os
import json
import requests
import time
from random import choice
from lib.database.schema_handler import get_latest_schema_info
from lib.decorator.trace import print_trace


@print_trace
def list_to_dict(data_list):
    # list形式如["key1=value1", "key2=value2",...]转成{key1:value1, key2:value2,...}
    data_dict = {}
    data_list = list(data_list)
    for i in data_list:
        k_v = i.split("=", 1)
        data_dict[k_v[0]] = k_v[1].replace('"', '')
    return data_dict


@print_trace
def dict_to_list(data_dict):
    # 将dict转成list形式如["key1=value1", "key2=value2",...]
    data_list = []
    for k, v in data_dict.items():
        data_list.append(str(k) + "=" + str(v))
    return data_list


@print_trace
def set_schema(topic, host, port):
    # 自定义schema格式

    schema = open(os.path.abspath(os.path.dirname(__file__)) + "/../avro_schema/" + topic + ".avsc").read()
    print schema

    headers = {"Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json",
               "Connection": "close",
               "Content-Type": "application/vnd.schemaregistry.v1+json"}
    schema_data = {"schema": schema}

    r = requests.post("http://%s:%s/subjects/%s-value/versions" % (host, str(port), topic),
                      headers=headers, data=json.dumps(schema_data))
    print r.text
    return requests.get("http://%s:%s/subjects/%s-value/versions" % (host, str(port), topic)).text


@print_trace
def schema_default(schema_host, schema_port, topic):
    # 将schema中有默认值的项作为dict传出

    # schema = open(os.path.abspath(os.path.dirname(__file__)) + "/../avro_schema/" + topic + ".avsc", "r")
    schema = get_latest_schema_info(schema_host, schema_port, topic)[0]
    # schema.seek(0)
    data_dict = {}
    for i in schema:
        line = i.strip()
        if line.__contains__('default'):
            if line.endswith(","):
                d = eval(line[:-1])
                data_dict[d["name"]] = d["default"]
                # l.append(str(d["name"] + "=" + str(d["default"])))
            else:
                d = eval(line[0:])
                data_dict[d["name"]] = d["default"]
                # l.append(str(d["name"] + "=" + str(d["default"])))
    # schema.close()
    return data_dict


@print_trace
def kafka_flume_ok(topic, keyword, log_path, flumehost, username, password):
    # 验证写入有效log时, kafka收到的数据正确
    # eg = SimpleKafkaClient(topic)
    # eg.consumer()
    prepare = kafka_consumer(KAFKA_HOST, SCHEMA_HOST, SCHEMA_PORT, topic, consumer_group="flume_test_group")
    print len(prepare)
    time.sleep(5)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flumehost,  username=username, password=password)

    # 将topic_data中准备的log写入kafka
    f = open(os.path.abspath(os.path.dirname(__file__)) + "/topic_data/ok_" + topic + ".log", 'r')
    # f.seek(0)
    logs = []
    logs_count = f.readline()
    for i in f.readlines():
        if i.startswith("topic="):
            i = i.strip()
            ssh.exec_command('echo "{0}" >> {1}{2}'.format(i, log_path, choice([1, 2, 3])))
            time.sleep(1)
            log = i.split("\x1f")
            logs.append(log)
    f.close()
    ssh.close()

    # 获取kafka中的log
    kafka_logs_all_info = kafka_consumer(KAFKA_HOST, SCHEMA_HOST, SCHEMA_PORT, topic, consumer_group="flume_test_group")
    kafka_logs = []
    for kafka_log_info in kafka_logs_all_info:
        kafka_logs.append(kafka_log_info[2])
    kafka_logs_count = len(kafka_logs)

    # 判断kafka收到的数据是否正确
    # wrong_log = {}
    # kafka_log_keyword_list = []

    default_n = schema_default(topic)
    # kafka返回的logs是乱序的, 而我们给flume的logs是有序的, 为了方便比较需要先按关键字的值进行排序
    kafka_logs_sort = sorted(kafka_logs, key=lambda kafka_log: kafka_log[keyword])
    result = 0
    for i in range(len(kafka_logs)):
        find_match = list_to_dict(logs[i])
        for k, v in kafka_logs_sort[i].iteritems():
            # print k, v
            if str(v) in (str(find_match.get(k)), str(default_n.get(k))):
                result += 0
            else:
                print "-------------------------------"
                print keyword, ":", kafka_logs[i][keyword], ", different:", str(v)
                result += 1

    if int(logs_count) != kafka_logs_count:
        print "results must be wrong"
        print "kafka gets", kafka_logs_count, "logs"
        return False
    else:
        if result == 0:
            return True
        else:
            return False

        # data_log = dict_to_list(find_match)
        # for j in range(kafka_logs_count-i):
        #     # 匹配对应的log并检验
        #     if find_match[keyword] == kafka_logs[j][keyword]:
        #         k_log = kafka_logs.pop(j)
        #         kafka_log = dict_to_list(k_log)
        #         value = list(set(kafka_log).intersection(set(data_log)))
        #         for x in value:
        #             kafka_log.remove(x)
        #         default = list(set(kafka_log).intersection(set(schema_default(topic))))
        #         print keyword, "=", find_match[keyword], "has", len(default), "default"
        #         for y in default:
        #             kafka_log.remove(y)
        #         if len(kafka_log) != 0:
        #             wrong_log[i+1] = kafka_log
        #         break
        #     else:
        #         kafka_log_keyword_list.append(find_match[keyword])
        #         break

    # 判断flume发送的和kafka收到的log数量是否一致
    # if int(logs_count) != kafka_logs_count:
    #     print "results must be wrong"
    #     print "kafka gets", kafka_logs_count, "logs"
    #     print "kafka does not get ", keyword, ":", kafka_log_keyword_list
    #     print "wrong logs:", wrong_log
    #     return False
    # else:
    #     if len(wrong_log) == 0:
    #         return True
    #     else:
    #         print len(wrong_log), "wrong logs"
    #         print "wrong logs:", wrong_log
    #         return False


@print_trace
def kafka_flume_invalid(topic, log_path, flumehost, username, password):
    # 验证写入无效log时, kafka不会收到数据
    # eg = SimpleKafkaClient(topic)
    # eg.consumer()
    prepare = kafka_consumer(KAFKA_HOST, SCHEMA_HOST, SCHEMA_PORT, topic, consumer_group="flume_test_group")
    print len(prepare)
    time.sleep(5)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(flumehost, username=username, password=password)

    f = open(os.path.abspath(os.path.dirname(__file__)) + "/topic_data/invalid_" + topic + ".log", 'r')
    # f.seek(0)
    logs = f.readlines()
    for i in logs:
        i = i.strip()
        ssh.exec_command('echo "{0}" >> {1}{2}'.format(i, log_path, choice([1, 2, 3])))
        time.sleep(1)
    f.close()
    ssh.close()

    # 获取kafka中的log
    kafka_logs_all_info = kafka_consumer(KAFKA_HOST, SCHEMA_HOST, SCHEMA_PORT, topic, consumer_group="flume_test_group")
    kafka_logs = []
    for kafka_log_info in kafka_logs_all_info:
        kafka_logs.append(kafka_log_info[2])

    if len(kafka_logs) == 1:
        return True
    else:
        print kafka_logs
        return False


@print_trace
def judge_kafka_logs_info(write_logs, kafka_logs_all_info, default_info, topic, keyword):
    """

    :param write_logs:
    :param kafka_logs_all_info:
    :param default_info:
    :param topic:
    :param keyword:
    :return:
    """
    kafka_logs = []
    for kafka_log_info in kafka_logs_all_info:
        kafka_logs.append(kafka_log_info[2])
    kafka_logs_count = len(kafka_logs)

    write_kafka_logs = []
    for i in range(len(write_logs)):
        if "topic={0}".format(topic) in str(write_logs[i]):
            write_kafka_logs.append(write_logs[i])

    # kafka返回的logs是乱序的, 而我们给flume的logs是有序的, 为了方便比较需要先按关键字的值进行排序
    kafka_logs_sort = sorted(kafka_logs, key=lambda kafka_log: kafka_log[keyword])
    result = 0
    for i in range(len(kafka_logs)):
        print write_kafka_logs[i]
        find_match = list_to_dict(write_kafka_logs[i])
        for k, v in kafka_logs_sort[i].iteritems():
            # print k, v
            if str(v) in (str(find_match.get(k)), str(default_info.get(k))):
                result += 0
            else:
                print "-------------------------------"
                print keyword, ":", kafka_logs[i][keyword], ", different:", str(v)
                result += 1

    if int(len(write_kafka_logs)) != kafka_logs_count:
        print "results must be wrong"
        print "kafka gets", kafka_logs_count, "logs"
        return False
    else:
        if result == 0:
            return True
        else:
            return False


@print_trace
def judge_logs_partition(kafka_logs):
    """
    判断同一peer_id的所有log是否写入到同一partition中
    :param kafka_logs: [[partition, offset, msg.value],...]
    :return:
    """
    result = 0

    if kafka_logs[0][2].has_key("peer_id"):
        pid_list = []  # 存放所有log中的peer_id
        for log in kafka_logs:
            pid_list.append(log[2]["peer_id"])
        pid_unique_list = list(set(pid_list))  # 对peer_id去重
        for pid in pid_unique_list:
            partition_list = [x[0] for x in kafka_logs if x[2]["peer_id"] == pid]
            # 筛选该peer_id的所有log对应的partition
            partition_unique_list = list(set(partition_list))  # partition去重
            # print "peer_id:", pid, "; partition:", partition_list
            if len(partition_unique_list) == 1:  # 判断该peer_id对应的log是否写入同一个partition
                pass
            elif len(partition_unique_list) == 0:
                print "Can't get %s logs partition" % pid
                result += 1
            else:
                print "Error !!! Too many partitions: %s" % partition_unique_list
                print "---peer_id:", pid, "; partition:", partition_list
                result += 1
    else:
        print "Logs field no peer_id para."
        print kafka_logs[0][2]
        pass
    if result == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    kafka_log = [{u'public_ip': u'116.231.167.180', u'province_id': u'0', u'macs': u'[{"name":"win0","addr":"74:D4:35:E5:F7:A1"}]',
                  u'os_version': u'XX', u'city_id': u'0', u'country': u'ZZ', u'public_port': 56659, u'nat_type': 1, u'private_port': 56659,
                  u'sdk_version': u'3.9.0', u'private_ip': u'192.168.1.2', u'isp_id': u'0\r', u'timestamp': 1500000000021L, u'os_type': None,
                  u'peer_id': u'0000000012345123451234512345ABCD', u'cpu': u'XX'},
                 {u'public_ip': u'116.231.167.180', u'province_id': u'0', u'macs': u'[{"name":"win0","addr":"74:D4:35:E5:F7:A1"}]',
                  u'os_version': u'XX', u'city_id': u'0', u'country': None, u'public_port': 56659, u'nat_type': 1, u'private_port': 56659,
                  u'sdk_version': u'3.9.0', u'private_ip': u'192.168.1.2', u'isp_id': u'0\r', u'timestamp': 1500000000024L, u'os_type': u'live',
                  u'peer_id': u'0000000012345123451234512345ABCD', u'cpu': u'XX'}, "..."]

    # print kafka_flume_ok("peer_info", "peer_id")
    # print kafka_flume_invalid("peer_info")

    # headers = {"Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json",
    #            "Connection": "close",
    #            "Content-Type": "application/vnd.schemaregistry.v1+json"}
    # #
    # r = requests.put("http://10.5.103.9:8081/config",
    #                   headers=headers, data='{"compatibility": "BACKWARD"}')
    # print r.text

    # for i in TOPIC_LIST:  # TEST_TOPIC_LIST
    #     print i, set_schema(i)
    #     r = requests.get("http://10.5.103.9:8081/subjects/%s-value/versions/latest" %(i))
    #     print r.text

    # set_schema("test1_heartbeat")
    # schema_default("peer_info")

    logs_list = [
        [1, 9, {u'peer_id': u'00000002FA7C478F8E04749178FE6208',
                u'cppc': 1,
                u'city_id': u'0'}],
        [5, 13, {u'peer_id': u'00000002FA7C478F8E04749178FE6207',
                 u'cppc': 1,
                 u'city_id': u'0'}],
        [6, 13, {u'peer_id': u'00000002FA7C478F8E04749178FE6208',
                 u'cppc': 1,
                 u'city_id': u'0'}],
        [6, 13, {u'peer_id': u'00000002FA7C478F8E04749178FE6208',
                 u'cppc': 1,
                 u'city_id': u'0'}],
        [5, 13, {u'peer_id': u'00000002FA7C478F8E04749178FE6206',
                 u'cppc': 1,
                 u'city_id': u'0'}]
                 ]
    # judge_logs_partition(logs_list)

