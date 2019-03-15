# 高阶函数

#   既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y,f):
    return f(x) + f(y)

# abs 是函数abs() 
a = add(-5,8,abs)
print(a)

# Python内建了map()和reduce()函数。

#   map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#   举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map() 
#   ---> [1,4,9,16,25,36,49,64,81]

def f(x):
    return x * x

r = map(f, range(1,10))
#   map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print( list(r) )

'''
    运行结果分析
    map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9]) = [f(1),f(2),f(3),f(4)....f(9)]

    [1,4,9,16,25,36,49,64,81]
'''


#   reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 求和运算
from functools import reduce

def sumf(x,y):
    return x + y

r = reduce(sumf,[1,2,3,4,5])
print( r)

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x * 10 + y
r = reduce(fn,[1, 3, 5, 7, 9])
print( r)
'''
    分析运行结果
    r = reduce(fn,[1, 3, 5, 7, 9]) =  fn(fn(fn(fn(1,3),5),7),9)
    fn(1,3) = 13
    fn(fn(fn(fn(1,3),5),7),9) ----> fn(fn(fn(13,5),7),9)

    fn(13,5) = 135
    fn(fn(fn(13,5),7),9) ----> fn(fn(135,7),9)

    fn(135,7) = 1357
    fn(fn(135,7),9) ---->  fn(1357,9)

    r = fn(1357,9) = 13579

'''

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

names = ['adam', 'LISA', 'barT']

def write(x):
    a = x[0].upper()
    b = x[1::].lower()
    return a + b

m = map(write,names)

print( list(m) )


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

print("-----------------------------")

def prod(L):
    return reduce(sumf,L)

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print ( prod(ls) )