#!/usr/bin/env bash
iptables -F
nginx

systemctl restart redis.service

systemctl restart mongod.service

docker start 9842d519914c
docker start a85b49683cae
docker start 047d809f69af



cd /root
cd live-push-srv
pm2 start app_live_push.js
cd ..
cd cd live-rawdata-srv
pm2 start app_live_rawdata.js
cd ..
cd live-mgr-srv
python app_live_mgr.py &
cd ..


cd live-src-srv
./objs/srs -c conf/yunshang.conf

cd /home/admin/p2pserver/tunnel/funnel
java -jar funnel-1.0.1.jar &

