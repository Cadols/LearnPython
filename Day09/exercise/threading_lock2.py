#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def run():
    lock.acquire()  # 修改数据前加锁
    global num
    num += 1
    lock.release()  # 修改数据后释放锁

num = 0
lock = threading.Lock()  # 生成全局锁
for i in range(500):
    t = threading.Thread(target=run)
    t.start()

print("------ all threads have finished ------")
print("num:", num)
