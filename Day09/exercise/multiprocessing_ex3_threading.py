#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import multiprocessing


def run(name):
    time.sleep(2)
    print("Hello", name)
    t = threading.Thread(target=thread_run, args=(name,))
    t.start()


def thread_run(name):
    print("%s's id" % name, threading.get_ident())

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=("bob %s" % i,))
        p.start()
