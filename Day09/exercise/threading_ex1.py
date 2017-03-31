#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def run(n):  # 定义每个线程要运行的函数
    print("task ", n)
    time.sleep(2)

t1 = threading.Thread(target=run, args=("t1",))  # 生成一个线程实例
t2 = threading.Thread(target=run, args=("t2",))  # 生成另一个线程实例

t1.start()  # 启动线程
t2.start()  # 启动另一个线程

print(t1.getName())  # 获取线程名
print(t2.getName())

# 非多线程对比
# run("t1")
# run("t2")
