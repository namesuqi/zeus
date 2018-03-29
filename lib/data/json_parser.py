# coding=utf-8
"""
Parse Json-like data

__author__ = 'zengyuetian'

"""

import json

class JsonParser(object):
    @staticmethod
    def GetPeerValue(peer_info, key):
        return json.loads(peer_info).get(key, None)


    @staticmethod
    def GetDataByPath(data, path):
        # if start with /，remove /
        if path.startswith("/"):
            path = path[1:]
        key_list = path.split("/")
        num_list = [str(x) for x in range(100)]  # import to support index more than 10

        try:
            for key in key_list:
                if key in num_list:  # for number array
                    index = int(key)
                    data = data[index]
                else:  # for key
                    data = data.get(key)
        except:
            data = None

        return data

    @staticmethod
    def TrimQuotations(origin_str):
        """
        if the first char is ' or ", remove it
        """
        if origin_str[0] == '"' and origin_str[-1] == '"':
            return origin_str[1: -1]
        if origin_str[0] == "'" and origin_str[-1] == "'":
            return origin_str[1: -1]

if __name__ == "__main__":
    my_list = [str(x) for x in range(100)]
    print my_list


