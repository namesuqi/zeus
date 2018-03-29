import flv_parse
import pycurl
import threading
import sys
import time
import datetime


BUFFER_REDUCE_TIME = 100 * 1000
BUFFERINT_TIME = 1000


def strtime():
    return time.strftime("[%Y-%m-%d %H:%M:%S") + ".%03d] " % ((datetime.datetime.now().microsecond / 1000))


def get_cur_ms():
    return time.time() * 1000


class BufferInfo:

    def __init__(self, log_name):
        self.logfile = open(log_name, "w")
        pass

    def start(self):
        self.bufferTime = 0
        self.lastTimeStamp = 0
        self.update_cnt = 0
        self.buffering = time.time()
        self.last_real_time = get_cur_ms()
        self.startup_time = time.time()
        self.startup = False
        self.last_delay_report_time = get_cur_ms()
        self.log("begin")
        self.timer = threading.Timer(0.047, self.onTimer)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def onTimer(self):
        self.update()
        self.timer = threading.Timer(0.05, self.onTimer)
        self.timer.start()

    def log(self, text):
        log = strtime() + text + "\n"
        self.logfile.write(log)
        self.logfile.flush()

    def addTag(self, pos, timestamp, size):
        self.bufferTime += (timestamp - self.lastTimeStamp)
        self.lastTimeStamp = timestamp
        if self.bufferTime > BUFFER_REDUCE_TIME:
            self.bufferTime -= 500
            self.log("skip 500ms , buffer=%.2f" % (self.bufferTime))
        if self.buffering and self.bufferTime > BUFFERINT_TIME:
            if not self.startup:
                self.startup = True
                self.log("startup time %.2f" % (time.time() - self.startup_time))
            else:
                self.log("buffering %.2f" % (time.time() - self.buffering))
            self.buffering = 0
            self.last_real_time = get_cur_ms()

    def update(self):
        if self.buffering:
            return
        else:
            spend = (get_cur_ms() - self.last_real_time)
            self.bufferTime -= spend

        if self.last_delay_report_time + 5000 < get_cur_ms():
            self.log("delay %.2f" % (self.bufferTime / 1000.0))
            self.last_delay_report_time = get_cur_ms()

        self.last_real_time = get_cur_ms()
        if self.bufferTime <= 0:
            self.bufferTime = 0
            if self.buffering == 0:
                self.buffering = time.time()


class ProcessData:

    def __init__(self, log_name):
        self.buffer_info = BufferInfo(log_name)

    def OpenClientReq(self):
        self.start()

    def CloseClientReq(self):
        self.stop()

    def start(self):
        self.parser = flv_parse.FLVParse()
        self.last_timestamp = 0
        self.frame_time_total = 0
        self.frame_count = 0
        self.buffer_info.start()

    def stop(self):
        self.last_timestamp = 0
        self.buffer_info.stop()

    def body_callback(self, buf):
        self.parser.parse(buf, self.tag_callback)

    def timestamp_verify(self, delta):
        if self.frame_count > 0:
            avg = self.frame_time_total / self.frame_count
            diff = avg - delta
            if diff < 0:
                diff = -diff
            if diff > 10:
                self.buffer_info.log("Frame timestamp error avg=%d cur=%d" % (avg, delta))
        if delta > 0:
            self.frame_time_total += delta
            self.frame_count += 1

    def tag_callback(self, pos, timestamp, vtype, size):
        if vtype == 9:
            delta = timestamp - self.last_timestamp
            self.timestamp_verify(delta)
            self.last_timestamp = timestamp
            self.buffer_info.addTag(pos, timestamp, size)
        if vtype == 18:
            pass


def bytes_coming(buf):
    process_data.body_callback(buf)


def cur_thread(url):
    print strtime() + " curl thread...." + url
    cur = pycurl.Curl()
    cur.setopt(cur.URL, url)
    cur.setopt(cur.WRITEFUNCTION, bytes_coming)
    process_data.OpenClientReq()
    cur.perform()
    print cur.getinfo(cur.HTTP_CODE)
    cur.close()
    print strtime() + " curl exit " + url
    process_data.CloseClientReq()


if __name__ == '__main__':
    url = "http://127.0.0.1:32717/live_flv/user/yunduan?url=http://live3.play.yunduan.cloutropy.com/live/test3.flv"
    if len(sys.argv) > 1:
        url = sys.argv[1]
        log_file_name = sys.argv[2]
    elif len(sys.argv) == 1:
        log_file_name = sys.argv[1]

    global process_data
    process_data = ProcessData(log_file_name)

    if url:
        t = threading.Thread(target=cur_thread, args=(url,))
        t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
