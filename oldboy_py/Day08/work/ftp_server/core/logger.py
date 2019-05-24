#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from conf.settings import *


def logger(log_file, log_type, log_level, message):
    # 设置 log 文件地址
    log_file_path = os.path.join(LOG_DIR_PATH, log_file + ".log")

    # 创建 logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)
    LOGGER_DIC = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }

    # 创建 console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 创建 file handler
    fh = logging.FileHandler(log_file_path, encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    LOGGER_DIC[log_level](message)  # 根据字典使用不同级别的日志

    logger.removeHandler(ch)
    logger.removeHandler(fh)
    return logger
