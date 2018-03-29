import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

class VodPerCleaned(dataprovider.Dataprovider):

    tablename = 'input_vod_performance_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format ='%s,%d,1000,%s,%s,0,0,%s,%s,cloudtropy,%s,%d,0,0,%d,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,,%d,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/VodPerCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0, 14)]
                    timestamp = get_timestamp_by_time(datavars.time_format % (11, 11))
                    peerid = datavars.peeid_range[random.randint(0, 9)]
                    fileid = datavars.file_range[random.randint(0, 9)]
                    url = datavars.url_range[random.randint(0, 4)]
                    username = datavars.url_username.values()[random.randint(0, 4)]
                    type = datavars.peertype[random.randint(0, 1)]
                    start_delay= datavars.delay_range[random.randint(0,14)]
                    seek_delay= datavars.delay_range[random.randint(0,14)]
                    filedemanddata.write(data_format %
                    ( id, int(timestamp), peerid, fileid, url,username,type,int(start_delay),int(seek_delay), int(timestamp)+random.randint(10, 1000),int(timestamp) + random.randint(1001, 10000)))
        return os.path.abspath(os.path.dirname(__file__)) + '/VodPerCleaned.txt'

