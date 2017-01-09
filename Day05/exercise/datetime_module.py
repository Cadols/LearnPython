#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime

print(datetime.datetime.now())  # 返回 当前时间
print(datetime.datetime.fromtimestamp(time.time()))  # 时间戳直接转成日期格式

print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=-3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分钟

c_time = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))  # 时间替换