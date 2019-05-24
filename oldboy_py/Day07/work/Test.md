### Test
#### Day07 - 简单FTP

#### 2017/2/23
1. 完成登录功能
2. 查询ftp常用命令格式
[Basic FTP Commands](https://www.cs.colostate.edu/helpdocs/ftp.html)
[ftp指令说明](http://www2.nsysu.edu.tw/csmlab/unix/ftp.htm)

#### 2017/2/24
1. 熟悉ftp常用命令格式和命令使用
2. 使用`os.mknod`方法创建空白文件时报错：`AttributeError: 'module' object has no attribute 'mknod'`
使用open()代替

#### 2017/2/27
1. 初步构建ftp_client功能
处理文件夹时如果输入文件名，则报错：`NotADirectoryError: [WinError 267] The directory name is invalid:`，使用异常处理来解决。
2. 实现ftp_client文件夹操作部分的命令（`ls`, `lls`, `pwd`, `cd`, `lcd`）

#### 2017/2/28
1. 修改代码，把实现的功能改为通过反射调用 ftp_client 的方法（`ls`, `lls`, `pwd`, `cd`, `lcd`）。
2. 改用re来处理`cd`和`lcd`命令的字符，熟悉re规则。

#### 2017/3/1
1. 翻阅了别人的博客[python之FTP程序(支持多用户在线)](http://www.cnblogs.com/0zcl/p/6259128.html)，明晰了一些ftp使用思路如：
服务器端，用户可以在自己的家目录内任意切换，但不能进入其他用户家目录
put file_name = 将客户端当前文件上传至服务器当前目录下
get file_name = 将服务器当前文件下载至客户端当前目录下

#### 2017/3/2
1. 初步构建ftp_server功能
2. 传递`ls`命令后，如目录下为空，连接会卡住。增加判断，如果`os.listdir()`后的列表为空，则提示信息

#### 2017/3/3
1. c/s传递信息时忘记使用encode和decode，频繁报错

#### 2017/3/4
1. 使用写 get 功能时，每次运行到`f = open(server_response[file_path] + ".new", 'wb')`，客户端就会自动断开连接，经过检查，是使用了错误的file地址，低级错误。
2 . 完成`get`功能，可以将服务器文件下载至当前本地文件夹

#### 2017/3/5
1. 复用代码完成`put`功能，可以将本地文件上传至用户家目录下的任意文件夹
2. 增加`mkdir`命令，用户可在家目录下建立文件夹。
修改代码，用户无法用`cd ..`命令离开自己的家目录
增加判断条件，如果要更改的服务器文件夹地址不是以家目录开始，则不会执行。

#### 2017/3/6
1. Test 和 Readme