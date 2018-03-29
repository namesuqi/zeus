# coding=utf-8
# author = 'donghao'
from lib.database.mysqldb import MysqlDB
from lib.special.ue.const import *
from lib.decorator.trace import *


@print_trace
@log_func_args
def db_get_current_number(obj, table):
    """
    :param obj:
    :param table:
    :return:
    """
    current_id = obj.select(table, 'count(*)')
    return current_id


@print_trace
@log_func_args
def db_add_result(obj, table, start_time, delay, loss_rate, mode, play_duration, sdk_version,
                  live_push_version, first_image_time, buffer_number, real_play_duration, band_width, p2p_percent,
                  lf_number):
    """
    往user_experience_data中插入数据
    :param obj:
    :param table:
    :param start_time:
    :param delay:
    :param loss_rate:
    :param mode:
    :param play_duration:
    :param sdk_version:
    :param live_push_version:
    :param first_image_time:
    :param buffer_number:
    :param real_play_duration:
    :param band_width:
    :param p2p_percent:
    :param lf_number:
    :return:
    """
    if mode == MODE_UDP:
        obj.insert(table, case_start_time=str(start_time), delay=int(delay), loss_rate=float(loss_rate),
                   mode=str(mode), play_duration=int(play_duration), sdk_version=str(sdk_version),
                   live_push_version=str(live_push_version), first_image_time=float(first_image_time),
                   buffer_number=float(buffer_number), real_play_duration=float(real_play_duration),
                   band_width=str(band_width), p2p_percent=p2p_percent, lf_number=lf_number)

    elif mode == MODE_HTTP:
        obj.insert(table, case_start_time=str(start_time), delay=int(delay), loss_rate=float(loss_rate),
                   mode=str(mode), play_duration=int(play_duration), sdk_version=str(sdk_version),
                   live_push_version=str(live_push_version), first_image_time=float(first_image_time),
                   buffer_number=float(buffer_number), real_play_duration=float(real_play_duration),
                   band_width=str(band_width), p2p_percent=p2p_percent, lf_number=lf_number)


@print_trace
@log_func_args
def db_select_result(obj, table, *args, **kwargs):
    """
    for the mysql standard query
    :param obj:
    :param table:
    :param args:
    :param kwargs:
    :return:
    """
    tuple_res = obj.select(table, *args, **kwargs)
    return tuple_res


@print_trace
@log_func_args
def db_fuzzy_select_result(obj, table, condition, *args):
    """
    for the fuzzy query
    :param obj:
    :param table:
    :param condition:
    :param args:
    :return:
    """
    tuple_res = obj.fuzzy_select(table, condition, *args)
    return tuple_res
