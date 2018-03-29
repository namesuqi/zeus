import os
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class FiveMinuteAverageLiveDelay(object):
    def compute(self, partition_time=''):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/live_delay.txt', 'r') as origin_file:
            origin_lines = origin_file.readlines()
        result_list = dict()

        for line in origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            prefix = line_list[5].split('=')[1][0:8]
            delay = line_list[-1].split('=')[1].replace('\n', '')

            if partition_time == '':
                if long(TimestampConversion.get_timestamp(test_day + now_hour)) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(test_day + str(int(now_hour) + 1))):
                    if prefix not in result_list:
                        result_list[prefix] = dict()
                    for i in range(12):
                        five_minute_start = TimestampConversion.get_timestamp(test_day + now_hour + '{:0>2}'.format(5 * i))
                        five_minute_end = TimestampConversion.get_timestamp(test_day + now_hour + '{:0>2}'.format(5 * (i + 1)))
                        if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                            if five_minute_start not in result_list[prefix]:
                                result_list[prefix][five_minute_start] = list()
                            result_list[prefix][five_minute_start].append(int(delay))

            elif partition_time != '' and len(partition_time) == 10:
                if long(TimestampConversion.get_timestamp(partition_time)) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(str(int(partition_time) + 1))):
                    if prefix not in result_list:
                        result_list[prefix] = dict()
                    for i in range(12):
                        five_minute_start = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * i))
                        five_minute_end = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * (i + 1)))
                        if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                            if five_minute_start not in result_list[prefix]:
                                result_list[prefix][five_minute_start] = list()
                            result_list[prefix][five_minute_start].append(int(delay))

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/FiveMinuteAverageLiveDelay_exp.txt',
                  "w") as expect_file:
            for pre in result_list.keys():
                for time_index, values in result_list[pre].items():
                    if len(values) != 0:
                        average_delay = float(sum(values))/len(values)
                    else:
                        average_delay = 0
                    expect_file.write('%s,%s,%f\n' % (pre, time_index, average_delay))

if __name__ == '__main__':
    dm = FiveMinuteAverageLiveDelay()
    dm.compute('2016082418')
