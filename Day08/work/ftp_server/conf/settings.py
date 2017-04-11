#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME_PATH = os.path.join(BASE_DIR, "home")
DB_PATH = os.path.join(BASE_DIR, "db")
LOG_DIR_PATH = os.path.join(BASE_DIR, "log")
STORAGE_SIZE = 102400000  # 新用户默认存储空间 100MB

server_ip = 'localhost'
server_port = 23333
