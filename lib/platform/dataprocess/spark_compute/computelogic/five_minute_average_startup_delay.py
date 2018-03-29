import os

from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class FiveMinuteAverageStartupDelay(object):

    def compute(self, partition_time=''):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/qos_startup.txt',
                  'r') as origin_file:
            origin_lines = origin_file.readlines()
        count_dict = dict()

        for line in origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            peer_id = line_list[3].split('=')[1]
            prefix = peer_id[0:8]
            play_type = line_list[4].split('=')[1]
            durtion = line_list[-1].replace('\n', '').split('=')[1]
            if partition_time == '':
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(test_day + now_hour + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(
                        test_day + now_hour + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in count_dict:
                            count_dict[five_minute_start] = dict()
                        if play_type not in count_dict[five_minute_start]:
                            count_dict[five_minute_start][play_type] = dict()
                        if prefix not in count_dict[five_minute_start][play_type]:
                            count_dict[five_minute_start][play_type][prefix] = dict()
                        if peer_id not in count_dict[five_minute_start][play_type][prefix]:
                            count_dict[five_minute_start][play_type][prefix][peer_id] = 0
                        count_dict[five_minute_start][play_type][prefix][peer_id] += int(durtion)
            else:
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in count_dict:
                            count_dict[five_minute_start] = dict()
                        if play_type not in count_dict[five_minute_start]:
                            count_dict[five_minute_start][play_type] = dict()
                        if prefix not in count_dict[five_minute_start][play_type]:
                            count_dict[five_minute_start][play_type][prefix] = dict()
                        if peer_id not in count_dict[five_minute_start][play_type][prefix]:
                            count_dict[five_minute_start][play_type][prefix][peer_id] = 0
                        count_dict[five_minute_start][play_type][prefix][peer_id] += int(durtion)

        all_count_dict = dict()

        with open(os.path.abspath(os.path.dirname(__file__)) +
                          '/../expectfile/five_minute_average_startup_delay.txt', "w") as expect_file:
            for timestamp in count_dict.keys():
                if timestamp not in all_count_dict:
                    all_count_dict[timestamp] = dict()
                    all_count_dict[timestamp]['all'] = dict()
                for type in count_dict[timestamp].keys():
                    for prefix in count_dict[timestamp][type].keys():
                        if prefix not in all_count_dict[timestamp]['all']:
                            all_count_dict[timestamp]['all'][prefix] = dict()
                        delay_sum = 0
                        for peer_id in count_dict[timestamp][type][prefix].keys():
                            delay_sum += count_dict[timestamp][type][prefix][peer_id]

                        expect_file.write('%s,%s,%s,buffer:delay,%f\n' % (prefix, timestamp, type, (
                            float(delay_sum)/float(len(count_dict[timestamp][type][prefix]))
                        )
                                                           )
                                          )
                        all_count_dict[timestamp]['all'][prefix][len(count_dict[timestamp][type][prefix])] = delay_sum
            for timestamp in all_count_dict.keys():
                for prefix in all_count_dict[timestamp]['all'].keys():
                    peer_sum = sum(peer_num for peer_num in all_count_dict[timestamp]['all'][prefix].keys())
                    all_delay_sum = sum(delay_num for delay_num in all_count_dict[timestamp]['all'][prefix].values())
                    expect_file.write('%s,%s,%s,buffer:delay,%f\n' % (prefix, timestamp, 'all', (
                        float(all_delay_sum) / float(peer_sum))
                    )
                                      )

if __name__ == '__main__':
    eg = FiveMinuteAverageStartupDelay()
    eg.compute(partition_time='2016091419')
