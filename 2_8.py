#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 多行匹配模式

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))

new_comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(new_comment.findall(text2))  # 加入了对换行的支持
new_comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)  # 使 . 可以匹配包括换行在内的任意字符
print(new_comment.findall(text2))
