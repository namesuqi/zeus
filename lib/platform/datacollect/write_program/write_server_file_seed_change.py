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


class server_file_seed_change(data_provider.DataProvider):

    def make_data(self):

        peerids = ReadConstantFlie('peer_id_db.txt')
        fileids = ReadConstantFlie('file_id_db.txt')
        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_file_seed_change.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "file_seed_change"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                file_id = 'file_id=' + fileids[random.randint(0, 2500)].replace("\n", "")
                operation = 'operation=' + '13'
                slice_map = 'slice_map=' + 'test_slice_map_data'
                cppc = 'cppc=' + '12306'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, file_id, operation, slice_map, cppc))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_file_seed_change.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_file_seed_change')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_file_seed_change')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_file_seed_change['inputtable'])
        print 'data clear done'