
# 迭代

#   如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

a = list(range(1,10))

for x in a:
    print(x)

maps = {'a':1,'b':2,"c":3}

for k,v in maps.items():
    print(k,':',v)

print("-----------------------------------")

for k in maps.keys():
    print(k,':',maps.get(k))

print("-----------------------------------")

for v in maps.values():
    print(v)

# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable

flag = isinstance('abc', Iterable) 
print( flag )

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for index,value in enumerate(a):
    print(index,' ',value)