#!/bin/bash
# Program:
#        Change uid by stopping one of the streams at intervals
# 192.168.4.195 /root/JKZ/ff_push/uid_change/
# __Author__: JKZ

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

PROCESS_0=`ps aux | grep stream_180_uidtest | awk '{print $2}'|cut -d " " -f1`
PROCESS_1=`ps aux | grep stream_181_uidtest | awk '{print $2}'|cut -d " " -f1`
PROCESS_180=`ps aux | grep ffmpeg|grep uidtest|grep 180 | awk '{print $2}'|cut -d " " -f1`
PROCESS_181=`ps aux | grep ffmpeg|grep uidtest|grep 181 | awk '{print $2}'|cut -d " " -f1`
kill -9 ${PROCESS_0}
kill -9 ${PROCESS_1}
kill -9 ${PROCESS_180}
kill -9 ${PROCESS_181}


nohup /root/JKZ/ff_push/uid_change/stream_180_uidtest.sh >/dev/null 2>&1 &
nohup /root/JKZ/ff_push/uid_change/stream_181_uidtest.sh >/dev/null 2>&1 &

UID_CHANGE_INTERVAL=60

# PROCESS_245=`ps aux | grep ffmpeg|grep uidtest|grep 245 | awk '{print $2}'|cut -d " " -f1`
# PROCESS_246=`ps aux | grep ffmpeg|grep uidtest|grep 246 | awk '{print $2}'|cut -d " " -f1`
# echo $PROCESS_245
# echo $PROCESS_246

while true; do
    sleep ${UID_CHANGE_INTERVAL}
    date_time=`date`
    PROCESS_180=`ps aux | grep ffmpeg|grep uidtest|grep 180 | awk '{print $2}'|cut -d " " -f1`
    kill -9 ${PROCESS_180}
    echo "[$date_time] Kill 180"
    sleep ${UID_CHANGE_INTERVAL}
    PROCESS_181=`ps aux | grep ffmpeg|grep uidtest|grep 181 | awk '{print $2}'|cut -d " " -f1`
    kill -9 ${PROCESS_181}
    echo "[$date_time] Kill 181"
done
