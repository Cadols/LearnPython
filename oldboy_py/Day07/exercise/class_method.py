#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def eat(self):
#         print("%s is eating %s" % (self.name, "food"))
#
# d = Dog("Doggy")
# d.eat()


class Dog(object):
    name = 'Wangwang'

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating %s" % (self.name, "food"))

d = Dog("Doggy")
d.eat()