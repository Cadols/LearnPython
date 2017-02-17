#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

d = Dog("Doggy")
d.eat("meat")


# staticmethod 与类已经没有关系了
class Cat(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print("%s is eating %s" % ("Kitty", "fish"))

    # 强行调用self属性
    @staticmethod
    def talk(self):
        print("%s is talking" % self.name)

c = Cat("Meo")
c.eat()
c.talk(c)
