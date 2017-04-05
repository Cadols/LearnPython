#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import multiprocessing


def info(title):
    print(title)
    print("Module name:", __name__)
    print("Parent process id:", os.getppid())
    print("Current process id:", os.getpid())
    print("\n")


def f(name):
    info("child process function f")
    print("Hello", name)


if __name__ == '__main__':
    info("Main process line")
    p = multiprocessing.Process(target=f, args=("bob",))
    p.start()
    p.join()
