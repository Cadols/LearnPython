#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.ERROR)

# create formatter
ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d - %(message)s')

# add formatter to ch and fh
ch.setFormatter(ch_formatter)
fh.setFormatter(fh_formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.warning("I'm warning.")
logger.error("I'm error.")