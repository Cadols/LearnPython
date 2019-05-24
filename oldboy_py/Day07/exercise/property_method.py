#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print("%s is eating %s" % (self.name, "meat"))
#
# d = Dog("Doggy")
# # d.eat()
# # 已经为静态属性，不是方法，不需要括号
# d.eat
#
# # 为静态属性后的方法传值


class Dog(object):
    def __init__(self, name):
        self.name = name
        self.__food = None  # 设置私有属性 food 为 None

    @property  # 设置属性方法，将方法变为静态属性
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter  # 为静态属性传值
    def eat(self, food):
        print("set %s to food %s" % (self.name, food))
        self.__food = food  # 将值赋给私有属性 food

    @eat.deleter  # 删除属性方法，普通方式无法删除。
    def eat(self):
        del self.__food
        print("It is deleted.")

d = Dog("Doggy")
d.eat
d.eat = 'pork'
d.eat
del d.eat  # 删除属性方法
