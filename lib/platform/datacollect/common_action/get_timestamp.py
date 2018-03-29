import time


def get_timestamp_now():

    timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    try:
        year = timestr[:4]
        month = timestr[4:6]
        day = timestr[6:8]
        hour = timestr[8:10]
        minute = timestr[10:12]
        second = timestr[12:]
        return str(time.mktime((int(year), int(month), int(day), int(hour), int(minute), int(second),
                                -1, -1, 0)))[:str(time.mktime((int(year), int(month), int(day), int(hour), int(minute),
                                                               int(second), -1, -1, 0))).index(".")] + "000"
    except:
        print 'exception raise when executing, return timestamp from current time now...'
        return str(time.time())[:str(time.time()).index(".")]


def get_timestamp(standard_time):

    timestr = standard_time
    try:
        year = timestr[:4]
        month = timestr[4:6]
        day = timestr[6:8]
        hour = timestr[8:10]
        minute = timestr[10:12]
        second = timestr[12:]
        return str(time.mktime((int(year), int(month), int(day), int(hour), int(minute), int(second),
                                -1, -1, 0)))[:str(time.mktime((int(year), int(month), int(day), int(hour), int(minute),
                                                               int(second), -1, -1, 0))).index(".")] + "000"
    except:
        print 'exception raise when executing, return timestamp from current time now...'
        return str(time.time())[:str(time.time()).index(".")]


if __name__ == '__main__':
    # timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # print(timestr)
    # print get_timestamp_now()
    print get_timestamp('20160526000001')
