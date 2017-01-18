#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SchoolMember(object):
    """学校成员基类"""
    member = 0
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        """注册"""
        print("A new school member [%s] has been enrolled" % self.name)
        SchoolMember.member += 1

    def tell(self):
        print("-----%s info-----" % self.name)
        for k, v in self.__dict__.items():
            print('\t', k, ':', v)

    def __del__(self):
        print("%s has been kicked off" % self.name)
        SchoolMember.member -= 1


class School(object):
    def branch(self, address):
        self.address = address
        print("Openning a new branch school in %s" % self.address)


class Teacher(SchoolMember, School):  # 多继承
    """讲师类"""
    def __init__(self, name, age, sex, salary, course):
        # SchoolMember.__init__(self, name, age, sex)  # 经典类写法
        super(Teacher, self).__init__(name, age, sex)  # 新式类写法
        self.salary = salary
        self.course = course

    def teach(self):
        print("Teacher [%s] is teaching [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, tuition, course):
        # SchoolMember.__init__(self, name, age, sex)
        super(Student, self).__init__(name, age, sex)
        self.tuition = tuition
        self.course = course
        self.amount = 0

    def pay_tuition(self, amount):
        print("student [%s] has paid [%s]" % (self.name, amount))
        self.amount += amount

t1 = Teacher('Alex', 32, 'Male', 1000000, 'Python')
s1 = Student('Will', 32, 'Male', 7000, 'PY_Net')
s2 = Student('Simth', 22, 'Male', 11000, 'PY_S14')

print(SchoolMember.member)
del s2
print(SchoolMember.member)

t1.tell()
s1.tell()
t1.branch("Shanghai")