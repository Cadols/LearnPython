#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 封装
# class F1:
#     def __init__(self, n):
#         self.N = n
#         print('F1')
#
# class F2:
#     def __init__(self, arg1):
#         self.a =arg1
#         print('F2')
#
# class F3:
#     def __init__(self, arg2):
#         self.b = arg2
#         print('F3')
#
# o1 = F1('Alex')
# o2 = F2(o1)
# o3 = F3(o2)
# ###### Print Alex ######
# o3.b.a.N


# 继承
class F1(object):
    def __init__(self):
        print('F1')

    def a1(self):
        print("F1a1")

    def a2(self):
        print("F1a2")

class F2(F1):
    def __init__(self):
        print('F2')

    def a1(self):
        self.a2()
        print("F2a1")

    def a2(self):
        print("F2a2")

class F3(F2):
    def __init__(self):
        print('F3')

    # def a1(self):
    #     print("F3a1")

    def a2(self):
        print("F3a2")

obj1 = F3()
obj1.a1()