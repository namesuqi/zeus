import os
import platform

sysstr = platform.system()

recorddate = '20160728' #it's a partition of odps tables, the date that you want to test data
recordmonth = recorddate[0:6]  #it's a partition of odps tables(part), the month that you want to test data

if sysstr == "Windows":
    folderpath = r'D:\gitCode\platform' #project folder path to compile
    commandpath = r'%s/misc/odpscmd_public/bin/odpscmd.bat' % os.path.abspath(os.path.dirname(__file__))  #odps client bat command path
    workpath = r'D:\gitCode\platform\whale\release\target\target-1.0.1-whale'   #running odps job path, the work path for AUT.
elif sysstr == "Linux":
    folderpath = r'/root/platform'  # project folder path to compile
    commandpath = r'%s/misc/odpscmd_public/bin/odpscmd' % os.path.abspath(os.path.dirname(__file__))  # odps client bat command path
    workpath = r'/root/platform/whale/release/target/target-1.0.1-whale'  # running odps job path, the work path for AUT.


configpath = r'%s/misc/cnf' % os.path.abspath(os.path.dirname(__file__)) #config file folder to insteat of those of git
exec_file = r'%s/misc/ODPS/odps_helper.jar'  % os.path.abspath(os.path.dirname(__file__))  #upload/download/sql tool for odps operation

