#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.ftp_server import *
from conf.settings import *

if __name__ == "__main__":
    FtpServer(HOST, PORT).run()