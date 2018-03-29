import os
import lib.platform.dataprocess.spark_compute.testdata as testdata
import lib.platform.datacollect.Action.GetTimeStamp as GetTimeStamp

def upload_flow_compute(hour ='00'):
    result = dict()
    j = 0
    totalresult = dict()
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../temp_file/my_server_upload_flow.txt', 'r') as originfile:
        origindata = originfile.readlines()
    timeformat = GetTimeStamp.get_timestamp(testdata.testday + '%02d0000' % int(hour))
    for line in origindata:
        line = line.replace('\n', '')
        _, _, timestamp, _, upload, _, _, _, _, _, _, peer_owner, file_type = line.split(',')

        if long(timeformat) <= long(timestamp) <= (long(timeformat) + 300*12*1000):
            for i in range(12):
                if (long(timeformat) + i*300*1000) <= long(timestamp) < (long(timeformat) + (i+1)*300*1000):
                    if i not in result:
                        result[i] = dict()
                    if peer_owner not in result[i]:
                        result[i][peer_owner] = dict()
                    if file_type not in result[i][peer_owner]:
                        result[i][peer_owner][file_type] = dict()
                        result[i][peer_owner][file_type]['upload_flow'] = 0
                    result[i][peer_owner][file_type]['upload_flow'] = result[i][peer_owner][file_type]['upload_flow'] + long(upload)

    print result

    for i in result.keys():
        for owner in result[i].keys():
            if 'all' not in totalresult:
                totalresult['all'] = dict()
            if owner not in totalresult:
                totalresult[owner] = dict()
            for type in result[i][owner].keys():
                if type not in totalresult['all']:
                    totalresult['all'][type] = dict()
                    totalresult['all'][type]['upload_flow'] = 0
                if type not in totalresult[owner]:
                    totalresult[owner][type] = dict()
                    totalresult[owner][type]['upload_flow'] = 0
                totalresult[owner][type]['upload_flow'] = totalresult[owner][type]['upload_flow'] + result[i][owner][type]['upload_flow']
                totalresult['all'][type]['upload_flow'] = totalresult['all'][type]['upload_flow'] + result[i][owner][type]['upload_flow']

    print totalresult

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/server_upload_flow_EXP.txt', 'w') as writefile:
        for peerowner in totalresult.keys():
            for playtype in totalresult[peerowner].keys():
                for flowtype in totalresult[peerowner][playtype]:
                    writefile.write("peerowner=" + peerowner + ", playtype=" + playtype + ", flowtype=" + flowtype + ", value=" + str(totalresult[peerowner][playtype][flowtype]) + "\n")


if __name__ == '__main__':
    upload_flow_compute()
