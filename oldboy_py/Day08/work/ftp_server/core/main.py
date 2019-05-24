#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socketserver
from conf.settings import *
from core.ftp_server import *


def run():
    try:
        os.mkdir(DB_PATH)
        os.mkdir(LOG_DIR_PATH)
        os.mkdir(HOME_PATH)
    except FileExistsError as e:
        pass
    server = socketserver.ThreadingTCPServer((server_ip, server_port), MyTCPHandler)
    server.serve_forever()
