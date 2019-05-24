#!/usr/bin/env python
# -*- coding: utf-8 -*-


# __doc__
class Dog(object):
    """This is a class for dog."""

    def __init__(self, name):
        self.name = name

d = Dog("Wangwang")
print(Dog.__doc__)
print(d.__doc__)

# __module__ & __class__
from lib.aa import C

obj = C()
print(obj.__module__)  # 输出 lib.aa，即：输出模块
print(obj.__class__)  # 输出 lib.aa.C，即：输出类


# __call__
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("call", args, kwargs)

obj = Foo()  # 执行 __init__
Foo()()
obj(1234, name='abc')  # 执行 __call__


# __dict__
class Dog(object):
    def __init__(self, name):
        self.name = name

d = Dog("Wangwang")
print(Dog.__dict__)  # 打印类里的所有属性，不包括实例属性
print(d.__dict__)  # 打印所有实例属性，不包括类属性


# __str__
class Dog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 在打印对象时，默认输出该方法的返回值
        return "<Dog : %s>" % self.name

d = Dog("Wangwang")
print(d)


# __getitem__, __setitem__, delitem__
class Foo(object):
    def __getitem__(self, key):
        print("__getitem__", key)

    def __setitem__(self, key, value):
        print("__setitem__", key, value)

    def __delitem__(self, key):
        print("__delitem__", key)

obj = Foo()
obj['name'] = 'Will'
