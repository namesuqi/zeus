
# post message can not contain SPACE
sdk_live_delay_version_1 = {
    "id": "",
    "timestamp": "",
    "peer_id": "",
    "file_id": "",
    "file_url": "test.funnel.requirfile.com",
    "source_type": "live_ts",
    "delays": [
        {
            "delay": 1231,
            "absolute_time": 3211
        }
    ]
}

sdk_delay_chunks_version_1 = {
    "id": "",
    "timestamp": "",
    "peer_id": "",
    "chunks": [
        {
            "file_id": "",
            "source_type": 4,
            "cid": 2311,
            "start_time": 12345,
            "end_time": 54321
        }
    ]
}

sdk_delay_items_version_1 = {
    "id": "",
    "timestamp": "",
    "peer_id": "",
    "items": [
        {
            "file_id": "",
            "source_type": "",
            "sequence": "",
            "delay": "",
            "absolute_time": ""
        }
    ]
}

sdk_push_state_version_1 = {
    "id": "",
    "timestamp": 1459307126,
    "peer_id": "",
    "file_id": "",
    "state": "200"
}

sdk_offering_version_1 = {
    "id": "",
    "timestamp": 1459307126,
    "peer_id": "",
    "rps": 100000,
    "delay": 999999,
}

sdk_qos_version_1 = {
    "id": "",
    "timestamp": "",
    "peer_id": "",
    "url": "test.cloudtropy.com",
    "vvid": "testvvid",
    "type": "live",
    "startup_delay": 5
}

sdk_vf_version_1 = {
    "id": "",
    "timestamp": "",
    "type": "hls",
    "peer_id": "",
    "downloads": [
        {
            "url": "demo.cloutropy.com/panda0002.flv",
            "vvid": "testvvid",
            "flow": [
                 {
                     "timestamp": 1414546789,
                     "duration": 60,
                     "download": 0
                 }
            ]
        }
    ]
}

sdk_vv_version_1 = {
    "id": "",
    "vvid": "testvvid",
    "timestamp": "1452483084",
    "url": "test.cloudtropy.com",
    "peer_id": "",
    "type": "vod"
}

sdk_fod_version_1 = {
    "id": "",
    "timestamp": "",
    "url": "test.cloudtropy.com",
    "fsize": 123,
    "peer_id": "",
    "fod_type": "vod"
}

sdk_flow_download_version_1 = {
    "id": "",
    "timestamp": "",
    "type": "hls",
    "peer_id": "",
    "downloads": [
        {
            "url": "demo.cloutropy.com/panda0002.flv",
            "fsize": 123123,
            "flow":
            [
                {
                    "timestamp": "",
                    "duration": 60,
                    "p2pDown": 3453,
                    "httpDown": 343
                }
            ]
        }
    ]
}

sdk_flow_upload_version_1 = {
    "id": "",
    "timestamp": "",
    "peer_id": "",
    "upload":
    [
        {
            "timestamp": 1450080435,
            "duration": 60,
            "p2pUp": 10000
        }
    ]
}

sdk_exception_version_1 = {
    "id": "",
    "timestamp": "",
    "osType": "Windows",
    "osVersion": "6.1",
    "cpuModel": "x86_64",
    "coreVersion": "1.8.0",
    "macAdress": [
        {
            "name": "win0",
            "addr": "74:D4:35:80:C0:60"
        }
    ],
    "natType": 1,
    # "publicIP": "116.231.160.155",
    "publicPort": 62367,
    "privateIP": "192.168.80.1",
    "privatePort": 62367,
    "peer_id": "",
    "op": "OP_DOWNLOAD_FILE",
    "error_code": "405"
}

sdk_performance_vod_version_1 = {
    "id": "00000000A4E351499433B371047A3856:12345678888",
    "timestamp": 1448261276971,
    "peer_id": "00000000A4E351499433B371047A3856",
    "file_id": "0A91884400001F900000004980405123",
    "duration": 96,
    "httpDown": 15219360,
    "p2pDown": 1871424,
    "url": "http://t027.vod05.icntvcdn.com/media/new/2011/10/20/hd_dy_xqnyh_20111020.ts",
    "user_name": "icntv",
    "user_agent": "YunShangSDK",
    "type": "SEED",
    "performance": {
        "startDelay": 909,
        "fwdSeeks": 0,
        "bwdSeeks": 0,
        "seekDelay": 0,
        "bufferCnt": 1,
        "chunk_num": 67,
        "chunk_avg_time": 1188,
        "chunk_max_time": 4187,
        "seeds_num": 37,
        "http_request_cnt": 14,
        "http_request_failed_cnt": 1,
        "http_request_avg_time": 296,
        "http_request_max_time": 884,
        "rq_decode_cnt": 67,
        "rq_decode_avg_time": 80,
        "rq_decode_max_time": 145,
        "seed_request_new_cnt": 1577,
        "seed_request_send_cnt": 1577,
        "seed_request_lost_cnt": 0,
        "seed_request_accept_cnt": 1541,
        "seed_request_declined_cnt": 4,
        "seed_request_cancel_cnt": 517,
        "seed_request_pieces_exp_cnt": 18924,
        "seed_request_pieces_recv_cnt": 17615,
        "seed_request_pieces_lost_cnt": 120,
        "seed_request_recv_first_piece_cnt": 1512,
        "seed_request_recv_first_piece_avg_time": 177,
        "seed_request_recv_finish_piece_cnt": 1373,
        "seed_request_recv_finish_piece_avg_time": 195,
        "bufferDelay": [
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0
        ]
    }
}

sdk_sync_time = {}