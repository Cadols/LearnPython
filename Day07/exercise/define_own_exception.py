#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 主动触发异常
try:
    raise IndexError("There is an IndexError")
except IndexError as e:
    print(e)


# 自定义异常
class OwnException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise OwnException("Cannot connect the database")
except OwnException as e:
    print(e)
