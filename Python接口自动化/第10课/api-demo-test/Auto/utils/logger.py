# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         logger
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import logging
from logging.handlers import RotatingFileHandler
import os
import time


def init_logger(log_file_path):
    """
    :param log_file_path:  日志路径
    :return:
    """
    dir_path = os.path.dirname(log_dir_path)

    if not os.path.isdir(dir_path):
        # TODO 默认路径
        os.makedirs(dir_path)

    handler = RotatingFileHandler(log_file_path, maxBytes=20 * 1024 * 1024, backupCount=10)
    fmt = "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logging_instance = logging.getLogger("logs")

    logging_instance.addHandler(handler)
    logging_instance.setLevel(logging.DEBUG)

    return logging_instance


main_path = str(__file__).split("Auto")
#
log_dir_path = main_path[0] + os.sep.join(["Auto", "log", "{}.log"])
#
# print(log_dir_path)
log_name = time.strftime("%Y-%m-%d", time.localtime())

logger = init_logger(str(log_dir_path).format(log_name))

if __name__ == '__main__':
    logger.info("---")
