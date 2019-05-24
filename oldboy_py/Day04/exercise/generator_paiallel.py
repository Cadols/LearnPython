#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
def customer(name):
    print("%s 准备吃包子了!" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了！" % (baozi, name))

def producer(name):
    c = customer('A')
    c2 = customer('B')
    c.__next__()
    c2.__next__()
    print("%s要开始做包子了啊！" % name)
    for i in range(10):
        time.sleep(1)
        print("第%d批包子做好了！" % (i + 1))
        c.send(i + 1)
        c2.send(i + 1)

producer("Will")