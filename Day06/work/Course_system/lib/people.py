#!/usr/bin/env python
# -*- coding: utf-8 -*-


class People(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def status(self):
        print(" %s 的信息 ".center(20, '-') % self.name)
        for k, v in self.__dict__.items():
            print(" %s : %s ".center(20, ' ') % (k, v))


class Teacher(People):
    def __init__(self, name, age, gender, salary):
        super(Teacher, self).__init__(name, age, gender)
        self.salary = salary
        self.teacher_class = {}  # 用于上课选择班级

    def relate_class(self, class_name, class_obj):
        self.teacher_class[class_name] = class_obj


class Student(People):
    def __init__(self, name, age, gender, money):
        super(Student, self).__init__(name, age, gender)
        self.money = money
        self.score = {}  # 用于存放课程成绩

    def gain_money(self):
        gain_flag = False
        while not gain_flag:
            new_money = input("\033[34m请输入您想储值的金额：\033[0m").strip()
            if new_money.isdigit():
                self.money = int(self.money)
                self.money += int(new_money)
                gain_flag = True
            else:
                print("\033[1;31m输入格式有误，请重试。\33[0m")

# will = Teacher('will', 31, 'male', 123, 30000)
# will.status()
