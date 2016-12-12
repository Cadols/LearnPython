#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, json, os

def write_file(backend_title, exist_res):   # 向文件写入 backend 和 server 信息
    with open('haproxy', 'r', encoding='utf-8') as f, open('haproxy_new', 'w', encoding='utf-8') as f2:
        write_flag = False
        for line in f:
            if line.strip() == 'backend %s' % backend_title:    # 如果该行的内容为匹配，说明从此往后的内容为新内容
                write_flag = True
                f2.write(line)
                for i in exist_res:
                    f2.write(' '*8 + i + '\n')
                continue
            elif line.strip().startswith('backend') and write_flag:  # 如果以backend开头且write_flag为真，说明新加信息已写完
                write_flag = False
                f2.write(line)
                continue
            elif write_flag and line.strip():   # 如果write_flag为真且该行有内容，说明是不需写入的旧信息。
                continue
            else:   # 正常写入
                f2.write(line)

def search(search_input):   # 按 backend 查询
    search_res = []
    with open('haproxy', 'r', encoding='utf-8') as f:
        check_flag = False
        for line in f:
            if line.strip() == 'backend %s' % search_input:  # 如果该行与'backend %s' % search_input相同
                check_flag = True
                continue
            elif line.strip().startswith('backend') and check_flag:  # 该行仅以'backend'开头，并且check_flag为真
                check_flag = False
                break
            elif check_flag and line.strip():  # 如果check_flag为真且该行有内容，说明是需查询到的server信息。
                search_res.append(line.strip())
    if not search_res:
        print("文件中没有 %s 的信息！" % search_input)
        return search_res
    else:
        return search_res

def add(backend_title, backend_info):
    exist_res = search(backend_title)   # 先查询输入记录是否已经存在
    if not exist_res:  # 输入的backend和server信息均不存在
        backup()
        with open('haproxy', 'r', encoding='utf-8') as f, open('haproxy_new', 'w', encoding='utf-8') as f2:
            for line in f:
                f2.write(line)
            f2.write('\n\nbackend %s\n' % backend_title)  # 开始添加新的backend和server信息
            f2.write(' '*8 + backend_info)  # 字符也可以用乘法，刷新认知了。
            print("新的 backend 和 server 信息已添加进入文件！")
        os.rename('haproxy_new', 'haproxy')  # 重命名文件
    else:   # 输入的backend信息已存在
        if backend_info in exist_res:   # 输入的server记录也已存在，即重复了
            print("您要添加的 backend 和 server 信息已经存在！")
        else:   # 输入的server记录为新记录
            backup()
            exist_res.append(backend_info)
            write_file(backend_title, exist_res)    # 调用write_file函数
            print("新的 server 信息已添加进入文件！")
            os.rename('haproxy_new', 'haproxy')  # 重命名文件

def delete(backend_title, backend_info):
    exist_res = search(backend_title)   # 先查询输入记录是否已经存在
    if not exist_res:  # 输入的backend和server信息均不存在
        return
    else:   # 输入的backend信息已存在
        if backend_info not in exist_res:   # 输入的server记录不存在
            print("%s 中没有您要删除的 server 信息！" % backend_title)
        else:   # 输入的server记录存在
            backup()
            exist_res.remove(backend_info)
            with open('haproxy', 'r', encoding='utf-8') as f, open('haproxy_new', 'w', encoding='utf-8') as f2:
                write_flag = False
                for line in f:
                    if line.strip() == 'backend %s' % backend_title:  # 如果该行与'backend %s' % backend_title相同
                        write_flag = True
                        if not exist_res:  # 如果exist_res列表为False，则跳过不写入
                            continue
                        else:  # 如果exist_res列表不为空，则写入已有内容
                            f2.write(line)
                            for i in exist_res:
                                f2.write(' '*8 + i + '\n')
                        continue
                    elif line.strip().startswith('backend') and write_flag:  # 该行仅以'backend'开头，并且write_flag为真
                        write_flag = False
                        f2.write(line)
                        continue
                    elif write_flag and line.strip():  # write_flag为真且不为空行
                        continue
                    else:
                        f2.write(line)
            print("backend 和 server 信息已删除！")
            os.rename('haproxy_new', 'haproxy')  # 重命名文件

def replace(backend_title, backend_info):
    exist_res = search(backend_title)
    if not exist_res:  # 根据server信息列表真假值，来判断要修改的backend是否存在于文件中。
        return
    elif backend_info in exist_res:  # 要修改的backend和server信息，文件中均已存在。
        print("文件中已经含有该条 backend 和 server 信息！")
        return
    else:
        backup()
        for server_info in enumerate(exist_res):
            print(server_info[0], server_info[1])
    server_num = input("请选择在 %s 中您要修改的记录：" % backend_title)
    while True:  # 判断选择是否正确，不然总是报错
        if server_num.isdigit():
            server_num = int(server_num)
            if server_num > len(exist_res):
                print("请输入正确的数字！")
            else:
                exist_res[server_num] = backend_info
            break
        else:
            print("请输入正确的格式！")
    write_file(backend_title, exist_res)
    print("已将 %s 中的信息修改为 %s" % (backend_title, exist_res[server_num]))
    os.rename('haproxy_new', 'haproxy')

def backup():  # 文件操作前先备份已有文件
    backup_time = time.strftime('%Y%m%d_%H%M%S')
    with open('haproxy', 'r', encoding='utf-8') as f,\
            open('haproxy_%s.bak' % backup_time, 'w', encoding='utf-8') as f2:
        for line in f:
            f2.write(line)
    return "原配置已备份为 haproxy_%s.bak" % backup_time

while True:
    print("1. 查询 backend 信息\n2. 添加 backend 和 server 信息\n3. 修改 backend 和 server 信息\n"
          "4. 删除 backend 和 server 信息\nq. 退出")
    choice_input = input("\n请输入您想进行的操作:").strip()
    if choice_input.isdigit():
        choice_input = int(choice_input)
        if choice_input == 1:
            user_input = input("请输入您想查询的 backend 信息:").strip()
            for info in search(user_input):
                print(info)
        elif choice_input in [2, 3, 4]:
            print('\n请以字典形式输入 backend 和 server 信息。\n例如：{"backend": "test.oldboy.org","record":'
                  '{"server": "100.1.7.9","weight": 20,"maxconn": 30}}\n')
            user_input = input("请输入您想进行操作的 backend 和 server 信息：").strip()
            backend_dict = json.loads(user_input)
            backend_title = backend_dict['backend']
            backend_info = 'server %s %s weight %d maxconn %d' % (backend_dict['record']['server'],
                                                                  backend_dict['record']['server'],
                                                                  backend_dict['record']['weight'],
                                                                  backend_dict['record']['maxconn'])
            if choice_input == 2:
                add(backend_title, backend_info)
            elif choice_input == 3:
                replace(backend_title, backend_info)
            elif choice_input == 4:
                delete(backend_title, backend_info)
        else:
            print("请输入正确的数字！")
    elif choice_input == 'q':
        exit("Bye！")
    else:
        print("请输入正确的格式！")