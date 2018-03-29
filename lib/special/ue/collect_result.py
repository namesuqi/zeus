# coding=utf-8
# control sdk
# author = 'dh'

from lib.special.ue.ue_analyze_controller import *
# from lib.remote.remoter import *
import csv
import codecs
import time
import sys


@print_trace
@log_func_args
def write_case_result(file_name, udp_buf_num, http_buf_num, udp_time, http_time):
    """

    :param file_name:
    :param udp_buf_num:
    :param http_buf_num:
    :param udp_time:
    :param http_time:
    :return:
    """
    output_file = open(file_name, "w")

    output_file.write(MODE_UDP)
    udp_time = float("%.2f" % udp_time)
    output_file.write(",{0}ms, {1}".format(udp_time, udp_buf_num))
    output_file.write("\n")

    output_file.write(MODE_HTTP)
    http_time = float("%.2f" % http_time)
    output_file.write(",{0}ms, {1}".format(http_time, http_buf_num))
    output_file.write("\n")

    output_file.close()


@print_trace
@log_func_args
def collect_results_files():
    """
    collect_results_files case entry function
    :return:
    """
    csv_file = codecs.open(CSV_FILE, "wb", "utf_8_sig")
    writer = csv.writer(csv_file)
    data = [CSV_HEADER]

    for i in DELAY_TIME_LIST:
        for j in LOSS_RATE_LIST:
            for k in MODE_LIST:
                temp = parse_file(i, j, k)
                if temp is not None:
                    for l in temp:
                        data.append(l)

    # print data
    new_data = generate_format(data)
    reload(sys)
    sys.setdefaultencoding("utf-8")
    writer.writerows(new_data)
    csv_file.close()


@print_trace
@log_func_args
def parse_file(delay, loss, mode):
    """
    For the collect_results_files case, parsing the specify txt to get result
    :param delay:
    :param loss:
    :param mode:
    :return:
    """
    file_name = RESULT_PATH + "{0}ms_{1}%_{2}.txt".format(delay, loss, mode)
    print file_name
    if "ms" and "%" not in file_name:
        return None
    if not os.path.exists(file_name):
        return None

    data_list = [
        [],
        []
    ]
    print len(data_list)
    for i in range(len(data_list)):
        data_list[i].append(str(delay * 2) + "ms")
        data_list[i].append(str(loss) + "%")
        if "image" in file_name:
            data_list[i].append(START_UP_TIME)
            data_list[i].append(str(SAMPLE_NUM) + u"次")
        else:
            data_list[i].append(BUFFERING_NUMBER)
            data_list[i].append(str(LAST_TIME_PLAY_DURATION / 60) + u"分钟")

    print "data_list_1:", data_list
    fr = open(file_name)

    count = 0
    for line in fr:
        temp_list = line.strip("\n").split(",")
        for i in temp_list:
            data_list[count].append(i)
        count += 1

    print "data_list:", data_list
    return data_list


@print_trace
@log_func_args
def back_up_logs():
    """
    Back_up_logs case entry function
    :return:
    """
    dir_name = time.strftime(ISO_TIME_FORMAT, time.localtime())
    mk_cmd = "mkdir -p {0}/{1}".format(REMOTE_PLAYER_PATH, dir_name)
    remote_execute(PEER_IP, ROOT_USER, ROOT_PASSWD, mk_cmd)

    mv_cmd = "mv {0}/*.log {1}/{2}/".format(REMOTE_PLAYER_PATH, REMOTE_PLAYER_PATH, dir_name)
    print mv_cmd
    remote_execute(PEER_IP, ROOT_USER, ROOT_PASSWD, mv_cmd)


@print_trace
@log_func_args
def generate_format(data):
    """
    For the collect_results_files case, parsing the specify txt to get result
    :param data:
    :return:
    """
    ret_list = [data[0]]
    print len(data)
    for i in range(1, len(data)):
        for j in range(i+1, len(data)):
            print "i,j:", i, j
            if compare_beyond(data[i], data[j]):
                temp_list = merge_list(data[i], data[j])
                ret_list.append(temp_list)
                break
            if j == len(data) - 1:
                ret_list.append(data[i])

    return ret_list


