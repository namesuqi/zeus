import constvars
import startodpsjob
import comparefile

print 'prepare jar to odps'
# if not preparejar.gitpullcode(constvars.folderpath):
#     quit()
# if not preparejar.mvnpackage(constvars.folderpath):
#     quit()
# perparejar.uploadjartoodps(constvars.folderpath, constvars.commandpath)

print 'perpare data upload to odps'
# createodpsdata.createalldata()
# createodpsdata.createtabledata('DownloadFlowCleaned')
# createodpsdata.createtabledata('PeerInfoCleaned')
# createodpsdata.createtabledata('FileOnDemandCleaned')
# createodpsdata.createtabledata('ClientExceptionCleaned')
# createodpsdata.createtabledata('PeerOnlineTimeCleaned')
# createodpsdata.createtabledata('QosBufferingCleaned')
# createodpsdata.createtabledata('LiveProgressCleaned')
# createodpsdata.createtabledata('UploadFlowCleaned')
# createodpsdata.createtabledata('VodPerformanceCleaned')
# createodpsdata.createtabledata('RawFileOnDemand')
# createodpsdata.createtabledata('RawDownloadFlow')
# createodpsdata.createtabledata('RawPeerInfo')
# createodpsdata.createtabledata('RawVodPerformance')
# createodpsdata.createtabledata('RawClientException')
# createodpsdata.createtabledata('RawPeerOnlineTime')



print 'make expected data'
# createodpsdata.createallexpecteddata()
# createodpsdata.createjobexpecteddata(constvars.HourPlayCountJob['name'])
# createodpsdata.createjobexpecteddata(constvars.PeerHourPlayCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.ClientExceptionJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.ClientExceptionJob['name'],['export="true"'])
# pipeofodps.downloaddatafromodps(constvars.ClientExceptionJob['outputtable'] , \
#     ( '/outputdata/%sDB.txt' % constvars.ClientExceptionJob['name']))
# comparefile.compareresultmysql(constvars.ClientExceptionJob['name'],
#                                r'select peer_id, url, op_type, err_code, err_message, err_time, mac, ip, province, isp_id, peer_prefix, play_type'
#                             r'from %s' % constvars.ClientExceptionJob['mysqltable'])
# comparefile.compareresult(constvars.ClientExceptionJob['name'])


# createodpsdata.createjobexpecteddata(constvars.DailyPlayCountJob['name'])
# createodpsdata.createjobexpecteddata(constvars.ISPProvinceParseJob['name'])
# createodpsdata.createjobexpecteddata(constvars.DailyStartTimeCountJob['name'])
# createodpsdata.createjobexpecteddata(constvars.DailySeekTimeCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.TodayP2PRateJob['name'],19)  # need index 22 ?
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayP2PRateJob['name'], ['export="true"','hour="true"','time=19'])
# comparefile.compareresultmysql(constvars.TodayP2PRateJob['name'],
#                                r'select username, url, p2p_rate, play_type '
#                             r'from %s where date_time="20160314"' % constvars.TodayP2PRateJob['mysqltable'])
# comparefile.compareresultabspatternmysql(constvars.TodayP2PRateJob['name'],
#                                r'select username, url, p2p_rate, play_type from %s where date_time=%d' % (
#                                    constvars.TodayP2PRateJob['mysqltable'], 20160314), 2, 0.17)


# createodpsdata.createjobexpecteddata(constvars.DailyProvinceFilePlayCountJob['name'])
# createodpsdata.createjobexpecteddata(constvars.CurrentOnlineProvinceDistributeJob['name'],16) # it's sql task, check data from mysql


# createodpsdata.createjobexpecteddata(constvars.CurrentOnlinePeerDistributeJob['name'], 20)  # it's sql task, check data from mysql
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentOnlinePeerDistributeJob['name'],['export="true"','hour="true"','time=20'])
# pipeofodps.downloaddatafromodps(constvars.CurrentOnlinePeerDistributeJob['outputtable'] , \
#     ('/outputdata/%sDB.txt' % constvars.CurrentOnlinePeerDistributeJob['name']))
# comparefile.compareresultlinenumber(constvars.CurrentOnlinePeerDistributeJob['name'])
# comparefile.compareresultmysql(constvars.CurrentOnlinePeerDistributeJob['name'],
#                                r'select username, online_count, play_type '
#                             r'from %s' % constvars.CurrentOnlinePeerDistributeJob['mysqltable'])


# createodpsdata.createjobexpecteddata(constvars.DailyClientErrorsStatisticsJob['name'])  # it's sql task, check data from mysql
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyClientErrorsStatisticsJob['name'],['export="true"'])
# pipeofodps.downloaddatafromodps(constvars.DailyClientErrorsStatisticsJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyClientErrorsStatisticsJob['name']))
# comparefile.compareresultmysql(constvars.DailyClientErrorsStatisticsJob['name'],
#                                r'select peer_prefix, err_type, error_count, play_type '
#                             r'from %s where date_time="20160314"' % constvars.DailyClientErrorsStatisticsJob['mysqltable'])
# comparefile.compareresult(constvars.DailyClientErrorsStatisticsJob['name'])


