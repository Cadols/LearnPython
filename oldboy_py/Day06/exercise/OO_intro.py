# 定义角色人的属性
def person(name, age, sex, job):
    data = {
        'name': name,
        'age': age,
        'sex': sex,
        'job': job
    }
    return data


# 定义角色狗的属性
def dog(name, dog_type):
    data = {
        'name': name,
        'type': dog_type
    }
    return data


# 定义角色的功能
def bark(d):
    print("dog %s:wang.wang..wang..." % d['name'])


def walk(p):
    print("person %s is walking..." % p['name'])


# 定义具体角色
d1 = dog("李闯", "京巴")
p1 = person("孙海涛", 36, "F", "运维")
p2 = person("林海峰", 27, "F", "Teacher")

walk(p1)
bark(d1)
