# TODO

## questions
* ?

## chapters
* 2.17 在字符串中处理html和xml
    * `s.encode('ascii', errors='xmlcharrefreplace')`

```python
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print(p.unescape(s))  # UnicodeEncodeError: 'gbk' codec can't encode character '\xf1' ...
```

* 2.20 字节字符串
    * 和文本字符串什么区别？？？
