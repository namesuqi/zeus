server_peer_info = {
    "peer_id": "",
    "sdk_version": "",
    "nat_type": "",
    "public_ip": "",
    "public_port": "",
    "private_ip": "",
    "private_port": "",
    "macs": ""
}

server_peer_online_time = {
    "peer_id": "",
    "quarter": 123123123123,
    "online": 1
}

server_file_seed_change = {
    "peer_id": "",
    "file_id": "",
    "operation": "",
    "slice_map": "",
    "cppc": 123
}

server_add_file = {
    "url": "",
    "file_id": "",
    "fsize": 12132131,
    "psize": 1232,
    "ppc": 12,
    "username":""
}

server_delete_file = {
    "file_id": ""
}

server_fod_report = {
    "peer_id": "",
    "fod_type": "",
    "public_ip": ""
}

server_sdk_lsm = {
    "peer_id": "",
    "public_ip": "",
    "lsm_used":131313
}
#
server_seeds_allocate = {
    "peerid": "",
    "seed_peer_id": "",
    "public_ip": "",
    "public_port": 1313,
    "private_ip": "",
    "private_port": 1313,
    "slice_map": 123123,
    "ppc": 1024
}

server_live_progress = {
    "peer_id": "",
    "public_ip": "",
    "file_id": "",
    "chunk_id": 12345
}

server_rsm_change = {
    "peer_id": "",
    "file_id": "",
    "operation": "",
    "start_chunk_id": "",
    "chunk_number": ""
}

server_rsm_reset = {
     "peer_id": ""
}

server_heartbeat = {
    "peer_id": "",
    "sdk_version": "",
    "nat_type":3,
    "public_ip": "",
    "public_port": 1313,
    "private_ip": "",
    "private_port": 1313,
}

server_live_create_channel = {
    "file_id": "",
    "file_url": "",
    "date_file_url": "",
    "rate":4086,
    "input_video_format": "",
    "output_video_format": "",
    "ppc": 123,
    "psize": 123213
}

server_live_delete_channel = {
    "file_id": ""
}

server_live_push_error = {
    "level": "",
    "module": "",
    "err_info": ""
}

server_live_push_channel ={
    "file_id": "",
    "connections": 12,
    "latest_offset": 1232131,
    "latest_chunk_id": 1232132,
    "push_chunk_id": 12312,
    "start_push_time": "",
    "push_duration": 25536
}

server_live_push_channel_count = {
    "file_count": 123,
    "file_ids": ""
}

server_add_tenant = {
    "tenant_id": "",
    "tenant_name": "",
    "groups": "",
    "peer_prefix": "",
    "domain": ""
}

server_push_error ={
    "level": "",
    "module": "",
    "err_info": ""
}

server_push_request = {
    "request_url": "",
    "response_status_code": 123123
}

server_push_memory_cache = {
    "file_id": "",
    "chunk_id": 12331,
    "behavior": "out"
}

server_push_disk_cache = {
    "universe": "",
    "file_id": "",
    "behavior": "out"
}

server_push_prefetch_task = {
    "file_id": "",
    "file_size": 1030498,
    "flag": "start"
}