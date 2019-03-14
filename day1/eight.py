# 条件判断

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>

'''
# input输入的是字符类型，需转换成int，否则会报错
age = input("请输入你的年龄：")
age = int(age)
if age  <10:
    print("青少年")
elif age <30:
    print("青年")
elif age<50:
    print("中年")
else:
    print("老年")
