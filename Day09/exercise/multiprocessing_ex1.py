#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time


def run(name):
    time.sleep(2)
    print("Hello", name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=run, args=('bob',))
    p.start()
