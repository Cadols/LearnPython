### Readme

#### Blog地址：
1. [Day08 - 网络编程基础](http://www.jianshu.com/p/dbd63e7c7684)
2. [Day08 - 作业：高级FTP](http://www.jianshu.com/p/f9a42902f4d2)

---
#### Day08 - 高级FTP
1. 请先运行服务器程序：ftp_server/bin/start.py
客户端程序位于：ftp_client/bin/start.py
2. 客户端首次运行请先进行账号注册
3. 本程序支持多用户同时登录使用
4. 每个用户默认家目录大小为100MB
5. 用户可以使用以下命令进行ftp操作：
`ls`：查看远程目录下文件情况；
`lls`：查看本地目录下文件情况；
`pwd`：查看远程目录地址；
`cd`：更改远程目录，支持格式`cd ~`, `cd ..`, `cd dirname`；
`lcd`：更改本地目录，支持格式`cd ..`, `cd dirname`, `cd abs_dir_path`；
`mkdir`：在远程目录创建下级文件夹，支持格式`mkdir dirname`；
`put`：上传本地文件至当前远程目录，支持格式`put filename`；
`get`：下载远程文件至当前本地目录，支持格式`get filename`
6. 请注意，用户无法使用`cd`命令离开家目录，只能在家目录下切换目录