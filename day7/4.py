# -*- coding: utf-8 -*-

# itertools提供了非常有用的用于操作迭代对象的函数。

import itertools

# its = itertools.count(1)

# for i in its:
#     print( i )

# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

# cycle()会把传入的一个序列无限重复下去：
# cs = itertools.cycle('abc')
# for c in cs:
#     print(c)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

ns = itertools.repeat("a",3)
for n in ns:
    print( n )


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('abc','123'):
    print( c )


# groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key , group in itertools.groupby("AAABBBDASSKQABK"):
    print( key, list(group))


print("-----------------------------------------------------------------")

# contextlib
#  编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：

from contextlib import contextmanager

class Query(object):

    def __init__(self,name):
        self.name = name

    def query(self):
        print("Query info about ",self.name)

@contextmanager
def create_query(name):
    print("Begin")
    q = Query(name)
    yield q
    print("End")

# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了

with create_query('Bob') as q:
    q.query()

# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。

from contextlib import closing

from urllib.request import urlopen

with closing( urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)




