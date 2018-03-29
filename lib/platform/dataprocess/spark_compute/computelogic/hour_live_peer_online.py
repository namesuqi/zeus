import os
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class HourLivePeerOnline(object):

    def compute(self, partition_time=''):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/live_progress.txt', 'r') as origin_file:
            origin_lines = origin_file.readlines()
        result_list = dict()
        peer_id_list = list()

        for line in origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            peer_id = line_list[5].split('=')[1]
            if partition_time == '':
                if long(TimestampConversion.get_timestamp(test_day + now_hour)) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(test_day + str(int(now_hour) + 1))):
                    if peer_id not in peer_id_list:
                        peer_id_list.append(peer_id)
            if partition_time != '' and len(partition_time) == 10:
                if long(TimestampConversion.get_timestamp(partition_time)) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(str(int(partition_time) + 1))):
                    if peer_id not in peer_id_list:
                        peer_id_list.append(peer_id)
        for item in peer_id_list:
            prefix = item[0:8]
            if prefix not in result_list:
                result_list[prefix] = 1
            else:
                result_list[prefix] += 1
        for key in result_list.keys():
            if 'all' not in result_list:
                result_list['all'] = 0
            result_list['all'] = result_list['all'] + result_list[key]

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/HourLivePeerOnline_exp.txt',
                  "w") as expect_file:
            for prefix, value in result_list.items():
                expect_file.write('%s,%d\n' % (prefix, value))

if __name__ == '__main__':
    dm = HourLivePeerOnline()
    dm.compute('2016082611')
