# list的使用

# 定义
list = ['苹果','香蕉','西瓜']
print(list)

# 获取list的长度

print(len(list))

# 通过下标索引访问list

print(list[1])
print(list[2])

# 除了正索引，还可以用负的，表示从最后一个往前推
print(list[-1])
print(list[-2])

# 添加数据
list.append(123)
print(list)

# 指定位置添加数据
list.insert(1,"tom")
print(list)

#删除数据，默认删除末尾数据，也可以通过index指定删除位置数据
list.pop()
list.pop(0)
print(list)

#改变list指定位置的值
list[1] = "hello"

print(list)