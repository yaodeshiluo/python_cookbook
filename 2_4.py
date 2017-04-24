#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串匹配和搜索
import re


text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))
print(text[10])

text = text1 = '11/27/2012'
datepat = re.compile('\d+/\d+/\d+')
print(datepat.findall(text))
print(datepat.match(text).group())
print(datepat.match(text).group(0))  # 和上面结果一样
print(datepat.match(text).groups())  # 返回()

datepat = re.compile('(\d+)/(\d+)/(\d+)')
print('________________')
print(datepat.findall(text))
print(datepat.match(text).group())
print(datepat.match(text).group(0))  # 和上面结果一样
print(datepat.match(text).group(1))
print(datepat.match(text).group(2))
print(datepat.match(text).group(3))

print('____________________')
for m in datepat.finditer(text):
    print(type(m))
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
