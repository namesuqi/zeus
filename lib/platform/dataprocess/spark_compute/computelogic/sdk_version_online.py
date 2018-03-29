import os
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class SdkVersionOnline(object):

    def compute(self, partition_time=''):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/peer_info.txt', 'r') as origin_file:
            origin_lines = origin_file.readlines()
        result_list = dict()
        for line in origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            sdk_version = line_list[6].split('=')[1]

            if partition_time == '':
                if long(TimestampConversion.get_timestamp(test_day + '00')) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(test_day + '24')):
                    if sdk_version not in result_list:
                        result_list[sdk_version] = 1
                    else:
                        result_list[sdk_version] += 1
            elif partition_time != '' and len(partition_time) == 8:
                if long(TimestampConversion.get_timestamp(partition_time + '00')) <= long(timestamp) < long(
                        TimestampConversion.get_timestamp(partition_time + '24')):
                    if sdk_version not in result_list:
                        result_list[sdk_version] = 1
                    else:
                        result_list[sdk_version] += 1
            else:
                raise Exception('Input partition time length should be 8!')

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/SdkVersionOnline_exp.txt', "w") as expect_file:
            for version, count in result_list.items():
                expect_file.write('%s,%d\n' % (version, count))


if __name__ == '__main__':
    dm = SdkVersionOnline()
    dm.compute('20160825')