# createodpsdata.createjobexpecteddata(constvars.CurrentOnlineISPDistributeJob['name'], 15) # it's sql task, check data from mysql
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentOnlineISPDistributeJob['name'],['export="true"','hour="true"','time=15'])
# pipeofodps.downloaddatafromodps(constvars.CurrentOnlineISPDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentOnlineISPDistributeJob['name']))
# comparefile.compareresult(constvars.CurrentOnlineISPDistributeJob['name'])
# comparefile.compareresultmysql(constvars.CurrentOnlineISPDistributeJob['name'],
#                                r'select isp, username, online_count, play_type '
#                             r'from %s' % constvars.CurrentOnlineISPDistributeJob['mysqltable'])

# createodpsdata.createjobexpecteddata(constvars.CurrentLivePeerOnlineCountJob['name'],15) # it's sql task, check data from mysql
# createodpsdata.createjobexpecteddata(constvars.DailyPeakBandWidthJob['name']) # output data in mysql, not middle table in odps
# createodpsdata.createjobexpecteddata(constvars.DailyLivePeerActivityJob['name'])
# createodpsdata.createjobexpecteddata(constvars.HourLivePeerOnlineDistributeJob['name'],15)



# createodpsdata.createjobexpecteddata(constvars.HourPeerOnlineDistributeJob['name'],19)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPeerOnlineDistributeJob['name'],['export="true"','hour="true"','time=19'])
# pipeofodps.downloaddatafromodps(constvars.HourPeerOnlineDistributeJob['outputtable'] , \
#     ('/outputdata/%sDB.txt' % constvars.HourPeerOnlineDistributeJob['name']))
# comparefile.compareresult(constvars.HourPeerOnlineDistributeJob['name'])


# createodpsdata.createjobexpecteddata(constvars.CurrentLiveRoughnessJob['name'],23) #precision problem  # if run in python mode(use mysql language to download and compare in local), partitions in mysql accordingly should be cleaned in advance
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentLiveRoughnessJob['name'],['export="true"','hour="true"','time=23'])
# pipeofodps.downloaddatafromodps(constvars.CurrentLiveRoughnessJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentLiveRoughnessJob['name']))
# comparefile.compareresultpattern(constvars.CurrentLiveRoughnessJob['name'], '.*%s.*', 1, 3)
# comparefile.compareresultabspatternmysql(constvars.CurrentLiveRoughnessJob['name'],
#                                r'select peer_prefix,roughness,five_minute_index,play_type '
#                             r'from %s where date_time=20160314' % constvars.CurrentLiveRoughnessJob['mysqltable'], 1, 0.001)

# createodpsdata.createjobexpecteddata(constvars.DailyP2PRatePerUserJob['name']) #precision problem
# createodpsdata.createjobexpecteddata(constvars.DailyTotalFlowJob['name'])
# createodpsdata.createjobexpecteddata(constvars.HourP2PRatePerUserJob['name'], 22)


# createodpsdata.createjobexpecteddata(constvars.HourPeakBandWidthJob['name'], 22) # precision problem
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPeakBandWidthJob['name'],['hour="true"','time=22'])
# pipeofodps.downloaddatafromodps(constvars.HourPeakBandWidthJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.HourPeakBandWidthJob['name']))
# comparefile.compareresultpattern(constvars.HourPeakBandWidthJob['name'], '.*%s.*', 2, 4)
# comparefile.compareresultabspatternmysql(constvars.HourPeakBandWidthJob['name'],
#                                r'select hour, username, peak_band_width, play_type from %s where date_time=%d' % (
#                                    constvars.HourPeakBandWidthJob['mysqltable'], 20160314), 2, 0.01)

# createodpsdata.createjobexpecteddata(constvars.HourPeakBandWidthJob['name'], 22)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.dropodpsdata(constvars.HourPeakBandWidthJob['outputtable'])
# startodpsjob.operatemysqldata('delete from %s where date_time="20160514"' % constvars.HourPeakBandWidthJob['mysqltable'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPeakBandWidthJob['name'],['hour="true"','time=22','export=true'])
# pipeofodps.downloaddatafromodps(constvars.HourPeakBandWidthJob['outputtable'], ('/outputdata/%sDB.txt' % constvars.HourPeakBandWidthJob['name']))
# comparefile.compareresultpatternlistmysql(constvars.HourPeakBandWidthJob['name'],
#                                r'select timestamp, username, total_bandwidth, cdn_bandwidth, p2p_bandwidth, play_type from %s where date_time=%d' % (
#                                    constvars.HourPeakBandWidthJob['mysqltable'], 20160514), '.*%s.*', [2,3,4], [3,3,3])

# startodpsjob.dropodpsdata(constvars.PeakBandWidthMiddleTableJob['outputtable'])
# for i in range(24):
#     startodpsjob.startodpsjob(constvars.workpath, constvars.FiveMinutePeakBandWidthJob['name'], ['hour="true"','time=%d'%i])
# createodpsdata.createjobexpecteddata(constvars.DailyPeakBandWidthJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.dropodpsdata(constvars.DailyPeakBandWidthJob['outputtable'])
# startodpsjob.operatemysqldata('delete from %s where date_time="20160514"' % constvars.DailyPeakBandWidthJob['mysqltable'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPeakBandWidthJob['name'],['hour="true"','export=true'])
# pipeofodps.downloaddatafromodps(constvars.HourPeakBandWidthJob['outputtable'], ('/outputdata/%sDB.txt' % constvars.HourPeakBandWidthJob['name']))
# comparefile.compareresultpatternlistmysql(constvars.DailyPeakBandWidthJob['name'],
#                                r'select username, total_bandwidth, cdn_bandwidth, p2p_bandwidth, play_type from %s where date_time=%d' % (
#                                    constvars.DailyPeakBandWidthJob['mysqltable'], 20160514), '.*%s.*', [1,2,3], [3,3,3])


