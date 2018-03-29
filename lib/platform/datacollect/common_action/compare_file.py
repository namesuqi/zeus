from file_to_dictlist import *


# the method compare list not contain child list and also not contain the key 'type'
def compare_file_by_its_list(file_name):
    input_list = inputfile_to_list(file_name + '.txt')
    # input_list = inputfilecontaindict2list(filename + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    print input_list
    print output_list
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['timestamp'])
                    # time delta between two num less than three seconds
                    if abs(input_time - output_time) < 3000:
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                input_list.remove(input_list[i])
                keys_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


'''
the method compare list contain child list and the key 'type'
input key : type or fod_type, startup_delay
output key : play_type, duration
'''


def compare_file_by_contain_type_list(file_name):
    input_list = inputfile_contain_list_to_list(file_name + '.txt')
    # input_list = inputfile2list(filename + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    # time delta between two num less than three seconds
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['timestamp'])
                    if abs(input_time - output_time) < 3000:
                        keys_count += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if input_list[i][keys[k]] == output_list[j]['play_type']:
                        keys_count += 1
                    continue
                if keys[k] == 'startup_delay':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['duration']):
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                input_list.remove(input_list[i])
                keys_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


'''
the method compare list contain child list and keys 'absolute_time','timestamp','source_type'
input key : 'absolute_time','timestamp','source_type'
output key : 'timestamp','input_time','play_type'
'''


def compare_file_by_contain_abtime_list(file_name):
    input_list = inputfile_contain_list_to_list(file_name + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    # time delta between two num less than three seconds
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['input_time'])
                    if abs(input_time - output_time) < 3000:
                        keys_count += 1
                    continue
                if keys[k] == 'absolute_time':
                    if input_list[i][keys[k]] == output_list[j]['timestamp']:
                        keys_count += 1
                    continue
                if keys[k] == 'source_type':
                    if input_list[i][keys[k]] == output_list[j]['play_type']:
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                input_list.remove(input_list[i])
                keys_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


'''
the method compare list contain child list and the key 'type'
input key : type or fod_type, duration
output key : play_type, duration(+'000')
'''


def compare_file_by_contain_duration_list(file_name):
    input_list = inputfile_contain_list_to_list(file_name + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['timestamp'])
                    # time delta between two num less than three seconds
                    if abs(input_time - output_time) < 3000:
                        keys_count += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if input_list[i][keys[k]] == output_list[j]['play_type']:
                        keys_count += 1
                    continue
                if keys[k] == 'duration':
                    # if int(input_list[i][keys[k]] + '000') == int(output_list[j]['duration']):
                    if int(input_list[i][keys[k]]) == int(output_list[j]['duration']):
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                input_list.remove(input_list[i])
                keys_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


'''
the method compare list contain child list
input key : type or fod_type, duration, p2pDown, httpDown, p2pUp
output key : play_type, duration(+'000'), p2p_download, cdn_download, upload
'''


def compare_file_by_contain_download_list(file_name):
    input_list = inputfile_contain_list_to_list(file_name + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['timestamp'])
                    # time delta between two num less than three seconds
                    if abs(input_time - output_time) < 10000:
                        keys_count += 1
                    continue
                if keys[k] == 'fod_type' or keys[k] == 'type':
                    if input_list[i][keys[k]] == output_list[j]['play_type']:
                        keys_count += 1
                    continue
                if keys[k] == 'duration':
                    # if int(input_list[i][keys[k]] + '000') == int(output_list[j]['duration']):
                    if int(input_list[i][keys[k]]) == int(output_list[j]['duration']):
                        keys_count += 1
                    continue
                if keys[k] == 'p2pDown':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['p2p_download']):
                        keys_count += 1
                    continue
                if keys[k] == 'httpDown':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['cdn_download']):
                        keys_count += 1
                    continue
                if keys[k] == 'p2pUp':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['upload']):
                        keys_count += 1
                    continue
                if keys[k] == 'id':
                    if input_list[i][keys[k]] == output_list[j]['id'].split('(')[0]:
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                input_list.remove(input_list[i])
                keys_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


'''
the method compare list not contain child list and also not contain the key 'type'
input key :name, osVersion, osType, coreVersion, cpuModel, publicPort, natType, privateIP, privatePort
output key :None, os_version, os_type, core_version, cpu_model, public_port, nat_type, private_ip, private_port
'''


