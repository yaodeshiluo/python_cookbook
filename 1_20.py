#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 合并多个字典或映射

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)  # 支持大部分字典操作
for each in c:
    print(each)  # 返回x, y, z
print('end')
print(c['x'])
print(c['y'])
print(c['z'])

print('____________')
print(len(c))
print(c.keys())
print(c.values())
for key in c.keys():
    print(key)
for value in c.values():
    print(value)

print('____________')
c['z'] = 10
print(a)  # a受到影响
print(b)

print('____________')
values = ChainMap()
values['x'] = 1
value = values.new_child()
print('value:', value)
print('values:', values)
value['x'] = 2
print('value:', value)

print('_____________')
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 10
print(merged['x'])  # 反应了字典的变化
print(merged['z'])  # 为3

merged = ChainMap(b, a)
print(merged['z'])  # 为4
