import os

__constant_file_path = os.path.dirname(__file__) + '/../data_file/constant_file/'
__expect_data_file_path = os.path.dirname(__file__) + '/../data_file/expect_data_file/'
__real_data_file_path = os.path.dirname(__file__) + '/../data_file/real_data_file/'
__temp_file_path = os.path.dirname(__file__) + '/../data_file/temp_file/'


def read_constant_file(file_name):
    with open(__constant_file_path + file_name) as temp_file:
        file_data = temp_file.readlines()
    return file_data


def read_expect_file(file_name):
    with open(__expect_data_file_path + file_name) as temp_file:
        file_data = temp_file.readlines()
    return file_data


def read_real_file(file_name):
    with open(__real_data_file_path + file_name) as temp_file:
        file_data = temp_file.readlines()
    return file_data


def read_temp_file(file_name):
    with open(__temp_file_path + file_name) as temp_file:
        file_data = temp_file.readlines()
    return file_data
