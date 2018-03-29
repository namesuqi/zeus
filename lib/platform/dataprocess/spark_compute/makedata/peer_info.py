from lib.platform.dataprocess.spark_compute.test_data import *
from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
import random
import os


class PeerInfo(object):

    def make_data(self, hour=''):
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/peer_info.txt', 'w') as writer:
            if hour == '':
                for hour in range(24):
                    for minute in range(60):
                        topic = 'topic=' + 'peer_info'
                        id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                            random.randint(1000, 1000000))
                        timestamp = 'timestamp=' + str(
                            TimestampConversion.get_timestamp(test_day + '%02d' % hour + '%02d' % minute))
                        input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                        output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 600)
                        peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                        sdk_version = 'sdk_version=' + test_sdk_version[random.randint(0, len(test_sdk_version) - 1)]
                        nat_type = 'nat_type=' + str(random.randint(1, 4))
                        public_ip = 'public_ip=' + '10.5.100.1'
                        public_port = 'public_port=' + '8888'
                        private_ip = 'private_ip=' + '192.168.1.110'
                        private_port = 'private_port=' + '8080'
                        macs = 'macs=' + '9C-5C-8E-87-6A-25'


                        writer.write(data_format % (topic, id, timestamp, input_time, output_time, peer_id, sdk_version,
                                                    nat_type, public_ip, public_port, private_ip, private_port, macs))
            else:
                for minute in range(60):
                    topic = 'topic=' + 'peer_info'
                    id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                        random.randint(1000, 1000000))
                    timestamp = 'timestamp=' + str(
                        TimestampConversion.get_timestamp("20160823" + '{:0>2}'.format(hour) + '%02d' % minute))
                    input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                    output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 600)
                    peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                    sdk_version = 'sdk_version=' + test_sdk_version[random.randint(0, len(test_sdk_version) - 1)]
                    nat_type = 'nat_type=' + str(random.randint(1, 4))
                    public_ip = 'public_ip=' + '10.5.100.1'
                    public_port = 'public_port=' + '8888'
                    private_ip = 'private_ip=' + '192.168.1.110'
                    private_port = 'private_port=' + '8080'
                    macs = 'macs=' + '9C-5C-8E-87-6A-25'

                    writer.write(data_format % (topic, id, timestamp, input_time, output_time, peer_id, sdk_version,
                                                nat_type, public_ip, public_port, private_ip, private_port, macs))

if __name__ == '__main__':
    pi = PeerInfo()
    pi.make_data('6')
