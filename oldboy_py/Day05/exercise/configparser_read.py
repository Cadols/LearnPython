#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read('example.ini')
print(config.read('example.ini'))
print(config.sections())

print('bitbucket.org' in config)
print('byebong.com' in config)

print(config['bitbucket.org']['User'])
print(config['DEFAULT']['compression'])

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])

val1 = config.get('bitbucket.org', 'user')
val2 = config.getint('topsecret.server.com', 'port')

print(val1, val2)
for key in config['bitbucket.org']:
    print(key)