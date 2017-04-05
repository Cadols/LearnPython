#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing


def f(conn):
    conn.send([42, None, "hello from child"])
    conn.send([42, None, "Are you Ok?"])
    print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("Good for you.")
    p.join()
