from makedata.live_delay import *
from makedata.peer_info import *
from makedata.live_progress import *
import test_data
import time
from commontool.sftp_client import *
from commontool.ssh_client import *

'''
 download_flow_ext tadk
'''
# operate_hadoop.delete_hdfsdata_appoint_time(testdata.download_flow_ext['topicname'], testdata.now_year,
#                                             testdata.now_month, testdata.now_day, testdata.now_hour)
# operate_hadoop.delete_all_row_appoint_time('LiveTotalFlow', testdata.now_year, testdata.now_month
#                                            ,  testdata.now_day, testdata.now_hour)
#
# download_flow_ext.download_flow_ext_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file(testdata.download_flow_ext['origin_data_name'])
# time.sleep(15)
# operate_hadoop.run_spark()
#
# get_my_data.get_my_data(testdata.download_flow_ext['origin_data_name'])
# download_flow_make.download_flow_compute(testdata.now_hour)
#
# get_hbase_file.get_hbase_file('LiveTotalFlow', testdata.now_year, testdata.now_month, testdata.now_day, testdata.now_hour, testdata.download_flow_ext['columnname'], testdata.download_flow_ext['real_data_name'])
# get_hbase_file.change_file_format(testdata.download_flow_ext['real_data_name'])
#
# a = comparefile.compare('server_download_flow')
# print a
'''
 upload_flow_ext task
'''
# operate_hadoop.delete_hdfsdata_appoint_time(testdata.upload_flow_ext['topicname'], testdata.now_year,
#                                             testdata.now_month, testdata.now_day, testdata.now_hour)
# operate_hadoop.delete_all_row_appoint_time('LiveTotalFlow', testdata.now_year, testdata.now_month
#                                            ,  testdata.now_day, '17')

# upload_flow_ext.upload_flow_ext_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file(testdata.upload_flow_ext['origin_data_name'])
# time.sleep(15)
# operate_hadoop.run_spark()
#
# get_my_data.get_my_data(testdata.upload_flow_ext['origin_data_name'])
# upload_flow_make.upload_flow_compute(testdata.now_hour)
#
# get_hbase_file.get_hbase_file('LiveTotalFlow', testdata.now_year, testdata.now_month, testdata.now_day, testdata.now_hour, testdata.upload_flow_ext['columnname'], testdata.upload_flow_ext['real_data_name'])
# get_hbase_file.change_file_format(testdata.upload_flow_ext['real_data_name'])
#
# a = comparefile.compare('server_upload_flow')
# print a

'''
 download_flow task
'''
# download_flow.download_flow_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file('server_download_flow.txt')

'''
 upload_flow task
'''
# upload_flow.upload_flow_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file('server_upload_flow.txt')

'''
 add_tenant_domain task
'''
# add_tenant_domain.add_tenant_domain_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file('add_tenant_domain.txt')

'''
 add_tenant task
'''
# add_tenant.add_tenant_makedata(testdata.now_hour)
# put_hdfs_file.put_hdfs_file('add_tenant.txt')

'''
    INPUT DATA
'''
# data_obj = LiveDelay()
# file_name = 'peer_info.txt'



# file_name = 'live_delay.txt'
# file_name = 'live_progress.txt'
# file_name = 'download_flow.txt'
file_name = 'upload_flow.txt'
# file_name = 'bd_flow.txt'
# file_name = 'qos_buffering_count.txt'
# file_name = 'qos_startup.txt'
# file_name = 'heartbeat.txt'
# data_obj.make_data('17')

sftp = SFTPClient('10.6.2.5', 'admin', 'yzhxc9!')
sftp.upload('/home/admin/TestInput/' + file_name, os.path.abspath(os.path.dirname(__file__)) + '/makedata/' + file_name)

ssh = SSHClient('10.6.2.5', 'admin', 'yzhxc9!')
ssh.excute_command('cat /home/admin/TestInput/' + file_name + ' >> /home/admin/logs/funnel/report.log')

