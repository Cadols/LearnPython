#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
from conf import settings
from lib import schools
from lib import courses
from lib import classes
from lib import people

school_db = settings.school_file_path
account_db = settings.account_file_path

class Manage(object):
    def __index__(self):
        pass

    def run(self):
        # view_dic = {
        #     '0': ManageView,
        #     '1': TeacherView,
        #     '2': StudentView
        # }
        # accounts_info = pickle.load(open(account_db, 'rb'))
        # print(accounts_info)
        # print("欢迎来到 \033[1;30m“没几个人在”\033[0m 选课系统")
        # username = input("请输入你的用户名：").strip()
        # password = input("请输入你的密码：").strip()
        # if username == accounts_info[username]['username'] and password == accounts_info[username]['password']:
        #     print("yes")
        #     view_dic[accounts_info[username]['type']]()

        menu = """欢迎来到 \033[1;30m“没几个人在”\033[0m 选课系统
1. 学生视图
2. 讲师视图
3. 管理视图
q. 退出系统
"""
        menu_dic = {
            '1': StudentView,
            '2': TeacherView,
            '3': ManageView,
            'q': self.exit_system
        }
        while True:
            print(menu)
            chosen_option = input("\033[34m请输入您想进入的视图编号：\033[0m")
            if chosen_option in ['1', '2', '3', 'q']:
                menu_dic[chosen_option]()
            else:
                print("\033[1;31m请输入正确的选项！\033[0m\n")

    def exit_system(self):
        exit("您已退出选课系统，感谢使用！")


