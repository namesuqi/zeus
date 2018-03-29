# coding=utf-8

# jenkins master server url，port
jenkins_server_url = 'http://10.4.0.1:8080/'

# User Id API Token
user_id = 'donghao'
api_token = 'a36ea26fdd50a32f652e8d56d7cb86e3'

# job_name
job_name = [
    'p2pclient_ut',
    'BJ-Auto-Test-System_SDK_Start',
    'BJ-Auto-Test-System_SDK_Check',
    'BJ-Auto-Test_Platform_Collect_Log',
    'BJ-Auto-Test_SDK_Api',
    'BJ-Auto-Test_SDK_Penetrate',
    'BJ-Auto-Test_SDK_Routine',
    'BJ-Auto-Test_Server_API_Channel',
    'BJ-Auto-Test_Server_API_Dir',
    'BJ-Auto-Test_Server_API_Panel',
    'BJ-Auto-Test_Server_API_Report',
    'BJ-Auto-Test_Server_API_Stats',
    'BJ-Auto-Test_Server_API_Stun-hub',
    'BJ-Auto-Test_Server_API_Stun_Rrpc',
    'BJ-Auto-Test_Server_API_Stun_Stun',
    'BJ-Auto-Test_Server_API_Stun_Thunder',
    'BJ-Auto-Test_Server_API_TS',
    'BJ-Auto-Test_Zeus_Deploy',
    'p2pserver_ut'
]

# get last x bulid_times result
LAST_BUILD_TIMES = 10