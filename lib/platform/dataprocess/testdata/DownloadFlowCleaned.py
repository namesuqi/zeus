import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

class DownloadFlowCleaned(dataprovider.Dataprovider):

    tablename = 'input_download_flow_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,CloutropySDK,%s,%d,%d,1000,%s,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/DownloadFlowCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    for k in range(60):
                        peerid = datavars.peeid_range[random.randint(0, 9)]
                        timestamp = get_timestamp_by_time(datavars.time_format_with_second % (i, j, k))
                        url = datavars.url_range[random.randint(0, 4)]
                        type = datavars.type_range[random.randint(0, 5)]
                        p2pdown = random.randint(10000,1000000)
                        cdndown = random.randint(10000,1000000)
                        id = datavars.id_range[random.randint(0, 14)]
                        if k % 9 == 0:
                            p2pdown = 0; cdndown = 0
                        filedemanddata.write(data_format % (
                        peerid, int(timestamp),url,type,p2pdown,cdndown,id,int(timestamp)+random.randint(10, 1000)))
        return os.path.abspath(os.path.dirname(__file__)) + '/DownloadFlowCleaned.txt'

