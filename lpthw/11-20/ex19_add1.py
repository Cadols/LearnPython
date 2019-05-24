#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have %d cheeses!" % cheese_count)
	print("You have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# call func and the variable is 20 and 30
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# define the variable amount_of_cheese and amount_of_crackers
amount_of_cheese = 10
amount_of_crackers = 50
# call func and the variable is 10 and 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# call func and the variable is 10+20 and 5+6
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# call func and the variable is amount_of_cheese+100 and amount_of_crackers+1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)