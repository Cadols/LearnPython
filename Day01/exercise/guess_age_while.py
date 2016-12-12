#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 31

count = 0
while True:
    guess_num = int(input('Please input your guees number:'))
    if guess_num == age:
        print('Yes, you got it!')
        break
    elif guess_num < age:
        print('Please think it bigger!')
    else:
        print('Please think it smaller!')