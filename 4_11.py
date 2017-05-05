#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 同时迭代多个序列

xpts = [1, 5, 4, 2, 10, 7]  # 6个
ypts = [101, 78, 37, 15, 62, 99, 100]  # 7个
for x, y in zip(xpts, ypts):
    print(x, y)  #
