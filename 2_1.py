#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用多个界定符分割字符串

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))
print(re.split(r'(;|,|\s)\s*', line)[::2])
print(re.split(r'(;|,|\s)\s*', line)[1::2])
print(re.split(r'(?:;|,|\s)\s*', line))  # (?:...)说明是非捕获分组
