# -*- coding:utf-8 -*-

# 字符串格式
#   在Python中，采用的格式化方式和C语言是一致的，用%实现
name = input("请输入您的名字：")

sex = input("请输入你的性别：")

age = input("请输入您的年龄：")

age = int(age)

chu = ('先生' if sex=='男' else '女士')

print("欢迎 %s %s光临，您的年龄是：%d" %(name,chu,age))

# 常见的占位符

# %s  字符串
# %d  整数
# %f  浮点数
# %x  十六进制整数


# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
name = input("请输入您的名字：")

sex = input("请输入你的性别：")

age = input("请输入您的年龄：")

print("欢迎 {0}光临,性别：{1}，您的年龄是：{2}".format(name,sex,age))

# 格式化 保留几位小数
print("您的成绩是{0}，比上一级进步了{1:.1f}%".format(80,70.1234))