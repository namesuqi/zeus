import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

class PeerOnlineTimeCleaned(dataprovider.Dataprovider):

    tablename = 'input_peer_online_time_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%d,%d,%d,%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/PeerOnlineTimeCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0, 14)]
                    timestamp = get_timestamp_by_time(datavars.time_format % (i, j))
                    peerid = datavars.peeid_range[random.randint(0, 9)]
                    quarter=random.randint(0,95)
                    online=random.randint(0,1)
                    type= datavars.type_range[random.randint(0, 3)]
                    filedemanddata.write(data_format % (
                    id, int(timestamp),peerid,quarter,online, int(timestamp)+random.randint(10, 1000),type))
        return os.path.abspath(os.path.dirname(__file__)) + '/PeerOnlineTimeCleaned.txt'


