import os
import random

from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import TimestampConversion
from lib.platform.dataprocess.spark_compute.test_data import *


class SeedFlow(object):

    def make_data(self, hour=''):
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/seed_flow.txt', 'w') as writer:
            if hour == '':
                for hour in range(24):
                    for minute in range(60):
                        topic = "topic=" + "seed_flow"
                        public_ip = 'public_ip=' + '10.5.100.1'
                        sdk_agent_name = 'sdk_agent_name=' + 'YunshangSDK'
                        sdk_agent_version = 'sdk_agent_version=' + test_sdk_version[random.randint(0, len(test_sdk_version) - 1)]
                        timestamp = 'timestamp=' + str(
                                TimestampConversion.get_timestamp(test_day + '{:0>2}'.format(hour) + '%02d' % minute))
                        id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                                random.randint(1000, 1000000))
                        peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                        file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                        file_type = 'file_type=' + 'live'
                        upload = 'upload=' + str(random.randint(100000, 900000))
                        download = 'download=' + str(random.randint(500000, 1000000))

                        writer.write(data_format % (topic, public_ip, sdk_agent_name, sdk_agent_version, timestamp, id,
                                                        peer_id, file_id, file_type, upload, download))
            else:
                for minute in range(60):
                    topic = "topic=" + "seed_flow"
                    public_ip = 'public_ip=' + '10.5.100.1'
                    sdk_agent_name = 'sdk_agent_name=' + 'YunshangSDK'
                    sdk_agent_version = 'sdk_agent_version=' + test_sdk_version[
                        random.randint(0, len(test_sdk_version) - 1)]
                    timestamp = 'timestamp=' + str(
                        TimestampConversion.get_timestamp(test_day + '{:0>2}'.format(hour) + '%02d' % minute))
                    id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                        random.randint(1000, 1000000))
                    peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                    file_id = 'file_id=' + test_file_id[random.randint(0, len(test_file_id) - 1)]
                    file_type = 'file_type=' + 'live'
                    upload = 'upload=' + str(random.randint(100000, 900000))
                    download = 'download=' + str(random.randint(500000, 1000000))

                    writer.write(data_format % (topic, public_ip, sdk_agent_name, sdk_agent_version, timestamp, id,
                                                peer_id, file_id, file_type, upload, download))
if __name__ == '__main__':
    eg = SeedFlow()
    eg.make_data(15)
