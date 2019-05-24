#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b

# 24 + 34 / 100 - 1023
result = subtract(add(24, divide(34, 100)), 1023)
print("The result is: ", result)
