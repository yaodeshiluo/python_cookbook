#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在字符串中处理html和xml
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape


s = 'Elements are written as "<tag>text</tag>".'
print(html.escape(s))

s = 'Spicy Jalapeño'
# print(s) # UnicodeEncodeError: 'gbk' codec can't encode character '\xf1' in position 12: illegal multibyte sequence
print(s.encode('ascii', errors='xmlcharrefreplace'))

print('___________________')
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
# print(p.unescape(s))  # UnicodeEncodeError: 'gbk' codec can't encode character '\xf1' in position 13: illegal multibyte sequence

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
