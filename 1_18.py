#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 映射名称到序列元素

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('test@qq.com', '2017-12-22')  # 有点类似字典，但耗内存更低
print(sub.addr)
print(sub.joined)
# print sub.test  ## AttributeError

a, b = sub  # sub 支持所有的普通元组操作
print(a, b)


def compute_cost(records):
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    total = 0
    for record in records:
        stock = Stock(*record)
        total += stock.shares * stock.price  # 代码可读性up
    return total


# sub.addr = ''  # 命名元组是不可改变属性， 但可以用_replace方法返回一个新的元组
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0.0, 0, None, None)


def dict_to_stock(d):
    return stock_prototype._replace(**d)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}  # 未给出的属性将使用stock_prototype的默认值
print(dict_to_stock(a))
