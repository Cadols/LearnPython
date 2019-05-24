#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 31
guess_num = int(input("Please input the number you guess:"))

if guess_num == age:
    print("Congratulations! You got it!")
elif guess_num > age:
    print("Think it smaller.")
else:
    print("Think it bigger.")