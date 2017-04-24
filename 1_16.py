#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 过滤序列元素

from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print [i for i in mylist if i > 2]
print (i for i in mylist if i > 2)
print [i if i > 0 else 0 for i in mylist]
print (i if i > 0 else 0 for i in mylist)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


# filter 和 compress 都是返回迭代器， 需要用list()将其转为list
print filter(is_int, values)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

_bools = [n > 5 for n in counts]
# _bools = []  # 这里为空或是长度大于addresses都不会报错

print list(compress(addresses, _bools))
