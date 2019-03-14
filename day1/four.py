# -*- coding: utf-8 -*-
#   注释是为了告诉Python解释器，按照UTF-8编码读取源代码，

# Python的字符串 编码

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print("中文的str")

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print("A字符串对应的数字： ",ord('A'))

print("中对应的数字 ：",ord("中"))

print("66对应的字符串： ",chr(66))

print("20000对应的字符串 ：",chr(20000))

print('\u4e2d\u6587')


#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

x = b'abc'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('abc'.encode('ascii'))

print('中文'.encode('utf-8'))

#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print(b'abc'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 字符串的长度 len()

print(len('abcde'))
