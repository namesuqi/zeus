# coding=utf-8
# author = 'donghao'

from lib.special.ue.database_controller import *
from lib.special.ue.const import *
from lib.dm.stats import *


@print_trace
@log_func_args
def iterate_condition(db_object, mode, sdk_version=SDK_VERSION, live_push_version=LIVE_PUSH_VERSION):
    """
    iterate case
    :param db_object:
    :param mode:
    :param sdk_version:
    :param live_push_version:
    :return:
    """
    result_list = []
    for delay in DELAY_TIME_LIST:
        for loss in LOSS_RATE_LIST:
            tmp_list = select_specify_condition(db_object, mode, delay, loss, sdk_version, live_push_version)
            if tmp_list is not None:
                result_list.append(tmp_list)

    return result_list


@print_trace
@log_func_args
def condition_select(db_object, sdk_version, live_push_version, mode, play_duration, lf):

    result_list = []
    for delay in DELAY_TIME_LIST:
        for loss in LOSS_RATE_LIST:
            tmp_list = select_full_condition(db_object, mode, delay, loss, sdk_version, live_push_version,
                                             play_duration, lf)
            if tmp_list is not None:
                result_list.append(tmp_list)

    return result_list


@print_trace
@log_func_args
def calculate():
    tmp_res = db_select_result(MYSQL_TABLE_NAME, "count(DISTINCT sdk_version, 'mode')")
    count_col = int(tmp_res[0][0])
    return count_col


@print_trace
@log_func_args
def select_specify_condition(db_object, mode, delay, loss_rate, sdk_version=SDK_VERSION,
                             live_push_version=LIVE_PUSH_VERSION):
    """
    :param db_object:
    :param mode:
    :param delay:
    :param loss_rate:
    :param sdk_version:
    :param live_push_version:
    :return:
    """
    if MODE_UDP == mode:
        records = db_select_result(db_object, MYSQL_TABLE_NAME, "*",  delay=delay, loss_rate=loss_rate,
                                   sdk_version=sdk_version, live_push_version=live_push_version)
    else:
        records = db_select_result(db_object, MYSQL_TABLE_NAME, "*",  delay=delay, loss_rate=loss_rate, mode=mode,
                                   live_push_version=live_push_version)

    return parse_tuple_res(records, delay, loss_rate, sdk_version, live_push_version=live_push_version)


@print_trace
@log_func_args
def select_full_condition(db_object, mode, delay, loss_rate, sdk_version, live_push_version, play_duration, lf):
    """
    :param db_object:
    :param mode:
    :param delay:
    :param loss_rate:
    :param sdk_version:
    :param live_push_version:
    :param play_duration:
    :param lf:
    :return:
    """
    if mode == 'udp':
        records = db_select_result(db_object, MYSQL_TABLE_NAME, "*",  delay=delay, loss_rate=loss_rate,
                                   sdk_version=sdk_version, live_push_version=live_push_version,
                                   play_duration=play_duration, lf_number=lf)
    elif mode == 'http':
        records = db_select_result(db_object, MYSQL_TABLE_NAME, "*",  delay=delay, loss_rate=loss_rate, mode=mode,
                                   play_duration=play_duration)
    else:
        print "##################################"
        print "######   condition error    ######"
        print "##################################"
        exit(0)

    return parse_tuple_res(records, delay, loss_rate, sdk_version, live_push_version=live_push_version)


@print_trace
@log_func_args
def select_by_time(db_object, start_time, end_time):
    """
    :param db_object:
    :param start_time:
    :param end_time:
    :return:
    """
    condition = 'case_start_time >= {0} and case_start_time <= {1}'.format(start_time, end_time)
    records = db_fuzzy_select_result(db_object, MYSQL_TABLE_NAME, condition, "*")
    # print records
    return parse_tuple_time_res(records)


@print_trace
@log_func_args
def parse_tuple_time_res(tuple_records):
    """
    parse tuple and return a list
    :param tuple_records:
    """
    if tuple_records is None:
        return None

    res_list = []

    for row in tuple_records:
        index = "{0}ms_{1}%".format(row[2], row[3])
        if row[4] == MODE_UDP:
            version = "udp_" + row[5]
        else:
            version = row[4]
        first_image_time = row[7]
        buffer_time = row[8]

        record = [
            index,
            version,
            1,
            first_image_time,
            buffer_time
        ]
        # print "record:", record
        res_list.append(record)

    return res_list


@print_trace
@log_func_args
def parse_tuple_res(tuple_records, delay, loss_rate, sdk_version, live_push_version):
    """
    parse tuple and return a list
    :param tuple_records:
    :param delay:
    :param loss_rate:
    :param sdk_version:
    :param live_push_version:
    :return: res_list
    """
    if tuple_records is None:
        return None

    udp_time_list = []
    http_time_list = []
    udp_buffer_num_list = []
    http_buffer_num_list = []
    udp_p2p_list = []

    udp_sample_num = 0
    http_sample_num = 0

    print tuple_records

    for row in tuple_records:
        if MODE_UDP == row[4]:
            udp_sample_num += 1
            udp_time_list.append(row[7])
            buffer_num_tmp = row[9] / row[10] * row[8]
            udp_buffer_num_list.append(buffer_num_tmp)
            if row[12] not in ['', None]:
                p2p_percent = float(row[12])
                udp_p2p_list.append(p2p_percent)

        elif MODE_HTTP == row[4]:
            http_sample_num += 1
            http_time_list.append(row[7])
            buffer_num_tmp = row[9] / row[10] * row[8]
            http_buffer_num_list.append(buffer_num_tmp)

    # remove_max_number_of_list(udp_time_list)
    udp_average_time = Stats.avg(udp_time_list)
    http_average_time = Stats.avg(http_time_list)
    print http_time_list
    print http_average_time

    udp_buffer_num = Stats.avg(udp_buffer_num_list)
    http_buffer_num = Stats.avg(http_buffer_num_list)
    print http_buffer_num_list
    print http_buffer_num

    udp_p2p_percent_num = Stats.avg(udp_p2p_list)

    # real_udp_buffer_num = row[10] / 60.0 *
    index = "{0}ms_{1}%".format(delay, loss_rate)
    udp_sdk = "sdk_" + sdk_version + '/live_push_version' + live_push_version

    res_list = [
        index,
        udp_sdk,
        udp_sample_num,
        udp_average_time,
        udp_buffer_num,
        udp_p2p_percent_num,
        MODE_HTTP,
        http_sample_num,
        http_average_time,
        http_buffer_num
    ]
    return res_list


def remove_max_number_of_list(in_list):
    in_list.remove(Stats.maximum(in_list))
    return in_list



