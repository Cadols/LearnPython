#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog(object):
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print("hello, %s is a dog!" % self.name)

    def eat(self, food):
        print("%s is eating %s!" % (self.name, food))

d = Dog("good")
d.sayhi()
d.eat('meat')
