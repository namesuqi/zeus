import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time


class QosBufferingCleaned(dataprovider.Dataprovider):

    tablename = 'input_qos_buffering_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,itsavvidstring,%s,1111,222,%d,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/QosBufferingCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in [2, 6, 15, 26]:
                    id = datavars.id_range[random.randint(0,14)]
                    peerid = datavars.peeid_range[random.randint(0,9)]
                    timestamp = get_timestamp_by_time(datavars.time_format% (i, j))
                    url = datavars.url_range[random.randint(0,4)]
                    type = datavars.type_range[random.randint(0, 3)]
                    line = data_format % (
                        id, int(timestamp), peerid, url, type, int(timestamp)+random.randint(1,100),
                        int(timestamp) + random.randint(100,10000))
                    filedemanddata.write(line)
        return os.path.abspath(os.path.dirname(__file__)) + '/QosBufferingCleaned.txt'
