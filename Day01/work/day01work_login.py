#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os, getpass  # 调用os、getpass模块
if not os.path.exists('blacklist.txt'):     # 判断本地是否有文件，没有创建一个新的。
    with open('blacklist.txt', "a+") as f:  # 以追加模式打开一次文件，保证如果没有文件存在，自动生成文件并继续运行
        f.read()
true_username = 'will'
true_password = '1234'
attempt_times = 0

print("""
********************************************
**                                        **
**                                        **
**          欢迎来到账户登录界面          **
**                                        **
**                                        **
**                                        **
********************************************
""")

while attempt_times < 3:
    with open('blacklist.txt', 'r') as f:
        blacklist = f.read().split()         # 读取文件内容后，拆分字符串，形成黑名单列表。
    #print(blacklist)
    username = input('请输入您的用户名：')
    if username in blacklist:            # 判断输入用户名是否在列表中
        print('您的账户： %s 已经被锁定。请联系管理员解锁，或者更换登录账户。' % username)
        continue
    else:
        password = getpass.getpass('请输入您的密码：')    # 隐藏输入的密码，但 Pycharm 中无法测试。
    if true_username == username and true_password == password:     # 验证用户名和密码
        #print("欢迎回来， %s " % username)
        print("""
********************************************
**                                        **
**                                        **
**           欢迎您回来， %s            **
**                                        **
**                                        **
**                                        **
********************************************
        """ % username)
        break
    else:
        print('用户名或密码错误，请重试')
        attempt_times += 1
    if attempt_times == 3:
        with open('blacklist.txt', 'a+') as f:
            f.write('%s\n' % username)
        print('已尝试3次登录，您的账户 %s 已锁定。' % username)
        break