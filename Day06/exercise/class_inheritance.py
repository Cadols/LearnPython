#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("This person %s is talking..." % self.name)


class Blackperson(Person):
    def __init__(self, name, age, musle):  # 先继承，再重构
        Person.__init__(self, name, age)
        self.musle = musle

    def talk(self):
        Person.talk(self)  # 继承父类方法
        print("The black person %s talk too much..." % self.name)

    def walk(self):
        print("The Black person %s is walking..." % self.name)

d = Blackperson('Will Simth', 45, 'strong')
d.talk()
d.walk()
