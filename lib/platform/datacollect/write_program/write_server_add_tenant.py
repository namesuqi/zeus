import os
import random
from lib.platform.datacollect.common_action.get_timestamp import *
from lib.platform.datacollect.global_vars.server import *
from lib.platform.datacollect.common_action.read_file import *
from lib.platform.datacollect.global_vars.constant import *
import data_provider
import common_action.copy_file_to_remote
import common_action.remote_command_Win_to_Lin
import global_vars.server


class server_add_tenant(data_provider.DataProvider):
    def make_data(self):

        peer_ids = read_constant_file('peer_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_add_tenant.txt', 'w') as file_demand_data:
            for i in range(write_log_number):
                topic = "topic=" + "add_tenant"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                tenant_id = 'tenant_id=' + "testtenantid" + str(random.randint(1, 100000))
                tenant_name = 'tenant_name=' + "testusename"
                groups = 'groups=' + 'TG1'
                peer_prefix = 'peer_prefix=' + peer_ids[random.randint(0, 2500)][0:8]
                domain = 'domain=' + 'mail.Mytest.com'
                file_demand_data.write(data_format % (topic, timestamp, tenant_id, tenant_name, groups, peer_prefix,
                                                      domain))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_add_tenant.txt'

    def write_log(self):
        common_action.copy_file_to_remote.local_copy_file('server_add_tenant')
        time.sleep(2)
        common_action.remote_command_Win_to_Lin.start_writer_log('server_add_tenant')

    def clear_data(self):
        common_action.odps_command.drop_odps_data(global_vars.server.server_add_tenant['inputtable'])
        print 'data clear done'
