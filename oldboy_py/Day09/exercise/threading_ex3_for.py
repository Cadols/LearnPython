#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def run(n):
    print("task ", n)
    time.sleep(2)
    print("task done", n)

start_time = time.time()
t_objs = []  # 保存线程实例
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    t.start()
    t_objs.append(t)  # 将线程对象放入列表

for i in t_objs:  # 循环线程实例列表，等待所有线程执行完毕
    t.join()

print("------ all threads have finished ------")
print(threading.current_thread(), threading.active_count())
print("cost:", time.time() - start_time)
