#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# dumps & loads
dic = {"k1": 123}
print(dic, type(dic))
# 将Python基本数据类型转换为字符串形式
result = json.dumps(dic)
print(result, type(result))

s1 = '{"k2": 321}'
print(s1, type(s1))
# 将字符串形式转换为Python基本数据类型
result2 = json.loads(s1)
print(result2, type(result2))

# dump & load
li = [11, 22, 33]
# 将Python基本数据类型转换为字符串形式，并且写入指定文件
json.dump(li, open('json_li', 'w', encoding='utf-8'))
# 将指定文件中的字符串形式转换为Python基本数据类型
li2 = json.load(open('json_li', 'r', encoding='utf-8'))
print(li2)


# 基于天气API获取天气相关Json数据
# import json
# import resquests  # 第三方模块，获取返回值
#
# response = resquests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# response.encoding = 'utf-8'
# print(response)
# dic = json.loads(response)
# print(type(dic), dic)
