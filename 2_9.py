#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将Unicode文本标准化
import sys
print(sys.getdefaultencoding())


s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# print(s1, s2)
