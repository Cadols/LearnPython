#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def while_loop(loop_times):
	i = 0
	numbers = []
	while i < int(loop_times):
		print("At the top i is %d" % i)
		numbers.append(i)

		add_value = 1
		i = i + add_value
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)

	print("The numbers: ")
	for num in numbers:
		print(num)

loop_times = input("Times: ")
while_loop(loop_times)
