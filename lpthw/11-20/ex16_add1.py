#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print("I'm going to open file:", filename)
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
