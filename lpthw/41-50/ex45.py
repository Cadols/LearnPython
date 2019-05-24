#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Test(object):
    name = "China"
    def __init__(self, age):
        self.age = age
        print(self.name)
    
    def dig(self):
        print("Here is a hole you can dig.")
        
t = Test(2017-1949)
print(t.name)
print(t.age)
print(t.__dict__)
print(Test.__dict__)

class Parent(object):
    """This is a class of Paarent"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print("%s is walking." % self.name)
    

class Child(Parent):
    """This is a class of Child"""
    def __init__(self, name, age, sex):
        super(Child, self).__init__(name, age)
        self.sex = sex
        self.dig = Test(self.age)
    
    def play(self):
        if self.sex == "Male":
            self.kid = "boy"
        else:
            self.kid = "girl"
        print("There is a %d years old %s who named %s is playing." % (self.age, self.kid, self.name))
        self.dig.dig()
        
dad = Parent("Carl", 40)
son = Child("Sam", 6, "Male")
daughter = Child("Nancy", 4, "Female")

dad.walk()
son.walk()
son.play()
daughter.walk()
daughter.play()
print(Parent.__doc__)
print(dad.__doc__)
