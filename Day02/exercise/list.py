#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
写一个列表，列表中包含本组所有成员。
往中间插入两个临组成员的名字
取出第3-8的人列表
删除第7个人
把刚才加入的那2个其他组的人一次性删除
把组长的名字加上组长备注
隔一个人取值
"""

name = ['sublime', 'Will', 'Null', 'D', 'Alvin', '半塘', 'Fedor', 'smoonb', '行者无疆']
print('写一个列表，列表中包含本组所有成员：\n',name)

name.insert(4, '9组:sdo')
name.insert(4, '7组:cicia')
print('\n往中间插入两个临组成员的名字：\n', name)

name2 = name[2:8]
print('\n取出第3-8的人列表：\n', name2)

name.remove('Alvin')
print('\n删除第7个人：\n', name)

del name[4:6]
print('\n把刚才加入的那2个其他组的人一次性删除：\n', name)

name[0] = 'sublime(导师)'
print('\n把导师的名字加上导师备注：\n', name)

print('\n隔一个人取值\n', name[::2])