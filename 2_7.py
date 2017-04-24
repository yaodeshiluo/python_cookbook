#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最短匹配模式
import re

text2 = 'Computer says "no." Phone says "yes."'
str_pat1 = re.compile('\"(.*)\"')
str_pat2 = re.compile('\"(.*?)\"')
print(str_pat1.findall(text2))
print(str_pat2.findall(text2))
