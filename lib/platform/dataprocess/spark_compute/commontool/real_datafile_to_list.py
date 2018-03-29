import re, os


class RealDatafileToList(object):

    @staticmethod
    def rowkey_no_type(filename):
        real_data_dict = dict()
        re_compile = re.compile(r' (.*):(\d*) column=(.*), time.*value=(.*)')
        with open(os.path.abspath(os.path.dirname(__file__)) +
                          '/../realfile/%s' % filename, "r") as real_file:
            origin_lines = real_file.readlines()
        for line in origin_lines:
            group = re_compile.match(line)
            if group:
                # print group.group(1), group.group(2), group.group(3), group.group(4)
                if group.group(1) not in real_data_dict:
                    real_data_dict[group.group(1)] = dict()
                if group.group(2) not in real_data_dict[group.group(1)]:
                    real_data_dict[group.group(1)][group.group(2)] = dict()
                if group.group(3) not in real_data_dict[group.group(1)][group.group(2)]:
                    real_data_dict[group.group(1)][group.group(2)][group.group(3)] = ''
                real_data_dict[group.group(1)][group.group(2)][group.group(3)] = group.group(4)
        return real_data_dict

    @staticmethod
    def rowkey_contain_type(filename):
        real_data_dict = dict()
        re_compile = re.compile(r' (.*):(\d*):(.*) column=(.*), time.*value=(.*)')
        with open(os.path.abspath(os.path.dirname(__file__)) +
                                  '/../realfile/%s' % filename, "r") as real_file:
            origin_lines = real_file.readlines()
        for line in origin_lines:
            group = re_compile.match(line)
            if group:
                # print group.group(1), group.group(2), group.group(3), group.group(4), group.group(5)
                if group.group(1) not in real_data_dict:
                    real_data_dict[group.group(1)] = dict()
                if group.group(2) not in real_data_dict[group.group(1)]:
                    real_data_dict[group.group(1)][group.group(2)] = dict()
                if group.group(3) not in real_data_dict[group.group(1)][group.group(2)]:
                    real_data_dict[group.group(1)][group.group(2)][group.group(3)] = dict()
                if group.group(4) not in real_data_dict[group.group(1)][group.group(2)][group.group(3)]:
                    real_data_dict[group.group(1)][group.group(2)][group.group(3)][group.group(4)] = ''
                real_data_dict[group.group(1)][group.group(2)][group.group(3)][group.group(4)] = group.group(5)
        return real_data_dict

if __name__ == '__main__':
    # RealDatafileToList.rowkey_no_type('play_fluency.txt')
    RealDatafileToList.rowkey_contain_type('five_minute_average_startup_delay.txt')
