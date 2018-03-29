# coding=utf-8
"""
play live channel on remote linux machines

__author__ = 'zengyuetian'

"""

import unittest
from lib.remote.remote_player import *


class TestLivePlayOnLinux(unittest.TestCase):
    ips = []
    sdk_num = 0
    urls = []

    def setUp(self):
        pass


    def tearDown(self):
        pass

    @classmethod
    def test_init_data_for_report_flow(cls):
        cls.ips = ["10.5.100.53"]
        cls.sdk_num = [5]
        cls.urls = []
        for i in range(cls.sdk_num):
            cls.urls.append("http://flv.srs.cloutropy.com/wasu/63C62873397640328337E95FBF5EF6FE.flv")
        print "init done"

    @classmethod
    def test_main_workflow(cls):
        print cls.ips
        player = RemotePlayer(cls.ips, cls.sdk_num, cls.urls, "{0}/misc/bin/live/peer/{1}".format(root, SDK_FILE))
        player.deploy_sdk()
        player.start_sdk()
        player.start_play()


if __name__ == "__main__":
    test_suite_report_flow = unittest.TestSuite()
    test_suite_report_flow.addTest(TestLivePlayOnLinux("test_init_data_for_report_flow"))
    test_suite_report_flow.addTest(TestLivePlayOnLinux("test_main_workflow"))


    runner = unittest.TextTestRunner()

    # if you want to use different test data, change from here
    runner.run(test_suite_report_flow)


    # unittest.main() # search for method name starts with "test"







