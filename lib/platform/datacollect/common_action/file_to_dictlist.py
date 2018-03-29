import read_file
import platform
from lib.platform.datacollect.global_vars.constant import *


def inputfile_to_list(file_name):
    input_file_lines = read_file.read_expect_file(file_name)
    input_list = []
    for input_file_line in input_file_lines:
        input_file_line = input_file_line.replace('\n', '')
        input_file_line = input_file_line.replace('\"', '')
        input_file_line = input_file_line.replace('{', '')
        input_file_line = input_file_line.replace('}', '')
        input_file_line = input_file_line.replace(': ', '=')
        input_file_line = input_file_line.replace(' ', '')
        if platform.system() == "Linux":
            input_file_line = input_file_line.replace('\\r', '')
            input_file_line = input_file_line.replace('\r', '')

        input_temp_list = input_file_line.split(',')
        input_dict = {}
        for i in range(len(input_temp_list)):
            input_temp_list2 = input_temp_list[i].split('=')
            input_dict[input_temp_list2[0]] = input_temp_list2[1]
        input_list.append(input_dict)
    return input_list


def inputfile_contain_list_to_list(file_name):
    input_file_lines = read_file.read_expect_file(file_name)
    input_list = []
    for input_file_line in input_file_lines:
        input_file_line = input_file_line.replace('\n', '')
        input_file_line = input_file_line.replace('\"', '')
        input_file_line = input_file_line.replace('{', '')
        input_file_line = input_file_line.replace('}', '')
        input_file_line = input_file_line.replace(': ', '=')
        input_file_line = input_file_line.replace(' ', '')
        if platform.system() == "Linux":
            input_file_line = input_file_line.replace('\\r', '')
            input_file_line = input_file_line.replace('\r', '')

        input_temp_list = input_file_line.split(",")
        input_dict = {}
        for i in range(len(input_temp_list)):
            if input_temp_list[i].find('=[') != -1:
                input_temp_list[i] = input_temp_list[i].split("=[")[1]
            if input_temp_list[i].find(']') != -1:
                input_temp_list[i] = input_temp_list[i][:-1]
            input_temp_list2 = input_temp_list[i].split('=')
            input_dict[input_temp_list2[0]] = input_temp_list2[1]
        input_list.append(input_dict)
    return input_list


def inputfile_contain_dict_to_list(file_name):
    input_file_lines = read_file.read_expect_file(file_name)
    input_list = []
    for input_file_line in input_file_lines:
        input_file_line = input_file_line.replace('\n', '')
        input_file_line = input_file_line.replace('\"', '')
        input_file_line = input_file_line.replace(': ', '=')
        input_file_line = input_file_line.replace(' ', '')
        input_file_line = input_file_line.replace('={', '=@')
        input_file_line = input_file_line.replace('},', '**,')
        input_file_line = input_file_line.replace('{', '')
        input_file_line = input_file_line.replace('}', '')
        input_file_line = input_file_line.replace('[0,0,1,0,0,0,0,0]', '###')
        if platform.system() == "Linux":
            input_file_line = input_file_line.replace('\\r', '')
            input_file_line = input_file_line.replace('\r', '')
        # print input_file_line

        input_temp_list = input_file_line.split(",")
        input_dict = {}
        for i in range(len(input_temp_list)):
            if input_temp_list[i].find('=@') != -1:
                input_temp_list[i] = input_temp_list[i].split("=@")[1]
            if input_temp_list[i].find('**') != -1:
                input_temp_list[i] = input_temp_list[i].split('**')[0]
            if input_temp_list[i].find('###') != -1:
                input_temp_list[i] = input_temp_list[i].replace("###", '[0,0,1,0,0,0,0,0]')
            input_temp_list2 = input_temp_list[i].split('=')
            input_dict[input_temp_list2[0]] = input_temp_list2[1]
        input_list.append(input_dict)
    return input_list


def funnel_outputfile_to_list(file_name):

    output_file_lines = read_file.read_real_file(file_name)
    output_list = []

    for output_file_line in output_file_lines:
        output_file_line = output_file_line.replace('\n', '')
        if platform.system() == "Linux":
            output_file_line = output_file_line.replace('\\r', '')
            output_file_line = output_file_line.replace('\r', '')
        output_file_line_list = output_file_line.split("\x1f")
        output_dict = {}
        for i in range(len(output_file_line_list)):
            output_temp_list = output_file_line_list[i].split('=')
            output_dict[output_temp_list[0]] = output_temp_list[1]
        output_list.append(output_dict)
    return output_list[-post_log_number:]


def agent_outputfile_to_list(file_name):

    output_file_lines = read_file.read_expect_file(file_name)
    output_list = []

    for output_file_line in output_file_lines:
        output_file_line = output_file_line.replace('\n', '')
        if platform.system() == "Linux":
            output_file_line = output_file_line.replace('\\r', '')
            output_file_line = output_file_line.replace('\r', '')
        output_file_line_list = output_file_line.split("\x1f")
        output_dict = {}
        for i in range(len(output_file_line_list)):
            output_temp_list = output_file_line_list[i].split('=')
            output_dict[output_temp_list[0]] = output_temp_list[1]
        output_list.append(output_dict)
    return output_list


def odps_outputfile_to_list(file_name):
    output_file_lines = read_file.read_real_file(file_name)
    output_list = []

    for output_file_line in output_file_lines:
        output_file_line = output_file_line.replace('\n', '')
        if platform.system() == "Linux":
            output_file_line = output_file_line.replace('\\r', '')
            output_file_line = output_file_line.replace('\r', '')
        output_file_line_list = output_file_line.split(",")
        output_list.append(output_file_line_list)
    return output_list


if __name__ == '__main__':
    # a = funneloutputfile2list('idc_peer_connection_report.log')
    # b = inputfile2list('idc_peer_connection_report.txt')
    # c = inputfilecontainlist2list('sdk_vf_version_1.txt')
    # c = inputfilecontainlist2list('sdk_flow_download_version_1.txt')
    # c = inputfilecontainlist2list('sdk_flow_upload_version_1.txt')
    # c = inputfilecontainlist2list('sdk_exception_version_1.txt')
    # c = inputfilecontaindict2list('sdk_performance_vod_version_1.txt')
    # d = funneloutputfile2list('sdk_performance_vod_version_1.log')
    # d = agentoutputfile2list('server_peer_info.txt')
    d = odps_outputfile_to_list('server_live_progress.log')
    # for i in range(len(c)):
    #     print c[i]
    # print c
    for i in range(len(d)):
        print d[i]
    print d
    # print len(d)
    # print d[0]
