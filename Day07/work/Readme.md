### Readme

#### Blog地址：
1. [Day07 - 常用模块学习](http://www.jianshu.com/p/d1f1ee9cbfd7)
2. [Day07 - 作业：简单FTP](http://www.jianshu.com/p/79d2597447cc)

---
#### Day07 - 简单FTP
1. 请依次运行bin目录下的`server.py`和`client.py`
2. 客户端首次运行请先进行账号注册。
3. 用户可以使用以下命令进行ftp操作：
`ls`：查看远程目录下文件情况；
`lls`：查看本地目录下文件情况；
`pwd`：查看远程目录地址；
`cd`：更改远程目录，支持格式`cd ~`, `cd ..`, `cd dirname`；
`lcd`：更改本地目录，支持格式`cd ..`, `cd dirname`, `cd abs_dir_path`；
`mkdir`：在远程目录创建下级文件夹，支持格式`mkdir dirname`；
`put`：上传本地文件至当前远程目录，支持格式`put filename`；
`get`：下载远程文件至当前本地目录，支持格式`get filename`
4. 请注意，用户无法使用`cd`命令离开家目录，只能在家目录下切换目录。