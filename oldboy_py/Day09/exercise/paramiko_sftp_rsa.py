#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

private_key = paramiko.RSAKey.form_priavte_key_file('/home/auto/.ssh/id_rsa')
transport = paramiko.Trasport(('127.0.0.1', 2222))
transport.connect(username='it', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将local file 上传至服务器 destination

# 将destination 下载至本地 local_path

transport.close()
