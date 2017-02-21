#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 普通方法
class Foo(object):
    def func(self):
        print("hello, Will")


# 特殊方法
def func(self):
    print("hello, Will")

Foo = type('Foo', (object,), {'func': func})  # type第一个参数：类名，第二个参数：当前类的基类，第三个参数：类的成员
f = Foo()


# example
def func(self):
    print("Hello, %s" % self.name)

def __init__(self, name, age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'__init__': __init__,
                              'func': func})
f = Foo("Will", 30)
print(type(Foo))
f.func()