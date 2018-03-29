import os
import random
from lib.platform.datacollect.common_action.get_timestamp import *
from lib.platform.datacollect.global_vars.server import *
from lib.platform.datacollect.common_action.read_file import *
from lib.platform.datacollect.global_vars.constant import *
import data_provider
import Action.CopyFileToRemote
import Action.RemoteCommandWin2Lin
import GlobalVars.SERVER


class server_live_push_channel_count(data_provider.DataProvider):

    def make_data(self):

        fileids = ReadConstantFlie('file_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_live_push_channel_count.txt', 'w') as filedemanddata:
            file_ids_ls = []
            for j in range(3):
                file_id = 'file_id =' + fileids[random.randint(0, 2500)].replace("\n", "")
                file_ids_ls.append(file_id)
            for i in range(writelognumber):
                topic = "topic=" + "live_push_channel_count"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_count = 'file_count=' + str(len(file_ids_ls))
                file_ids = 'file_ids=' + str(file_ids_ls)
                filedemanddata.write(data_format % (topic, timestamp, file_count, file_ids))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_live_push_channel_count.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_live_push_channel_count')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_push_channel_count')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_push_channel_count['inputtable'])
        print 'data clear done'