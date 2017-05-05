#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 序列组合的迭代


def parse_data(filename):
    with open(filename, 'r') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error；{}'.format(lineno, e))


# 当你在一个已经解压后的元组序列上使用 enumerate() 函数时

data = [(1, 2), (3, 4), (5, 6), (7, 8)]

for n, (x, y) in enumerate(data):
    print(n, x, y)
for n, s in enumerate(data):
    print(n, s)
