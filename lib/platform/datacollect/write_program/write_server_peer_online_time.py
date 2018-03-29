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

class server_peer_online_time(data_provider.DataProvider):

    def make_data(self):

        peerids = ReadConstantFlie('peer_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_peer_online_time.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "peer_online_time"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                quarter = 'quarter=' + "131413344"
                online = 'online=' + '1'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, quarter, online))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_peer_online_time.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_peer_online_time')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_peer_online_time')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_peer_online_time['inputtable'])
        print 'data clear done'
