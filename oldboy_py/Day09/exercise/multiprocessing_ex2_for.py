#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import multiprocessing


def run(name):
    time.sleep(2)
    print("Hello", name)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=("bob %s" % i,))
        p.start()
