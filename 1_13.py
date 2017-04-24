#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通过某个关键字排序一个字典列表
from collections import _itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

for each in rows:
    print _itemgetter('fname', 'uid')(each)

print sorted(rows, key=_itemgetter('uid', 'fname'))  # min max 同理
