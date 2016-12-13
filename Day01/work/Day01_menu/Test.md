### Test
#### Day01 - 三级菜单
---
#### 2016/11/17
##### 1. 根据Alex的视频，学习知识点：字典。google相关的博客（[Python 字典(Dictionary)](http://www.runoob.com/python/python-dictionary.html)）进行学习，其中的代码全部手打一遍，感受实际效果。

#### 2016/11/18
##### 1. 完成作业：三级菜单的流程图。
##### 2. 完成作业：三级菜单的字典内容（省市信息）。

####  2016/11/19
##### 1. 学习他人的代码实现逻辑以及函数使用。
##### 2. 搜索学习函数'enumerate'[博客地址](http://blog.csdn.net/xyw_blog/article/details/18401237)。

#### 2016/11/20
#####1. 当运行程序尝试输入数字进行选择时报错：
```
Traceback (most recent call last):
  File "/Users/wangwei/OneDrive/MyPython/Day01/day01work_menu.py", line 29, in <module>
    key1 = list(menu)[menu1]
TypeError: list indices must be integers or slices, not str
```

原因为输入的数字程序不认为是数字而是字符串。
使用`int()`将字符串强行转为整数型，但是当输入内容为字符时就会报错。
```
Traceback (most recent call last):
  File "/Users/wangwei/OneDrive/MyPython/Day01/day01work_menu.py", line 29, in <module>
    menu1 = int(menu1)
ValueError: invalid literal for int() with base 10: 'b'
```

经过搜索，可使用`.isdigit()`[博客地址](http://www.runoob.com/python/att-string-isdigit.html)对输入内容进行判断，当结果为真时再进行整数转换。

##### 2. 当输入的数字大于实际的序列时，报错：
```
Traceback (most recent call last):
  File "/Users/wangwei/OneDrive/MyPython/Day01/day01work_menu.py", line 30, in <module>
    key1 = list(menu)[menu1]
IndexError: list index out of range
```

原因为输入数值大于实际列表的元素个数。
经过搜索，使用`len()`[博客地址](http://www.runoob.com/python/att-list-len.html)来得到列表的实际元素个数，用'<='作为判断条件进行限制。

#### 2016/11/21
##### 1. 完成Readme.md
##### 2. 继续补看新版视频