class ManageView(object):
    """管理视图"""
    def __init__(self):
        if os.path.exists(school_db):
            self.school_db = pickle.load(open(school_db, 'rb'))
            # print(self.school_db)
            self.view_menu()
        else:
            self.school_db = {}
            self.default_school()
            self.view_menu()

    def view_menu(self):
        """管理视图功能"""
        while True:
            print("\n" + " 系统中已有的校区 ".center(20, '-'))
            for key in self.school_db:
                print("学校名称：", key)
            choice_school = input("\033[34m请输入您要管理的校区名称：\033[0m").strip()
            if choice_school in self.school_db:
                self.choice_school = choice_school
                self.school_obj = self.school_db[choice_school]
                while True:
                    print("""\n欢迎来到 %s校区 管理视图
添加/更新课程 create_course
招聘讲师 create_teacher
增加班级 create_class
查看校区信息 show_info
退出程序 exit
                    """ % choice_school)
                    menu_func = input("\033[34m请输入您要操作的功能命令：\033[0m").strip()
                    if hasattr(self, menu_func):
                        getattr(self, menu_func)()
                    else:
                        print("\033[1;31m命令错误，请重新输入！\033[0m")
            else:
                print("\033[1;31m没有学校 %s ，请检查后再试一次。\033[0m" % choice_school)

    def default_school(self):
        """创建 北京 和 上海 的学校实例，并创建 Linux, Python, Go 课程到不同的学校"""
        beijing = schools.School('北京', '中国北京市')
        shanghai = schools.School('上海', '中国上海市')
        beijing.create_course('Linux', 10000, 8)
        beijing.create_course('Python', 10000, 8)
        shanghai.create_course('Go', 10000, 8)
        self.school_db['北京'] = beijing
        self.school_db['上海'] = shanghai
        # print(self.school_db)
        pickle.dump(self.school_db, open(school_db, 'wb'))

    def create_school(self):
        """创建新的学校实例"""
        new_school_name = input("\033[34m请输入新学校的名称：\033[0m").strip()
        new_school_location = input("\033[34m请输入新学校的地址：\033[0m").strip()
        new_school = schools.School(new_school_name, new_school_location)
        print("\033[33m学校 %s 已成功创建。\033[0m" % new_school_name)
        self.school_db[new_school_name] = new_school
        pickle.dump(self.school_db, open(school_db, 'wb'))

    def create_course(self):
        """创建新的课程"""
        new_course_name = input("\033[34m请输入要增加的课程名称：\033[0m").strip()
        new_course_tuition = input("\033[34m请输入要增加的课程学费：\033[0m").strip()
        new_course_period = input("\033[34m请输入要增加的课程学时：\033[0m").strip()
        if new_course_name in self.school_obj.school_course:
            update = input("\033[31m该课程已经存在，是否要更新课程信息？ y/n ：\033[0m")
            if update == 'y':
                self.school_obj.create_course(new_course_name, new_course_tuition, new_course_period)
                print("\033[33m课程 %s 已成功更新！\033[0m" % new_course_name)
            elif update == 'n':
                pass
        else:
            self.school_obj.create_course(new_course_name, new_course_tuition, new_course_period)
            print("\033[33m课程 %s 已成功增加。\033[0m" % new_course_name)
        self.school_db[self.choice_school] = self.school_obj
        pickle.dump(self.school_db, open(school_db, 'wb'))

    def create_class(self):
        """创建新的班级"""
        new_class_name = input("\033[34m请输入新的班级名称：\033[0m").strip()
        if new_class_name not in self.school_obj.school_class:
            for key in self.school_obj.school_course:
                print("课程： %s" % key)
            selected_course = input("\033[34m请输入班级 %s 要关联的课程名称：\033[0m" % new_class_name).strip()
            if selected_course in self.school_obj.school_course:
                for key in self.school_obj.school_teacher:
                    print("讲师： %s" % key)
                selected_teacher = input("\033[34m请输入班级 %s 的培训讲师姓名：\033[0m" % new_class_name).strip()
                self.school_obj.create_class(new_class_name, self.school_obj.school_course[selected_course])
                # 关联讲师
                self.school_obj.school_class[new_class_name].class_teacher[selected_teacher] =\
                    self.school_obj.school_teacher[selected_teacher]
                self.school_obj.school_teacher[selected_teacher].teacher_class[new_class_name] = \
                    self.school_obj.school_class[new_class_name]
                self.school_db[self.choice_school] = self.school_obj
                pickle.dump(self.school_db, open(school_db, 'wb'))
                print("\033[33m班级 %s 创建成功，教授课程为 %s，讲师为 %s。\033[0m" %
                      (new_class_name, selected_course, selected_teacher))
            else:
                print("\033[1;31m课程 %s 不存在。\033[0m" % selected_course)
        else:
            print("\033[1;31m班级 %s 已经存在。\033[0m" % new_class_name)
            self.create_class()

    def create_teacher(self):
        """创建讲师信息"""
        new_teacher_name = input("\033[34m请输入讲师的姓名：\033[0m").strip()
        new_teacher_age = input("\033[34m请输入讲师的年龄：\033[0m").strip()
        new_teacher_gender = input("\033[34m请输入讲师的性别：\033[0m").strip()
        new_teacher_salary = input("\033[34m请输入讲师的薪水：\033[0m").strip()
        if new_teacher_name in self.school_obj.school_teacher:
            update = input("\033[31m该讲师信息已经存在，是否需要更新？ y/n ：\033[0m")
            if update == 'y':
                new_teacher = people.Teacher(new_teacher_name, new_teacher_age,
                                             new_teacher_gender, new_teacher_salary)
                self.school_obj.school_teacher[new_teacher_name] = new_teacher
                print("\033[33m讲师 %s 信息已成功更新，目前属于 %s 校区！\033[0m" %
                      (new_teacher_name, self.school_obj.school_name))
            elif update == 'n':
                pass
        else:
            new_teacher = people.Teacher(new_teacher_name, new_teacher_age,
                                         new_teacher_gender, new_teacher_salary)
            self.school_obj.school_teacher[new_teacher_name] = new_teacher
            print("\033[33m讲师 %s 的资料已建立，属于 %s 校区。\033[0m" %
                  (new_teacher_name, self.school_obj.school_name))
        self.school_db[self.choice_school] = self.school_obj
        pickle.dump(self.school_db, open(school_db, 'wb'))

    def show_info(self):
        self.school_obj.show_course_info()
        self.school_obj.show_class_info()
        self.school_obj.show_teacher_info()

    def exit(self):
        exit("感谢您的使用，下次再见。")


