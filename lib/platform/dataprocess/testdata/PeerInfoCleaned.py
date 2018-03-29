import random
import sys
import os

import datavars
import dataprovider

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from commonfunc import get_timestamp_by_time
from commonfunc import create_random_unique_peerid


class PeerInfoCleaned(dataprovider.Dataprovider):

    tablename = 'input_peer_info_cleaned'

    @classmethod
    def gettablename(cls):
        return cls.tablename

    def makedata(self):
        data_format = '%s,%d,%s,%s,%s,android,%d,%s,80,192.168.1.10,80,%s,Intel,%d\n'
        with open(os.path.abspath(os.path.dirname(__file__)) + '/PeerInfoCleaned.txt', 'w') as filedemanddata:
            for i in range(24):
                for j in range(60):
                    id = datavars.id_range[random.randint(0, 14)]
                    timestamp = get_timestamp_by_time(datavars.time_format % (i, j))
                    peerid = create_random_unique_peerid()
                    os_type= datavars.os_versions[random.randint(0, 1)].split(',')[0]
                    os_version= datavars.os_versions[random.randint(0, 1)].split(',')[1]
                    nat_type= datavars.nattype[random.randint(0, 2)]
                    publicip = datavars.publicip_range[random.randint(0, 4)]
                    macs= datavars.macs[random.randint(0, 1)]
                    filedemanddata.write(data_format % (
                    id, int(timestamp),peerid,os_type,os_version,int(nat_type),publicip,macs,int(timestamp)+random.randint(10, 1000)))
        return os.path.abspath(os.path.dirname(__file__)) + '/PeerInfoCleaned.txt'

if __name__ == '__main__':
    print dir(datavars)
    temp = PeerInfoCleaned()
    temp.makedata()