# createodpsdata.createjobexpecteddata(constvars.MonthlyPeakBandWidthJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.dropodpsdata(constvars.MonthlyPeakBandWidthJob['outputtable'])
# startodpsjob.operatemysqldata('delete from %s where month="201605"' % constvars.MonthlyPeakBandWidthJob['mysqltable'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeakBandWidthJob['name'],['exectime=201605','partitiontype=month','export=true'])
# pipeofodps.downloaddatafromodps(constvars.HourPeakBandWidthJob['outputtable'], ('/outputdata/%sDB.txt' % constvars.HourPeakBandWidthJob['name']))
# comparefile.compareresultpatternlistmysql(constvars.MonthlyPeakBandWidthJob['name'],
#                                r'select username, total_bandwidth, cdn_bandwidth, p2p_bandwidth, play_type from %s where month=%d' % (
#                                    constvars.MonthlyPeakBandWidthJob['mysqltable'], 201605), '.*%s.*', [1,2,3], [3,3,3])


# createodpsdata.createjobexpecteddata(constvars.HourTotalFlowJob['name'], 11)

# createodpsdata.createjobexpecteddata(constvars.InputDownloadFlowJob['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputDownloadFlowJob['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.InputDownloadFlowJob['outputtable'],
#     ( '/outputdata/%sDB.txt' % constvars.InputDownloadFlowJob['name']))
# comparefile.compareresultlinenumber(constvars.InputDownloadFlowJob['name'])


# createodpsdata.createjobexpecteddata(constvars.FileOnDemandJob['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.FileOnDemandJob['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.FileOnDemandJob['outputtable'],
#     ( '/outputdata/%sDB.txt' % constvars.FileOnDemandJob['name']))
# comparefile.compareresultlinenumber(constvars.FileOnDemandJob['name'])


# createodpsdata.createjobexpecteddata(constvars.InputPeerInfoJob['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputPeerInfoJob['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.InputPeerInfoJob['outputtable'],
#     ( '/outputdata/%sDB.txt' % constvars.InputPeerInfoJob['name']))
# comparefile.compareresultlinenumber(constvars.InputPeerInfoJob['name'])


# createodpsdata.createjobexpecteddata(constvars.InputVODPerformanceJob['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputVODPerformanceJob['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.InputVODPerformanceJob['outputtable'],
#     ('/outputdata/%sDB.txt' % constvars.InputVODPerformanceJob['name']))
# comparefile.compareresultlinenumber(constvars.InputVODPerformanceJob['name'])


# createodpsdata.createjobexpecteddata(constvars.InputClientExceptionJob['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputClientExceptionJob['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.InputClientExceptionJob['outputtable'],
#     ('/outputdata/%sDB.txt' % constvars.InputClientExceptionJob['name']))
# comparefile.compareresultlinenumber(constvars.InputClientExceptionJob['name'])


# createodpsdata.createjobexpecteddata(constvars.InputPeerOnlineTime['name'])    #cleanup job
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputPeerOnlineTime['name'], ['hour="true"','time=23','cleanup="true"']) # it's a cleanup job
# pipeofodps.downloaddatafromodps(constvars.InputPeerOnlineTime['outputtable'],
#     ('/outputdata/%sDB.txt' % constvars.InputPeerOnlineTime['name']))
# comparefile.compareresultlinenumber(constvars.InputPeerOnlineTime['name'])



# createodpsdata.createjobexpecteddata(constvars.FiveMinutePeakBandWidthJob['name'], 22)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.dropodpsdata(constvars.PeakBandWidthMiddleTableJob['outputtable'])
# startodpsjob.operatemysqldata('delete from %s where date_time="20160514"' % constvars.FiveMinutePeakBandWidthJob['mysqltable'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.FiveMinutePeakBandWidthJob['name'], ['hour="true"','time=22','export=true'])
# comparefile.compareresultpatternlistmysql(constvars.FiveMinutePeakBandWidthJob['name'],
#                                        r'select timestamp, username, total_bandwidth, p2p_bandwidth, cdn_bandwidth, play_type '
#                                    r'from %s where date_time="20160514"' % constvars.FiveMinutePeakBandWidthJob['mysqltable'],
#                                           '.*%s.*', [2,3,4], [3,3,3])
a = comparefile.compareresultabspatternlistmysql(constvars.FiveMinutePeakBandWidthJob['name'],
                                       r'select timestamp, username, total_bandwidth, p2p_bandwidth, cdn_bandwidth, play_type '
                                   r'from %s where date_time="20160514"' % constvars.FiveMinutePeakBandWidthJob['mysqltable'],
                                          [2,3,4], 0.1)
print a