class TeacherView(object):
    """讲师视图"""
    def __init__(self):
        if os.path.exists(school_db):
            self.school_db = pickle.load(open(school_db, 'rb'))
            self.select_school()
        else:
            print("\033[1;31m现在还没有学校呢，招讲师来搓麻将吗？\033[0m")

    def select_school(self):
        """选择登录讲师"""
        print("欢迎，您现在位于讲师视图")
        print("\n" + " 系统中已有的校区 ".center(20, '-'))
        for key in self.school_db:
            print("学校名称：", key)
        selected_school = input("\033[34m请输入您要注册的校区名称：\033[0m").strip()
        if selected_school in self.school_db:
            self.selected_school = selected_school
            self.school_obj = self.school_db[self.selected_school]
            self.select_teacher()
        else:
            print("\033[1;31m学校 %s 不存在，请检查后重新输入。\033[0m" % selected_school)
            self.select_school()

    def select_teacher(self):
        """选择登录讲师"""
        for key in self.school_obj.school_teacher:
            print("讲师姓名：", key)
        selected_teacher = input("\033[34m请输入要登录的讲师姓名：\033[0m").strip()
        if selected_teacher in self.school_obj.school_teacher:
            self.select_teacher = self.school_obj.school_teacher[selected_teacher]
            self.view_menu()
        else:
            print("\033[1;31m讲师 %s 不存在，请检查后重新输入。\033[0m" % selected_teacher)
            self.select_teacher()

    def select_class(self):
        """选择班级"""
        for key in self.school_obj.school_class:
            print("班级名称：", key)
        selected_class = input("\033[34m请输入要选择的班级名称：\033[0m").strip()
        if selected_class in self.school_obj.school_class:
            self.selected_class = self.school_obj.school_class[selected_class]
        else:
            print("\033[1;31m班级 %s 不存在，请检查后重新输入。\033[0m" % selected_class)
            self.select_class()

    def select_student(self):
        """选择学员"""
        for key in self.selected_class.class_student:
            print("学员姓名：", key)
        selected_student = input("\033[34m请输入要选择的学员姓名：\033[0m").strip()
        if selected_student in self.selected_class.class_student:
            self.selected_student = self.selected_class.class_student[selected_student]
        else:
            print("\033[1;31m学员 %s 不存在，请检查后重新输入。\033[0m" % selected_student)
            self.select_student()

    def view_menu(self):
        """视图菜单"""
        while True:
            print("""欢迎来到 %s校区 讲师管理中心，%s
管理班级 manage_class
开始授课 take_class
查看学员 show_student
修改成绩 change_score
退出程序 exit
            """ % (self.school_obj.school_name, self.select_teacher.name))
            input_code = input("\033[34m请输入您要操作的功能命令：\033[0m").strip()
            if hasattr(self, input_code):
                getattr(self, input_code)()
            else:
                print("\033[1;31m命令错误，请重新输入！\033[0m")
                # self.view_menu()

    def manage_class(self):
        print("\033[1;31m没明白管理班级的需求具体是要做什么操作，所以没有写具体功能。\n\033[0m")

    def take_class(self):
        self.select_class()
        exit("讲师 %s 已经去给 %s 班级教 %s 课程去了，本系统自动关闭，谢谢使用。" % (
            self.select_teacher.name, self.selected_class.class_name,
            self.selected_class.class_course.course_name))

    def show_student(self):
        self.select_class()
        print("\033[33m班级 %s 的学员有：\033[0m" % self.selected_class.class_name)
        for key in self.selected_class.class_student:
            print("\033[33m%s\033[0m" % key)

    def change_score(self):
        self.select_class()
        self.select_student()
        new_score = input("\033[34m请输入 %s 班级学员 %s 的 %s 课程成绩：\033[0m" % (
            self.selected_class.class_name, self.selected_student.name,
            self.selected_class.class_course.course_name))
        self.selected_student.score[self.selected_class.class_course.course_name] = new_score
        # 保存信息进文件
        self.selected_class.class_student[self.selected_student.name] = self.selected_student
        self.school_obj.school_student[self.selected_student.name] = self.selected_student
        self.school_db[self.selected_school] = self.school_obj
        pickle.dump(self.school_db, open(school_db, 'wb'))
        print("\033[33m%s 班级学员 %s 现在的 %s 课程成绩为 %s\033[0m" % (
            self.selected_class.class_name, self.selected_student.name,
            self.selected_class.class_course.course_name, new_score))

    def exit(self):
        exit("感谢您的使用，下次再见。")



