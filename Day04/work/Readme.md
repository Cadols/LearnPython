### Readme

#### Blog地址：
1. [Day04 - Python基础4](http://www.jianshu.com/p/f098b3154bf0)
2. [Day04 - 作业](http://www.jianshu.com/p/3e7a6dcd846f)

---
#### Day04 - 员工信息表程序
1. 运行程序后可根据菜单选项，选择要进行的操作。
2. 模糊查询，支持以下语法：
`select name,age from staff_table where age > 22` 可以按年龄查询，支持符号“`>` `<` `=` `>=` `<=`”
`select * from staff_table where dept = "IT"` 可以按部门查询
`select * from staff_table where enroll_date like "2013"` 可以按年查询
3. 创建新员工，格式如下（注意是英文输入状态下的,）：
`姓名,年龄,手机号码,部门,登记日期` 如：Alex Li,22,13651054608,IT,2013-04-01
4. 修改员工信息，语法如下（注意空格）：
`UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"`
5. 删除员工：
进入选项后会列出所有员工信息，输入员工的id即可删除。