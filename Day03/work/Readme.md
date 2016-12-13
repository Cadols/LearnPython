### Readme

#### Blog地址：
1. [Day03 - Python基础3](http://www.jianshu.com/p/a2ab18a0e31c)
2. [Day03 - 作业](http://www.jianshu.com/p/f47e4296e786)

---
#### Day03 - HAproxy配置文件操作
1. 运行程序后可根据菜单选项选择要进行的操作。
2. 在选择添加、修改、删除操作后，均需输入要操作的backend和server信息。该信息需要以字典形式来输入。例如：`{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}`，否则会报错。
3. 修改操作在输入要修改的信息后，会要求选择修改的server信息，请根据server信息前的数字序号选择。
4. 在文件的改动操作前（添加、修改、删除）会自动生成备份文件，可根据备份文件名中的时间来查询恢复。