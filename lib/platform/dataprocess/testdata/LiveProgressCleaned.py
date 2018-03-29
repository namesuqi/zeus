import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time


class LiveProgressCleaned(dataprovider.Dataprovider):

    tablename = 'input_live_progress_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,%d,%d,%d,%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/LiveProgressCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0,14)]
                    peerid = datavars.peeid_range[random.randint(0,9)]
                    timestamp = get_timestamp_by_time(datavars.time_format% (i, j))
                    fileid = datavars.file_range[random.randint(0,9)]
                    chunkid = datavars.chunkid_range[random.randint(0,3)]
                    type= datavars.type_range[random.randint(0, 3)]
                    filedemanddata.write(data_format%(
                        id, int(timestamp), peerid, fileid, chunkid, int(timestamp)+random.randint(1,100),
                        int(timestamp) + random.randint(100,10000), type))
        return os.path.abspath(os.path.dirname(__file__)) + '/LiveProgressCleaned.txt'
