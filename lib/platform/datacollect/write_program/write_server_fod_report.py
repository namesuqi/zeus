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


class server_fod_report(data_provider.DataProvider):

    def make_data(self):

        peerids = ReadConstantFlie('peer_id_db.txt')

        data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/'\
                                                               'server_fod_report.txt', 'w') as filedemanddata:
            for i in range(writelognumber):
                topic = "topic=" + "fod_report"
                timestamp = "timestamp=" + get_timestamp(server_input_time)
                peer_id = 'peer_id=' + peerids[random.randint(0, 2500)].replace("\n", "")
                fod_type = 'fod_type=' + "hls"  # or channel
                public_ip = 'public_ip=' + '192.168.0.110'
                filedemanddata.write(data_format % (topic, timestamp, peer_id, fod_type, public_ip))
        return os.path.abspath(os.path.dirname(__file__)) + '/../Datafile/expect_data_file/server_fod_report.txt'

    def write_log(self):
        Action.CopyFileToRemote.localcopyfile('server_fod_report')
        time.sleep(2)
        Action.RemoteCommandWin2Lin.startwriterlog('server_fod_report')

    def clear_data(self):
        Action.ODPScommand.dropodpsdata(GlobalVars.SERVER.server_fod_report['inputtable'])
        print 'data clear done'