import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time


class FileOnDemandCleaned(dataprovider.Dataprovider):

    tablename = 'input_file_on_demand_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%s,%d,%s,%s,%s,%s,%d,%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/FileOnDemandCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0,14)]
                    peerid = datavars.peeid_range[random.randint(0,9)]
                    timestamp = get_timestamp_by_time(datavars.time_format% (i, j))
                    url = datavars.url_range[random.randint(0,4)]
                    fod_type = datavars.type_range[random.randint(0,3)]
                    publicip = datavars.publicip_range[random.randint(0,4)]
                    fileid = datavars.file_range[random.randint(0,9)]
                    type= datavars.type_range[random.randint(0, 3)]
                    filedemanddata.write(data_format%(id,peerid,int(timestamp),url,fod_type,publicip,fileid,int(timestamp)+random.randint(10,1000),type))
        return os.path.abspath(os.path.dirname(__file__)) + '/FileOnDemandCleaned.txt'
