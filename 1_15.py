#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通过某个字段将记录分组
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))

groups = groupby(rows, itemgetter('date'))  # 迭代时按日期排序
for date, items in groups:
    print 'date', date
    for i in items:
        print ' ', i

new_groups = defaultdict(list)
for row in rows:
    new_groups[row['date']].append(row)  # 最终得到的defaultdict迭代时并不按日期排序
