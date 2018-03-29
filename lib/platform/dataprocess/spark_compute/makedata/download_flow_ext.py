import os
import random

import lib.platform.datacollect.Action.GetTimeStamp as GetTimeStamp
import lib.platform.dataprocess.spark_compute.testdata as testdata

def download_flow_ext_makedata(hour ='00'):
    '''

    :param hour: the hour data need to created
    :return: data file, contain every minute's report data in the hour
    '''

    time_format = testdata.testday + "%02d%02d00"

    data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
    with open(os.path.abspath(os.path.dirname(__file__)) + '/server_download_flow_ext.txt', 'w') as filedemanddata:
        for i in range(60):
            topic = "topic=" + "download_flow_ext"
            file_id = 'file_id=' + testdata.file_id[random.randint(0, len(testdata.file_id)-1)]
            id = "id=" + file_id.split('=')[1] + ":" + str(random.randint(1000, 1000000))
            timestamp = 'timestamp=' + str(GetTimeStamp.get_timestamp(time_format % (int(hour), i)))
            # timestamp = 'timestamp=' + str(GetTimeStamp.get_timestamp_now())
            peer_id = 'peer_id=' + testdata.peer_id[random.randint(0, len(testdata.peer_id)-1)]
            p2p_download = 'p2p_download=' + str(random.randint(1000000, 100000000))
            cdn_download = 'cdn_download=' + str(random.randint(1000000, 100000000))
            output_time = 'output_time=' + str(long(timestamp.split('=')[1]) + 5*60*1000)
            public_ip = 'public_ip=' + '10.5.100.1'
            country = 'country=' + 'China'
            location = 'location=' + '10'
            isp = 'isp=' + '2222'
            peer_owner = 'peer_owner=' + 'ciwen'
            fsize = 'fsize=' + str(random.randint(100, 10000))
            play_type = 'play_type=' + testdata.file_type[random.randint(0, len(testdata.file_type)-1)]
            # play_type = 'play_type='

            filedemanddata.write(data_format % (topic, file_id, id, timestamp, peer_id, p2p_download, cdn_download,
                                                output_time, public_ip, country, location, isp, peer_owner, fsize,
                                                play_type))
    return os.path.abspath(os.path.dirname(__file__)) + '/server_download_flow_ext.txt'

if __name__ == '__main__':
    download_flow_ext_makedata()
