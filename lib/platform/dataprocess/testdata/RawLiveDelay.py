import random
import os

import datavars
import dataprovider
from commonfunc import get_timestamp_by_time


class RawLiveDelay(dataprovider.Dataprovider):

    tablename = 'raw_input_live_delay'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,%s,%s,%d,%d,%d,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/RawLiveDelay.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0, 14)]
                    timestamp = get_timestamp_by_time(datavars.time_format % (i, j))
                    peerid = datavars.peeid_range[random.randint(0, 9)]
                    fileid = datavars.file_range[random.randint(0, 9)]
                    url = datavars.url_range[random.randint(0, 4)]
                    sourcetype = datavars.peertype[random.randint(0, 1)]
                    offset = int(timestamp) - random.randint(50, 5000)
                    delay = random.randint(100, 10000)
                    filedemanddata.write(data_format % (
                        id, int(timestamp), peerid, fileid, url, sourcetype, offset, delay, int(timestamp) +
                        random.randint(1, 100), int(timestamp)+random.randint(100, 1000)))

        return os.path.abspath(os.path.dirname(__file__)) + '/RawLiveDelay.txt'