# createodpsdata.createjobexpecteddata(constvars.HourFilePlayCountAccumulateModeJob['name'], 21)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourFilePlayCountAccumulateModeJob['name'],['hour="true"','time=21'])
# pipeofodps.downloaddatafromodpsnoprefix(constvars.HourFilePlayCountAccumulateModeJob['outputtable'],
#     ( '/outputdata/%sDB.txt' % constvars.HourFilePlayCountAccumulateModeJob['name']))
# comparefile.compareresult(constvars.HourFilePlayCountAccumulateModeJob['name'])


# createodpsdata.createjobexpecteddata(constvars.TodayFilePlayCountJob['name'],21)   # execute after the job: HourFilePlayCountAccumulateModeJob
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayFilePlayCountJob['name'],['hour="true"','time=21'])
# pipeofodps.downloaddatafromodps(constvars.TodayFilePlayCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.TodayFilePlayCountJob['name']))
# comparefile.compareresult(constvars.TodayFilePlayCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.TodayTotalFlowJob['name'], 23)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayTotalFlowJob['name'],['hour="true"','time=23'])
# pipeofodps.downloaddatafromodps(constvars.TodayTotalFlowJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.TodayTotalFlowJob['name']))
# comparefile.compareresult(constvars.TodayTotalFlowJob['name'])


# createodpsdata.createjobexpecteddata(constvars.TodayP2PRatePerUserJob['name'], 23)   # precision problem
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayP2PRatePerUserJob['name'],['export="true"','hour="true"','time=23'])
# pipeofodps.downloaddatafromodps(constvars.TodayP2PRatePerUserJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.TodayP2PRatePerUserJob['name']))
# comparefile.compareresultpattern(constvars.TodayP2PRatePerUserJob['name'], '.*%s.*', 1, 2)
# comparefile.compareresultabspatternmysql(constvars.TodayP2PRatePerUserJob['name'],
#                                r'select username, p2p_rate, play_type from %s where date_time=%d' % (
#                                    constvars.TodayP2PRatePerUserJob['mysqltable'], 20160314), 1, 0.05)


# createodpsdata.createjobexpecteddata(constvars.PeerDailyPlayCountJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.PeerDailyPlayCountJob['name'])
# pipeofodps.downloaddatafromodps(constvars.PeerDailyPlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.PeerDailyPlayCountJob['name']))
# comparefile.compareresult(constvars.PeerDailyPlayCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.DailyFilePlayCountJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyFilePlayCountJob['name'])
# pipeofodps.downloaddatafromodps(constvars.DailyFilePlayCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyFilePlayCountJob['name']))
# comparefile.compareresultpattern(constvars.DailyFilePlayCountJob['name'], '.*%s.*', 2, 7)


# createodpsdata.createjobexpecteddata(constvars.DailyPeerOnlineTimeJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPeerOnlineTimeJob['name'],['export="true"'])
# pipeofodps.downloaddatafromodps(constvars.DailyPeerOnlineTimeJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyPeerOnlineTimeJob['name']))
# comparefile.compareresultpattern(constvars.DailyPeerOnlineTimeJob['name'], '.*%s.*', 1, 5)
# comparefile.compareresultlinenumbermysql(constvars.DailyPeerOnlineTimeJob['name'],
#                                r'select peer_prefix, average_online_time, play_type from %s where date_time=%d' % (
#                                    constvars.DailyPeerOnlineTimeJob['mysqltable'], int(constvars.recorddate)))

# createodpsdata.createjobexpecteddata(constvars.HourFilePlayCountJob['name'], 21)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourFilePlayCountJob['name'], ['hour="true"','time=21'])
# pipeofodps.downloaddatafromodps(constvars.HourFilePlayCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourFilePlayCountJob['name']))
# comparefile.compareresult(constvars.HourFilePlayCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.PeerInfoRecordingJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.PeerInfoRecordingJob['name'])
# pipeofodps.downloaddatafromodps(constvars.PeerInfoRecordingJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.PeerInfoRecordingJob['name']))
# comparefile.compareresultlinenumber(constvars.PeerInfoRecordingJob['name'])


# createodpsdata.createjobexpecteddata(constvars.TotalPeerCountJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.TotalPeerCountJob['name'])
# pipeofodps.downloaddatafromodps(constvars.TotalPeerCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.TotalPeerCountJob['name']))
# comparefile.compareresult(constvars.TotalPeerCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.DailyPeerActivityJob['name'], 21)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPeerActivityJob['name'], ['hour="true"','time=21'])
# pipeofodps.downloaddatafromodps(constvars.DailyPeerActivityJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyPeerActivityJob['name']))
# comparefile.compareresult(constvars.DailyPeerActivityJob['name'])


# createodpsdata.createjobexpecteddata(constvars.WeeklyProvinceFilePlayCountJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.WeeklyProvinceFilePlayCountJob['name'],['exectime="20160320"','export="true"'])# stored in 20160314 Monday
# pipeofodps.downloaddatafromodps(constvars.WeeklyProvinceFilePlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.WeeklyProvinceFilePlayCountJob['name']))
# comparefile.compareresult(constvars.WeeklyProvinceFilePlayCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.WeeklyAverageOnlineTimeJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.WeeklyAverageOnlineTimeJob['name'],['exectime="20160320"','export="true"'])# stored in 20160320 Sunday
# pipeofodps.downloaddatafromodps(constvars.WeeklyAverageOnlineTimeJob['outputtable'] , \
#     ('/outputdata/%sDB.txt' % constvars.WeeklyAverageOnlineTimeJob['name']), 6)
# comparefile.compareresultpattern(constvars.WeeklyAverageOnlineTimeJob['name'],'.*%s.*', 1, 5)


