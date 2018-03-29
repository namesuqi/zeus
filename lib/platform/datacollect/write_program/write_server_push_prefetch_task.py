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


class server_push_prefetch_task(data_provider.DataProvider):

    def make_data(self):

        fileids = ReadConstantFlie('file_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_push_prefetch_task.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "push_prefetch_task"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                file_size = 'file_size=' + '6553548'
                flag = 'flag=' + 'end'
                filedemanddata.write(data_format % (topic, timestamp, file_id, file_size, flag))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_push_prefetch_task.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_push_prefetch_task')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_push_prefetch_task')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_push_prefetch_task['inputtable'])
        print 'data clear done'
