
# 函数的参数

# 位置参数
def pwoer(x):
    return x*x

print( pwoer(5) )

# 计算x的 n 次方
def pwoer2(x,n):
    sum = 1
    while n>0:
        sum *= x
        n -= 1
    return sum

print( pwoer2(5,3) )


# 默认参数
# 默认参数必须放在最后，而且设置好默认值
def pwoer3(x,n=2):
    sum = 1
    while n>0:
        sum *= x
        n -= 1
    return sum

print( pwoer3(5) )


# 可变参数  传入的参数个数是可变的
#   可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#   定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]

result = calc(nums[0], nums[1], nums[2])
# 简写
result2 = calc(*nums)

print(result,"   ",result2)


# 关键字参数
#   关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name,age,**kw):
    print('name:',name,' age:',age,' other:',kw)

person('jack',22)

person('tom',25,city='南京')

person('mary',19,city='苏州',gender='女',job='美')

# 命名关键字参数
#   对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print("我的城市是：",kw['city'])
    if 'job' in kw:
       print("我的工作是：",kw['job'])

    print('name:', name, 'age:', age, 'other:', kw)

person2('jack',22)

person2('tom',25,city='南京')

person2('mary',19,city='苏州',gender='女',job='美')

#   和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

def person3(name, age, *, city, job):
    print(name, age, city, job)

person3('mary',19,city='苏州',job='美')



# 参数组合
#   在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#   但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。 a,b=2,*c,(*,e),**d

