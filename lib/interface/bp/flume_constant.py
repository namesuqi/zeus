# coding=utf-8


null = None

# FlUME_HOST = "192.168.1.229"
# FLUME_PASSWORD = "admin"
FlUME_HOST = "192.168.4.229"
FLUME_USERNAME = "admin"
FLUME_PASSWORD = "admin"

# log path
FLUME_LOG_PATH = "/home/admin/logs/funnel/report.log_test"  # remote_log_path

INVALID_PEER_INFO_LOG_PATH = "/topic_data/invalid_peer_info.log"
OK_PEER_INFO_LOG_PATH = "/topic_data/ok_peer_info.log"
FLUME_PARTITION_LOG_PATH = "/topic_data/flume_partition.log"

PARTITION_LOG_TOPICS = ["user_strategy_switch",
                        "channel_strategy_switch",
                        "heartbeat",
                        "lf_report",
                        "peer_info",
                        "live_report"]

# # topic
TOPIC_LIST = ["add_file", "add_tenant", "add_tenant_domain", "bd_flow", "b_download_flow",
              "cache_report", "channel_strategy_switch", "delete_file", "download_flow", "file_seed_change",
              "fod_report", "heartbeat", "lf_report", "live_create_channel", "live_delete_channel",
              "live_progress", "live_report", "peer_info", "push_disk_cache", "push_prefetch_task",
              "push_srv_task", "qos_buffering_count", "qos_startup", "sdk_directional_task_live",
              "sdk_directional_task_vod", "sdk_lsm", "sdk_random_task_vod", "seed_flow", "seed_info",
              "upload_flow", "user_strategy_switch"]

TOPIC_PEER_INFO = "peer_info"
# 测试用topic
TEST_TOPIC_LIST = ["test_b_download_flow", "test_upload_flow", "test1_heartbeat"]

# keyword
KEYWORD_PEER_ID = "peer_id"





