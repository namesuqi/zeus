import optparse

from lib.database.mysql_db import MysqlDB
from lib.special.ue.database_controller import db_add_result
from lib.special.ue.leifeng_controller import lf_main, stop_lf
from lib.special.ue.peer_controller import get_peer_p2p
from lib.special.ue.player_controller import *
from lib.special.ue.push_controller import get_live_push_version
from lib.special.ue.sdk_controller import deploy_sdk, start_sdk, get_sdk_version, stop_sdk, back_up_log
from lib.special.ue.set_gateway import set_gateway_delay, set_delay_by_holowan


def custom_play_by_fake_play(play_mode_type, play_time, peer_ip=PEER_IP, player_ip=PEER_IP, peer_port=SDK_PORT):
    player_deploy(peer_ip)
    log_name = "{0}/{1}_{2}_buffer_count.log".format(REMOTE_PLAYER_PATH, play_mode_type, play_time)
    sdk_version = SDK_VERSION
    live_push_version = get_live_push_version(LIVE_PUSH_IP)
    p2p_percent = 0

    if play_mode_type == 'udp':
        deploy_sdk(peer_ip)
        start_sdk(peer_ip)
        sdk_version = get_sdk_version(peer_ip)
        # peer start time
        time.sleep(3)
        # peer play
        player_start(player_ip, BEIJING_URL, log_name)
        # play time
        time.sleep(play_time)
        p2p_percent = get_peer_p2p(peer_ip, peer_port)
        stop_sdk(peer_ip)
        player_stop(player_ip)

    elif play_mode_type == 'http':
        http_flv_player_start(player_ip, BEIJING_HTTP_FLV_URL, log_name)
        time.sleep(play_time)
        player_stop(player_ip)

    else:
        print "##########################################"
        print "##### play mode type is not support! #####"
        print "##########################################"
        exit(0)

    first_image_time = player_first_image_time(player_ip, log_name)
    buffer_number = player_buffering_num(player_ip, log_name)

    return first_image_time, buffer_number, sdk_version, live_push_version, p2p_percent


def main():
    time_format = '%Y%m%d%H%M%S'
    case_time = time.strftime(time_format, time.localtime())

    parser = optparse.OptionParser("Usage: %prog -p <play mode> -t <play time> -delay <gateway delay> "
                                   "-loss <gateway loss rate>")
    parser.add_option('-p', dest='play_mode_type', type='string', help='specify play mode [udp or http]')
    parser.add_option('-t', dest='play_time', type='int', help='specify play time [second]')
    parser.add_option('--delay', dest='delay_time', type='int', help='specify delay time [ms]')
    parser.add_option('--loss', dest='loss_rate', type='float', help='specify loss rate [%]')
    parser.add_option('--lf', dest='lf', type='int', help='specify LF sdk number')

    (options, args) = parser.parse_args()
    play_mode_type = options.play_mode_type
    play_time = options.play_time
    delay_time = options.delay_time
    loss_rate = options.loss_rate
    lf = options.lf

    if lf is None:
        print "NO NEED LF!"
        lf_number = 0
    else:
        print "#############################"
        print "#####  START JOIN LF... #####"
        print "#############################"
        lf_main(lf)
        print "#############################"
        print "#####  JOIN LF SUCCESS! #####"
        print "#############################"
        lf_number = lf

    # set_gateway_delay(delay_time=delay_time, loss_rate=loss_rate)
    set_delay_by_holowan(delay_time=delay_time, loss_rate=loss_rate, bandwidth=2)

    first_image_time, buffer_number, sdk_version, live_push_version, p2p_percent = \
        custom_play_by_fake_play(play_mode_type=play_mode_type, play_time=play_time)
    back_up_log(PEER_IP, case_time)

    real_play_time = play_time - first_image_time

    db_object = MysqlDB(MYSQL_HOST, MYSQL_UE_USER, MYSQL_PASSWORD, MYSQL_DB_NAME)
    db_add_result(db_object, MYSQL_TABLE_NAME, case_time, delay_time, loss_rate, play_mode_type, play_time, sdk_version,
                  live_push_version, first_image_time, buffer_number, real_play_time, ACTUAL_BAND_WIDTH, p2p_percent,
                  lf_number)

if __name__ == '__main__':
    main()
