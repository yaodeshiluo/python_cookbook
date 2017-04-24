#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串开头或结尾匹配
import os
import re

url = 'http://www.python.org'
print(url.startswith('http'))
print(url.endswith('org'))
print()

files = os.listdir('.')
print(len(files))
print(file for file in files if file.startswith(('1', '2')))  # 放入元组,不能放入列表
print([file for file in files if file.startswith(tuple(['1', '2']))])  # 放入元组,不能放入列表
print(any(file.endswith(('.py', '.pyc')) for file in files))


url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url).group())