# createodpsdata.createjobexpecteddata(constvars.MonthlyActivePeerCountAverageJob['name'])  # follow the task DailyPeerOnlineTime  # precision problem
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyActivePeerCountAverageJob['name'],['exectime="201603"','partitiontype="month"'])
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyActivePeerCountAverageJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyActivePeerCountAverageJob['name']),
#                                          'month=201603')
# comparefile.compareresultpattern(constvars.MonthlyActivePeerCountAverageJob['name'],'.*%s.*', 1, 1)
# comparefile.compareresultabspatternmysql(constvars.MonthlyActivePeerCountAverageJob['name'],
#                                r'select peer_prefix, active_count, play_type from %s where month_time=%d' % (
#                                    constvars.MonthlyActivePeerCountAverageJob['mysqltable'], 201603), 1, 2)


# createodpsdata.createjobexpecteddata(constvars.MonthlyTotalFlowJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyTotalFlowJob['name'],['exectime="201603"','partitiontype="month"','export="true"'])
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyTotalFlowJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyTotalFlowJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyTotalFlowJob['name'])


# createodpsdata.createjobexpecteddata(constvars.MonthlyDistinctPeerIDJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyDistinctPeerIDJob['name'])
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyDistinctPeerIDJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyDistinctPeerIDJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyDistinctPeerIDJob['name'])


# createodpsdata.createjobexpecteddata(constvars.ThirtyDayStartTimeCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.ThirtyDayStartTimeCountJob['name'] ,['export="true"'])
# pipeofodps.downloaddatafromodps(constvars.ThirtyDayStartTimeCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ThirtyDayStartTimeCountJob['name']))
# comparefile.compareresult(constvars.ThirtyDayStartTimeCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.ThirtyDaySeekTimeCountJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.ThirtyDaySeekTimeCountJob['name'] ,['export="true"'])
# pipeofodps.downloaddatafromodps(constvars.ThirtyDaySeekTimeCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ThirtyDaySeekTimeCountJob['name']))
# comparefile.compareresult(constvars.ThirtyDaySeekTimeCountJob['name'])


# createodpsdata.createjobexpecteddata(constvars.MonthlyPeakBandWidthJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeakBandWidthJob['name'],['exectime="201603"','partitiontype="month"','export="true"'])
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyPeakBandWidthJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyPeakBandWidthJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyPeakBandWidthJob['name'])


# createodpsdata.createjobexpecteddata(constvars.MonthlyPeerActivityJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeerActivityJob['name'],['exectime="201603"','partitiontype="month"'])
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyPeerActivityJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyPeerActivityJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyPeerActivityJob['name'])


# createodpsdata.createjobexpecteddata(constvars.AllPeerISPProvinceDistributeJob['name'])
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.operatemysqldata(r'delete from %s' % constvars.AllPeerISPProvinceDistributeJob['mysqltable1'])
# startodpsjob.operatemysqldata(r'delete from %s' % constvars.AllPeerISPProvinceDistributeJob['mysqltable2'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.AllPeerISPProvinceDistributeJob['name'], ['export=true'])
# comparefile.compareresultmysql(constvars.AllPeerISPProvinceDistributeJob['aliasname1'],
#                                r'-- select username, isp, total_count from %s' % constvars.AllPeerISPProvinceDistributeJob['mysqltable1'])
# comparefile.compareresultmysql(constvars.AllPeerISPProvinceDistributeJob['aliasname2'],
#                                r'-- select username, province, total_count from %s' % constvars.AllPeerISPProvinceDistributeJob['mysqltable2'])


# createodpsdata.createtabledata('RawLiveDelay')
# createodpsdata.createjobexpecteddata(constvars.FiveMinuteAverageLiveDelayJob['name'], 19)
# startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.operatemysqldata(r'delete from %s where date_time=%d' % (constvars.FiveMinuteAverageLiveDelayJob['mysqltable'],
#                                                                       int(constvars.recorddate)))
# startodpsjob.startodpsjob(constvars.workpath, constvars.FiveMinuteAverageLiveDelayJob['name'],
#                           ['export=true', 'hour=true', 'time=19'])
# comparefile.compareresultmysql(constvars.FiveMinuteAverageLiveDelayJob['name'],
#                                r'select username, five_minute_index, average_delay from %s where date_time=%d' % (
#                                    constvars.FiveMinuteAverageLiveDelayJob['mysqltable'], int(constvars.recorddate)))



print 'run odps job'
startodpsjob.perpareconfig(constvars.workpath, constvars.configpath)
# startodpsjob.startodpsjob(constvars.workpath, constvars.InputDownloadFlowJob['name'], hour='true', time=23, cleanup='true') # it's a cleanup job

