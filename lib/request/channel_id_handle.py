import random

from lib.utility.path import PathController


def update_channel_id():
    channel_id_file_path = PathController.get_root_path() + "/misc/data/channel_id/channel_id"
    with open(channel_id_file_path, 'a') as writer:
        while True:
            random_channel_id = random.randint(1, 65535)
            if check_repeat(random_channel_id):
                writer.write(str(random_channel_id) + '\n')
                break
            else:
                continue


def get_channel_id():
    channel_id_file_path = PathController.get_root_path() + "/misc/data/channel_id/channel_id"
    with open(channel_id_file_path, 'r') as reader:
        lines = reader.readlines()
    # print lines[-1]
    return int(lines[-1])


def check_repeat(channel_id):
    channel_id_file_path = PathController.get_root_path() + "/misc/data/channel_id/channel_id"
    with open(channel_id_file_path, 'r') as reader:
        lines = reader.readlines()
    id_list = list()
    for line in lines:
        id_list.append(int(line))
    # print id_list
    if channel_id in id_list:
        return False
    else:
        return True


if __name__ == '__main__':
    # print check_is_repeat(39)
    update_channel_id()
    print get_channel_id()
