# coding=utf-8
# author: zengyuetian
# 将大文件按行提取其中一部分内容

if __name__ == "__main__":
    # 大文件
    origin_file = "e:/debug.log"
    # 提取内容存入的新文件
    new_file = "e:/debug_new.log"

    # 从哪一行开始
    begin_line = 27000000

    # 到哪一行结束，如果到文件尾部，就设置为0
    end_line = 0

    f = open(origin_file, 'r')
    f_new = open(new_file, 'w')

    num = 1
    while True:
        l = f.readline()  # 无法一次性读入内存的话就用readline

        if num > begin_line:
            f_new.write(l)
        if num == end_line or l == "":
            print num
            break

        # 打印下处理进度
        if num % 10000 == 0:
            print num

        num += 1
    f.close()
    f_new.close()
