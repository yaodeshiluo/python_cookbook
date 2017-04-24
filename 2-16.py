#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 以指定列宽格式化字符串
import os


import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print('_____________________')
print(textwrap.fill(s, initial_indent='    '))
print('______________________')
print(textwrap.fill(s, subsequent_indent='   '))

print('____________________')
print(os.get_terminal_size().columns)  # 需在terminal中运行
