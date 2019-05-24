#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
config = configparser.ConfigParser()
config.read('example.ini')

# 读取
print(config.sections())
print(config.options('bitbucket.org'))
print(config.options('topsecret.server.com'))

val1 = config.get('bitbucket.org', 'user')
val2 = config.getint('topsecret.server.com', 'port')
print(val1, val2)

# 改写
config.remove_section('bitbucket.org')  # 删除section
config.write(open('exmaple2.ini', 'w'))

config.has_section('www.server.com')  # 如果有section
config.add_section('www.server.com')  # 添加section
config.write(open('exmaple2.ini', 'w'))

config.set('topsecret.server.com', 'port', '3000')  # 修改
config.write(open('exmaple2.ini', 'w'))

config.remove_option('topsecret.server.com', 'forwardx11')  # 删除option中的值
config.write(open('exmaple2.ini', 'w'))