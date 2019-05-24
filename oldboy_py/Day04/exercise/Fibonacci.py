#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(100)
"""

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield  b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print(g.__next__())
print(g.__next__())
print(g.__next__())
print("======")
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


fib_gen = fib(10)
for i in fib_gen:
    print(i)