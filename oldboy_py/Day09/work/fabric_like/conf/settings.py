#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR_PATH = os.path.join(BASE_DIR, "db")
DB_FILE_PATH = os.path.join(DB_DIR_PATH, "host.db")
LOG_DIR_PATH = os.path.join(BASE_DIR, "log")
FILE_DIR_PATH = os.path.join(BASE_DIR, 'files')
DOWNLOAD_PATH = os.path.join(BASE_DIR, 'downloads')
