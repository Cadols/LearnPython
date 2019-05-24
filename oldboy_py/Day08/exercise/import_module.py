#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 解释器内部使用
# lib = __import__('lib.aa')
# print(lib.aa.C().name)


# 官方建议用这个
import importlib
aa = importlib.import_module("lib.aa")
print(aa.C().name)
