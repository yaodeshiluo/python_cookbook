#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串搜索和替换
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# print(re.sub(r'\d+/\d+/\d+', r'\3-\1-\2', text))  # 报错
print(re.sub(r'\d+/\d+/\d+', r'\\3-\\1-\\2', text))  # Today is \3-\1-\2. PyCon starts \3-\1-\2.


print('___________________')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


def change_date(m):
    from calendar import month_abbr
    month_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), month_name, m.group(3))


print(datepat.sub(change_date, text))

print(re.sub(r'(\d+)/(\d+)/(\d+)', change_date, text))  # 等同上面