#job name info list
HourPlayCountJob = {'name':'HourPlayCount','outputtable':'output_hour_play_count','mysqltable':'ops_play_count_hour'}
DailyPlayCountJob = {'name':'DailyPlayCount','outputtable':'output_daily_play_count','mysqltable':'ops_play_count_day'}
PeerHourPlayCountJob={'name':'PeerHourPlayCount','outputtable':'output_peer_hour_play_count','mysqltable':'ops_ppc_hour'}
ISPProvinceParseJob={'name':'ISPProvinceParse','outputtable':'output_peer_province_isp','mysqltable':'ops_user_info'}
ClientExceptionJob={'name':'ClientException','outputtable':'output_client_exception','mysqltable':'ops_client_play_errors'}
DailyStartTimeCountJob={'name':'DailyStartTimeCount','outputtable':'output_daily_start_time_count','mysqltable':'ops_play_start_time_daily'}
DailySeekTimeCountJob={'name':'DailySeekTimeCount','outputtable':'output_daily_seek_time_count','mysqltable':'ops_play_seek_time_daily'}
DailyProvinceFilePlayCountJob={'name':'DailyProvinceFilePlayCount','outputtable':'output_daily_province_file_play_count','mysqltable':'ops_province_play_count_daily'}
TodayP2PRateJob={'name':'TodayP2PRate','outputtable':'output_today_p2p_rate','mysqltable':'ops_p2p_rate'}
DailyClientErrorsStatisticsJob={'name':'DailyClientErrorsStatistics','outputtable':'output_daily_client_errors_statistics','mysqltable':'ops_errors_statistics'}
CurrentOnlinePeerDistributeJob={'name':'CurrentOnlinePeerDistribute','outputtable':'output_current_peer_online_distribute','mysqltable':'ops_current_peer_online_distribute'}
CurrentOnlineProvinceDistributeJob={'name':'CurrentOnlineProvinceDistribute','outputtable':'output_current_online_province_distribute','mysqltable':'ops_current_online_province_distribute'}
CurrentOnlineISPDistributeJob={'name':'CurrentOnlineISPDistribute','outputtable':'output_current_online_isp_distribute','mysqltable':'ops_current_online_isp_distribute'}
HourPeerOnlineDistributeJob={'name':'HourPeerOnlineDistribute','outputtable':'output_hour_peer_online_distribute','mysqltable':'ops_current_peer_online_distribute_hourly'}
DailyPeerOnlineTimeJob={'name':'DailyPeerOnlineTime','outputtable':'output_daily_peer_online_time','mysqltable':'ops_peers_average_online_time_daily'}
CurrentLivePeerOnlineCountJob={'name':'CurrentLivePeerOnlineCount','outputtable':'output_current_live_peer_online_distribute','mysqltable':'ops_current_live_peer_online_distribute'}
HourLivePeerOnlineDistributeJob={'name':'HourLivePeerOnlineDistribute','outputtable':'output_hour_live_peer_online_distribute','mysqltable':'ops_current_live_peer_online_distribute_hourly'}
DailyLivePeerActivityJob={'name':'DailyLivePeerActivity','outputtable':'output_daily_live_peer_activity','mysqltable':'ops_active_live_peers_count_daily'}
CurrentLiveRoughnessJob={'name':'CurrentLiveRoughness','outputtable':'output_current_live_roughness','mysqltable':'ops_current_live_roughness'}
DailyP2PRatePerUserJob={'name':'DailyP2PRatePerUser','outputtable':'output_daily_p2p_rate_per_user','mysqltable':'ops_p2p_rate_per_user_daily'}
DailyPeakBandWidthJob={'name':'DailyPeakBandWidth','outputtable':'output_daily_peak_bandwidth','mysqltable':'ops_peak_bandwidth_daily'}
DailyTotalFlowJob={'name':'DailyTotalFlow','outputtable':'output_daily_total_flow','mysqltable':'ops_total_flow_daily'}
FiveMinuteBandWidthJob={'name':'FiveMinuteBandWidth','outputtable':'output_bandwidth_every_five_minute','mysqltable':'ops_bandwidth_every_five_minute'}
HourFilePlayCountAccumulateModeJob={'name':'HourFilePlayCountAccumulateMode','outputtable':'output_hour_file_play_count_accumulate_mode'}
HourP2PRatePerUserJob={'name':'HourP2PRatePerUser','outputtable':'output_hour_p2p_rate_per_user','mysqltable':'ops_p2p_rate_per_user_hourly'}
HourPeakBandWidthJob={'name':'HourPeakBandWidth','outputtable':'output_hour_peak_bandwidth','mysqltable':'ops_peak_bandwidth_hourly'}
HourTotalFlowJob={'name':'HourTotalFlow','outputtable':'output_hour_total_flow','mysqltable': 'ops_total_flow_hourly'}
InputDownloadFlowJob={'name':'InputDownloadFlow','outputtable':'input_download_flow_cleaned'}
TodayFilePlayCountJob={'name':'TodayFilePlayCount','outputtable':'output_today_file_play_count','mysqltable':'ops_file_play_count_today'}
TodayP2PRatePerUserJob={'name':'TodayP2PRatePerUser','outputtable':'output_today_p2p_rate_per_user','mysqltable':'ops_p2p_rate_per_user_today'}
TodayTotalFlowJob={'name':'TodayTotalFlow','outputtable':'output_today_total_flow','mysqltable':'ops_total_flow_today'}
PeerDailyPlayCountJob={'name':'PeerDailyPlayCount','outputtable':'output_peer_daily_play_count','mysqltable':'ops_ppc_day'}
DailyFilePlayCountJob = {'name': 'DailyFilePlayCount', 'outputtable': 'output_daily_file_play_count','mysqltable':'ops_file_play_count_daily'}
WeeklyProvinceFilePlayCountJob={'name': 'WeeklyProvinceFilePlayCount', 'outputtable': 'output_weekly_province_file_play_count','mysqltable':'ops_province_play_count_weekly'}
WeeklyAverageOnlineTimeJob={'name': 'WeeklyAverageOnlineTime', 'outputtable': 'output_weekly_average_online_time','mysqltable':'ops_peers_average_online_time_weekly'}
MonthlyActivePeerCountAverageJob={'name': 'MonthlyActivePeerCountAverage', 'outputtable': 'output_monthly_active_peer_count_average','mysqltable':'ops_active_peers_count_month_average'}
MonthlyTotalFlowJob={'name': 'MonthlyTotalFlow', 'outputtable': 'output_monthly_total_flow','mysqltable':'ops_total_flow_monthly'}
MonthlyDistinctPeerIDJob = {'name': 'MonthlyDistinctPeerID', 'outputtable': 'output_monthly_distinct_peerid'}
ThirtyDaySeekTimeCountJob={'name': 'ThirtyDaySeekTimeCount', 'outputtable': 'output_previous_thirty_days_seek_time_count','mysqltable':'ops_play_seek_time_days'}
MonthlyPeakBandWidthJob={'name': 'MonthlyPeakBandWidth', 'outputtable': 'output_monthly_peak_bandwidth','mysqltable':'ops_peak_bandwidth_monthly'}
ThirtyDayStartTimeCountJob={'name': 'ThirtyDayStartTimeCount', 'outputtable': 'output_previous_thirty_days_start_time_count','mysqltable':'ops_play_start_time_days'}
MonthlyPeerActivityJob={'name': 'MonthlyPeerActivity', 'outputtable': 'output_monthly_peer_activity','mysqltable':'ops_active_peers_count_month'}
HourFilePlayCountJob = {'name': 'HourFilePlayCount', 'outputtable': 'output_hour_file_play_count','mysqltable':'ops_file_play_count_hour'}
PeerInfoRecordingJob = {'name': 'PeerInfoRecording', 'outputtable': 'output_peer_info'}
TotalPeerCountJob = {'name': 'TotalPeerCount', 'outputtable': 'output_total_peer_count','mysqltable':'ops_total_peers_count'}
DailyPeerActivityJob = {'name': 'DailyPeerActivity', 'outputtable': 'output_daily_peer_activity','mysqltable':'ops_active_peers_count_daily'}
AllPeerISPProvinceDistributeJob = {'name': 'AllPeerISPProvinceDistribute', 'outputtable': 'msqltask',
                                   'aliasname1': 'AllPeerISPProvinceDistributeISP', 'aliasname2': 'AllPeerISPProvinceDistributeProvince',
                                   'mysqltable1': 'ops_peer_isp_distribute', 'mysqltable2': 'ops_peer_province_distribute'}
FileOnDemandJob={'name':'FileOnDemand','outputtable':'input_file_on_demand_cleaned'}
InputPeerInfoJob={'name':'InputPeerInfo','outputtable':'input_peer_info_cleaned'}
InputVODPerformanceJob={'name':'InputVODPerformance','outputtable':'input_vod_performance_cleaned'}
InputClientExceptionJob={'name':'InputClientException','outputtable':'input_client_exception_cleaned'}
InputPeerOnlineTimeJob={'name':'InputPeerOnlineTime','outputtable':'input_peer_online_time_cleaned'}
InputUploadFlowJob={'name':'InputUploadFlow','outputtable':'input_upload_flow_cleaned'}
InputLiveProgress={'name':'InputLiveProgress','outputtable':'input_live_progress_cleaned'}
InputQOSBuffering={'name':'InputQOSBuffering','outputtable':'input_qos_buffering_cleaned'}
FiveMinuteAverageLiveDelayJob={'name':'FiveMinuteAverageLiveDelay','outputtable':'output_average_live_delay_every_five_minute','mysqltable':'ops_average_live_delay_every_five_minute'}
PeakBandWidthMiddleTableJob={'name':'PeakBandWidthMiddleTable','outputtable':'output_intermediate_bandwidth_every_five_minute'}
