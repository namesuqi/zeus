# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170813

作用: 针对单个模块的功能点的测试脚本
参数说明:
  1. <>_range 表示该字段可以为单个值, 如 1, 也可以为范围值, 如 [1, 10] (两边都取到); 处理时会处理为 [int, int]
  2. <>_random_range 表示该字段每次会获得指定范围的一个随机数, 取值方式同range (左闭右开); 处理时会处理为 float
  3. <>_unique_id 表示该字段为单个值, 用来标识不同组的数据
     (如 在prefix和suffix相同的情况下, 可以通过unique_id标识其为play节点还是lf节点, 也可以标识该组数据为哪一次测试的数据)
  4. <>_count 表示该行为的次数
  5. <>_interval 表示两次行为之间的时间间隔, 单位为秒

"""

import time

from lib.interface.strategy.lf_strategy.lib.log_handler import logger
from lib.interface.strategy.lf_strategy.lib.producer import send_peer_info, send_heartbeat, send_lf_report, send_live_report
from lib.interface.strategy.lf_strategy.lib.utility import get_p2p_ratio, get_peer_id_list, get_ssid_list, get_file_id_list
from lib.interface.strategy.lf_strategy.lib.time_handler import get_time_now, get_millisecond_now, get_second_now, to_millisecond
from lib.interface.strategy.lf_strategy.lib.kafka_handler import get_latest_schema_info
from lib.interface.strategy.lf_strategy.lib.const import TOPIC_PEER_INFO, TOPIC_HEARTBEAT, TOPIC_LF_REPORT, TOPIC_LIVE_REPORT


# ---------------------------------------------------------------------------------------------------------------------


# 用于peer模块的短时case
def once_for_peer_info(prefix_range, peer_index_range, ssid_unique_id, ts_ms=get_millisecond_now(),
                       province_id="p_1", isp_id="i_1", sdk_version="3.15.0", peer_unique_id="AB"):
    # 获取peer_id和file_id的list
    peer_id_list = get_peer_id_list(prefix_range, peer_index_range, peer_unique_id)
    ssid_list = get_ssid_list(prefix_range, peer_index_range, ssid_unique_id)

    # 获取topic的schema信息
    pi_schema, pi_schema_id = get_latest_schema_info(TOPIC_PEER_INFO)

    # 向kafka发送logs
    send_peer_info(peer_id_list, ssid_list, ts_ms, province_id, isp_id, sdk_version, pi_schema, pi_schema_id)

    # 记录logs的汇总信息
    logger.error("peer_online - send - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} \t (province, isp): {4} \
\t sdk_version: {5} \t timestamp: {6} \t type: peer_info"
                 .format(prefix_range, peer_index_range, peer_unique_id, ssid_unique_id, (province_id, isp_id),
                         sdk_version, ts_ms))


def once_for_heartbeat(prefix_range, peer_index_range, ssid_unique_id, ts_ms=get_millisecond_now(),
                       province_id="p_1", isp_id="i_1", sdk_version="3.15.0", peer_unique_id="AB"):
    # 获取peer_id和file_id的list
    peer_id_list = get_peer_id_list(prefix_range, peer_index_range, peer_unique_id)
    ssid_list = get_ssid_list(prefix_range, peer_index_range, ssid_unique_id)

    # 获取topic的schema信息
    hb_schema, hb_schema_id = get_latest_schema_info(TOPIC_HEARTBEAT)

    # 向kafka发送logs
    send_peer_info(peer_id_list, ssid_list, ts_ms, province_id, isp_id, sdk_version, hb_schema, hb_schema_id)

    # 记录logs的汇总信息
    logger.error("peer_online - send - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} \t (province, isp): {4} \
\t sdk_version: {5} \t timestamp: {6} \t type: heartbeat"
                 .format(prefix_range, peer_index_range, peer_unique_id, ssid_unique_id, (province_id, isp_id),
                         sdk_version, ts_ms))


# 用于play模块和lf模块的case
def once_for_lf_report(lf_type, prefix_range, peer_index_range, file_id_range, upload_random_range,
                       download_random_range, ts_ms=get_millisecond_now(), province_id="p_1", isp_id="i_1", op="-",
                       file_unique_id=0, peer_unique_id="C"*3):
    assert lf_type in ("lf_valid", "lf_invalid", "lf_random")

    # 获取peer_id和file_id的list
    peer_id_list = get_peer_id_list(prefix_range, peer_index_range, peer_unique_id)
    file_id_list = get_file_id_list(file_id_range, file_unique_id)

    # 获取topic的schema信息
    lf_schema, lf_schema_id = get_latest_schema_info(TOPIC_LF_REPORT)

    # 向kafka发送logs
    send_lf_report(peer_id_list, file_id_list, upload_random_range, download_random_range, ts_ms,
                   province_id, isp_id, op, lf_schema, lf_schema_id)

    # 记录logs的汇总信息
    logger.error("{0} - send - prefix: {1} \t peer_index: {2} ({3}) \t file_id: {4} ({5}) \t (province, isp): {6} \
\t op: {7} \t timestamp: {8}".format(lf_type, prefix_range, peer_index_range, peer_unique_id,
                                     file_id_range, file_unique_id, (province_id, isp_id), op, ts_ms))


def once_for_live_report(prefix_range, peer_index_range, file_id_range, p2p_ratio_random_range,
                         ts_ms=get_millisecond_now(), province_id="p_1", isp_id="i_1", op="-", p2p_enable=True,
                         file_unique_id=0, peer_unique_id="D"*3):
    # 获取peer_id和file_id的list
    peer_id_list = get_peer_id_list(prefix_range, peer_index_range, peer_unique_id)
    file_id_list = get_file_id_list(file_id_range, file_unique_id)

    # 获取topic的schema信息
    play_schema, play_schema_id = get_latest_schema_info(TOPIC_LIVE_REPORT)

    # 向kafka发送logs
    record = send_live_report(peer_id_list, file_id_list, p2p_ratio_random_range, ts_ms, province_id, isp_id,
                              op, p2p_enable, play_schema, play_schema_id)
    p2p_sum, cdn_sum = record

    # 记录logs的汇总信息
    p2p_ratio_sum = round(get_p2p_ratio(p2p_sum, cdn_sum), 3)
    logger.error("play - send - prefix: {0} \t peer_index: {1} ({2}) \t file_id: {3} ({4}) \t (province, isp): {5} \t \
p2p_ratio (p2p, cdn): {6} {7} \t op: {8} \t p2p_enable: {9} \t timestamp: {10}"
                 .format(prefix_range, peer_index_range, peer_unique_id, file_id_range, file_unique_id, (province_id,
                         isp_id), p2p_ratio_sum, (p2p_sum, cdn_sum), op, p2p_enable, ts_ms))

# ---------------------------------------------------------------------------------------------------------------------

#


# 用于blacklist模块的case
# def tt(bl_type, key_path=blacklist_src):
#     assert bl_type in ("channels", "users", "versions")
#     etcd_result = get_etcd_result(bl_type, key_path)
#     key_list = analysis_etcd_result(etcd_result, "key", True)
#     for index, key in enumerate(key_list):
#         str(key_list[index]).replace(BLACKLIST_SRC, "")
#     print key_list
#
#
# def case_for_blacklist(bl_type):
#     assert bl_type in ("channels", "users", "versions")

# read_etcd_key("users")

# ---------------------------------------------------------------------------------------------------------------------


# 用于peer模块的长时case
def peer_online(prefix_range, peer_index_range, ssid_start, start_time=get_time_now(), end_time="2020-01-01 00:00:00",
                login_count=1, login_interval=3*60, heartbeat_interval=1*60, hb_per_pi=-1, adjust_second=0,
                province_id="p_1", isp_id="i_1", sdk_version="3.15.0", peer_unique_id="AB"*3):
    """
    保持一组节点在指定时间段内在线, 可设定在线时长和在线次数
    :param prefix_range: peer_id的prefix的范围, 可以为单个值, 也可以为范围值, 如 1 或 [1, 10] (两边都取到)
    :param peer_index_range: peer_id的后缀的范围, 取值方式同上; peer_id总数为 (prefix范围 * index范围)
    :param ssid_start: int, peer_id首次登录的ssid的后缀
    :param start_time: 设定本组节点的在线的起始时间, 可以为timestamp, 也可以为"YYYY-MM-DD HH:MM:SS"格式的时间字符串
    :param end_time: 设定本组节点的在线的结束时间, 取值方式同上
    :param login_count: int, 节点在指定时间段内的登录次数
    :param login_interval: int, 节点每次登录(peer_info)的时间间隔
    :param heartbeat_interval: int, 节点每次心跳的时间间隔
    :param hb_per_pi: int, 节点每次登录的时长约为(heartbeat_interval*hb_per*pi), 注意与login_interval结合考虑
                           可以为负数, 表示不指定时长, 在指定时间内持续在线
    :param adjust_second: int, 避免策略服务器的时间与脚本所在服务器的时间存在差异, 导致用例的执行结果不符合预期;
                               根据跨天切换点进行调整, 使用例的执行结果符合预期
    :param province_id: string
    :param isp_id: string
    :param sdk_version: string
    :param peer_unique_id: int/string, 用来标识不同组节点
    :return:
    """
    # 防止输入数据错误, 导致运行失败
    assert int(login_interval) > 0 and int(heartbeat_interval) > 0 and (int(login_count) or int(hb_per_pi))
    start_ts_ms = to_millisecond(start_time) + int(adjust_second * 1000)
    end_ts_ms = to_millisecond(end_time) + int(adjust_second * 1000)
    assert start_ts_ms < end_ts_ms and (get_millisecond_now() + int(adjust_second * 1000)) < end_ts_ms

    # 获取基本信息
    peer_id_list = get_peer_id_list(prefix_range, peer_index_range, peer_unique_id)
    ssid_list = get_ssid_list(prefix_range, peer_index_range, ssid_start)

    pi_schema, pi_schema_id = get_latest_schema_info(TOPIC_PEER_INFO)
    hb_schema, hb_schema_id = get_latest_schema_info(TOPIC_HEARTBEAT)

    logger.error("peer_online - ready - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} + {4} \t (province, isp): \
{5} \t sdk_version: {6} \t time: {7} ~ {8} \t login_interval: {9}s \t ssid_duration: {10}s * {11}"
                 .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, login_count, (province_id, isp_id),
                         sdk_version, start_time, end_time, login_interval, heartbeat_interval, hb_per_pi))

    # 控制在线时长的相关参数
    time_switch = pi_switch = 0  # switch为0表示需要运行, 为1表示不需要运行
    login_round = heartbeat_round = 0
    hb_switch = 0 if int(hb_per_pi) < 0 else 1
    actual_start_time = start_tag = "***"  # 只是为了防止IDE提示语法问题

    # 准备向kafka发送数据
    while True:
        ts_s_now = get_second_now()
        ts_ms_now = get_millisecond_now()
        if start_ts_ms <= ts_ms_now <= end_ts_ms:
            # 记录起始信息
            if time_switch == 0:
                actual_start_time = get_time_now()  # 记录实际开始的时间
                start_tag = ts_s_now  # 标记实际开始的timestamp(ms)
                time_switch = 1
                logger.error("peer_online - start - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} + {4} \t \
(province, isp): {5} \t sdk_version: {6} \t login_interval: {7}s \t ssid_duration: {8}s * {9}"
                             .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, login_count,
                                     (province_id, isp_id), sdk_version, login_interval, heartbeat_interval, hb_per_pi))
            # 判断是否需要切换ssid
            if (ts_s_now - start_tag) > ((login_round + 1) * login_interval) and (login_round + 1) < int(login_count):
                login_round += 1
                ssid_list = get_ssid_list(prefix_range, peer_index_range, int(ssid_start) + login_round)
                heartbeat_round = 0
                pi_switch = 0
            try:
                # 判断是否需要发送peer_info
                if pi_switch == 0 and login_round < int(login_count):
                    send_peer_info(peer_id_list, ssid_list, ts_ms_now, province_id, isp_id,
                                   sdk_version, pi_schema, pi_schema_id)
                    logger.warning("peer_online - send - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} + {4} \t \
(province, isp): {5} \t sdk_version: {6} \t timestamp: {7} \t type: peer_info"
                                   .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, login_round,
                                           (province_id, isp_id), sdk_version, ts_ms_now))
                    pi_switch = 1
                    time.sleep(float(heartbeat_interval))
                # 判断是否需要发送heartbeat
                elif heartbeat_round < int(hb_per_pi) or hb_switch == 0:
                    send_heartbeat(peer_id_list, ssid_list, ts_ms_now, province_id, isp_id,
                                   sdk_version, hb_schema, hb_schema_id)
                    logger.warning("peer_online - send - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} + {4} \t \
(province, isp): {5} \t sdk_version: {6} \t timestamp: {7} \t type: heartbeat"
                                   .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, login_round,
                                           (province_id, isp_id), sdk_version, ts_ms_now))
                    heartbeat_round += 1
                    time.sleep(float(heartbeat_interval))
                # 不发送汇报, 等待一段时间
                else:
                    time.sleep(5)
            except Exception as e:
                logger.error("peer_online - error - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} \t -- \t {4}"
                             .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, e.message))
                time.sleep(5)
        elif start_ts_ms > ts_ms_now:
            # 在指定时间之前, 先等待一段时间
            time.sleep(10)
        else:
            # 在指定时间之后, 记录结束信息
            logger.error("peer_online - quit - prefix: {0} \t peer_index: {1} ({2}) \t ssid: {3} + {4} \t (province, \
isp): {5} \t sdk_version: {6} \t time: {7} ~ {8} \t login_interval: {9}s \t ssid_duration: {10}s * {11}"
                         .format(prefix_range, peer_index_range, peer_unique_id, ssid_start, login_count,
                                 province_id, isp_id, sdk_version, actual_start_time, get_time_now(),
                                 login_interval, heartbeat_interval, hb_per_pi))
            break

# ---------------------------------------------------------------------------------------------------------------------


# 用于channel模块计算部分的case
def keep_lf_invalid(file_range, lf_invalid_count, end_time="2020-01-01 00:00:00", lf_invalid_interval=1*60,
                    province_id="p_1", isp_id="i_1", file_unique_id=0, peer_unique_id="C"*7, **kwargs):
    """
    确保该组频道(file_id, province, isp)有无效lf节点
    :param file_range: file_id的范围, 也是peer_id的prefix的范围, 可以为单个值, 也可以为范围值, 如 1 或 [1, 10] (两边都取到)
    :param lf_invalid_count: 无效lf数, peer_id的后缀从9999999开始向下递减
    :param end_time: 设定无效lf的结束时间
    :param lf_invalid_interval: 每次汇报的时间间隔
    :param province_id:
    :param isp_id:
    :param file_unique_id: 用来标识不同组的file_id
    :param peer_unique_id: 用来标识不同组的peer_id
    :param kwargs: 预留字段
    :return:
    """
    # 防止输入数据错误, 导致运行失败
    assert int(lf_invalid_interval) > 0 and int(lf_invalid_count) > 0
    end_ts_ms = to_millisecond(end_time)
    assert get_millisecond_now() < end_ts_ms

    # 获取基本信息
    peer_index_range = [(9999999 - int(lf_invalid_count) + 1), 9999999]
    file_id_list = get_file_id_list(file_range, file_unique_id)
    peer_id_list = get_peer_id_list(file_range, peer_index_range, peer_unique_id)

    lf_schema, lf_schema_id = get_latest_schema_info(TOPIC_LF_REPORT)

    # 记录起始信息
    start_time = get_time_now()
    logger.error("lf_invalid - start - file_id: {0} ({1}) \t peer_id: {0} * {2} ({3}) \t (province, isp): \
({4}, {5}) \t".format(file_range, file_unique_id, peer_index_range, peer_unique_id, province_id, isp_id))

    # 准备向kafka发送数据
    while get_millisecond_now() < end_ts_ms:
        ts_ms_now = get_millisecond_now()
        send_lf_report(peer_id_list, file_id_list, 0, [0, 1000], ts_ms_now, province_id, isp_id,
                       "-", lf_schema, lf_schema_id)
        logger.warning("lf_invalid - send - file_id: {0} ({1}) \t peer_id: {0} * {2} ({3}) \t (province, isp): {4} \t \
timestamp: {5}".format(file_range, file_unique_id, peer_index_range, peer_unique_id, (province_id, isp_id), ts_ms_now))
        time.sleep(float(lf_invalid_interval))

    # 记录结束信息
    logger.error("lf_invalid - quit - file_id: {0} ({1}) \t peer_id: {0} * {2} ({3}) \t (province, isp): {4} \t \
time: {5} ~ {6}".format(file_range, file_unique_id, peer_index_range, peer_unique_id, (province_id, isp_id),
                        start_time, get_time_now()))


def channel_path(file_range, play_count, p2p_ratio, lf_valid_count, round_count=4, round_interval=1*60,
                 province_id="p_1", isp_id="i_1", play_start=0, lf_start=0,
                 file_unique_id=0, play_unique_id="CDDD", lf_unique_id="CDCC", **kwargs):
    """
    设定一组频道(file_id, province, isp)的play节点数, p2p_ratio, 有效lf数, 覆盖channel计算的路径
    :param file_range: file_id的范围, 也是play节点和lf节点的peer_id的prefix的范围; * 建议为单个值 *
    :param play_count: 每组频道的play节点数
    :param p2p_ratio: 每组频道的p2p占比
    :param lf_valid_count: 每组频道的有效lf数
    :param round_count: 设定发送数据的次数, 建议 (round_count * round_interval)的值在统计间隔的1~2倍之间
    :param round_interval: 发送每轮数据的时间间隔
    :param province_id:
    :param isp_id:
    :param play_start: play节点peer_id的起始值
    :param lf_start: lf节点peer_id的起始值
    :param file_unique_id: 标识不同组的file_id
    :param play_unique_id: 标识不同组的play节点
    :param lf_unique_id: 标识不同组的lf节点
    :param kwargs: 预留字段
    :return:
    """
    # 防止输入数据错误, 导致运行失败
    assert int(round_interval) > 0

    # 获取基本信息
    file_id_list = get_file_id_list(file_range, file_unique_id)
    if int(play_count) > 0:
        play_range = [int(play_start), (int(play_start) + int(play_count) - 1)]
        play_peer_id_list = get_peer_id_list(file_range, play_range, play_unique_id)
    else:
        play_range = "-"
    if int(lf_valid_count) > 0:
        lf_range = [int(lf_start), (int(lf_start) + int(lf_valid_count) - 1)]
        lf_peer_id_list = get_peer_id_list(file_range, lf_range, lf_unique_id)
    else:
        lf_range = "-"

    play_schema, play_schema_id = get_latest_schema_info(TOPIC_LIVE_REPORT)
    lf_schema, lf_schema_id = get_latest_schema_info(TOPIC_LF_REPORT)

    # 记录起始信息
    start_time = get_time_now()
    logger.error("channel - start - file_id: {0} ({1}) \t play: {0} * {2} ({3}) \t lf_valid: {0} * {4} ({5}) \t \
p2p_ratio: {6} \t (province, isp): {7}".format(file_range, file_unique_id, play_range, play_unique_id,
                                               lf_range, lf_unique_id, p2p_ratio, (province_id, isp_id)))

    # 准备向kafka发送数据
    for r in range(int(round_count)):
        ts_ms_now = get_millisecond_now()
        if int(play_count) > 0:
            record = send_live_report(play_peer_id_list, file_id_list, p2p_ratio, ts_ms_now, province_id, isp_id,
                                      "-", True, play_schema, play_schema_id)
            p2p_sum, cdn_sum = record
        if int(lf_valid_count) > 0:
            send_lf_report(lf_peer_id_list, file_id_list, [1, 1000], [0, 1000], ts_ms_now, province_id, isp_id,
                           "-", lf_schema, lf_schema_id)

        # 记录本轮的汇总信息
        p2p_ratio_sum = round(get_p2p_ratio(p2p_sum, cdn_sum), 3)
        logger.warning("channel - round {0} - file_id: {1} ({2}) \t play: {1} * {3} ({4}) \t lf_valid: {1} * {5} \
({6}) \t p2p_ratio (p2p, cdn): {7} {8} \t (province, isp): {9} \t timestamp: {10}"
                       .format(r, file_range, file_unique_id, play_range, play_unique_id, lf_range, lf_unique_id,
                               p2p_ratio_sum, (p2p_sum, cdn_sum), (province_id, isp_id), ts_ms_now))
        if (r + 1) == int(round_count):
            break
        time.sleep(float(round_interval))

    # 记录结束信息
    logger.error("channel - quit - file_id: {0} ({1}) \t play: {0} * {2} ({3}) \t lf_valid: {0} * {4} ({5}) \t \
p2p_ratio: {6} \t (province, isp): {7} \t time: {8} ~ {9}"
                 .format(file_range, file_unique_id, play_range, play_unique_id, lf_range, lf_unique_id, p2p_ratio,
                         (province_id, isp_id), start_time, get_time_now()))

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    logger.setLevel("WARN")

    # case_for_peer_info([1, 3], [1, 5], 0)

    # peer_online([1, 2], [1, 5], 1, login_interval=5*60, heartbeat_interval=10, login_count=1, hb_per_pi=-1)










