#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
find_str = sys.argv[1]
replace_str = sys.argv[1]

with open('Yesterday2', 'r', encoding='utf-8')as f,\
        open('Yesterday3', 'w', encoding='utf-8') as f_new:
    for line in f:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        f_new.write(line)
