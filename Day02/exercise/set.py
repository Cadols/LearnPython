#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
list1 = [1, 4, 5, 1, 7, 1, 5, 9]
list1 = set(list1)
print(list1, type(list1))

list2 = set([2, 3, 1, 6, 8, 7])
print(list2)

print(len(list1), len(list2))
print(4 in list1, 4 in list2)
print(2 not in list1, 2 not in list2)

print(list1.union(list2), list1 | list2)    # 并集
print(list1.intersection(list2), list1 & list2) # 交集
print(list1.difference(list2), list1 - list2)   # 差集
print(list2.difference(list1), list2 - list1)

list3 = set([4, 5, 9])
print(list3.issubset(list1), list3 <= list1)    # 子集
print(list1.issuperset(list3), list1 >= list3)  # 父集
print(list1.symmetric_difference(list2))    # 对称差集

list4 = set ([0, 10, 100])
print(list3.isdisjoint(list1), list4.isdisjoint(list1))     # 零交集

list5 = list1.copy()    # 浅复制
print(list1, list5)

# 添加
list1.add('a')      # 单个
list2.update(['b', 'c', 'd'])   #多个
print(list1, list2)

# 删除
list1.pop()
list2.remove('b')
list2.discard('c')
list2.discard('aaaa')
print(list1, list2)
"""

# 课堂练习
old_dict = {
    '#1': 8,
    '#2': 4,
    '#4': 2
}

new_dict ={
    '#1': 4,
    '#2': 4,
    '#3': 2
}

old_set = set(old_dict.keys())
new_set = set(new_dict.keys())

del_set = old_set.difference(new_set)   # 应该删除old中有new中无的差集
update_set = old_set.intersection(new_set)  # 应该更新old和new的交集
add_set = new_set.difference(old_set)   # 应该增加new中有old中无的差集

print(del_set)
print(update_set)
print(add_set)