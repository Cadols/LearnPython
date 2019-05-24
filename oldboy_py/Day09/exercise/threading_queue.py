#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue


# 先入先出
q = queue.Queue()
q.put("disk1")
q.put("disk2")
q.put("disk3")
q.put("disk4")
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# Last in first out
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 存储数据时可设置优先级的队列
q = queue.PriorityQueue()
q.put((10, "people1"))
q.put((4, "people2"))
q.put((-1, "VIP"))
q.put((6, "people3"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
