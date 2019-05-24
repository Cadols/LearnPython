#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
print(sys.getdefaultencoding())     # 获取默认编码格式

"""
# Python2
s = '学习学习再学习'
s_gb = s.decode('uft-8').encode('gb2312')   # utf-8 -> gb2312
print(s_gb.decode('gb2312'))
s_gb_utf8 = s_gb.decode('gb2312').encode('utf-8')   # gb2312 -> utf-8
s_gb_utf8_gbk = s_gb_utf8.decode('utf-8').encode(gbk)   # utf-8 -> gbk
"""

# Python3
s = '学习学习再学习'       # py3_default = unicode
s_gb = s.encode('gb2312')   # unicode -> gb2312
s_gb_utf8 = s_gb.decode('gb2312').encode('utf-8')   # gb2312 -> utf-8
s_gb_utf8_gbk = s_gb_utf8.decode('utf-8').encode('gbk')     # utf-8 -> gbk
print(s_gb.decode('gb2312'))
print(s_gb_utf8.decode('utf-8'))
print(s_gb_utf8_gbk.decode('gbk'))