#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Role(object):
    nationality = 'Japan'  # 公有属性

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name  # 成员属性
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = 'normal'

    def shot(self):
        print("%s is shooting..." % self.name)

    def got_shot(self):
        print("ah..., %s got shot..." % self.name)
        self.__heart = 'broken'  # 私有属性
        print(self.__heart)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))
        self.weapon = gun_name

    def get_heart(self):
        return self.__heart  # 外部访问私有属性，但不能修改

    def __del__(self):  # 析构方法
        print("del......run......")

r1 = Role('Alex', 'police', 'AK47')  # 生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色

r1.shot()
r2.buy_gun('AK-47')
print(r2.weapon)
print(r2.get_heart())
r2.got_shot()

print(r1._Role__heart)  # 强行调用私有属性

print(r1.nationality)
print(r2.nationality)

Role.nationality = "USA"  # 更改类的公有属性
print(r1.nationality, r2.nationality)

r1.nationality = 'CN'
print(r1.nationality)
print(r2.nationality)

def shot2(self):  # 将公有方法改掉
    print("use %s own shot method" % self.name)

r1.shot = shot2
r1.shot(r1)
r2.shot()
