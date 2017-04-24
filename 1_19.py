#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 转换并同时计算数据

from operator import itemgetter

import os
files = os.listdir('./')
print(type(files))  # list
if any(s.endswith('.py') or s.endswith('.pyc') for s in files):  # any all
    print('there be python!')
else:
    print('no python')

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(item['shares'] for item in portfolio)
min_shares = min(portfolio, key=itemgetter('shares'))
min_shares = min(portfolio, key=lambda _: _['shares'])
print(min_shares)
