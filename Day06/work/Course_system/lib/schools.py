#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from lib import courses
from lib import classes


class School(object):
    """学校类：带名称、地址、课程、班级、讲师"""
    def __init__(self, school_name, school_location):
        self.school_name = school_name
        self.school_location = school_location
        self.school_course = {}
        self.school_class = {}
        self.school_teacher = {}
        self.school_student = {}

    def create_course(self, course_name, course_tuition, course_period):
        """创建课程"""
        course_obj = courses.Course(course_name, course_tuition, course_period)
        self.school_course[course_name] = course_obj

    def create_class(self, class_name, course_obj):
        """创建班级"""
        class_obj = classes.Class(class_name, course_obj)
        self.school_class[class_name] = class_obj

    def show_course_info(self):
        """显示课程信息"""
        print(" %s校区已有课程 ".center(20, '-') % self.school_name)
        for key in self.school_course:
            course_info = self.school_course[key]
            print("课程：%s ，学费：%s 元，学时：%s 个月" % (course_info.course_name,
                                              course_info.course_tuition, course_info.course_period))

    def show_class_info(self):
        """显示班级信息"""
        print(" %s校区已有班级 ".center(20, '-') % self.school_name)
        for key in self.school_class:
            class_info = self.school_class[key]
            course_info = class_info.class_course
            print("班级： %s ， 课程： %s ，学费： %s ，课时： %s" % (class_info.class_name,
                                                       course_info.course_name,
                                                       course_info.course_tuition,
                                                       course_info.course_period))

    def show_teacher_info(self):
        """显示讲师信息"""
        print(" %s校区已有讲师 ".center(20, '-') % self.school_name)
        for key in self.school_teacher:
            teacher_info = self.school_teacher[key]
            print("姓名： %s ，年龄： %s ， 性别： %s ， 工资： %s" % (teacher_info.name,
                                                        teacher_info.age,
                                                        teacher_info.gender,
                                                        teacher_info.salary))


# beijing = School('beijing', 'china')
# beijing.create_course('python', 10000, 'eight months')
# print(beijing.school_course['python'])
# beijing.show_course_info()
# beijing.create_class('s14', beijing.school_course['python'])
# beijing.show_class_info()
