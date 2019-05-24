#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import queue
import threading


def producer(name):
    count = 1
    while True:
        q.put("bread%s" % count)
        print("%s produced bread%s" % (name, count))
        count += 1
        time.sleep(0.5)


def consumer(name):
    while True:
        print("%s have eaten %s" % (name, q.get()))
        time.sleep(1)

q = queue.Queue(maxsize=10)

p1 = threading.Thread(target=producer, args=("wang",))
p2 = threading.Thread(target=producer, args=("wei",))
c1 = threading.Thread(target=consumer, args=("will",))
c2 = threading.Thread(target=consumer, args=("lee",))

p1.start()
p2.start()
c1.start()
c2.start()
