#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用Shell通配符匹配字符串
# 使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串
# 适用于简单的通配符

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '*TXT'))  # fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式， OS X 返回False ; Windows 返回True
print(fnmatchcase('foo.txt', '*TXT'))  # fnmatchcase() 函数对大小写敏感

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatch(addr, '* ST')])
print([addr for addr in addresses if fnmatch(addr, '54[0-9][0-9] *')])
