#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加断点
for i in range(0, 10):
    if i < 3:
        print('loop', i)
    else:
        continue
    print('yeah')