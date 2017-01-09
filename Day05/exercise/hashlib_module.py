#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

# 多次update写入内存，多次md5
m = hashlib.md5()
m.update(b'Will')
print(m.hexdigest())
m.update(b'Wang')
print(m.hexdigest())

# 写入内存后，一次性MD5
m2 = hashlib.md5()
m2.update(b'WillWang')
print(m2.hexdigest())

# ######## md5 ########
hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha1 ########
hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha256 ########
hash = hashlib.sha256()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha384 ########
hash = hashlib.sha384()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha512 ########
hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())

# hmac 加盐
import hmac
h_obj = hmac.new(b'salt', b'hello')  # 网络消息加密传输
print(h_obj.hexdigest())