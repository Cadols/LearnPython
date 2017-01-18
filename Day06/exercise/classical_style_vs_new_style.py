#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""类的写法区别"""
# class Person(object):  # new style
#     super(Person, self).()
#
#
# class Person:  # classical style
#     Person.__init__()


"""多继承时，继承顺序的区别"""
# 新式类
# class A(object):
#     def __init__(self):
#         self.n = 'A'
#
# class B(A):
#     def __init__(self):
#         self.n = 'B'
#
# class C(A):
#     def __init__(self):
#         self.n = 'C'
#
# class D(B, C):
#     def __init__(self):
#         self.n = 'D'
#
# d = D()
# print(d.n)


# 经典类
class A:
    def __init__(self):
        self.n = 'A'

class B(A):
    # pass
    def __init__(self):
        self.n = 'B'

class C(A):
    # pass
    def __init__(self):
        self.n = 'C'

class D(B, C):
    # pass
    def __init__(self):
        self.n = 'D'

d = D()
print(d.n)
