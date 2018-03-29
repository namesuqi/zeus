import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time


class RawDownloadFlow(dataprovider.Dataprovider):

    tablename = 'raw_input_download_flow'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,CloutropySDK,%s,%d,%d,1000,%d,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/RawDownloadFlow.txt', 'w') as filedemanddata:
            for i in range(1000):
                peerid = datavars.peeid_range[random.randint(0, 9)]
                timestamp = get_timestamp_by_time(datavars.time_format % (11, 11))
                url = datavars.url_range[random.randint(0, 4)]
                type = datavars.peertype[random.randint(0, 1)]
                p2pdown = random.randint(10000,1000000)
                cdndown = random.randint(10000,1000000)
                id = datavars.id_range[random.randint(0, 14)]
                if i%5 ==0:
                    p2pdown = 0; cdndown = 0
                filedemanddata.write(data_format % (
                id,int(timestamp),peerid,url,type,p2pdown,cdndown,int(timestamp)+random.randint(1, 100),int(timestamp)+random.randint(100, 10000)))
        return os.path.abspath(os.path.dirname(__file__)) + '/RawDownloadFlow.txt'

