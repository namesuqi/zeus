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


class server_live_push_error(data_provider.DataProvider):

    def make_data(self):


        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_live_push_error.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "live_push_error"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                level = 'level=' + "warn"
                module = 'module=' + 'testmodle'
                err_info = 'err_info=' + 'TESTERROE!!!'
                filedemanddata.write(data_format % (topic, timestamp, level, module, err_info))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_live_push_error.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_live_push_error')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_live_push_error')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_live_push_error['inputtable'])
        print 'data clear done'