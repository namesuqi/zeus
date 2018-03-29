import os
import random
from lib.platform.dataprocess.spark_compute.test_data import *
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *


class UploadFlow(object):

    def make_data(self, hour=''):
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/upload_flow.txt', 'w') as writer:
            if hour == '':
                for hour in range(24):
                    for minute in range(60):
                        topic = "topic=" + "upload_flow"
                        file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                        id = "id=" + file_id.split('=')[1] + ":" + str(random.randint(1000, 1000000))
                        timestamp = 'timestamp=' + str(
                            TimestampConversion.get_timestamp(test_day + '%02d' % hour + '%02d' % minute))
                        peer_id = 'peer_id=' + test_peer_id[random.randint(0, 9)]
                        upload = 'upload=' + str(random.randint(10000000, 100000000))
                        input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                        output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 5 * 60 * 1000)
                        public_ip = 'public_ip=' + '10.5.100.1'
                        play_type = 'play_type=' + test_file_type[random.randint(0, len(test_file_type) - 1)]
                        duration = 'null'
                        writer.write(data_format % (topic, id, timestamp, peer_id, upload, input_time, output_time, public_ip,
                                                    play_type))
            else:
                for minute in range(60):
                    topic = "topic=" + "upload_flow"
                    file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                    id = "id=" + file_id.split('=')[1] + ":" + str(random.randint(1000, 1000000))
                    timestamp = 'timestamp=' + str(
                        TimestampConversion.get_timestamp(test_day + '%02d' % hour + '%02d' % minute))
                    peer_id = 'peer_id=' + test_peer_id[random.randint(0, 9)]
                    upload = 'upload=' + str(random.randint(10000000, 100000000))
                    input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                    output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 5 * 60 * 1000)
                    public_ip = 'public_ip=' + '10.5.100.1'
                    play_type = 'play_type=' + test_file_type[random.randint(0, len(test_file_type) - 1)]
                    duration = 'null'
                    writer.write(data_format % (topic, id, timestamp, peer_id, upload, input_time, output_time, public_ip,
                                                play_type))


if __name__ == '__main__':
    pass
    eg = UploadFlow()
    eg.make_data(22)
