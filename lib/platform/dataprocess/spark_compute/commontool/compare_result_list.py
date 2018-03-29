from lib.platform.dataprocess.spark_compute.commontool.expect_datafile_to_list import ExpectDatafileToList
from lib.platform.dataprocess.spark_compute.commontool.real_datafile_to_list import RealDatafileToList


class CompareResultList(object):

    @staticmethod
    def compare_contain_type(filename):
        flag = True
        real_list = RealDatafileToList().rowkey_contain_type(filename)
        expect_list = ExpectDatafileToList().rowkey_contain_type(filename)
        for row1 in real_list.keys():
            for timestamp in real_list[row1].keys():
                for play_type in real_list[row1][timestamp].keys():
                    for column in real_list[row1][timestamp][play_type].keys():
                        if abs((float(real_list[row1][timestamp][play_type][column]) -
                                float(expect_list[row1][timestamp][play_type][column]))) < 0.0001:
                            pass
                        else:
                            flag = False
                            print row1, timestamp, play_type, column
        return flag

    @staticmethod
    def compare_no_type(filename):
        flag = True
        real_list = RealDatafileToList().rowkey_no_type(filename)
        expect_list = ExpectDatafileToList().rowkey_no_type(filename)
        for row1 in real_list.keys():
            for timestamp in real_list[row1].keys():
                for column in real_list[row1][timestamp].keys():
                    if abs((float(real_list[row1][timestamp][column]) -
                            float(expect_list[row1][timestamp][column]))) < 0.0001:
                        pass
                    else:
                        flag = False
                        print row1, timestamp, column
        return flag


if __name__ == '__main__':
    CompareResultList.compare_no_type('play_fluency.txt')
