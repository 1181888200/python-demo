# -*- coding: utf-8 -*-

# 定义函数

# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
    if not isinstance(x,(int,float)):       # 数据类型检查可以用内置函数isinstance()
        raise TypeError('bad operand type')

    if x>0:
        return x
    else:
        return -x

# 方法调用
print (my_abs(12314))
print (my_abs(-12314))


# 定义一个控函数
#   pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

def nop():
    pass

print(nop())


# 返回多个值
def move(x,y,step):
    nx = x + step * 10
    ny = y + step * 12
    return nx , ny

nx , ny = move(2,1,4)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#   所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

xy =  move(2,1,4)

print(nx,ny)
print(xy)