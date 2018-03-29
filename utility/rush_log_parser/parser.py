# coding=utf-8
# author: zengyuetian
# 展示如何编程
# 1. 分解任务
# 2. 持续集成，总是可用的代码
"""
如何使用该工具
python parser.py client_closed_to_synsent
"""

import sys
import re

check_dict = dict()

check_dict["all"] = [
    ".*__send_internal.*ackpkt.*",
    ".*send_internal.*seq.*",
    ".*rush_connection_on_receive.*",
    ".*state.*->.*"
]

# client
check_dict["client_closed_to_synsent"] = [".*state CLOSED -> SYN_SENT.*"]
check_dict["client_synsent_to_established1"] = [".*state SYN_SENT -> ESTABLISHED.*", ".*send_internal.*seq=0*.", ".*send_internal.*pureack=0.*"]
check_dict["client_established_to_closewait1"] = [".*state ESTABLISHED -> CLOSE_WAIT.*", ".*send_internal.*stoppkt=1.*"]
check_dict["client_established_to_closewait2"] = [".*send FIN.*", ".*state ESTABLISHED -> CLOSE_WAIT.*"]
check_dict["client_closewait_to_closed1"] = [".*state CLOSE_WAIT -> CLOSED.*"]
check_dict["client_closewait_to_closed2"] = [".*state ESTABLISHED -> CLOSE_WAIT.*", ".*state CLOSE_WAIT -> CLOSED.*"]
check_dict["client_synsent_to_closed"] = [".*send_internal.*sent seq=.*", ".*resend_internal.*packet is resent.*", ".*resend_internal.*startpkt=1.*", ".*state SYN_SENT -> CLOSED.*"]
check_dict["client_established_to_closed"] = [".*state ESTABLISHED -> CLOSED.*", ".*send_internal.*stoppkt=1.*"]

# server
check_dict["server_closed_to_synrecv"] = [".*state CLOSED -> SYN_RECV.*", ".*send_internal.*.*startpkt=1.*"]
check_dict["server_synrecv_to_established"] = [".*state SYN_RECV -> ESTABLISHED.*"]
check_dict["server_established_to_closewait"] = [".*send FIN.*", ".*state ESTABLISHED -> CLOSE_WAIT.*", ".*send_internal.*stoppkt=1.*"]
check_dict["server_closewait_to_closed2"] = [".*state ESTABLISHED -> CLOSE_WAIT.*", ".*state CLOSE_WAIT -> CLOSED.*"]
check_dict["server_established_to_closed"] = [".*state ESTABLISHED -> CLOSED.*", ".*send_internal.*.*stoppkt=1.*"]



#############################################################
#    Main Function
#############################################################
if __name__ == "__main__":

    line_num = 0
    care_dist = 200                 # 感兴趣的行范围
    testcase = "all"
    log_file = "yunshang.log"
    res_file = "result.log"

    # 读取测试用例名
    if len(sys.argv) == 3:
        testcase = sys.argv[1]
        care_dist = int(sys.argv[2])
        print care_dist
    elif len(sys.argv) == 2:
        testcase = sys.argv[1]

    print testcase, care_dist

    # 获得每个用例指定的关键字pattern列表
    pattern_strings = check_dict.get(testcase, None)
    if pattern_strings is None:
        print("Testcase not configured, please try again.")
        exit(1)

    # 转换成正则pattern列表
    patterns = [re.compile(p) for p in pattern_strings]

    # 打开日志文件
    fil_log = open(log_file, 'r')

    # 打开结果文件
    res_log = open(res_file, 'w')

    # 循环读取日志，如果感兴趣，存入结果，或者打印出
    find_loi = False
    need_exit = False
    first_match = 0
    line = fil_log.readline()
    while line:
        line_num += 1
        # 找感兴趣的特征行
        for index, pattern in enumerate(patterns):
            if re.search(pattern, line) is not None:
                if index == 0:                              # 确保第一个pattern被找到，才会正式开始打印
                    find_loi = True
                    first_match = line_num                  # 记录第一个pattern起始的行号
                if find_loi:
                    output_line = "{0}: {1}".format(line_num, line)
                    if line_num > first_match + care_dist:  # 如果发现pattern的行号超过感兴趣的范围，不处理
                        need_exit = True
                    else:                                   # 还在范围内，继续处理
                        print output_line
                        res_log.write(output_line)
                        break
                else:
                    continue
            # else:
            #     # [WARN]care_dist number + first_match must be lt log total line number
            #     if line_num > first_match + care_dist:      # 如果发现pattern的行号超过感兴趣的范围，不处理
            #         need_exit = True
        if need_exit:                                       # 已经超出范围，退出
            break
        line = fil_log.readline()

    # 关闭文件
    fil_log.close()
    res_log.close()




