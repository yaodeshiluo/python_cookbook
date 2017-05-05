#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代器切片

from itertools import islice


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
for num in islice(c, 10, 20):
    print(num)
