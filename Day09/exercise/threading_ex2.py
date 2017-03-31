#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):  # 定义每个线程要运行的函数
        print("running task ", self.n)
        time.sleep(2)

t1 = MyThread("t1")
t2 = MyThread("t2")
t1.start()
t2.start()
