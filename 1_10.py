#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 删除序列相同元素并保持顺序


# hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = key(item) if key else item
        if val not in seen:
            yield item
            seen.add(val)