# startodpsjob.startodpsjob(constvars.workpath, constvars.ClientExceptionJob['name'],['export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPlayCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPlayCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyProvinceFilePlayCountJob['name'],['export="true"','hour="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailySeekTimeCountJob['name'],['export="true"','hour="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyStartTimeCountJob['name'],['export="true"','hour="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.ISPProvinceParseJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.PeerHourPlayCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyClientErrorsStatisticsJob['name'],['export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentOnlinePeerDistributeJob['name'],['export="true"','hour="true"','time=21'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentOnlineProvinceDistributeJob['name'],['export="true"','hour="true"','time=16'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentOnlineISPDistributeJob['name'],['export="true"','hour="true"','time=15'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPeerOnlineDistributeJob['name'],['export="true"','hour="true"','time=19'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPeerOnlineTimeJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentLivePeerOnlineCountJob['name'],['export="true"','hour="true"','time=15'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourLivePeerOnlineDistributeJob['name'],export='true',hour='true',time=15)
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyLivePeerActivityJob['name'],['export="true"','hour="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.CurrentLiveRoughnessJob['name'],['export="true"','hour="true"','time=23'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyP2PRatePerUserJob['name'],export='true')
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyPeakBandWidthJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyTotalFlowJob['name'])
# for i in range(24):
#     startodpsjob.startodpsjob(constvars.workpath, constvars.FiveMinutePeakBandWidthJob['name'], hour='true', time=i)
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourFilePlayCountAccumulateModeJob['name'],['hour="true"','time=21'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourP2PRatePerUserJob['name'],['hour="true"','time=22'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourPeakBandWidthJob['name'],['hour="true"','time=22'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.HourTotalFlowJob['name'],['export="true"','hour="true"','time=11'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayFilePlayCountJob['name'],['hour="true"','time=21'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayP2PRateJob['name'], ['export="true"','hour="true"', 'time=22'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayTotalFlowJob['name'],['hour="true"','time=23'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.TodayP2PRatePerUserJob['name'],['hour="true"','time=23'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.PeerDailyPlayCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.DailyFilePlayCountJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.WeeklyProvinceFilePlayCountJob['name'],['exectime="20160320"','export="true"'])# stored in 20160314 Monday
# startodpsjob.startodpsjob(constvars.workpath, constvars.WeeklyAverageOnlineTimeJob['name'],['exectime="20160320"','export="true"'])# stored in 20160320 Sunday
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyActivePeerCountAverageJob['name'],['exectime="201603"','partitiontype="month"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyTotalFlowJob['name'],['exectime="201603"','partitiontype="month"','export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyDistinctPeerIDJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeerActivityJob['name'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.ThirtyDayStartTimeCountJob['name'] ,['export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.ThirtyDaySeekTimeCountJob['name'] ,['export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeakBandWidthJob['name'],['exectime="201603"','partitiontype="month"','export="true"'])
# startodpsjob.startodpsjob(constvars.workpath, constvars.MonthlyPeerActivityJob['name'],['exectime="201603"','partitiontype="month"'])


print 'download date and check'
# pipeofodps.downloaddatafromodps(constvars.ClientExceptionJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ClientExceptionJob['name']))
# comparefile.compareresult(constvars.ClientExceptionJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.HourPlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourPlayCountJob['name']))
# comparefile.compareresult(constvars.HourPlayCountJob['name'])
# comparefile.compareresultmysql(constvars.HourTotalFlowJob['name'],
#                                r'select hour, username, cdn_download, p2p_download, total_download, upload, play_type '
#                                r'from %s where date_time="20160314" and hour=11' % constvars.HourTotalFlowJob['mysqltable'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyPlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyPlayCountJob['name']))
# comparefile.compareresult(constvars.DailyPlayCountJob['name'])

#
# pipeofodps.downloaddatafromodps(constvars.DailyProvinceFilePlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyProvinceFilePlayCountJob['name']))
# comparefile.compareresultmysql(constvars.DailyProvinceFilePlayCountJob['name'],
#                                r'select province, username, play_count, play_type '
#                             r'from %s where date_time="20160314"' % constvars.DailyProvinceFilePlayCountJob['mysqltable'])
#
# pipeofodps.downloaddatafromodps(constvars.DailySeekTimeCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailySeekTimeCountJob['name']))
# comparefile.compareresult(constvars.DailySeekTimeCountJob['name'])
# comparefile.compareresultmysql(constvars.DailySeekTimeCountJob['name'],
#                                r'select peer_prefix,seek_time,seek_count,play_type '
#                                r'from %s where date_time="20160314" ' % constvars.DailySeekTimeCountJob['mysqltable'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyStartTimeCountJob['outputtable'] ,(os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyStartTimeCountJob['name']))
# comparefile.compareresultmysql(constvars.DailyStartTimeCountJob['name'],
#                                r'select peer_prefix,start_time,play_count,play_type '
#                                r'from %s where date_time="20160314" ' % constvars.DailyStartTimeCountJob['mysqltable'])
# comparefile.compareresult(constvars.DailyStartTimeCountJob['name'])

# pipeofodps.downloaddatafromodps(constvars.ISPProvinceParseJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ISPProvinceParseJob['name']))
# comparefile.compareresultpattern(constvars.ISPProvinceParseJob['name'], '.*%s.*', 12, 1)
# comparefile.compareresultlinenumbermysql(constvars.ISPProvinceParseJob['name'],
#                                          r'select peer_id, yunshang_core, ip, mac, os_version, cpu, province, isp_id, os_type '
#                                          r'from %s ' % constvars.ISPProvinceParseJob['mysqltable'])
#
# pipeofodps.downloaddatafromodps(constvars.PeerHourPlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.PeerHourPlayCountJob['name']))
# comparefile.compareresult(constvars.PeerHourPlayCountJob['name'])
# comparefile.compareresultmysql(constvars.PeerHourPlayCountJob['name'],
#                                r'select peer_id,hour_time,play_count,play_type '
#                                r'from %s where date_time="20160314"' % constvars.PeerHourPlayCountJob['mysqltable'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyClientErrorsStatisticsJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyClientErrorsStatisticsJob['name']))
# comparefile.compareresult(constvars.DailyClientErrorsStatisticsJob['name'])
# comparefile.compareresultmysql(constvars.DailyClientErrorsStatisticsJob['name'],
#                                r'select peer_prefix, err_type, error_count, play_type '
#                                r'from %s where date_time="20160314"' % constvars.DailyClientErrorsStatisticsJob['mysqltable'])


# pipeofodps.downloaddatafromodps(constvars.CurrentOnlinePeerDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentOnlinePeerDistributeJob['name']))
# comparefile.compareresult(constvars.CurrentOnlinePeerDistributeJob['name'])

# pipeofodps.downloaddatafromodps(constvars.CurrentOnlineProvinceDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentOnlineProvinceDistributeJob['name']))
# comparefile.compareresult(constvars.CurrentOnlineProvinceDistributeJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.CurrentOnlineISPDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentOnlineISPDistributeJob['name']))
# comparefile.compareresult(constvars.CurrentOnlineISPDistributeJob['name'])
# comparefile.compareresultmysql(constvars.CurrentOnlineISPDistributeJob['name'],
#                                r'select isp, username, online_count, play_type '
#                                r'from %s' % constvars.CurrentOnlineISPDistributeJob['mysqltable'])

# pipeofodps.downloaddatafromodps(constvars.HourPeerOnlineDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourPeerOnlineDistributeJob['name']))
# comparefile.compareresult(constvars.HourPeerOnlineDistributeJob['name'])
# comparefile.compareresultmysql(constvars.HourPeerOnlineDistributeJob['name'],
#                                r'select hour, username, online_count, play_type '
#                                r'from %s where date_time="20160314" and hour=19' % constvars.HourPeerOnlineDistributeJob['mysqltable'])

#
# pipeofodps.downloaddatafromodps(constvars.DailyPeerOnlineTimeJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyPeerOnlineTimeJob['name']))
# comparefile.compareresultpattern(constvars.DailyPeerOnlineTimeJob['name'], '.*%s.*', 1, 5)
#
# pipeofodps.downloaddatafromodps(constvars.CurrentLivePeerOnlineCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentLivePeerOnlineCountJob['name']))
# comparefile.compareresultmysql(constvars.CurrentLivePeerOnlineCountJob['name'],
#                                r'select username, online_count, play_type '
#                                 r'from %s where date_time="20160314"and hour=15 ' % constvars.CurrentLivePeerOnlineCountJob['mysqltable'])
# comparefile.compareresult(constvars.CurrentLivePeerOnlineCountJob['name'])
# #
# pipeofodps.downloaddatafromodps(constvars.HourLivePeerOnlineDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourLivePeerOnlineDistributeJob['name']))
# comparefile.compareresult(constvars.HourLivePeerOnlineDistributeJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyLivePeerActivityJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyLivePeerActivityJob['name']))
# comparefile.compareresultmysql(constvars.DailyLivePeerActivityJob['name'],
#                                r'select peer_prefix, active_count, play_type '
#                                 r'from %s where date_time="20160314" ' % constvars.DailyLivePeerActivityJob['mysqltable'])
# comparefile.compareresult(constvars.DailyLivePeerActivityJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.CurrentLiveRoughnessJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentLiveRoughnessJob['name']))
# comparefile.compareresultpattern(constvars.CurrentLiveRoughnessJob['name'], '.*%s.*', 1, 3)
# comparefile.compareresultpatternmysql(constvars.CurrentLiveRoughnessJob['name'],
#                                       r'select peer_prefix, roughness, five_minute_index, play_type '
#                                   r'from %s where date_time="20160314"' % constvars.CurrentLiveRoughnessJob['mysqltable'] ,'.*%s.*', 1, 3)

#
# pipeofodps.downloaddatafromodps(constvars.DailyP2PRatePerUserJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyP2PRatePerUserJob['name']))
# comparefile.compareresultpattern(constvars.DailyP2PRatePerUserJob['name'], '.*%s.*', 1, 5)
#
# pipeofodps.downloaddatafromodps(constvars.CurrentLivePeerOnlineCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentLivePeerOnlineCountJob['name']))
# comparefile.compareresult(constvars.CurrentLivePeerOnlineCountJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.CurrentOnlineISPDistributeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.CurrentOnlineISPDistributeJob['name']))
# comparefile.compareresult(constvars.CurrentOnlineISPDistributeJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyPeakBandWidthJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.DailyPeakBandWidthJob['name']))
# comparefile.compareresultpatternmysql(constvars.DailyPeakBandWidthJob['name'],
#                                       r'-- select username, peak_band_width, play_type '
#                                   r'from %s where date_time="20160314"' % constvars.DailyPeakBandWidthJob['mysqltable'] ,'.*%s.*', 2, 4)
# comparefile.compareresultpattern(constvars.DailyPeakBandWidthJob['name'], '.*%s.*', 1, 5)

# pipeofodps.downloaddatafromodps(constvars.DailyTotalFlowJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyTotalFlowJob['name']))
# comparefile.compareresult(constvars.DailyTotalFlowJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.FiveMinutePeakBandWidthJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.FiveMinutePeakBandWidthJob['name']))
# comparefile.compareresultpattern(constvars.FiveMinutePeakBandWidthJob['name'], '.*%s.*', 2, 7)
# #
# pipeofodps.downloaddatafromodps(constvars.HourFilePlayCountAccumulateModeJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourFilePlayCountAccumulateModeJob['name']))
# comparefile.compareresult(constvars.HourFilePlayCountAccumulateModeJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.HourP2PRatePerUserJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourP2PRatePerUserJob['name']))
# comparefile.compareresultpattern(constvars.HourP2PRatePerUserJob['name'], '.*%s.*', 2, 4)
#
# pipeofodps.downloaddatafromodps(constvars.HourPeakBandWidthJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.HourPeakBandWidthJob['name']))
# comparefile.compareresultpattern(constvars.HourPeakBandWidthJob['name'], '.*%s.*', 2, 4)

# pipeofodps.downloaddatafromodps(constvars.HourTotalFlowJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.HourTotalFlowJob['name']))
# comparefile.compareresult(constvars.HourTotalFlowJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.InputDownloadFlowJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.InputDownloadFlowJob['name']))
# comparefile.compareresultlinenumber(constvars.InputDownloadFlowJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.TodayFilePlayCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.TodayFilePlayCountJob['name']))
# comparefile.compareresult(constvars.TodayFilePlayCountJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.TodayTotalFlowJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.TodayTotalFlowJob['name']))
# comparefile.compareresult(constvars.TodayTotalFlowJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.TodayP2PRateJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.TodayP2PRateJob['name']))
# comparefile.compareresultpatternmysql(constvars.TodayP2PRateJob['name'],
#                                       r'select username, url, p2p_rate, play_type '
#                                   r'from %s where date_time="20160314"' % constvars.TodayP2PRateJob['mysqltable'] ,'.*%s.*', 2, 2)
# comparefile.compareresultpattern(constvars.TodayP2PRateJob['name'], '.*%s.*', 2, 2)
#
# pipeofodps.downloaddatafromodps(constvars.TodayP2PRatePerUserJob['outputtable'],
#                                 (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' %
#                                  constvars.TodayP2PRatePerUserJob['name']))
# comparefile.compareresultpattern(constvars.TodayP2PRatePerUserJob['name'], '.*%s.*', 1, 2)
#
# pipeofodps.downloaddatafromodps(constvars.PeerDailyPlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.PeerDailyPlayCountJob['name']))
# comparefile.compareresult(constvars.PeerDailyPlayCountJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.DailyFilePlayCountJob['outputtable'],
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.DailyFilePlayCountJob['name']))
# comparefile.compareresultpattern(constvars.DailyFilePlayCountJob['name'], '.*%s.*', 2, 7)

# pipeofodps.downloaddatafromodps(constvars.WeeklyProvinceFilePlayCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.WeeklyProvinceFilePlayCountJob['name']))
# comparefile.compareresult(constvars.WeeklyProvinceFilePlayCountJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.WeeklyAverageOnlineTimeJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.WeeklyAverageOnlineTimeJob['name']), 6)
# comparefile.compareresultpattern(constvars.WeeklyAverageOnlineTimeJob['name'],'.*%s.*', 1, 5)
#
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyActivePeerCountAverageJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyActivePeerCountAverageJob['name']),
#                                          'month=201603')
# comparefile.compareresultpattern(constvars.MonthlyActivePeerCountAverageJob['name'],'.*%s.*', 1, 4)
#
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyTotalFlowJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyTotalFlowJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyTotalFlowJob['name'])

# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyDistinctPeerIDJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyDistinctPeerIDJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyDistinctPeerIDJob['name'])

# pipeofodps.downloaddatafromodps(constvars.MonthlyPeerActivityJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyPeerActivityJob['name']))
# comparefile.compareresult(constvars.MonthlyPeerActivityJob['name'])

# pipeofodps.downloaddatafromodps(constvars.ThirtyDayStartTimeCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ThirtyDayStartTimeCountJob['name']))
# comparefile.compareresult(constvars.ThirtyDayStartTimeCountJob['name'])
#
# pipeofodps.downloaddatafromodps(constvars.ThirtyDaySeekTimeCountJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.ThirtyDaySeekTimeCountJob['name']))
# comparefile.compareresult(constvars.ThirtyDaySeekTimeCountJob['name'])
#
# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyPeakBandWidthJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyPeakBandWidthJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyPeakBandWidthJob['name'])

# pipeofodps.downloaddatafromodpsbypartten(constvars.MonthlyPeerActivityJob['outputtable'] , \
#     (os.path.abspath(os.path.dirname(__file__)) + '/outputdata/%sDB.txt' % constvars.MonthlyPeerActivityJob['name']),
#                                          'month=201603')
# comparefile.compareresult(constvars.MonthlyPeerActivityJob['name'])



