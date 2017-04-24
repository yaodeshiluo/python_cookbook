#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 删除字符串中不需要的字符
s = ' hello world \n'
print(s.rstrip() + '|')
print(s.lstrip())
t = '-----hello====='
print(t.lstrip('-'))
print(t.lstrip('-h'))
print(t.strip('-='))

# with open('README.md') as f:
#     lines = (line.strip() for line in f)
# for line in lines:  # 这样会报错 ValueError: I/O operation on closed file.
#     print(line)

with open('README.md') as f:
    lines = (line.strip() for line in f)  # 不需要预先读取所有数据放到一个临时的列表中去
    for line in lines:
        print(line)
