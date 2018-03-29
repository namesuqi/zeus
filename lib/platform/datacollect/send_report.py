import os
import types
from data_sent.idc_peer_connection_report import *
from data_sent.sdk_exception_version_1 import *
from data_sent.sdk_flow_download_version_1 import *
from data_sent.sdk_flow_upload_version_1 import *
from data_sent.sdk_fod_version_1 import *
from data_sent.sdk_live_delay_version_1 import *
from data_sent.sdk_offering_version_1 import *
from data_sent.sdk_performance_vod_version_1 import *
from data_sent.sdk_push_state_version_1 import *
from data_sent.sdk_qos_version_1 import *
from data_sent.sdk_vf_version_1 import *
from data_sent.sdk_vv_version_1 import *


# def send_report(task_name):
#     for pyfile in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/data_sent'):
#         if pyfile.endswith('.py') and not pyfile.startswith('__init__'):
#             tmp_module = __import__('data_sent.%s' % pyfile[:-3])
#
#     attstr = dir(tmp_module)
#     # print(attstr)
#     for astr in attstr:
#         if astr.find(task_name) > -1:
#             att = getattr(tmp_module, astr)
#             # print(att)
#             # print(type(att))
#             if type(att) == types.ModuleType:
#                 subattstr = dir(att)
#                 # print dir(att)
#                 for substr in subattstr:
#                     subatt = getattr(att, substr)
#                     # print subatt
#                     if type(subatt) == types.FunctionType and subatt.__name__ == 'send_log':
#                         subatt()
#                         break
#                 else:
#                     continue
#                 break

def send_report(task_name):
    task_object = eval(task_name + '()')
    task_object.send_log()

if __name__ == '__main__':
    # send_report('IdcPeerConnectionReport')
    send_report('SdkExceptionVersion1')
