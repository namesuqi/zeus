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


class server_push_request(data_provider.DataProvider):

    def make_data(self):


        data_format = '%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_push_request.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "push_request"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                request_url = 'request_url=' + "http://request.test.com"
                response_status_code = 'response_status_code=' + '200'
                filedemanddata.write(data_format % (topic, timestamp, request_url, response_status_code))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_push_request.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_push_request')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_push_request')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_push_request['inputtable'])
        print 'data clear done'