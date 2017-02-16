#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Class(object):
    def __init__(self, class_name, course_obj):
        self.class_name = class_name
        self.class_course = course_obj
        self.class_teacher = {}
        self.class_student = {}  # 用于查看班级学员列表

    def status(self):
        print(" %s 的信息 ".center(20, '-') % self.class_name)
        for k, v in self.__dict__.items():
            print(" %s : %s ".center(10, ' ') % (k, v))

# s14 = Classes('s14', 'python')
# print(s14.class_name, s14.class_course, s14.class_student)
