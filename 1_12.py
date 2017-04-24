#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 序列中出现次数最多的元素

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

words_counter = Counter(words)
top_three = words_counter.most_common(3)
print top_three
print words_counter['eyes']  # Counter对象就是一个字典
# print words_counter

more_words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes']
words_counter.update(more_words)
print words_counter
