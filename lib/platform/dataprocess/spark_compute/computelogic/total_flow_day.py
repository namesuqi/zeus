import os

from lib.platform.dataprocess.spark_compute.commontool.timestamp_conversion import *
from lib.platform.dataprocess.spark_compute.test_data import *


class TotalFlowDay(object):

    def compute(self, partition_time=''):
        download_count = dict()
        all_download_count = dict()
        upload_count = dict()
        all_upload_count = dict()

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/download_flow.txt',
                  'r') as origin_file:
            download_origin_lines = origin_file.readlines()

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../makedata/upload_flow.txt',
                  'r') as origin_file:
            upload_origin_lines = origin_file.readlines()

        for line in download_origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[3].split('=')[1]
            peer_id = line_list[4].split('=')[1]
            prefix = peer_id[0:8]
            p2p_download = int(line_list[5].split('=')[1])
            cdn_download = int(line_list[6].split('=')[1])
            play_type = line_list[-2].split('=')[1]
            if play_type in ('vod', 'hls'):
                play_type = 'vod'
            elif play_type.startswith('live'):
                play_type = 'live'
            else:
                pass

            if partition_time == '':
                day_start = TimestampConversion.get_timestamp(test_day + '00')
                day_end = TimestampConversion.get_timestamp(test_day + '24')
                if long(day_start) <= long(timestamp) < long(day_end):
                    if day_start not in download_count:
                        download_count[day_start] = dict()
                    if prefix not in download_count[day_start]:
                        download_count[day_start][prefix] = dict()
                    if play_type not in download_count[day_start][prefix]:
                        download_count[day_start][prefix][play_type] = dict()
                        download_count[day_start][prefix][play_type]['cdn_download'] = 0
                        download_count[day_start][prefix][play_type]['p2p_download'] = 0
                    download_count[day_start][prefix][play_type]['cdn_download'] += cdn_download
                    download_count[day_start][prefix][play_type]['p2p_download'] += p2p_download
                    download_count[day_start][prefix][play_type]['total_download'] += (cdn_download + p2p_download)

            elif partition_time != '' and len(partition_time) == 8:
                day_start = TimestampConversion.get_timestamp(partition_time + '00')
                day_end = TimestampConversion.get_timestamp(partition_time + '24')
                if long(day_start) <= long(timestamp) < long(day_end):
                    if day_start not in download_count:
                        download_count[day_start] = dict()
                    if prefix not in download_count[day_start]:
                        download_count[day_start][prefix] = dict()
                    if play_type not in download_count[day_start][prefix]:
                        download_count[day_start][prefix][play_type] = dict()
                        download_count[day_start][prefix][play_type]['cdn_download'] = 0
                        download_count[day_start][prefix][play_type]['p2p_download'] = 0
                        download_count[day_start][prefix][play_type]['total_download'] = 0
                    if 'all' not in download_count[day_start][prefix]:
                        download_count[day_start][prefix]['all'] = dict()
                        download_count[day_start][prefix]['all']['cdn_download'] = 0
                        download_count[day_start][prefix]['all']['p2p_download'] = 0
                        download_count[day_start][prefix]['all']['total_download'] = 0
                    download_count[day_start][prefix][play_type]['cdn_download'] += cdn_download
                    download_count[day_start][prefix][play_type]['p2p_download'] += p2p_download
                    download_count[day_start][prefix][play_type]['total_download'] += (cdn_download + p2p_download)
                    download_count[day_start][prefix]['all']['cdn_download'] += cdn_download
                    download_count[day_start][prefix]['all']['p2p_download'] += p2p_download
                    download_count[day_start][prefix]['all']['total_download'] += (cdn_download + p2p_download)

            else:
                raise Exception('Input partition time length should be 8 or null!')

        for line in upload_origin_lines:
            line_list = line.split('\x1f')
            timestamp = line_list[2].split('=')[1]
            peer_id = line_list[3].split('=')[1]
            prefix = peer_id[0:8]
            upload = int(line_list[4].split('=')[1])

            if partition_time == '':
                day_start = TimestampConversion.get_timestamp(test_day + '00')
                day_end = TimestampConversion.get_timestamp(test_day + '24')
                if long(day_start) <= long(timestamp) < long(day_end):
                    if day_start not in upload_count:
                        upload_count[day_start] = dict()
                    if prefix not in upload_count[day_start]:
                        upload_count[day_start][prefix] = 0
                    upload_count[day_start][prefix] += upload

            elif partition_time != '' and len(partition_time) == 8:
                day_start = TimestampConversion.get_timestamp(partition_time + '00')
                day_end = TimestampConversion.get_timestamp(partition_time + '24')
                if long(day_start) <= long(timestamp) < long(day_end):
                    if day_start not in upload_count:
                        upload_count[day_start] = dict()
                    if prefix not in upload_count[day_start]:
                        upload_count[day_start][prefix] = 0
                    upload_count[day_start][prefix] += upload
            else:
                raise Exception('Input partition time length should be 8 or null!')

        for timestamp in download_count.keys():
            if timestamp not in all_download_count:
                all_download_count[timestamp] = dict()
            for user in download_count[timestamp].keys():
                if 'all' not in all_download_count[timestamp]:
                    all_download_count[timestamp]['all'] = dict()
                for play_type in download_count[timestamp][user].keys():
                    if play_type not in all_download_count[timestamp]['all']:
                        all_download_count[timestamp]['all'][play_type] = dict()
                        all_download_count[timestamp]['all'][play_type]['cdn_download'] = 0
                        all_download_count[timestamp]['all'][play_type]['p2p_download'] = 0
                        all_download_count[timestamp]['all'][play_type]['total_download'] = 0
                    all_download_count[timestamp]['all'][play_type]['cdn_download'] += \
                        download_count[timestamp][user][play_type]['cdn_download']
                    all_download_count[timestamp]['all'][play_type]['p2p_download'] += \
                        download_count[timestamp][user][play_type]['p2p_download']
                    all_download_count[timestamp]['all'][play_type]['total_download'] += (
                        download_count[timestamp][user][play_type]['cdn_download'] +
                        download_count[timestamp][user][play_type]['p2p_download'])

        for timestamp in upload_count.keys():
            if timestamp not in all_upload_count:
                all_upload_count[timestamp] = dict()
            for user in upload_count[timestamp].keys():
                if 'all' not in all_upload_count[timestamp]:
                    all_upload_count[timestamp]['all'] = 0
                all_upload_count[timestamp]['all'] += upload_count[timestamp][user]

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/total_flow_download.txt', "w") as download_expect_file:
            for timestamp in download_count.keys():
                for username in download_count[timestamp].keys():
                    for play_type in download_count[timestamp][username].keys():
                        download_expect_file.write('%s,%s,%s,download:cdn,%d\n' % (username, timestamp, play_type, download_count[timestamp][username][play_type]['cdn_download']))
                        download_expect_file.write('%s,%s,%s,download:p2p,%d\n' % (username, timestamp, play_type, download_count[timestamp][username][play_type]['p2p_download']))
                        download_expect_file.write('%s,%s,%s,download:total,%d\n' % (username, timestamp, play_type, download_count[timestamp][username][play_type]['total_download']))

            for timestamp in all_download_count.keys():
                for play_type in all_download_count[timestamp]['all'].keys():
                    download_expect_file.write('all,%s,%s,download:cdn,%d\n' % (timestamp, play_type, all_download_count[timestamp]['all'][play_type]['cdn_download']))
                    download_expect_file.write('all,%s,%s,download:p2p,%d\n' % (timestamp, play_type, all_download_count[timestamp]['all'][play_type]['p2p_download']))
                    download_expect_file.write('all,%s,%s,download:total,%d\n' % (timestamp, play_type, all_download_count[timestamp]['all'][play_type]['total_download']))

        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/total_flow_upload.txt', "w") as upload_expect_file:
            for timestamp in upload_count.keys():
                for username in upload_count[timestamp].keys():
                    upload_expect_file.write('%s,%s,upload:upload,%d\n' % (username, timestamp, upload_count[timestamp][username]))

            for timestamp in all_upload_count.keys():
                upload_expect_file.write('all,%s,upload:upload,%d\n' % (timestamp, all_upload_count[timestamp]['all']))


if __name__ == '__main__':
    eg = TotalFlowDay()
    eg.compute(partition_time='20161014')
