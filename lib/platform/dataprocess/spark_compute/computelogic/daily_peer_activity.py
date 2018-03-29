import os
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *


class DailyPeerActivity(object):

    def compute(self, partition_time=''):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../tempfile/heartbeat.txt', 'r') as origin_file:
            origin_lines = origin_file.readlines()

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/DailyPeerActivity_exp.txt', "w") as expect_file:
            result_list = dict()
            peer_id_list = list()
            for line in origin_lines:
                _, time_stamp, _, _, peer_id, _, _, _, _, _, _ = line.split(',')
                if partition_time != '' and len(partition_time) == 8:
                    if long(time_stamp) <= long(TimestampConversion.get_timestamp(partition_time)) \
                            and peer_id not in peer_id_list:
                        prefix = peer_id[:8]
                        result_list[prefix] = result_list.setdefault(prefix, 0) + 1
                        peer_id_list.append(peer_id)
                else:
                    if peer_id not in peer_id_list:
                        prefix = peer_id[:8]
                        result_list[prefix] = result_list.setdefault(prefix, 0) + 1
                        peer_id_list.append(peer_id)
            total_count = 0
            for prefix, count in result_list.items():
                total_count += count
                expect_file.write('%s,%d\n' % (prefix, count))
            expect_file.write('%s,%d\n' % ('99999999', total_count))

        return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt" % __name__.split('.')[-1]

if __name__ == '__main__':
    dm = DailyPeerActivity()
    dm.compute('2016081011')
