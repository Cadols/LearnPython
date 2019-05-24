#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将文本中全部的"我"替换为"你"
"""
f = open('Yesterday2', 'r', encoding='utf-8')
f_new = open('Yesterday2.bak', 'w', encoding='utf-8')
for line in f:
    if '我' in line:
        line = line.replace('我', '你')
    f_new.write(line)
f.close()
f_new.close()

# 带with语句
with open('Yesterday2', 'r', encoding='utf-8') as f:
    for line in f:
        if '我' in line:
            line = line.replace('我', '你')
        with open('Yesterday.bak', 'w', encoding='utf-8') as f_new:
            f_new.write(line)
"""

with open('Yesterday2', 'r', encoding='utf-8') as f,\
        open('Yesterday2.bak', 'w', encoding='utf-8') as f_new:
    for line in f:
        if '我' in line:
            line = line.replace('我', '你')
        f_new.write(line)