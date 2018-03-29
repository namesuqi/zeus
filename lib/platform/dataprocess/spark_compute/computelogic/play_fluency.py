import os

from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class PlayFluency(object):

    def compute(self, partition_time=''):

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/qos_buffering_count.txt', 'r') as origin_file:
            buffer_origin_lines = origin_file.readlines()
        buffer_count = dict()

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/bd_flow.txt', 'r') as origin_file:
            bd_origin_lines = origin_file.readlines()
        tenant_count = dict()

        for line in buffer_origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            peer_id = line_list[3].split('=')[1]
            prefix = peer_id[0:8]
            if partition_time == '':
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(test_day + now_hour + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(
                        test_day + now_hour + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in buffer_count:
                            buffer_count[five_minute_start] = dict()
                        if prefix not in buffer_count[five_minute_start]:
                            buffer_count[five_minute_start][prefix] = set()
                        buffer_count[five_minute_start][prefix].add(peer_id)
            elif partition_time != '' and len(partition_time) == 10:
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in buffer_count:
                            buffer_count[five_minute_start] = dict()
                        if prefix not in buffer_count[five_minute_start]:
                            buffer_count[five_minute_start][prefix] = set()
                        buffer_count[five_minute_start][prefix].add(peer_id)
            else:
                raise Exception('Input partition time length should be 10 or null!')

        for line in bd_origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            peer_id = line_list[3].split('=')[1]
            prefix = peer_id[0:8]
            if partition_time == '':
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(test_day + now_hour + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(
                        test_day + now_hour + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in tenant_count:
                            tenant_count[five_minute_start] = dict()
                        if prefix not in tenant_count[five_minute_start]:
                            tenant_count[five_minute_start][prefix] = set()
                        tenant_count[five_minute_start][prefix].add(peer_id)
            elif partition_time != '' and len(partition_time) == 10:
                for i in range(12):
                    five_minute_start = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * i))
                    five_minute_end = TimestampConversion.get_timestamp(partition_time + '{:0>2}'.format(5 * (i + 1)))
                    if long(five_minute_start) <= long(timestamp) < long(five_minute_end):
                        if five_minute_start not in tenant_count:
                            tenant_count[five_minute_start] = dict()
                        if prefix not in tenant_count[five_minute_start]:
                            tenant_count[five_minute_start][prefix] = set()
                        tenant_count[five_minute_start][prefix].add(peer_id)
            else:
                raise Exception('Input partition time length should be 10 or null!')

        print tenant_count
        print buffer_count

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/play_fluency.txt', "w") as expect_file:

            for timestamp in tenant_count.keys():
                for pre_peer in tenant_count[timestamp].keys():
                    if pre_peer not in buffer_count[timestamp]:
                        expect_file.write('%s,%s,%s,%d\n' % (pre_peer, timestamp, 'buffer:buffer_cnt',
                                                             len(buffer_count[timestamp][pre_peer])))
                        expect_file.write('%s,%s,%s,%d\n' % (pre_peer, timestamp, 'buffer:tenant_cnt',
                                                             len(tenant_count[timestamp][pre_peer])))
                        expect_file.write('%s,%s,%s,%f\n' % (pre_peer, timestamp, 'buffer:fluency', float(1)))
                    else:
                        expect_file.write('%s,%s,%s,%d\n' % (pre_peer, timestamp, 'buffer:buffer_cnt',
                                                             len(buffer_count[timestamp][pre_peer])))
                        expect_file.write('%s,%s,%s,%d\n' % (pre_peer, timestamp, 'buffer:tenant_cnt',
                                                             len(tenant_count[timestamp][pre_peer])))
                        expect_file.write('%s,%s,%s,%f\n' % (pre_peer, timestamp, 'buffer:fluency',
                                                             1-(float(len(buffer_count[timestamp][pre_peer])) /
                                                                float(len(tenant_count[timestamp][pre_peer])))
                                                             )
                                          )

if __name__ == '__main__':
    eg = PlayFluency()
    eg.compute(partition_time='2016091419')
