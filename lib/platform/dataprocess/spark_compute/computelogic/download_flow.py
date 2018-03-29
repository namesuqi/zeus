import os
import lib.platform.dataprocess.spark_compute.testdata as testdata
import lib.platform.datacollect.Action.GetTimeStamp as GetTimeStamp


def download_flow_compute(hour='00'):
    result = dict()
    totalresult = dict()
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../temp_file/my_server_download_flow.txt', 'r') as originfile:
        origindata = originfile.readlines()
    timeformat = GetTimeStamp.get_timestamp(testdata.testday + '%02d0000' % int(hour))
    for line in origindata:
        line = line.replace('\n', '')
        _, _, _, timestamp, _, p2p_download, cdn_download, _, _, _, _, _, peer_owner, _, play_type = line.split(',')
        if long(timeformat) <= long(timestamp) <= (long(timeformat) + 300*12*1000):
            for i in range(12):
                if (long(timeformat) + i*300*1000) <= long(timestamp) < (long(timeformat) + (i+1)*300*1000):
                    if i not in result:
                        result[i] = dict()
                    if peer_owner not in result[i]:
                        result[i][peer_owner] = dict()
                    if play_type not in result[i][peer_owner]:
                        result[i][peer_owner][play_type] = dict()
                        result[i][peer_owner][play_type]['p2p_download'] = 0
                        result[i][peer_owner][play_type]['cdn_download'] = 0
                    result[i][peer_owner][play_type]['p2p_download'] = result[i][peer_owner][play_type]['p2p_download'] + long(p2p_download)
                    result[i][peer_owner][play_type]['cdn_download'] = result[i][peer_owner][play_type]['cdn_download'] + long(cdn_download)

    print result
    for minitem in result.keys():
        for owner in result[minitem].keys():
            if 'all' not in totalresult:
                totalresult['all'] = dict()
            if owner not in totalresult:
                totalresult[owner] = dict()
            for typeitem in result[minitem][owner].keys():
                if typeitem not in totalresult['all']:
                    totalresult['all'][typeitem] = dict()
                    totalresult['all'][typeitem]['p2p_download'] = 0
                    totalresult['all'][typeitem]['cdn_download'] = 0
                    totalresult['all'][typeitem]['total_download'] = 0
                    totalresult['all'][typeitem]['p2p_percentage'] = 0.0
                if typeitem not in totalresult[owner]:
                    totalresult[owner][typeitem] = dict()
                    totalresult[owner][typeitem]['p2p_download'] = 0
                    totalresult[owner][typeitem]['cdn_download'] = 0
                    totalresult[owner][typeitem]['total_download'] = 0
                    totalresult[owner][typeitem]['p2p_percentage'] = 0.0
                totalresult[owner][typeitem]['p2p_download'] = totalresult[owner][typeitem]['p2p_download'] + result[minitem][owner][typeitem]['p2p_download']
                totalresult[owner][typeitem]['cdn_download'] = totalresult[owner][typeitem]['cdn_download'] + result[minitem][owner][typeitem]['cdn_download']
                totalresult[owner][typeitem]['total_download'] = totalresult[owner][typeitem]['total_download'] + \
                                                          result[minitem][owner][typeitem]['p2p_download'] + result[minitem][owner][typeitem]['cdn_download']
                totalresult[owner][typeitem]['p2p_percentage'] = float(totalresult[owner][typeitem]['p2p_download']) / \
                                                        (float(totalresult[owner][typeitem]['p2p_download']) + float(totalresult[owner][typeitem]['cdn_download']))
                totalresult['all'][typeitem]['p2p_download'] = totalresult['all'][typeitem]['p2p_download'] + result[minitem][owner][typeitem]['p2p_download']
                totalresult['all'][typeitem]['cdn_download'] = totalresult['all'][typeitem]['cdn_download'] + result[minitem][owner][typeitem]['cdn_download']
                totalresult['all'][typeitem]['total_download'] = totalresult['all'][typeitem]['p2p_download'] + totalresult['all'][typeitem]['cdn_download']
                totalresult['all'][typeitem]['p2p_percentage'] = float(totalresult['all'][typeitem]['p2p_download']) / \
                                                                 float(totalresult['all'][typeitem]['total_download'])
                # totalresult['all'][typeitem]['p2p_download'] = totalresult['all'][typeitem]['p2p_download'] + totalresult[owner][typeitem]['p2p_download']
                # totalresult['all'][typeitem]['cdn_download'] = totalresult['all'][typeitem]['cdn_download'] + totalresult[owner][typeitem]['cdn_download']
                # totalresult['all'][typeitem]['total_download'] = totalresult['all'][typeitem]['p2p_download'] + totalresult[owner][typeitem]['p2p_download']
                # totalresult['all'][typeitem]['p2p_percentage'] = float(totalresult['all'][typeitem]['p2p_download']) / \
                #                                                      float(totalresult['all'][typeitem]['total_download'])




    print totalresult

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/server_download_flow_EXP.txt', 'w') as writerfile:
        for peerowner in totalresult.keys():
            for playtype in totalresult[peerowner].keys():
                for flowtype in totalresult[peerowner][playtype]:
                    writerfile.write("peerowner=" + peerowner + ", playtype=" + playtype + ", flowtype=" + flowtype + ", value=" + str(totalresult[peerowner][playtype][flowtype]) + "\n")


if __name__ == '__main__':
    download_flow_compute('13')