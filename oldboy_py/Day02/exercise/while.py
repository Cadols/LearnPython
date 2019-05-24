#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
while True:
    count += 1
    if count > 50 and count < 60:
        continue
    print('Hello world! No.%d' % count)
    if count == 100:
        print("I'm tired. Bye!")
        break