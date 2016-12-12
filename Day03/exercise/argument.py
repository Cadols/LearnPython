#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
def test(x,y,z):
    print(x)
    print(y)
    print(z)

test(1, 2, 3)       # 位置参数
test(3, z=6, y=9)   # 关键参数

# 默认参数
def test(x,y=2):
    print(x)
    print(y)

test(1)
test(1,10)

# 非固定参数
def test(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    print(kwargs['sex'])
    print(kwargs['age'])

# test(2, 5)      # 不传值则为空
test(1, 3, 5, 7, 9, sex='F', age=11)     # 前面加*设为非固定参数，多出的实参为元组

# 全局变量与局部变量
name = 'Will'

def change_name(name):
    print("before change:", name)
    name = 'William'
    print('after name', name)

change_name(name)
print(name)

# 在函数内改变全局变量要先声明
name = 'Will'
school = 'Hometown'

def change_name(name):
    global school
    print("before change:", name)
    name = 'William'
    school = 'University'
    print('after name', name)

change_name(name)
print(name,school)
"""
# 高阶函数
def add(a, b, f):
    return f(a)+f(b)

res = add(3, 6, abs)
print(res)