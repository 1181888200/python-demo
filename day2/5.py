# 切片

# 取一个list或tuple的部分元素是非常常见的操作

L = ['jack','mark','lwl','tom']

# 取前三个

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
k  = L[0:3]
print(k)

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# 记住倒数第一个元素的索引是-1。
k = L[-2:-1]
print(k)

a = list(range(100))


# 取奇数
# 表示从第几位开始，每隔几位取一个数
b = a[1::2]
print(b)

# 取前50位的偶数
b = a[0:50:2]
print(b)

# 总结：切片 a[start:end:skip] start开始位置，end结束位置不包括在内，skip跳过长度
# start可以用0开始，也可以是负数-1

# tuple 和 str 同样适用于切片

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格

def trim(s):
    while(s[0]==' '):
        s = s[1::]

    while(s[-1]==' '):
        s = s[:-1:]
    
    return s

# s = " hello!"
# print( trim(s))

s = "    hello!    "
s = trim(s)
print( s,len(s))

# s = "hello!"
# print( trim(s))