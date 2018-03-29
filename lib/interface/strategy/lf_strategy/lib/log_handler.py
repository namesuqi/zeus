# -*- coding: utf-8 -*-

"""
__author__ = 'liwenxuan'
__modify__ = 20170808

作用: 记录测试过程中的输入数据

"""

import logging
import time

# ---------------------------------------------------------------------------------------------------------------------

# 记录输入数据的文件名
date = time.strftime("%m-%d", time.localtime())

log_file_name = "log/" + date + "_ss_input"
script_file_name = "log/" + date + "_ss_input"

# ---------------------------------------------------------------------------------------------------------------------

# 日志输出等级(level), 从高到低为: CRITICAL/FATAL, ERROR, WARNING/WARN, INFO, DEBUG, NOTSET

# ---------------------------------------------------------------------------------------------------------------------

# 将发送给kafka的logs的具体信息记录在指定文件中
log_logger = logging.getLogger("lf_scheduling_strategy_log")
log_logger.setLevel(logging.DEBUG)

log_file_handler = logging.FileHandler(log_file_name + "_detail.log", 'a')
log_file_handler.setFormatter(logging.Formatter("%(asctime)s -- %(message)s", '%Y-%m-%d %H:%M:%S'))
log_logger.addHandler(log_file_handler)

# ---------------------------------------------------------------------------------------------------------------------

# 将测试过程中产生的需要关注的信息记录在指定文件中
logger = logging.getLogger("lf_scheduling_strategy")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(script_file_name + "_info.log", 'a')
file_handler.setFormatter(logging.Formatter("%(asctime)s -- %(message)s", '%Y-%m-%d %H:%M:%S'))
logger.addHandler(file_handler)

# 建立一个stream_handler, 用于在窗口中打印需要关注的信息
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter("%(asctime)s -- %(message)s", '%m-%d %H:%M:%S'))
logger.addHandler(console)

# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    pass
    # logger.debug("logger debug msg")
    # logger.info("logger info msg")
    # logger.warning("logger warn msg")
    # logger.error("logger error msg")




