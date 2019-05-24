#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Pycharm下不可用，仅限于Linux命令行或Windows的CMD

import getpass
username = input("username:")
passward = getpass.getpass("password:")
print(username, passward)