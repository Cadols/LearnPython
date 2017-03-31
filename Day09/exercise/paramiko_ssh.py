#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_host文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.19.200', port=22, username='will', password='1q2w3e')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df, ifconfig')
# 获取命令结果
result = stdout.read()
print(result.decode())

# 关闭连接
ssh.close()
