import os
import random

import lib.platform.datacollect.Action.GetTimeStamp as GetTimeStamp
import lib.platform.dataprocess.spark_compute.testdata as testdata


def add_tenant_makedata(hour ='00'):
    '''

    :param hour: the hour data need to created
    :return: data file, contain every minute's report data in the hour
    '''

    time_format = testdata.testday + "%02d%02d00"

    data_format = '%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\x1f%s\n'
    with open(os.path.abspath(os.path.dirname(__file__)) + '/add_tenant.txt', 'w') as filedemanddata:
        for i in range(60):
            topic = "topic=" + "add_tenant"
            file_id = 'file_id=' + testdata.file_id[random.randint(0, len(testdata.file_id) - 1)]
            id = "id=" + file_id.split('=')[1] + ":" + str(random.randint(1000, 1000000))
            timestamp = 'timestamp=' + str(GetTimeStamp.get_timestamp(time_format % (int(hour), i)))
            # timestamp = 'timestamp=' + str(GetTimeStamp.get_timestamp_now())
            tenant_id = "tenant_id=" + "12345ABCD"
            tenant_name = "tenant_name=" + "yunshangtest"
            groups = 'groups=' + 'testgroup'
            peer_prefix = 'peer_prefix=' + testdata.peer_id[random.randint(0, 9)][0:8]


            filedemanddata.write(data_format % (topic, id, timestamp, tenant_id, tenant_name, groups, peer_prefix))
    return os.path.abspath(os.path.dirname(__file__)) + '/add_tenant.txt'

if __name__ == '__main__':
    add_tenant_makedata()