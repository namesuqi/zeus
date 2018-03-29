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


class server_peer_info(data_provider.DataProvider):

    def make_data(self):

        peerids = ReadConstantFlie('peer_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_peer_info.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "peer_info"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                sdk_version = 'sdk_version=' + "2.4.0.1"
                nat_type = 'nat_type=' + '3'
                public_ip = 'public_ip=' + '192.168.0.110'
                public_port = 'public_port=' + '8888'
                private_ip = 'private_ip=' + '10.5.0.254'
                private_port = 'private_port=' + '8080'
                macs = 'macs=' + '74:D4:35:80:C0:60'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, sdk_version, nat_type, public_ip,
                                                    public_port, private_ip, private_port, macs))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_peer_info.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_peer_info')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_peer_info')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_peer_info['inputtable'])
        print 'data clear done'