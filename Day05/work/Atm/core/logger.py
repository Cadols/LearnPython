#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from conf import settings


def logger(log_type, user_name, message):
    # 根据文件夹是否存在，确定是否创建该文件夹
    log_file_dir = "%s/log/%s" % (settings.BASE_DIR, user_name)
    if not os.path.exists(log_file_dir):
        os.mkdir(log_file_dir)
    log_file = "%s/log/%s/%s" % (settings.BASE_DIR, user_name, settings.LOG_TYPES[log_type])

    # 创建logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    # 创建console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 创建file handler
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info(message)
    logger.removeHandler(ch)
    logger.removeHandler(fh)
    return logger
