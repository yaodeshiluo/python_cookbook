#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串令牌解析
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
for _ in iter(scanner.match, None):  # iter()接受一个函数，并不断调用直到出现None(也可以设置成其它值)
    print _.lastgroup, _.group()

print('___________________')
_pat = re.compile(r'(?P<NAME>[A-Za-z]+)')
_match = _pat.match('foo')
print _match.lastgroup, _match.group()
