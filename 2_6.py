#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串忽略大小写的搜索替换
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))  # 等同于print(re.findall('python', text, flags=re.I))

print(re.sub('python', 'snake', text, flags=re.I))  # 结果不同于print(re.sub('python', 'snake', text, re.I))


def matchcase(word):
    def replace(m):  # 接受的参数必须是_sre.SRE_Match对象
        print(type(m))
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.I))
