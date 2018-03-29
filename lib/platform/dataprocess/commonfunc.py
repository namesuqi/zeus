import time
import os
import random

import constvars
import testdata.datavars as datavars


def comdict(dict1, dict2):
    if len(dict1.keys()) != len(dict2.keys()):
        print 'the count of keys is not equal bwteen two dictionary\n'
    for k in dict1.keys():
        if type(k) == int: print 'check KEY (%s)\n'%str(k)
        if k not in dict2.keys():
            #print dict2.keys()
            print 'the Key (%s) is not including the second dictionary\n'%str(k)
        else:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                comdict(dict1[k], dict2[k])
            elif (not isinstance(dict1[k], dict)) and (not isinstance(dict2[k], dict)):
                if(dict1[k] != dict2[k]):
                    print 'value is not equal in dictionary for key (%s): value1: %s ---- value2: %s\n'%(str(k),str(dict1[k]),str(dict2[k]))
                else:
                    pass #print 'value of Key (%s) match OK'%str(k)
            else:
                print 'value type is not match in dictionary for key (%s)\n'%str(k)


def get_timestamp_by_time(timestr):
    try:
        year = timestr[:4]
        month = timestr[4:6]
        day = timestr[6:8]
        hour = timestr[8:10]
        minute = timestr[10:12]
        second = timestr[12:]
        return str(time.mktime((int(year), int(month), int(day), int(hour),int(minute),int(second),-1,-1,0)))[:str(time.mktime((int(year), int(month), int(day), int(hour),int(minute),int(second),-1,-1,0))).index(".")] + "111"
    except:
        print 'exception raise when executing, return timestamp from current time now...'
        return str(time.time())[:str(time.time()).index(".")] + "111"


def exec_odps_commands(commandlines):

    javacommand = 'java -jar %s %s' % (constvars.exec_file, commandlines)
    ret = os.system(javacommand)
    return ret

def exec_odps_commands_notnull(commandlines):

    javacommand = 'java -jar %s %s' % (constvars.exec_file, commandlines) + ' test_cloutropy false'
    ret = os.system(javacommand)
    return ret

def create_random_unique_peerid():
    per_fix_list = datavars.name_list.keys()
    peerid_prefix = per_fix_list[random.randint(0, len(per_fix_list)-1)]
    peerid_postfix = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(18)))[:24]
    return ''.join((peerid_prefix, peerid_postfix))
