# coding=utf-8
# control sdk
# author = 'zengyuetian'
# in order to make a clean test, you'd better to reboot test machines before start test

from lib.special.ue.gateway_controller import *
from lib.special.ue.holowan.holowan_const import *
from lib.special.ue.holowan.setting_handle import delete_path, create_path, start_path, setting_path_params, \
    setting_packet_classifier
from lib.special.ue.ue_analyze_controller import *
from lib.decorator.trace import *


@print_trace
@log_func_args
def add_route(ip, dest, mask, gw, dev):
    """
    peer add route interface
    :param ip:
    :param dest:
    :param mask:
    :param gw:
    :param dev:
    :return:
    """
    route_add_gateway(ip, dest, mask, gw, eth=dev)


@print_trace
@log_func_args
def close_icmp_redirect(ip):
    """
    icmp redirect interface
    :param ip:
    :return:
    """
    icmp_redirect(ip)


@print_trace
@log_func_args
def peer_route_init(delay_time, loss_rate, band_width):
    """
    initization include set delay_time and loss_rate and live_push_ip
    :param delay_time:
    :param loss_rate:
    :param band_width:
    :param live_push_ip:
    :return:
    """
    # setup: clean network
    delete_remote_iptables(PEER_IP)
    delete_remote_iptables(LF_IP)
    delete_remote_iptables(LIVE_PUSH_IP)

    route_delete_gateway(PEER_IP, PUSH_NET, PUSH_NET_MASK, PEER_PUSH_GW_IP, PEER_PUSH_GW_ETH)
    route_delete_gateway(PEER_IP, LF_IP, PUSH_NET_MASK, PEER_PUSH_GW_IP, PEER_PUSH_GW_ETH)
    route_delete_gateway(LF_IP, PEER_IP, PUSH_NET_MASK, PEER_PUSH_GW_IP, LF_DEV)
    route_delete_gateway(LIVE_PUSH_IP, PEER_IP, PUSH_NET_MASK, PEER_PUSH_GW_IP, LIVE_PUSH_DEV)

    # set network
    add_route(PEER_IP, PUSH_NET, PUSH_NET_MASK, gw=PEER_PUSH_GW_IP, dev=PEER_ETH)
    add_route(PEER_IP, LF_IP, PUSH_NET_MASK, gw=PEER_PUSH_GW_IP, dev=PEER_ETH)
    add_route(LF_IP, PEER_IP, PUSH_NET_MASK, gw=PEER_PUSH_GW_IP, dev=LF_DEV)
    add_route(LIVE_PUSH_IP, PEER_IP, PUSH_NET_MASK, gw=PEER_PUSH_GW_IP, dev=LIVE_PUSH_DEV)

    close_icmp_redirect(PEER_IP)
    close_icmp_redirect(LF_IP)
    close_icmp_redirect(LIVE_PUSH_IP)

    gateway_package_delay_and_loss(PEER_PUSH_GW_IP, PEER_PUSH_GW_ETH, delay_time, loss_rate, band_width, LIVE_PUSH_IP)


@print_trace
@log_func_args
def set_gateway_delay(delay_time, loss_rate):

    real_delay_time = delay_time / 2 - BASIC_DELAY_TIME
    one_way_loss_rate = loss_rate / 2.0

    if real_delay_time < 0:
        real_delay_time = 0

    # have 2 review
    peer_route_init(real_delay_time, one_way_loss_rate, ACTUAL_BAND_WIDTH)


def set_delay_by_holowan(delay_time, loss_rate, bandwidth):
    real_delay_time = delay_time / 2 - BASIC_DELAY_TIME
    one_way_loss_rate = loss_rate / 2.0

    if real_delay_time < 0:
        real_delay_time = 0

    # delete path
    delete_path(path_id=PATH1_ID, path_name=PATH1_NAME)
    delete_path(path_id=PATH_FREE_ID, path_name=PATH_FREE_NAME)

    # create test path
    create_path(path_id=PATH1_ID, path_name=PATH1_NAME)
    start_path(path_id=PATH1_ID, path_name=PATH1_NAME)

    # create free path
    create_path(path_id=PATH_FREE_ID, path_name=PATH_FREE_NAME)
    start_path(path_id=PATH_FREE_ID, path_name=PATH_FREE_NAME)

    # set path params
    setting_path_params(path_id=PATH1_ID, path_name=PATH1_NAME, path_director=PATH_DIRECTOR,
                        pltr_delay_co_devalue=real_delay_time, pltr_loss_random_rate=one_way_loss_rate,
                        pltr_bandwidth_rate=bandwidth,
                        prtl_delay_co_devalue=real_delay_time, prtl_loss_random_rate=one_way_loss_rate,
                        prtl_bandwidth_rate=bandwidth)
    setting_path_params(path_id=PATH_FREE_ID, path_name=PATH_FREE_NAME, path_director=PATH_DIRECTOR,
                        pltr_delay_co_devalue=0, pltr_loss_random_rate=0, pltr_bandwidth_rate=1000,
                        prtl_bandwidth_rate=1000, prtl_loss_random_rate=0, prtl_delay_co_devalue=0)

    # set packet classifier, waiting improve
    setting_packet_classifier(src_ip=PEER_IP, dst_ip=LIVE_PUSH_IP, path_id=PATH1_ID)


if __name__ == "__main__":
    # delay = int(sys.argv[1])
    # loss = float(sys.argv[2])
    # set_gateway_delay(delay, loss)
    set_delay_by_holowan(100, 5, 2)
