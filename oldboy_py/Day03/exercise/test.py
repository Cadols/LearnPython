#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('haproxy', 'r') as f:
    for line in f:
        print(line.strip())
        print(bool(line.strip()))

# {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
# {"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}