def compare_file_by_exception_list(file_name):
    input_list = inputfile_contain_list_to_list(file_name + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        keys_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    input_time = long(input_list[i]['timestamp'])
                    output_time = long(output_list[i]['timestamp'])
                    # time delta between two num less than three seconds
                    if abs(input_time - output_time) < 3000:
                        keys_count += 1
                    continue
                if keys[k] == 'name':
                    keys_count += 1
                    continue
                if keys[k] == 'osVersion':
                    if input_list[i][keys[k]] == output_list[j]['os_version']:
                        keys_count += 1
                    continue
                if keys[k] == 'osType':
                    if input_list[i][keys[k]] == output_list[j]['os_type']:
                        keys_count += 1
                    continue
                if keys[k] == 'coreVersion':
                    if input_list[i][keys[k]] == output_list[j]['core_version']:
                        keys_count += 1
                    continue
                if keys[k] == 'cpuModel':
                    if input_list[i][keys[k]] == output_list[j]['cpu_model']:
                        keys_count += 1
                    continue
                if keys[k] == 'publicPort':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['public_port']):
                        keys_count += 1
                    continue
                if keys[k] == 'natType':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['nat_type']):
                        keys_count += 1
                    continue
                if keys[k] == 'privateIP':
                    if input_list[i][keys[k]] == output_list[j]['private_ip']:
                        keys_count += 1
                    continue
                if keys[k] == 'privatePort':
                    if int(input_list[i][keys[k]]) == int(output_list[j]['private_port']):
                        keys_count += 1
                    continue
                if keys[k] == 'addr':
                    if input_list[i][keys[k]] == output_list[j]['macs']:
                        keys_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    keys_count += 1
            if keys_count == len(keys):
                    input_list.remove(input_list[i])
                    keys_count = 0
                    compare_num -= 1
        if (j + 1) == len(output_list):
            break
#    print len(input_list)
    if len(input_list) == 0:
        return True
    else:
        return False


# the method compare list not contain child list ,it method create for case sdk_performace
def compare_file_by_performance_list(file_name):
    input_list = inputfile_contain_dict_to_list(file_name + '.txt')
    output_list = funnel_outputfile_to_list(file_name + '.log')
    compare_num = len(input_list)
    i = 0
    while i < compare_num:
        keys = input_list[i].keys()
        print len(keys)
        key_count = 0
        for j in range(len(output_list)):
            for k in range(len(keys)):
                if keys[k] == 'timestamp':
                    longnum = long(input_list[i]['timestamp'])
                    longnum2 = long(output_list[i]['timestamp'])
                    # time delta between two num less than three seconds
                    if abs(longnum - longnum2) < 3000:
                        key_count += 1
                    continue
                if keys[k] == 'httpDown':
                    if input_list[i][keys[k]] == output_list[j]['http_download']:
                        key_count += 1
                    continue
                if keys[k] == 'p2pDown':
                    if input_list[i][keys[k]] == output_list[j]['p2p_download']:
                        key_count += 1
                    continue
                if keys[k] == 'startDelay':
                    if input_list[i][keys[k]] == output_list[j]['start_delay']:
                        key_count += 1
                    continue
                if keys[k] == 'fwdSeeks':
                    if input_list[i][keys[k]] == output_list[j]['fwd_seeks']:
                        key_count += 1
                    continue
                if keys[k] == 'bwdSeeks':
                    if input_list[i][keys[k]] == output_list[j]['bwd_seeks']:
                        key_count += 1
                    continue
                if keys[k] == 'seekDelay':
                    if input_list[i][keys[k]] == output_list[j]['seek_delay']:
                        key_count += 1
                    continue
                if keys[k] == 'bufferCnt':
                    if input_list[i][keys[k]] == output_list[j]['buffer_cnt']:
                        key_count += 1
                    continue
                if keys[k] == 'bufferDelay':
                    if input_list[i][keys[k]] == output_list[j]['buffer_delay']:
                        key_count += 1
                    continue
                if input_list[i][keys[k]] == output_list[j][keys[k]]:
                    key_count += 1
            if key_count == len(keys):
                input_list.remove(input_list[i])
                key_count = 0
                compare_num -= 1
        if (j + 1) == len(output_list):
            break
    if len(input_list) == 0:
        return True
    else:
        return False


def compare_odps_data(file_name):
    input_lists = agent_outputfile_to_list(file_name + '.txt')
    output_lists = odps_outputfile_to_list(file_name + '.log')
    input_len = len(input_lists)
    out_putlen = len(output_lists)
    list_count = 0
    item_count = 0
    for i in range(input_len):
        del input_lists[i]['topic']
        keys = input_lists[i].keys()

        for j in range(out_putlen):
            for key in keys:
                if input_lists[i][key] in output_lists[j]:
                    item_count += 1
            if item_count == len(input_lists[i]):
                item_count = 0
                list_count += 1
                break
            else:
                item_count = 0

    if list_count == input_len:
        return True
    else:
        return False


def compare_odps_data_output_without_pip(file_name):
    input_lists = agent_outputfile_to_list(file_name + '.txt')
    output_lists = odps_outputfile_to_list(file_name + '.log')
    input_len = len(input_lists)
    output_len = len(output_lists)
    list_count = 0
    item_count = 0
    for i in range(input_len):
        del input_lists[i]['topic']
        del input_lists[i]['public_ip']
        keys = input_lists[i].keys()

        for j in range(output_len):
            for key in keys:
                if input_lists[i][key] in output_lists[j]:
                    item_count += 1
            if item_count == len(input_lists[i]):
                item_count = 0
                list_count += 1
                break
            else:
                item_count = 0

    if list_count == input_len:
        return True
    else:
        return False


if __name__ == '__main__':
    # c = comparefilebyperformancelist('sdk_performance_vod_version_1')
    c = compare_odps_data('server_peer_info')

    # c = comparefilebyexceptionlist('sdk_exception_version_1')
    # c = comparefilebycotainabtimelist('sdk_live_delay_version_1')
    if c:
        print "EQUAL!"
    else:
        print "NOT EQUAL!!!"
