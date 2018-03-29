# coding=utf-8
"""
主进程监视文件夹：
1. 找到被删除的频道，清理
2. 查找新的M3u8文件，新起线程处理该文件


__author__ = 'zengyuetian'

"""

import threading
from time import sleep
import sys
import os
import shutil
import datetime

Live_PATH = "/root/testcopym3u8"

def delete_old_ts(ts_dir, max_ts_num):
    '''
    删除超过指定数目的ts文件，总是删旧的文件
    :param ts_dir: ts目录.list
    :param max_ts_num: 最多允许多少个文件存在
    :return: void
    '''
    l = os.listdir(ts_dir)
    print l
    if len(l) > max_ts_num:
        l.sort(key=lambda fn: os.path.getmtime(ts_dir + "/" + fn))
        delete_num = len(l) - max_ts_num
        for ts_file in l[0: delete_num]:
            ts_file_full_name = ts_dir + "/" + ts_file
            print "REMOVE ts file", ts_file_full_name
            os.remove(ts_file_full_name)


def handle_file_id(file_id):
    # 循环次数，便于观察
    loop = 0

    # MAIN loop
    while True:
        print "file_id", file_id
        # 重置所有变量
        current_start = 0  # 记录当前文件的start位置
        current_end = 0  # 记录当前文件的结束位置

        # 存放处理过的ts文件信息 {seq: {start: xxxx, length: xxx}}
        handled_ts_files = {}

        # 组合新旧文件和文件夹信息
        old_m3u8_file_name = "{0}/{1}.m3u8".format(Live_PATH, file_id)
        old_m3u8_files_dir = "{0}/{1}.list".format(Live_PATH, file_id)
        new_m3u8_file_name = old_m3u8_file_name.replace(".m3u8", ".new.m3u8")
        new_m3u8_files_dir = old_m3u8_files_dir.replace(".list", ".new.list")
        new_m3u8_pos_file_name = old_m3u8_file_name.replace(".m3u8", ".new.pos")

        print old_m3u8_file_name
        print old_m3u8_files_dir
        print new_m3u8_file_name
        print new_m3u8_files_dir

        # clean and create .new.list dir
        print "REMOVE new list dir", new_m3u8_files_dir
        if os.path.exists(new_m3u8_files_dir):
            shutil.rmtree(new_m3u8_files_dir)
        print "CREATE new list dir", new_m3u8_files_dir
        os.makedirs(new_m3u8_files_dir)

        # create new file
        new_m3u8_file = open(new_m3u8_file_name, 'w')

        if os.path.exists(new_m3u8_files_dir):
            new_m3u8_pos_file = open(new_m3u8_pos_file_name, 'r')
            saved_pos = new_m3u8_pos_file.read()
            saved_pos = int(saved_pos)
            new_m3u8_pos_file.close()

        new_m3u8_pos_file = open(new_m3u8_pos_file_name, 'w')
        # 分析m3u8文件
        with open(old_m3u8_file_name) as old_m3u8_file:
            for line in old_m3u8_file:
                if line[
                   0:7] == 'http://':  # http://cdn.entropycode.com/p2plive/62F51AFCA69048778033AF008B682D69.list/62F51AFCA69048778033AF008B682D69-776.ts
                    ts_file_short_name = line.split("/")[-1][0:-1]  # 62F51AFCA69048778033AF008B682D69-776.ts, remove \n
                    print "ts_file_short_name", ts_file_short_name
                    seq_with_postfix = ts_file_short_name.split("-")[-1]  # 776.ts
                    print "seq_with_postfix", seq_with_postfix
                    seq_id = seq_with_postfix[0:-3]  # 776
                    print "seq_id", seq_id
                    ts_file_name = old_m3u8_files_dir + "/" + ts_file_short_name
                    print "ts_file_name", ts_file_name
                    file_size = os.path.getsize(ts_file_name)

                    # 查找字典
                    handled_info = handled_ts_files.get(seq_id, None)
                    if handled_info is None:
                        # 如果没有处理过，就加到存储字典里面去
                        current_start = current_end
                        current_end += file_size

                        new_ts_file_name = ts_file_name.replace("-{0}".format(seq_id),
                                                                "-{0}-start-{1}-length-{2}".format(seq_id,
                                                                                                   current_start,
                                                                                                   file_size))
                        new_ts_file_name = new_ts_file_name.replace("list", "new.list")
                        print "new_ts_file_name", new_ts_file_name

                        new_line = line.replace("-{0}".format(seq_id),
                                                "-{0}-start-{1}-length-{2}".format(seq_id, current_start, file_size))
                        new_line = new_line.replace("list", "new.list")
                        # 写入新m3u8文件
                        new_m3u8_file.write(new_line)
                        print "NEW LINE:", new_line

                        # copy ts file to .list folder
                        shutil.copy(ts_file_name, new_ts_file_name)

                        # 现在处理过了，添加到字典
                        file_info = {"start": current_start, "length": file_size}
                        handled_ts_files[seq_id] = file_info
                    else:
                        # 如果已经处理过了，那么就从存储的字典中获取
                        current_start = handled_info["start"]
                        file_size = handled_info["length"]

                        new_ts_file_name = ts_file_name.replace("-{0}".format(seq_id),
                                                                "-{0}-start-{1}-length-{2}".format(seq_id,
                                                                                                   current_start,
                                                                                                   file_size))
                        new_ts_file_name = new_ts_file_name.replace("list", "new.list")
                        print "new_ts_file_name", new_ts_file_name

                        new_line = line.replace("-{0}".format(seq_id),
                                                "-{0}-start-{1}-length-{2}".format(seq_id, current_start, file_size))
                        new_line = new_line.replace("list", "new.list")
                        new_m3u8_file.write(new_line)
                        print "NEW LINE:", new_line

                        print seq_id, "skipped"
                else:  # NOT URL
                    # 直接写入新m3u8文件
                    new_m3u8_file.write(line)
                    print "LINE:", line
            # end for
            new_m3u8_pos_file.write(current_end)

        # save the new m3u8 file
        new_m3u8_file.close()
        new_m3u8_pos_file.close()
        loop += 1
        print "Finish loop --------->", loop

        # 删除多余的ts，每个文件夹下保持最多12个
        delete_old_ts(new_m3u8_files_dir, 12)

        # sleep to release cpu
        sleep(1)

def get_m3u8_files_id():
    pass

def delete_useless_channel():
    pass

if __name__ == "__main__":

    file_dict = {}
    while True:

        # 获得m3u8文件列表
        file_id_list = get_m3u8_files_id()

        for file_id in file_id_list:
            if file_dict.get(file_id, None) is None:
                # start new thread
                t = threading.Thread(target=handle_file_id, args=(file_id,))
                t.start()
                file_dict[file_id] = True
            else:
                pass



        # 获得没有相应m3u8文件，但是有.list文件夹的fild_id, 直接删除相关文件
        delete_useless_channel()

        # release cpu
        sleep(1)





