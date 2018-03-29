import os
import random

from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.commontool.create_hex_string import *
from lib.platform.dataprocess.spark_compute.test_data import *


class BDFlow(object):

    def make_data(self, hour=''):
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/bd_flow.txt', 'w') as writer:
            if hour == '':
                for hour in range(24):
                    for minute in range(60):
                        for i in range(random.randint(2, 4)):
                            topic = 'topic=' + 'bd_flow'
                            id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                                random.randint(1000, 1000000))
                            timestamp = 'timestamp=' + str(
                                TimestampConversion.get_timestamp(test_day + '%02d' % hour + '%02d' % minute))
                            # peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                            peer_id = 'peer_id=' + '00010026' + CreateHexString.create_by_length(24)
                            play_type = 'play_type=' + random.choice(['live', 'vod'])
                            url = 'url=' + 'http://testcloudtropy.com'
                            vvid = 'vvid=' + CreateHexString.create_by_length(32)
                            durtion = 'duration=' + str(random.randint(200, 2000))
                            download = 'download=' + str(random.randint(100000, 1000000))
                            public_ip = 'public_ip=' + '10.5.100.1'
                            input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                            sdk_agent_name = 'sdk_agent_name=' + 'YunshangSDk'
                            sdk_agent_version = 'sdk_agent_version=' + test_sdk_agent_version[
                                                                        random.randint(0, len(test_sdk_agent_version)-1)]

                            writer.write(data_format % (topic, id, timestamp, peer_id, play_type, url, vvid, durtion
                                                    , download, public_ip, input_time, sdk_agent_name,
                                                    sdk_agent_version))
            else:
                for minute in range(60):
                    for i in range(random.randint(2, 4)):
                        topic = 'topic=' + 'bd_flow'
                        id = "id=" + test_file_id[random.randint(0, len(test_file_id) - 1)] + ":" + str(
                            random.randint(1000, 1000000))
                        timestamp = 'timestamp=' + str(
                            TimestampConversion.get_timestamp(test_day + '%02d' % hour + '%02d' % minute))
                        # peer_id = 'peer_id=' + test_peer_id[random.randint(0, len(test_peer_id) - 1)]
                        peer_id = 'peer_id=' + '00010026' + CreateHexString.create_by_length(24)
                        play_type = 'play_type=' + random.choice(['live', 'vod'])
                        url = 'url=' + 'http://testcloudtropy.com'
                        vvid = 'vvid=' + CreateHexString.create_by_length(32)
                        durtion = 'duration=' + str(random.randint(200, 2000))
                        download = 'download=' + str(random.randint(100000, 1000000))
                        public_ip = 'public_ip=' + '10.5.100.1'
                        input_time = 'input_time=' + str(long(timestamp.split('=')[1]) + 300)
                        sdk_agent_name = 'sdk_agent_name=' + 'YunshangSDk'
                        sdk_agent_version = 'sdk_agent_version=' + test_sdk_agent_version[
                            random.randint(0, len(test_sdk_agent_version) - 1)]

                        writer.write(data_format % (topic, id, timestamp, peer_id, play_type, url, vvid, durtion
                                                , download, public_ip, input_time, sdk_agent_name,
                                                sdk_agent_version))

if __name__ == '__main__':
    qbc = BDFlow()
    qbc.make_data(16)
