#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(name):
	print("What's your name?")
	print("My name is %s.\n" % name)

# 1
func("Will")
# 2
func("Will" + "Wang")
# 3
name1 = 'Hello'
func(name1)
# 4
func(name1 + "Will")
# 5
name2 = 'Woo'
func(name1 + name2)
# 6
name3 = input("Please input your name.\n> ")
func(name3)
# 7
func(name1 + name3)
# 8
func(func('What?'))
# 9
# 10