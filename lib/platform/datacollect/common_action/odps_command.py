import os
import lib.platform.datacollect.global_vars.server


def drop_odps_data(table_name):
    drop_partition = 'alter table %s drop if exists partition(recorddate=%s)' % (
        table_name, lib.platform.datacollect.global_vars.server.server_recorddate)
    commandlines = drop_partition
    exec_odps_commands('\"' + commandlines + '\"')


def download_data_from_odps(task_name, table_name, recorddate):

    file_path_name = os.path.dirname(__file__) + "/../data_file/real_data_file/%s.log" % task_name
    download_data = 'tunnel d %s/recorddate=%s %s' % (table_name, recorddate, file_path_name)
    commandlines = ';'.join((download_data,))
    # print commandlines
    exec_odps_commands('\"' + commandlines + '\"')


def exec_odps_commands(commandlines):
    java_command = 'java -jar %s %s' % (os.path.abspath(os.path.dirname(__file__)) +
                                        "/../../misc/ODPS/odps_helper.jar", commandlines)
    ret = os.system(java_command)
    return ret

if __name__ == '__main__':
    download_data_from_odps('server_peer_info', 'raw_input_peer_info', '20160501')
