from lib.platform.dataprocess.spark_compute.test_data import *
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
import struct
import random
import os


class LiveProgress(object):

    def make_data(self, hour=''):
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/live_progress.txt', 'w') as writer:
            if hour == '':
                for hour in range(24):
                    for minute in range(60):
                        topic = 'topic=' + 'live_progress'
                        id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                            random.randint(1000, 1000000))
                        timestamp = 'timestamp=' + str(
                            TimestampConversion.get_timestamp(test_day + '{:0>2}'.format(hour) + '%02d' % minute))
                        input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                        output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 600)
                        peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                        file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                        chunk_id = 'chunk_id={}'.format(random.randint(1000, 99999))
                        public_ip = 'public_ip=' + '10.5.100.1'
                        writer.write(data_format % (topic, id, timestamp, input_time, output_time, peer_id, public_ip,
                                                    file_id, chunk_id))
            else:
                for minute in range(60):
                    topic = 'topic=' + 'live_progress'
                    id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                        random.randint(1000, 1000000))
                    timestamp = 'timestamp=' + str(
                        TimestampConversion.get_timestamp(test_day + '{:0>2}'.format(hour) + '%02d' % minute))
                    input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                    output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 600)
                    peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                    file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                    chunk_id = 'chunk_id={}'.format(random.randint(1000, 99999))
                    public_ip = 'public_ip=' + '10.5.100.1'
                    writer.write(data_format % (topic, id, timestamp, input_time, output_time, peer_id, public_ip,
                                                file_id, chunk_id))

if __name__ == '__main__':
    pi = LiveProgress()
    pi.make_data('11')
