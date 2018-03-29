# coding=utf-8

__author__ = 'liwenxuan'

import os
import json
import requests


def set_schema(topic, host, port):
    # 自定义schema格式

    schema = open(os.path.abspath(os.path.dirname(__file__)) + "/../avro_schema/" + topic + ".avsc").read()
    print schema

    headers = {"Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json",
               "Connection": "close",
               "Content-Type": "application/vnd.schemaregistry.v1+json"}
    schema_data = {"schema": schema}

    r = requests.post("http://%s:%s/subjects/%s-value/versions" % (host, str(port), topic),
                      headers=headers, data=json.dumps(schema_data))
    print r.text
    return requests.get("http://%s:%s/subjects/%s-value/versions" % (host, str(port), topic)).text


def schema_config(compatibility, host, port):
    # 设置schema的配置方式 : NONE, FULL, FORWARD, BACKWARD
    headers = {"Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json",
               "Connection": "close",
               "Content-Type": "application/vnd.schemaregistry.v1+json"}
    data = {"compatibility": compatibility}
    r = requests.put("http://{0}:{1}/config".format(host, port), headers=headers, data=json.dumps(data))
    print "status:", r.status_code
    return r


if __name__ == "__main__":
    pass
    # print set_schema("ss_lf_report", "192.168.3.230", 8081)

    # schema_config("BACKWARD", "192.168.3.230", 8081)
