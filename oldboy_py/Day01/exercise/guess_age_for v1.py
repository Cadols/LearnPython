#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 31
for i in range(10):
    if i < 3:
        guess_num = int(input("Please input the number you guess:"))
        if guess_num == age:
            print("Congratulations! You got it!")
            break #停止往后继续走，跳出整个loop
        elif guess_num > age:
            print("Think it smaller.")
        else:
            print("Think it bigger.")
    else:
        print("You have tried too many times, good bye.")
        break