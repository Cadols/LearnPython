#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


# in python2
def run():
    global num
    num += 1

num = 0

for i in range(500):
    t = threading.Thread(target=run)
    t.start()

print("------ all threads have finished ------")
print("num:", num)
