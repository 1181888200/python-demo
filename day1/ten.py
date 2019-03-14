# dict和set 的使用

# dict    dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'jack': 100, 'tom': 87, 'lwl': 97, 'mark': 56}

# 获取方式,通过key获取
print(d['jack']) # 这种方式如果key 不存在会报错

print(d.get('lwl')) # 这种方式如果key不存在，则会返回一个None

print( d.get('lwl2',-1)) # 这种方式如果key不存在，则会返回一个给定的默认值

# 修改数值 和 添加

d['jack'] = 81
print(d)

#如果key 不存在，则添加
d['sky'] = 66
print(d)

# 所以key是唯一的，不会同时出现2个相同的key

# 通过in判断key是否存在：
print( 'lwl' in d) # 返回True 表示存在，返回False表示不存在

'''
和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
'''

# set  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1,2,3,4])
print(s)

# 添加
s.add('jack')
print(s)

#删除  移除不存的元素会报错
s.remove(2)
print(s)
# 移除不存的元素不会报错
s.discard(5)
# 移除末尾元素并把移除的元素赋给新值
v = s.pop()

# 请问Python如何实现将列表：['a','a','b','a','b','c']输出为字典：{'a':3,'b':2,'c':1}?

lis = ['a','a','b','a','b','c']
maps = {}
for x in lis:
    v = 1
    if x in maps:
        v += maps.get(x)
    maps[x] = v
    
print(maps)

# 循环map
for k,v in maps.items():
    print("key = ",k," , value = " ,v)

print("----------------------------")

# 循环map
for k in maps.keys():
    print("key = ",k," , value = " ,maps.get(k))
