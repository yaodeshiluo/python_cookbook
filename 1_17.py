#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从字典中提取子集

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print({k: v for k, v in prices.items() if v > 200})  # 最快
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# print type(tech_names)
print({k: v for k, v in prices.items() if k in tech_names})  # 最快
# print {k: prices[k] for k in prices.keys() & tech_names}  # 比上面慢
print(dict((k, v) for k, v in prices.items() if v > 200))
print(dict((('test', 1), ('test1', 2))))


def kw(**kw):
    print(kw)


kw(test=10)
