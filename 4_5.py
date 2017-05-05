#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 反向迭代

a = range(1, 4)
b = reversed(a)
print(type(b))  # listreverseiterator
print(next(b))
print('-------------------')
for x in reversed(a):
    print(x)
print('-------------------')
for x in b:
    print(x)
# print(next(b))  # StopIteration

print('-------------------')
# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


c = CountDown(10)
for each in c:
    print(each)
print('-------------')
for each in reversed(c):
    print(each)
