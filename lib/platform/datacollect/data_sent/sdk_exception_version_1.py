import os
# import tornado.httpclient
import requests
import json
import random
from lib.platform.datacollect.common_action.read_file import *
from lib.platform.datacollect.common_action.get_timestamp import *
from lib.platform.datacollect.global_vars.sdk_report import *
from lib.platform.datacollect.global_vars.url import *
from lib.platform.datacollect.global_vars.constant import *


class SdkExceptionVersion1(object):
    def send_log(self):
        prefix = "/sdk/exception/version/1"
        peer_ids = read_constant_file('peer_id_db.txt')
        file_ids = read_constant_file('file_id_db.txt')
        expect_file = open(os.path.abspath(os.path.dirname(__file__)) +
                           "/../data_file/expect_data_file/%s.txt" % __name__.split('.')[-1], 'w')
        body_data = sdk_exception_version_1

        for i in range(post_log_number):
            rand_index = random.randint(0, 2500)
            url = funnel_host + prefix
            body_data["id"] = file_ids[rand_index].replace("\n", "")+":"+str(random.randint(1000, 1000000))
            body_data['timestamp'] = get_timestamp_now()
            body_data["peer_id"] = peer_ids[rand_index].replace("\n", "")
            data = json.dumps(body_data)
            expect_file.write(data + "\n")
            # old tornado method
            # client = tornado.httpclient.HTTPClient()
            # resp = client.fetch(url, method="POST", body=data, headers={'Content-Type': 'application/json'})
            resp = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
            print "response from " + str(i) + " request: " + resp.text
        expect_file.close()

        print "sdk offering version1 script execute finish..."
        return os.path.abspath(os.path.dirname(__file__)) + "../data_file/output_data_file/%s.txt" % __name__.split('.')[-1]

if __name__ == '__main__':
    sdk_exception = SdkExceptionVersion1()
    sdk_exception.send_log()
