#!/bin/sh
for((;;)); do \
        ffmpeg -re -i rtmp://192.168.3.180:3005/pullsdk.uid.com/live/test2 \
        -vcodec copy -acodec copy \
        -f flv -y rtmp://192.168.3.180:3005/pullsdk.cloutropy.com/live/uidtest
       sleep 40
done
