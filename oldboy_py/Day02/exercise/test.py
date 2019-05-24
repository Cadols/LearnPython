#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
进度条
文件移动seek
r+ w+


import sys, time
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.3)

f = open('Yesterday', 'r')
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.seek(0))
print(f.readline())

f = open('Yesterday2', 'w+')
f.write('what?')
f.readline()
"""