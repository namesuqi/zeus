# coding=utf-8
"""
stats-srv related constants

__author__ = 'zsw'

"""

# BUSINESS_REPORT
MSG_ID = "9975336C362E8447BDD31034A356FF22"
PEER_ID = "6666666666ABCDEABCDEABCDE1000000"
DURATION = 300
TYPE_LIVE = "live"
TYPE_VOD = "vod"
BYTES_0 = 0

# DOWNLOADS
URL_DOWNLOADS = "http://flv.srs.cloutropy.com/wasu/test2.flv"
VVID = "A8A9C10ADE3689448070666734C5CB32"
FIRSTPLAYTIME = 0.5
BUFFERINGCOUNT = 3
TIMESTAMP_DOWNLOADS = 1450080435111
DURATION_DOWNLOADS = 60
BYTES_APP = 0
BYTES_CDN = 0
BYTES_P2P = 5000

# UPLOADS
TIMESTAMP_UPLOADS = 1450080435111
DURATION_UPLOADS = 60
BYTES_UPLOADS = 10000

# DISTRIBUTES
URL_DISTRIBUTES = "http://flv.srs.cloutropy.com/wasu/test.flv"
TIMESTAMP_DISTRIBUTES = 1450080435111
DURATION_DISTRIBUTES = 60
BYTES_DISTRIBUTES = 3000

INVALID_NUM = -1
INVALID_STR = "INVALID*"



# flow = {"timestamp": 1450080435111,
#          "duration": 60,
#          "bytes": bytes_flow}  # [timestamp, flows_duration, bytes]
# flow_downloads = {"timestamp": 1450080435111,
#                    "duration": 60,
#                    "app": bytes_app,
#                    "cdn": bytes_cdn,
#                    "p2p": bytes_p2p}
# flows = [flow, flow]
# downloads = [{"url": url,
#               "vvid": vvid,
#               "type": report_type,
#               "firstplaytime": firstplaytime,
#               "bufferingcount": bufferingcount,
#               "flows": flows}]
# uploads = {"flows": flows}
# distributes = [{"url": url, "type": report_type, "flows": flows}]
# report = {
#     "id": report_id,
#     "peer_id": peer_id,
#     "duration": duration,
#     "downloads": downloads,
#     "uploads": uploads,
#     "distributes": distributes
# }

# def flow(timestamp, duration, bytes):
#     flow = {"timestamp": timestamp,
#             "duration": duration,
#             "bytes": bytes}
#     return flow
#
# FLOW_OK = {"timestamp": 1450080435111, "duration": 60, "bytes": 0}
#
# def flow_downloads(timestamp, duration, app_bytes, cdn_bytes, p2p_bytes):
#     flow = {"timestamp": timestamp,
#             "duration": duration,
#             "app": app_bytes,
#             "cdn": cdn_bytes,
#             "p2p": p2p_bytes}
#     return flow
#
# FLOW_DOWNLOADS_OK = {"timestamp": 1450080435111, "duration": 60,
#                      "app": 0, "cdn": 0, "p2p": 0}
#
# def flows(*flowlist):
#     flows = []
#     for flow in flowlist:
#         flows.append(flow)
#     return flows
#
# FLOWS_1 = flows(FLOW_OK)
# FLOWS_2 = flows(FLOW_OK,FLOW_OK)
# FLOWS_DOWNLOADS_1 = flows(FLOW_DOWNLOADS_OK)
#
# def download(url, vvid, report_type, firstplaytime, bufferingcount,flows):
#     download = {"url": url,
#                 "vvid": vvid,
#                 "type": report_type,
#                 "firstplaytime": firstplaytime,
#                 "bufferingcount": bufferingcount,
#                 "flows": flows}
#     return download
#
# def downloads(*download_list):
#     downloads = []
#     for download in download_list:
#         downloads.append((download))
#     return downloads