@print_trace
@log_func_args
def compare_beyond(list_A, list_B):
    """
    compare two lists whether they belong to one case
    :param list_A:
    :param list_B:
    :return:
    """
    if list_A[0] == list_B[0] and list_A[1] == list_B[1] and list_A[4] == list_B[4]:
        return True
    else:
        return False


@print_trace
@log_func_args
def merge_list(list_A, list_B):
    """
    merge two lists if they belong to one case
    :param list_A:
    :param list_B:
    :return:
    """
    if len(list_B) > 6:
        list_C = list_A
        list_A = list_B
        list_B = list_C

    list_A.append(list_B[2])
    list_A.append(list_B[3])
    list_A.append(list_B[5])

    return list_A


@print_trace
@log_func_args
def write_database_csv():
    """
    Write_Database_Csv case entry function
    :return:
    """
    db_object = MysqlDB(MYSQL_HOST, MYSQL_UE_USER, MYSQL_PASSWORD, MYSQL_DB_NAME)
    csv_file = codecs.open(CSV_FILE, "wb", "utf_8_sig")
    writer = csv.writer(csv_file)
    data = [
        CSV_DATABASE_HEADER
    ]

    for record in iterate_condition(db_object, MODE_UDP):
        data.append(record)

    # print data
    # new_data = generate_format(data)
    reload(sys)
    sys.setdefaultencoding("utf-8")
    writer.writerows(data)
    csv_file.close()


@print_trace
@log_func_args
def get_result_csv(sdk_version, live_push_version, play_duration, lf=0, mode_type=MODE_UDP):

    db_object = MysqlDB(MYSQL_HOST, MYSQL_UE_USER, MYSQL_PASSWORD, MYSQL_DB_NAME)
    csv_file = codecs.open(CSV_FILE, "wb", "utf_8_sig")
    writer = csv.writer(csv_file)
    data = [
        CSV_DATABASE_HEADER
    ]

    for record in condition_select(db_object, sdk_version=sdk_version, live_push_version=live_push_version,
                                   mode=mode_type, play_duration=play_duration, lf=lf):
        data.append(record)

    # print data
    # new_data = generate_format(data)
    reload(sys)
    sys.setdefaultencoding("utf-8")
    writer.writerows(data)
    csv_file.close()


# @print_trace
# @log_func_args
# def write_http_database_csv(live_push_version=LIVE_PUSH_VERSION):
#     """
#     Write_Http_Database_Csv case entry function
#     :param live_push_version:
#     :return:
#     """
#     db_object = MysqlDB(MYSQL_HOST, MYSQL_UE_USER, MYSQL_PASSWORD, MYSQL_DB_NAME)
#     csv_file = codecs.open(CSV_HTTP_FILE, "wb", "utf_8_sig")
#     writer = csv.writer(csv_file)
#     data = [
#         CSV_DATABASE_HTTP_HEADER
#     ]
#
#     for record in iterate_condition(db_object, MODE_HTTP):
#         data.append(record)
#
#     # print data
#     # new_data = generate_format(data)
#     reload(sys)
#     sys.setdefaultencoding("utf-8")
#     writer.writerows(data)
#     csv_file.close()


@print_trace
@log_func_args
def get_database_res_from_time(start_time, file_name=CSV_FILE):
    """
    :param start_time:
    :param file_name:
    :return:
    """
    db_object = MysqlDB(MYSQL_HOST, MYSQL_UE_USER, MYSQL_PASSWORD, MYSQL_DB_NAME)
    csv_file = codecs.open(file_name, "wb", "utf_8_sig")
    writer = csv.writer(csv_file)
    data = [
        CSV_DATABASE_TIME_HEADER
    ]
    time_format = '%Y%m%d%H%M%S'
    case_stop_time = time.strftime(time_format, time.localtime())

    for record in select_by_time(db_object, start_time, case_stop_time):
        data.append(record)
    # for record in iterate_condition(db_object):
    #     data.append(record)

    reload(sys)
    sys.setdefaultencoding("utf-8")
    writer.writerows(data)
    csv_file.close()


if __name__ == "__main__":
    # write_database_csv()
    get_result_csv(sdk_version=SDK_VERSION, live_push_version=LIVE_PUSH_VERSION, play_duration=600, mode_type='udp',
                   lf=50)
