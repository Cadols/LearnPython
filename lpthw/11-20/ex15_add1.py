#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# open the file 'filename'
txt = open(filename)

# read the file
print("Here's your file %r: " % filename)
print(txt.read())

# type the file's name
print("Type the filename again:")
file_again = input("> ")

# print it's txt
txt_again = open(file_again)

print(txt_again.read())