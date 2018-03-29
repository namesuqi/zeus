import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time

class RawClientException(dataprovider.Dataprovider):

    tablename = 'raw_input_client_exception'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,%s,Intel,i7,%d,%s,80,192.168.1.10,80,%s,%s,%s,error,%d,%d,%s\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/RawClientException.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0, 14)]
                    timestamp = get_timestamp_by_time(datavars.time_format % (11, 11))
                    peerid = datavars.peeid_range[random.randint(0, 9)]
                    os_type= datavars.os_versions[random.randint(0, 1)].split(',')[0]
                    os_version= datavars.os_versions[random.randint(0, 1)].split(',')[1]
                    nat_type= datavars.nattype[random.randint(0, 2)]
                    publicip = datavars.publicip_range[random.randint(0, 4)]
                    macs= datavars.macs[random.randint(0, 1)]
                    op= datavars.op_and_error[random.randint(0, 8)].split(',')[0]
                    errorcode= datavars.op_and_error[random.randint(0, 8)].split(',')[1]
                    type= datavars.type_range[random.randint(0, 3)]
                    filedemanddata.write(data_format % (
                    id, int(timestamp), peerid,os_type,os_version,int(nat_type),publicip,macs,op,errorcode, int(timestamp)+random.randint(10, 1000),int(timestamp) + random.randint(1001, 10000),type))
        return os.path.abspath(os.path.dirname(__file__)) + '/RawClientException.txt'



