#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue
import threading


def producer(name):
    for i in range(10):
        q.put("bread%s" % i)
        print("%s produced bread%s" % (name, i))


def consumer(name):
    while q.qsize() > 0:
        print("%s have eaten %s" % (name, q.get()))

q = queue.Queue()

p = threading.Thread(target=producer, args=("will",))
c = threading.Thread(target=consumer, args=("grubby",))

p.start()
c.start()
