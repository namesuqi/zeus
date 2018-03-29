# coding=utf-8
"""
deploy fake player related script to remote machines

"""

from lib.remote.remote_deployer import *

#SDK_IP_LIST = ['222.222.12.12', '101.254.185.18', '124.68.11.169', '115.238.245.25', '103.246.152.47',
#               '122.226.181.111', '60.12.69.100', '60.169.74.3', '221.203.235.2', '222.175.232.115',
#               '59.63.166.73', '60.12.145.12']

SDK_IP_LIST = ['222.222.12.12']

local_player_dir = "{0}/utility/fake_player".format(root)
remote_player_dir = "/home/admin/fake_player"

def start_deploy():
    deployer = RemoteDeployer(SDK_IP_LIST)
    deployer.deploy_folder(local_player_dir, remote_player_dir, kill_proc="python")


###############################
# Main Function
###############################
if __name__ == "__main__":
    start_deploy()