class StudentView(object):
    """学生视图"""
    def __init__(self):
        if os.path.exists(school_db):
            self.school_db = pickle.load(open(school_db, 'rb'))
            self.view_menu()
        else:
            print("\033[1;31m到现在连学校都没有，招什么学生啊？\033[0m")

    def view_menu(self):
        print("欢迎，您现在位于学生视图")
        print("\n" + " 系统中已有的校区 ".center(20, '-'))
        for key in self.school_db:
            print("学校名称：", key)
        selected_school = input("\033[34m请输入您要注册的校区名称：\033[0m").strip()
        if selected_school in self.school_db:
            self.selected_school = selected_school
            self.school_obj = self.school_db[self.selected_school]
            self.create_student()
        else:
            print("\033[1;31m学校 %s 不存在，请检查后重新输入。\033[0m" % selected_school)
            self.view_menu()

    def create_student(self):
        print("现在开始学生注册")
        student_name = input("\033[34m请输入学生的名字：\033[0m").strip()
        if student_name in self.school_obj.school_student:
            choice_class = input("\033[33m学生 %s 已存在，是否继续选班级？ y/n：\033[0m" % student_name)
            if choice_class == 'y':
                self.new_student = self.school_obj.school_student[student_name]
            else:
                exit("\033[31m感谢您的使用，再见。\33[0m")
        else:
            student_age = input("\033[34m请输入学生的年龄：\033[0m").strip()
            student_gender = input("\033[34m请输入学生的性别：\033[0m").strip()
            student_money = input("\033[34m请输入学生的金额储值：\033[0m").strip()
            self.new_student = people.Student(student_name, student_age, student_gender, student_money)
            print("\033[33m学生 %s 的信息已记录。\033[0m" % student_name)
        # 保存student信息，并写入文件
        self.school_obj.school_student[student_name] = self.new_student
        self.school_db[self.selected_school] = self.school_obj
        pickle.dump(self.school_db, open(school_db, 'wb'))
        self.select_class()

    def select_class(self):
        self.school_obj.show_class_info()
        self.selected_class = input("\033[34m请输入学生 %s 要上课的班级：\033[0m" % self.new_student.name).strip()
        if self.selected_class not in self.school_obj.school_class:
            print("\033[1;31m班级 %s 不存在。\033[0m" % self.selected_class)
            self.select_class()
        elif self.new_student.name in self.school_obj.school_class[self.selected_class].class_student:
            print("\033[33m学员 %s 已经在 %s 班级里了。\033[0m" % (self.new_student.name, self.selected_class))
        elif self.selected_class in self.school_obj.school_class:
            self.pay_tuition()
        # else:
        #     print("\033[1;31m班级 %s 不存在。\033[0m" % self.selected_class)
        #     self.select_class()

    def pay_tuition(self):
        tuition = self.school_obj.school_class[self.selected_class].class_course.course_tuition
        choice_pay = input("\033[34m即将从学生 %s 的储值金额中扣除 %s 元学费，是否继续？ y/n：\033[0m" %
                           (self.new_student.name, tuition))
        if choice_pay == 'y':
            self.new_student.money = int(self.new_student.money)
            tuition = int(tuition)
            if self.new_student.money >= tuition:
                self.new_student.money -= tuition
                # 保存student信息，并写入文件
                self.school_obj.school_class[self.selected_class].class_student[self.new_student.name] =\
                    self.new_student
                self.school_obj.school_student[self.new_student.name] = self.new_student
                self.school_db[self.selected_school] = self.school_obj
                pickle.dump(self.school_db, open(school_db, 'wb'))
                print("\033[33m学生 %s 已成功缴费 %s 元，当前储值金额为： %s 元\033[0m" % (
                    self.new_student.name, tuition, self.new_student.money))
            else:
                choice_gain_money = input("\033[34m学生 %s 的储值金额中不足，是否充值？ y/n：\033[0m" %
                                          self.new_student.name)
                if choice_gain_money == 'y':
                    self.new_student.gain_money()
                    # 保存student信息，并写入文件
                    self.school_obj.school_student[self.new_student.name] = self.new_student
                    self.school_db[self.selected_school] = self.school_obj
                    pickle.dump(self.school_db, open(school_db, 'wb'))
                    print("\033[33m学员 %s 储值成功，当前储值金额为：%s 元" % (
                        self.new_student.name, self.new_student.money))
                    self.pay_tuition()
                else:
                    exit("\033[31m感谢您的使用，再见。\33[0m")
        else:
            exit("\033[31m感谢您的使用，再见。\33[0m")
