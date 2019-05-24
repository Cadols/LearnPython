#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db')
ACCOUNT_DB_PATH = os.path.join(BASE_DIR, 'db', 'account.db')
USER_HOME_PATH = os.path.join(BASE_DIR, 'home')
HOST = 'localhost'
PORT = 23333

# print(ACCOUNT_DB_PATH)
# print(USER_HOME_PATH)