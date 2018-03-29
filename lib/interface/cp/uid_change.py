# encoding=utf-8
import json
import shutil
import urllib
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import io

import time


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.process(2)

    def process(self, req_type):
        print self.requestline

        if req_type == 2 and self.path.startswith("/uid_idx"):
            query = urllib.splitquery(self.path)[1].split("&")
            print "---", query
            uid = urllib.splitvalue(query[1])[1]
            f_url = urllib.splitvalue(query[0])[1]
            print "---url=", f_url
            print "---uid=", uid

            resp_uid = "9bd2936001794d0381d76a37b74a6dff"
            uid_idx = 1
            content = {
                # "uid": int(2),
                "uid": str(resp_uid),
                "uid_idx": int(uid_idx)
            }
            print "***resp", content
            # url, uid = query.split("&")
            # print url, uid

        # time.sleep(1)
        content = json.dumps(content)
        f = io.BytesIO()
        f.write(content)
        f.seek(0)
        self.send_response(400)
        # self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        # self.end_headers()
        shutil.copyfileobj(f, self.wfile)


def start_server(port):
    http_server = HTTPServer(('', int(port)), MyRequestHandler)
    print 'started httpserver...'
    print 'listening port:', port
    print 'try to click it:', 'http://127.0.0.1:' + str(port)
    http_server.serve_forever()

if __name__ == "__main__":

    start_server(9570)