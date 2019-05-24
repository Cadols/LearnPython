#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def logger(user_data, message):
    # 创建日志
    pur_list = logging.getLogger()
    pur_list.setLevel(logging.INFO)

    # 创建
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    log_path = "%s/log/%s_purchased.log" % (BASE_DIR, user_data['user_name'])
    fh = logging.FileHandler(log_path, encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 日志格式
    log_format = logging.Formatter('%(asctime)s - %(message)s')

    ch.setFormatter(log_format)
    fh.setFormatter(log_format)

    pur_list.addHandler(ch)
    pur_list.addHandler(fh)
    pur_list.info(message)
    pur_list.removeHandler(ch)
    pur_list.removeHandler(fh)
    return pur_list
