#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# doc = open('Yesterday', encoding='utf-8').read()      # 不符合规范
# f = open('Yesterday', 'r', encoding='utf-8')     # 文件句柄
# doc = f.read()
# f = open('Yesterday2', 'w', encoding='utf-8')
# doc = f.write('昨天还是昨天')
# f = open('Yesterday2', 'a', encoding='utf-8')
# doc = f.write('\n今天成为今天')
# print(doc)

"""
# 读取到第9行时，打印分割线
# low
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("我是分隔线".center(20, '-'))
    print(line.strip())

# superior
count = 0
for line in f:
    if count == 9:
        print("我是分隔线".center(20, '-'))
        count += 1
        continue
    print(line.strip())
    count += 1


print(f.tell())         # 获取当前光标位置。 （0）
print(f.readline())     # 打印第一行
print(f.readline())     # 打印第二行
print(f.tell())         # 获取当前光标位置。 （140）
print(f.seek(0))        # 光标移回至起始处
print(f.readline())     # 打印从0起始到一行结束

import sys, time
for i in range(100):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)     # 每打印一个sleep0.1秒
"""

f = open('Yesterday2', 'r+', encoding='utf-8')      # 读写
f = open('Yesterday2', 'w+', encoding='utf-8')      # 写读
f = open('Yesterday2', 'a+', encoding='utf-8')      # 追加读
f = open('Yesterday2', 'rb', encoding='utf-8')      # 二进制格式读
