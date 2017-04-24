#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串对齐

text = 'Hello World'
print(text.ljust(20))
print(len(text.ljust(20)))
print(text.rjust(20))
print(len(text.rjust(20)))

print(text.ljust(20, '='))
print(text.rjust(20, '*'))  # The fill character must be exactly one character long

print('__________________')
print(format(text, '>20'))  # '>20s'结果一样
print(format(text, '<20'))  # '<20s'结果一样
print(format(text, '^20'))  # '^20s'结果一样
print(format(text, '=>20s'))  # '=>20'结果一样
print(format(text, '=<20s'))  # '=<20'结果一样

print('{:=>10s} {:*<10s}'.format('Hello', 'World'))
print('___________________')
x = 1.23
print(format(x, '=>10'))
print(format(x, '=>10f'))
print(format(x, '=>10.1f'))
print(format(x, '=>10.2f'))
print(format(x, '=>10.3f'))
print(format(x, '=>10.4f'))
print(format(x, '=>10.5f'))
print(format(x, '=>10.6f'))
print(format(x, '=^10'))
print(format(x, '=^10.4f'))
print(format(x, '=^10.5f'))

print('___________________')
print('%-20s' % text)
print('%20s' % text)
