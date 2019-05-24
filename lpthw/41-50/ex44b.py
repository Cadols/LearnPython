#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):

    def implicit(self):
        print("CHILD implicit()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
