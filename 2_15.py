#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串中插入变量
import sys
import string

s = '{name} has {n} messages.'
print(s.format(name='yao', n=3))
print(s.format_map({'name': 'yao', 'n': 3}))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('yao', 3)
# print(vars())
print(vars(a))
print(type(vars(a)))


class Info(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n


b = Info('yao', 3)
print(vars(b))
print(type(vars(b)))

print(s.format_map(vars(b)))
# print(s.format_map({'name': 'yao'}))  # KeyError: 'n'


class safesub(dict):

    def __missing__(self, key):
        return '{' + key + '}'


print(safesub())
print(safesub({'name': 'yao'}))
print(dict({'name': 'yao'}))
print(dict([('name', 'yao')]))
print(dict([('name', 'yao')]))
safe = safesub(vars())
print(safe)

print('__________________')
name = 'yao'
print(s.format_map(safe))  # name not in vars()
safe = safesub(vars())
print(s.format_map(safe))  # name in vars()


print('_____________________')
# print(sys._getframe().f_locals)
# print(sys._getframe(1).f_locals)  # ValueError: call stack is not deep enough


def sub(text):
    locals = sys._getframe(1).f_locals  # 不报错了， stack deep here is 1
    # locals2 = sys._getframe(2).f_locals  # ValueError: call stack is not deep enough
    print(locals)
    return text.format_map(safesub(locals))


print(sub('Hello {name}'))


print('______________________')
print('%(name)s has %(n)s messages' % {'name': 'yao', 'n': 3})
n = 3
template = string.Template('$name has $n messages.')
print(template.substitute(vars()))  # formate() 和 format_map()相比%s以及上面这些方法都更加先进

# locals = sys._getframe().f_locals
# for each in locals:
#     print(each)  # RuntimeError: dictionary changed size during iteration
