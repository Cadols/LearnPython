#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from conf.settings import *


def logger(log_file, log_level, log_type, message):
    """log日志"""
    log_file_path = os.path.join(LOG_DIR_PATH, log_file + ".log")

    # 创建logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    logger_dic = {
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

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    logger_dic.get(log_level)(message)
    logger.removeHandler(ch)
    logger.removeHandler(fh)

    return logger
