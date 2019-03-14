# 函数的调用

# 绝对值
print( abs(123) )

print( abs(-123) )

# help() 方法可以帮助你查看 对应方法的使用
help(abs)

# 函数max()可以接收任意多个参数，并返回最大的那个：

m = max(1,3,6,2,1)
print("最大值为：",m)


#数据类型转换

# 1. int()函数可以把其他数据类型转换为整数

print (int('123'))

print (int(123.52))

# 2. float()函数可以把其他数据类型转换为浮点型
print (float('123'))

print (float(123))

# 3. str()函数可以把其他数据类型转换为字符串
print (str(123.55))

print (str(123))

# 4. bool()函数返回true or false
print(bool(1))

# 5. hex()函数把一个整数转换成十六进制表示的字符串：
print( hex(20) )