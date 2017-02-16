#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from lib import schools
from lib import courses
from lib import classes
from lib import people

school_db = settings.school_file_path
self_school_db = pickle.load(open(school_db, 'rb'))

# print('beijing' in self_school_db)
#
# # 测试学校建立后，信息是否保存
# print(self_school_db)
# print(self_school_db['北京'].school_course)
# print(self_school_db['上海'].school_course)
#
# # 测试课程建立后，信息是否保存
# print(self_school_db['北京'].school_course['Linux'].status())
# print(self_school_db['北京'].school_course['Python'].status())
# print(self_school_db['上海'].school_course['Go'].status())

# # 测试讲师建立后，信息是否保存
# print(self_school_db['上海'].school_teacher['will'].status())

# # 测试班级建立后，信息是否保存
# print(self_school_db['上海'].school_class['s14'].status())
# print(self_school_db['上海'].school_class['s14'].class_course.status())
# print(self_school_db['上海'].school_class['s14'].class_teacher['will'].status())
# print(self_school_db['上海'].school_class['s14'].class_teacher['will'].teacher_class['s14'].status())

# 测试学员建立后，信息是否保存
# print(self_school_db['上海'].school_student['wang'].status())
# print(self_school_db['上海'].school_class['s14'].class_student['wang'].status())
