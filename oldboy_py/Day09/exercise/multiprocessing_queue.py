#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing


def f(q):
    q.put([42, None, "hello"])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
