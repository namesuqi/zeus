# coding=utf-8
"""
for xmtp dump, backup
__Author__: JKZ
"""
import os
import random
import time
import sys

XMTP = ["xmtpdump", "xmtpoutput.flv"]
HTTPFLV = ["httpflvdump", "output.flv"]
DOWNLOAD_TIME_RANGE = 4200


def main(para_file, para_time=DOWNLOAD_TIME_RANGE):
    i = 0
    j = 0
    if str(para_file) == "xmtp":
        para_file = XMTP
    elif str(para_file) == "httpflv":
        para_file = HTTPFLV
    while i < 50 and j < 50:
        exe_file = para_file[0]
        output_file = para_file[1]
        os.system("rm yunshang.log")
        download_time = random.randint(1, int(para_time))
        os.system("echo {0}-{1}:{2} >> test.log".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                                        str(para_file[0]), str(download_time)))
        os.system("/mnt/hgfs/CDNVlog/V2/{0} &".format(exe_file))
        time.sleep(download_time)
        os.system("pkill {0}".format(exe_file))
        result = os.system("/root/flv-parser/build/flv_parser {0}".format(output_file))
        if result != 0:
            # print "************", result
            i += 1
            os.system("cp {0} /mnt/hgfs/CDNVlog/errorflv/{1}_{0}".format(output_file, str(i)))
            os.system("cp yunshang.log /mnt/hgfs/CDNVlog/errorflv/{0}{1}_yunshang.log".format(str(i), output_file))
        elif result == 0:
            j += 1
            os.system("cp {0} /mnt/hgfs/CDNVlog/okflv/{1}_{0}".format(output_file, str(j)))

# ffmpeg -re -i special_1_xmtpoutput.flv -vcodec copy -acodec copy -f flv -y rtmp://192.168.3.181:3005/pullsdk.testzzz.com/live/test2

pull_url_180 = "rtmp://192.168.3.180:3005/pullsdk.uid.com/live/test2"
pull_url_181 = "rtmp://192.168.3.181:3005/pullsdk.uid.com/live/test2"
def uid_pull():
    # init
    os.system("ffmpeg -re -i uid_t{0}.flv -vcodec copy -acodec copy -f flv -y {1} 2> /dev/null &".
              format(1, pull_url_180))  # host
    os.system("ffmpeg -re -i uid_t{0}.flv -vcodec copy -acodec copy -f flv -y {1} 2> /dev/null &".
              format(2, pull_url_181))  # backup
    for i in range(1, 10):
        time.sleep(10)
        os.system("pgrep 192.168.3.180 | xargs kill")  # kill host, turn to backup
        # pid_180 = os.system("ps -ef|grep 192.168.3.180|grep -v grep |awk '{print $2}'")
        # os.system("kill -9 ${0}".format(str(pid_180))
        time.sleep(5)
        os.system("ffmpeg -re -i uid_t{0}.flv -vcodec copy -acodec copy -f flv -y {1} 2> /dev/null &".
                  format(2*i+1, pull_url_180))
        time.sleep(15)
        os.system("pgrep 192.168.3.181 | xargs kill")  # kill backup, turn to host
        # pid_181 = os.system("ps -ef|grep 192.168.3.181|grep -v grep |awk '{print $2}'")
        # os.system("kill -9 ${0}".format(str(pid_181))
        time.sleep(5)
        os.system("ffmpeg -re -i uid_t{0}.flv -vcodec copy -acodec copy -f flv -y {1} 2> /dev/null &".
                  format(2*i+2, pull_url_180))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])


