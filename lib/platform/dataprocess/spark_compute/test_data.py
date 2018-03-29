import time

test_peer_id = ['00010026168E7B45BAE01DFD4C61FA9B', '000100269229554EA550CFB1E84858CB', '000000009A90A740B67B94D5D964E1CA', '00010026D9A1B54FAE718CC7AB0E83A9'
           , '00000000DE60B64ABFFEABE0CFE8A9E3', '00010026F3EFBA43AFFEDD937DEB2C20', '000100260054442AAE5F3D44FE013891'
           , '00000000006F4164AA87983E6AD436B4', '0001002600D0483C9B4E0CE3F047B3D3', '66666666012A4735A4E21D6FFA3B9CD2']
test_file_type = ['vod', 'hls', 'download', 'live_m3u8', 'live_ts', 'live_flv', 'null']


time_str = time.strftime("%Y%m%d%H", time.localtime())
test_day = time_str[0:8]
now_hour = time_str[-2:]
now_day = time_str[6:8]
now_month = time_str[4:6]
now_year = time_str[0:4]


test_file_id = ['35D0DA2954B34A8E8D9E8E8A23334DC5', '35D0DA2954B34A8E8D9E8E8A23334DC5', '35D0DA2954B34A8E8D9E8E8A23334DC5',
           '373DAEBFCFF94635BE744DA78A625C3C', '373DAEBFCFF94635BE744DA78A625C3C', '37776C7653854CB5B1FEF75F19157BAC',
           '37776C7653854CB5B1FEF75F19157BAC', '37776C7653854CB5B1FEF75F19157BAC', '378FB10C64F14DB2A44338515FBC2192',
           '378FB10C64F14DB2A44338515FBC2192']

download_flow_ext = {'origin_data_name': 'server_download_flow_ext.txt', 'real_data_name': 'server_download_flow_ext_REL', 'topicname': 'download_flow_ext'
                    , 'columnname': 'DownloadFlow'}

upload_flow_ext = {'origin_data_name': 'server_upload_flow_ext.txt', 'real_data_name': 'server_upload_flow_ext_REL', 'topicname': 'upload_flow_ext'
                   , 'columnname': 'UploadFlow'}

test_sdk_version = ('3.0.0', '3.0.1', '3.0.2', '3.1.0', '3.1.1', '2.4.0', '2.4.1', '2.4.6', '2.4.7', '2.4.8', '2.4.9',
               '2.4.10')

test_sdk_agent_version = ('03.00.00', '03.00.01', '03.00.02', '03.01.00', '03.01.01', '02.04.00', '02.04.01', '02.04.06',
                    '02.04.07', '02.04.08', '02.04.09', '02.04.10')

hadoop_ip = '10.5.100.46'
hadoop_username = 'root'
hadoop_password = 'Yunshang2014'
flume_ip = '10.6.2.5'
flume_username = 'admin'
flume_password = 'yzhxc9!'
