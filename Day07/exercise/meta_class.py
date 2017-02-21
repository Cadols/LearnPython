#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyType(type):
    def __init__(self, child_cls, bases=None, dict=None):
        print("--MyType init---", child_cls, bases, dict)
        # super(MyType, self).__init__(child_cls, bases, dict)

    # def __new__(cls, *args, **kwargs):
    #     print("in mytype new:",cls,args,kwargs)
    #     type.__new__(cls)

    def __call__(self, *args, **kwargs):
        print("in mytype call:", self, args, kwargs)
        obj = self.__new__(self, args, kwargs)

        self.__init__(obj, *args, **kwargs)


class Foo(object, metaclass=MyType):  # in python3
    # __metaclass__ = MyType  # in python2

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):
        print("Foo --new--")
        return object.__new__(cls)  # 继承父类的__new__方法

    def __call__(self, *args, **kwargs):
        print("Foo --call--", args, kwargs)


# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Alex")
# print(obj.name)