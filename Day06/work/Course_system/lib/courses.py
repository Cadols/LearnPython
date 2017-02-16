#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Course(object):
    def __init__(self, course_name, course_tuition, course_period):
        self.course_name = course_name
        self.course_tuition = course_tuition
        self.course_period = course_period

    def status(self):
        print(" %s 的信息 ".center(20, '-') % self.course_name)
        for k, v in self.__dict__.items():
            print(" %s : %s ".center(10, ' ') % (k, v))

# python1 = Courses('python', 10000, 'eight months')
# print(python1.course_name, python1.course_tuition, python1.course_period)
