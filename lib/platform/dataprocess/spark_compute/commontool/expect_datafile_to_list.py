import os


class ExpectDatafileToList(object):

    @staticmethod
    def rowkey_contain_type(filename):
        expect_data_dict = dict()
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/%s' % filename, "r") as expect_file:
            origin_line = expect_file.readlines()
        for line in origin_line:
            row1, timestamp, play_type, column, value = line.replace('\n', '').split(',')
            if row1 not in expect_data_dict:
                expect_data_dict[row1] = dict()
            if timestamp not in expect_data_dict[row1]:
                expect_data_dict[row1][timestamp] = dict()
            if play_type not in expect_data_dict[row1][timestamp]:
                expect_data_dict[row1][timestamp][play_type] = dict()
            if column not in expect_data_dict[row1][timestamp][play_type] :
                expect_data_dict[row1][timestamp][play_type][column] = dict()
            expect_data_dict[row1][timestamp][play_type][column] = value
        return expect_data_dict

    @staticmethod
    def rowkey_no_type(filename):
        expect_data_dict = dict()
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../expectfile/%s' % filename, "r") as expect_file:
            origin_line = expect_file.readlines()
        for line in origin_line:
            row1, timestamp, column, value = line.replace('\n', '').split(',')
            if row1 not in expect_data_dict:
                expect_data_dict[row1] = dict()
            if timestamp not in expect_data_dict[row1]:
                expect_data_dict[row1][timestamp] = dict()
            if column not in expect_data_dict[row1][timestamp]:
                expect_data_dict[row1][timestamp][column] = dict()
            expect_data_dict[row1][timestamp][column] = value
        return expect_data_dict
