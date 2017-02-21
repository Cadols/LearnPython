#!/usr/bin/env python
# -*- coding: utf-8 -*-


class OwnException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise OwnException("Cannot connect the database")
except OwnException as e:
    print(e)
