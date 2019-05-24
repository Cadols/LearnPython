#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import multiprocessing


def f(d, l):
    d["%s" % os.getpid()] = os.getpid()
    l.append(os.getpid())
    print("For now is", os.getpid())
    print(d)
    print(l)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    d = manager.dict()  # 生成一个可在多个进程间共享和传递的字典
    l = manager.list(range(5))  # 生成一个可在多个进程间共享和传递的列表
    p_list = []
    for i in range(10):
        p = multiprocessing.Process(target=f, args=(d, l))
        p.start()
        p_list.append(p)
    for res in p_list:
        p.join()
