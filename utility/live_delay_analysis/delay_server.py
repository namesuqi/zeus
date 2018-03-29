# coding=utf-8
"""
collect chunk delay data and provide http service

1. HTTP server
2. Read the xxx.cts file from end to start

Support SRS server and Push server

# run on SRS
$ nohup python delay_server srs &

# run on Push
$ nohup python delay_server push &



__author__ = 'zengyuetian'

"""

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
import urlparse
import json
import threading
import time

import inspect
import os
import sys

HTTP_PORT = 32720
CHUNK_NUM = 100



file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
parent_path = os.path.dirname(file_path)

class GetHandlerSrs(BaseHTTPRequestHandler):



    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        # message_parts = [
        #     'Client value:',
        #     'client_address=%s (%s)' % (self.client_address, self.address_string()),
        #     'command=%s' % self.command,
        #     'path=%s' % self.path,
        #     'real path=%s' % parsed_path.path,
        #     'query=%s' % parsed_path.query,
        #     'request_version=%s' % self.request_version,
        #     '',
        #     'Server value:',
        #     'server_version=%s' % self.server_version,
        #     'sys_version=%s' % self.sys_version,
        #     'protocol_version=%s' % self.protocol_version,
        #     '',
        #     'HEADERS RECEIVED:',
        # ]
        '''
            {"4484": "1463554053343", "4485": "1463554055848",
            "4479": "1463554034074", "4478": "1463554031824",
            "4486": "1463554059599", "4480": "1463554037956",
            "4481": "1463554042211", "4482": "1463554045583",
            "4483": "1463554049220"}
        '''
        query = parsed_path.query
        fid = query.replace('fid=', '')
        print fid
        data_dict = dict()

        lines = last_lines(parent_path+"/{0}.cts".format(fid), CHUNK_NUM).strip()
        datas = lines.split('\n')
        for data in datas:
            items = data.split(',')
            data_dict[items[0]] = items[1]

        # package data as json
        message = json.dumps(data_dict)

        # print message_parts
        # for name, value in sorted(self.headers.items()):
        #     message_parts.append('%s=%s' % (name, value.rstrip()))
        # message_parts.append('')
        # message = '\r\n'.join(message_parts)
        # message = threading.currentThread().getName()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(message)
        return



class GetHandlerPush(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        '''
            {"90": {"base_time": 1463553793951, "local_time": 1463553798744, "chunk_id": 90},
             "91": {"base_time": 1463553798899, "local_time": 1463553802939, "chunk_id": 91},
             "92": {"base_time": 1463553802927, "local_time": 1463553806460, "chunk_id": 92},
             "93": {"base_time": 1463553806645, "local_time": 1463553810532, "chunk_id": 93},
             "94": {"base_time": 1463553810521, "local_time": 1463553813706, "chunk_id": 94}}
        '''
        query = parsed_path.query
        fid = query.replace('fid=', '')
        print fid
        data_dict = dict()

        lines = last_lines(parent_path + "/{0}.cts".format(fid), CHUNK_NUM).strip()
        datas = lines.split('\n')
        for data in datas:
            items = data.split(',')
            sub_dict = dict()
            sub_dict["base_time"] = long(items[1])
            sub_dict["local_time"] = long(items[2])
            sub_dict["chunk_id"] = long(items[0])
            data_dict[str(items[0])] = sub_dict

        # package data as json
        message = json.dumps(data_dict)

        # print message_parts
        # for name, value in sorted(self.headers.items()):
        #     message_parts.append('%s=%s' % (name, value.rstrip()))
        # message_parts.append('')
        # message = '\r\n'.join(message_parts)
        # message = threading.currentThread().getName()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(message)
        return


# use thread to handle http requests
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

# tail.py
# Usage: python tail.py FILENAME LINES
# similar to linux command: tail -n LINES FILENAME
def last_lines(filename, lines=1):
    """
    Print the last several line(s) of a text file.
    Argument filename is the name of the file to print.
    Argument lines is the number of lines to print from last.
    """
    lines = int(lines)
    block_size = 1024
    block = ''
    nl_count = 0
    start = 0
    fsock = file(filename, 'rU')
    try:
        # seek to end
        fsock.seek(0, 2)
        # get seek position
        current_pos = fsock.tell()
        while(current_pos > 0):  #while not EOF
            # seek ahead block_size+the length of last read block
            current_pos -= (block_size + len(block))
            if current_pos < 0:
                current_pos = 0
            fsock.seek(current_pos)
            # read to end
            block = fsock.read()
            nl_count = block.count('\n')
            # if read enough(more)
            if nl_count >= lines:
                break
        # get the exact start position
        for n in range(nl_count - lines + 1):
            start = block.find('\n', start) + 1
    finally:
        fsock.close()
    return block[start:]

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Please specify server name and try again"
        exit(-1)
    else:
        if sys.argv[1] == "srs":
            # server = HTTPServer(('localhost', HTTP_PORT), GetHandler)
            server = ThreadedHTTPServer(('0.0.0.0', HTTP_PORT), GetHandlerSrs)
        else:
            server = ThreadedHTTPServer(('0.0.0.0', HTTP_PORT), GetHandlerPush)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()