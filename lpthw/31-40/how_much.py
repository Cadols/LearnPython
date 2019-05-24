#!/usr/bin/env python3
# -*- coding: utf-8 -*-

work_term = input("实际服务（月）：")
serve_term = input("应服务期限（年）：")
salary = input("前12个月平均收入（元）：")

res = int(work_term) / (int(serve_term) * 12) * int(salary) * 3
true_res = (1- int(work_term) / (int(serve_term) * 12)) * int(salary) * 3
# wrong_res = int(work_term) / int(serve_term) * 12 * int(salary) * 3

print("\n烂公式违约金为：", int(res))
print("想罚的违约金为：", int(true_res))
# print("错误公式的结果：", wrong_res)