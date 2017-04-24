#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 命名切片

nums = range(1, 100)
pick = slice(0, 10, 2)
print nums[pick]
print pick.start
print pick.stop
print pick.step


# indices
s = 'hello'
new = pick.indices(len(s))
print pick
print new

for i in range(*new):
    print s[i]
