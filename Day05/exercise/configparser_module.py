#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'Will'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'

config['DEFAULT']['Forward11'] = 'yes'

with open('example.ini', 'w') as configfile:
    config.write(configfile)