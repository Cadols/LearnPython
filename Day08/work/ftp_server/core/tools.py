#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib


def hash(data):
    """进行MD5处理"""
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()


def color(path):
    """更改输出的文件或文件夹名称颜色"""
    dir_str = "server: "
    if os.listdir(path):
        dir_list = os.listdir(path)
        for i in dir_list:
            if os.path.isfile(os.path.join(path, i)):
                dir_str += "\033[1;37m%s\033[0m  " % i
            elif os.path.isdir(os.path.join(path, i)):
                dir_str += "\033[1;34m%s\033[0m  " % i
    else:
        dir_str += "空文件夹"
    # print(dir_str)
    return dir_str


def get_dir_size(dir_name):
    """遍历文件夹获得文件夹总大小"""
    size = 0
    for root, dirs, files in os.walk(dir_name):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size
