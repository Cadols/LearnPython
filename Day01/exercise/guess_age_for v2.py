#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 31
counter = 0 #自己的计数器
for i in range(10):
    if counter < 3:
        guess_num = int(input("Please input the number you guess:"))
        if guess_num == age:
            print("Congratulations! You got it!")
            break #停止往后继续走，跳出整个loop
        elif guess_num > age:
            print("Think it smaller.")
        else:
            print("Think it bigger.")
    else:
        continue_confirm = input("Do you want try it again? type y to continue : ")
        if continue_confirm == "y":
            counter = 0
            continue #跳出本次循环
        else:
            print("bye")
            break
    counter += 1