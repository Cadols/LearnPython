#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time

from logging import handlers

logger = logging.getLogger(__name__)

log_file = "timelog.log"
# fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)
fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3)

formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)

logger.warning("test1")
logger.warning("test12")
time.sleep(2)
logger.warning("test13")
logger.warning("test14")
time.sleep(2)
logger.warning("test15")
logger.warning("test16")
time.sleep(2)
logger.warning("test17")
logger.warning("test18")
time.sleep(2)
logger.warning("test19")