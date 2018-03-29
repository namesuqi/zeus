import time


class TimestampConversion(object):

    @staticmethod
    def get_timestamp(incoming_time=''):
        if incoming_time == '':
            time_string = str(time.time())[:str(time.time()).index(".")] + '000'
            return time_string
        else:
            try:
                if len(incoming_time) == 10:
                    year = incoming_time[:4]
                    month = incoming_time[4:6]
                    day = incoming_time[6:8]
                    hour = incoming_time[8:10]
                    minute = 00
                    second = 00
                    return str(time.mktime((int(year), int(month), int(day), int(hour), int(minute),
                                        int(second), -1, -1, 0))).split('.')[0] + "000"
                elif len(incoming_time) == 12:
                    year = incoming_time[:4]
                    month = incoming_time[4:6]
                    day = incoming_time[6:8]
                    hour = incoming_time[8:10]
                    minute = incoming_time[10:12]
                    second = 00
                    return str(time.mktime((int(year), int(month), int(day), int(hour), int(minute),
                                            int(second), -1, -1, 0))).split('.')[0] + "000"
                else:
                    raise Exception('incoming time most accurate to minute!')
            except:
                raise Exception('incoming time illegal format!')


if __name__ == '__main__':
    print TimestampConversion.get_timestamp('201608091105')
