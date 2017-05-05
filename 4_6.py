#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 带有外部状态的生成器函数

from collections import deque
import types


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):  # 从1开始计数
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()  # list没有这个方法

    def next(self):  # 加入这行代码好像无影响??? 只有__iter__()方法返回自身时此方法有效
        return 1


with open('1_10.py') as f:
    lines = linehistory(f)
    # print(next(lines))  # instance has no next() method, 'linehistory' object is not an iterator
    print(isinstance(lines, types.GeneratorType))  # False
    for line in lines:
        if '#' in line:
            print('---------------------------')
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline))


class News(object):  # 仅有next()方法无法for循环，TypeError: iteration over non-sequence

    def __iter__(self):
        return self  # 如果返回自身，则会调用next()方法

    def next(self):  # 不是__next__(self):
        return 1


# n = News()
# for each in n:
#     print(each)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):  # 如果没有这个方法，仅有next方法会报错。 Fib object is not iterable
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 10:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


# fib = Fib()
# for each in fib:
#     print(each)
