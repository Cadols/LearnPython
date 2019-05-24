#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# logging.basicConfig(filename='example.log', level=logging.WARNING)
# logging.debug("test debug")
# logging.info("test info")
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.error("test error")
# logging.critical("server is down")

logging.basicConfig(format='%(asctime)s %(filename)s:%(lineno)d - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug("test debug")
logging.info("test info")
logging.warning("user [alex] attempted wrong password more than 3 times")
logging.error("test error")
logging.critical("server is down")