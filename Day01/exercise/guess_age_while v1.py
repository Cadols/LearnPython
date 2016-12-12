#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 31

count = 0
while count < 3:
    guess_num = int(input('Please input your guess number:'))
    if guess_num == age:
        print('Yes, you got it!')
        break
    elif guess_num < age:
        print('Please think it bigger')
    else:
        print('Please think it smaller!')
    count += 1
else:
    print('You have trid too many times. Byebye')