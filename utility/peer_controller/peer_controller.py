# coding=utf-8
"""
simulate background live play in production environment

"""

from lib.remote.remote_player import *

# SDK_IP_LIST = ['115.236.100.46']
"""
SDK_IP_LIST = ['222.222.12.12', '101.254.185.18', '124.68.11.169', '115.238.245.25', '103.246.152.47',
               '122.226.181.111', '60.12.69.100', '60.169.74.3', '221.203.235.2', '222.175.232.115',
               '59.63.166.73', '60.12.145.12']
SDK_NUM_LIST = [i * 3 for i in [8, 8, 4, 4, 4, 4,
                                4, 4, 8, 4, 8, 4]
                ]
"""

# 8.31 downstream bandwidth test  1 peer start
SDK_IP_LIST = ['222.222.12.12']
SDK_NUM_LIST = [50]

CHANNEL_URL = "http://flv.srs.cloutropy.com/wasu/test2222.flv"
SDK_FILE_PATH = "{0}/utility/peer_controller/{1}".format(root, SDK_FILE)
CHANNEL_URL_LIST = []


def start_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_play()
    player.stop_fake_play()

    player.stop_sdk()

    player.deploy_sdk()

    player.start_sdk()

def restart_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_play()
    player.stop_fake_play()

    player.stop_sdk()

    player.start_sdk()


def play_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.deploy_sdk()
    player.start_sdk()
    player.start_play()

def replay_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_play()
    player.stop_fake_play()

    player.stop_sdk()

    player.start_sdk()
    player.start_play()

def fake_play_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_sdk()

    player.start_sdk()
    player.start_fake_play()

def fake_replay_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_play()
    player.stop_fake_play()
    player.stop_sdk()

    player.start_sdk()
    player.start_fake_play()

def stop_test():
    for i in range(len(SDK_IP_LIST)):
        CHANNEL_URL_LIST.append(CHANNEL_URL)

    player = RemotePlayer(SDK_IP_LIST, SDK_NUM_LIST, CHANNEL_URL_LIST, SDK_FILE_PATH)
    player.stop_play()
    player.stop_fake_play()
    player.stop_sdk()

def print_help():
    print "Please use control type: [start] or [restart] or [stop] or [play] or [replay] " \
          "or [fake_play] or [fake_replay]"

###############################
# Main Function
###############################
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
    else:
        if sys.argv[1] == "start":
            start_test()
        elif sys.argv[1] == "restart":
            restart_test()
        elif sys.argv[1] == "stop":
            stop_test()
        elif sys.argv[1] == "play":
            play_test()
        elif sys.argv[1] == "replay":
            replay_test()
        elif sys.argv[1] == "fake_play":
            fake_play_test()
        elif sys.argv[1] == "fake_replay":
            fake_replay_test()
        else:
            print_help()






