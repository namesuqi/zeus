# coding=utf-8
# author: zengyuetian

AUTO_TEST_CASE_TAGS = ["httpdns", "channel", "ops", "stun_thunder", "stun_rrpc",
                       "stun2_udp", "kafka_flume", "ts_go", "ts_node", "stun-hub",
                       "platform_collect_sdk", "stats", "sdk", "penetrate",
                       "sdk_api", "system_check", "system_start", "sdk_init",
                       "sdk_login", "boss_internal_api", "boss_external_api"
                       ]

HERA_HOST = "10.3.0.16"
HERA_PORT = "5000"
HERA_HOME = "http://{0}:{1}/".format(HERA_HOST, HERA_PORT)
HERA_AUTO_TEST_URL = "http://{0}:{1}/auto_test".format(HERA_HOST, HERA_PORT)
URLS = ["jenkins_builds", "auto_test", "manual_test", "auto_rate"]
NAVIGATE_URLS = ["http://{0}:{1}/{2}".format(HERA_HOST, HERA_PORT, x) for x in URLS]
