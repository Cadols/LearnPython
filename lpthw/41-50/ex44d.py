#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Parent(object):

    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")
        
        
class Child(Parent):

    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

# use class Parent's method
dad.implicit()
son.implicit()

# use class Parent or Child's method
dad.override()
son.override()

# use class Parent and Child inheritance method
dad.altered()
son.altered()
