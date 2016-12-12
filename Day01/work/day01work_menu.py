#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
menu = {
    '京津冀': {
        '北京市': ['东城区', '西城区', '朝阳区', '丰台区', '海淀区'],
        '天津市': ['和平区', '河西区', '南开区', '河东区', '河北区'],
        '河北省': ['石家庄市', '保定市', '沧州市', '承德市', '邯郸市']
    },
    '长三角': {
        '上海市': ['黄浦区', '徐汇区', '长宁区', '静安区', '浦东新区'],
        '浙江省': ['杭州市', '宁波市', '绍兴市', '湖州市', '嘉兴市'],
        '江苏省': ['南京市', '无锡市', '常州市', '苏州市', '南通市']
    },
    '珠三角': {
        '广州市': ['荔湾区', '越秀区', '海珠区', '天河区', '白云区'],
        '深圳市': ['罗湖区', '福田区', '南山区', '宝安区', '龙岗区'],
        '佛山市': ['禅城区', '南海区', '顺德区', '三水区', '高明区']
    }
}

print("""
********************************************
**                                        **
**                                        **
**          欢迎来到区域选择界面          **
**                                        **
**                                        **
**                                        **
********************************************
""")

while True:
    for i1,v1 in enumerate(menu):          # 将字典menu组成索引序列
        # print(i1, v1)
        print('按 "%d" 进入 “%s” 区域' % (i1, v1))
    menu1 = input('\n请输入您想查询区域的编号：')
    if menu1 == 'q':
        break
    elif menu1.isdigit():  # 如果输入的是数字则
        menu1 = int(menu1)         # 将字符串强制转成整数
        if menu1 <= len(menu):     # 如果输入的数字不大于menu_1序列
            key1 = list(menu)[menu1]   # 将所选择数字对应的键赋值给key_1
        else:
            print('\n请输入正确的数字。\n')
            continue
        while True:
            for i2, v2 in enumerate(menu[key1]):  # 将字典menu中key_1 赋值的所有的键组成索引序列
                print('按 “%d” 进入 “%s”' % (i2, v2))
            menu2 = input('\n请输入您想查询的省、市编号，“b”键返回，“q”键退出：')
            if menu2 == 'b':
                break
            elif menu2 == 'q':
                sys.exit()          # 退出程序
            elif menu2.isdigit():  # 如果参数为数字且为规定的选项则执行以下
                menu2 = int(menu2)
                if menu2 <= len(menu[key1]):
                    key2 = list(menu[key1])[menu2]   # 将所选择数字对应的键赋值给key_2
                else:
                    print('\n请输入正确的数字。\n')
                    continue
                while True:
                    for i3, v3 in enumerate(menu[key1][key2]):  # 将字典menu中key_2 赋值的所有的键组成索引序列
                        print(v3)
                    menu3 = input('\n“q”键退出，其他键返回：')
                    if menu3 == 'q':
                        sys.exit()
                    else:
                        break
            else:
                print('\n您所输入的内容不正确，请重新输入。\n')
    else:
        print('\n您所输入的内容不正确，请重新输入。\n')