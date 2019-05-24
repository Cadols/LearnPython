#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import hashlib


def hash(data):
    """进行MD5处理"""
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()


def color(path):
    """更改输出的文件或文件夹名称颜色"""
    dir_str = "local: "
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


def progress_bar(amount, total):
    rate = (amount / total)
    rate_num = int(round(rate * 100))
    # if rate_num < 100:
    #     bar_str = "\r[%d%%] %s" % (rate_num, "*" * int(rate_num/2))
    # else:
    #     bar_str = "\r[%d%%] %s" % (rate_num, "Done" + " " * 50)
    if rate_num < 100:
        bar_str = "\r%s[%d%%]" % ("*" * int(rate_num / 2), rate_num)
    else:
        bar_str = "\r%s[%d%%]" % ("*" * int(rate_num / 2), rate_num) + "Done"
    sys.stdout.write(bar_str)
    sys.stdout.flush()
