#!/usr/bin/env bash
for((;;)); do
/root/ffmpeg-2.8.6-64bit-static/ffmpeg -re -f lavfi -i "movie=/root/videosource/fengjing_2mbps.ts:loop=0, setpts=N/(FRAME_RATE*TB)" -vf drawtext="fontfile=/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf:text='%{localtime}              %{pts}':fontcolor=white:fontsize=30:x=7:y=20" -vcodec libx264 -acodec copy -x264opts   keyint=80 -f flv rtmp://localhost/hls/fengjing
sleep 1
done


for((;;)); do
/root/ffmpeg-2.8.6-64bit-static/ffmpeg -re -f lavfi -i "movie=/root/videosource/fengjing_2mbps.ts:loop=0, setpts=N/(FRAME_RATE*TB)" -vf drawtext="fontfile=/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf:text='%{localtime}              %{pts}':fontcolor=white:fontsize=30:x=7:y=20" -vcodec libx264 -acodec copy -f    flv rtmp://$1.srs.cloutropy.com/p2plive/$2
sleep 1
    done
