### Readme

#### Blog地址：
1. [Day09 - 进程、线程、协程篇](http://www.jianshu.com/p/f55a39f94def)
2. [Day09 - 作业：类 Fabric 主机管理程序开发](http://www.jianshu.com/p/68c161701e39)

---
#### Day09 - 类 Fabric 主机管理程序开发
1. 本程序测试环境为windows
2. 请先运行程序：fabric_like/bin/start.py
3. 首次运行后请先录入远程主机信息（仅限linux系统）
4. 远程主机信息可以进行新增和删除
5. 操作远程主机前需要先激活远程主机（all命令可以直接全部进行激活）
6. 已激活的主机会进行标注，并且不可重复激活。
7. 远程主机的操作可分为命令和文件传输：
命令为常规linux命令，文件传输分为上传和下载
上传为将本地文件夹`files`（默认为空文件夹，需另行放入文件）中的文件上传至已激活远程主机
命令为`put filename`
下载为将已激活远程主机的文件下载至本地downloads文件夹下
命令为`get filename`
