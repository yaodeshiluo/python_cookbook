#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 合并拼接字符串

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(','.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))
print('Hello''World')
print('Hello' 'World')

data = ['ACME', 50, 91.1]
print(','.join(str(s) for s in data))  # 巧用生成器

print('__________________')
a = '1, 2, 3'
b = 'Hello World'
c = 'Test'
print(a, b, c)
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better
