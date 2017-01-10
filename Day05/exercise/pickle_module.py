#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

# dumps & loads
li = [11, 22, 33]
# 将数据通过特殊的形式转换为只有Python语言认识的字符串
res = pickle.dumps(li)
print(res, type(res))
# 将只有Python语言认识的字符串转换为数据
result = pickle.loads(res)
print(result, type(result))

# dump & load
li = [11, 22, 33]
# 将数据通过特殊的形式转换为只有Python语言认识的字符串，并写入文件
pickle.dump(li, open('pickle_li', 'wb'))
# 将文件中只有Python语言认识的字符串转换为数据
result = pickle.load(open('pickle_li', 'rb'))
print(result)
