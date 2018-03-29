import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time


class RawFileOnDemand(dataprovider.Dataprovider):

    tablename = 'raw_input_file_on_demand'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,%s,%s,%s,%d,%d,%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/RawFileOnDemand.txt', 'w') as filedemanddata:
            for i in range(1000):
                id = datavars.id_range[random.randint(0, 14)]
                timestamp = get_timestamp_by_time(datavars.time_format % (11, 11))
                peerid = datavars.peeid_range[random.randint(0, 9)]
                url = datavars.url_range[random.randint(0, 4)]
                fodtype = datavars.type_range[random.randint(0, 3)]
                fileid = datavars.file_range[random.randint(0, 9)]
                publicip = datavars.publicip_range[random.randint(0, 4)]
                type = datavars.type_range[random.randint(0, 3)]
                filedemanddata.write(data_format % (
                id,int(timestamp),peerid,url,fodtype,fileid,publicip,int(timestamp)+random.randint(1, 100),int(timestamp)+random.randint(100, 10000),type))
        return os.path.abspath(os.path.dirname(__file__)) + '/RawFileOnDemand.txt'


