# -*- coding: utf-8 -*-
# StringIO和BytesIO

'''
    StringIO
    很多时候，数据读写不一定是文件，也可以在内存中读写。

    StringIO顾名思义就是在内存中读写str。

    要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
'''

from io import StringIO

f = StringIO()

f.write("jack")
f.write("tom")
f.write("哈哈哈哈")
# getvalue()方法用于获得写入后的str。
print( f.getvalue() )

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取

def readStr(s):
    f = StringIO(s)
    while True:
        lne = f.readline()
        if lne =='':
            break
        print( lne.strip() )


readStr("Hello!\nHi!\nGoodbye!")


# BytesIO
'''
    StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

    BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
'''

from io import BytesIO

f = BytesIO()

f.write("中文".encode("utf-8"))

print( f.getvalue() )

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

