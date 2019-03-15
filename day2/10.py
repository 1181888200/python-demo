# 匿名函数

# 匿名函数lambda x: x * x
# 等同于
def fu(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

'''
    匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

    用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

'''

fx = lambda x: x* x
print( fx(5) )


# 装饰器
# 函数对象有一个__name__属性，可以拿到函数的名字
def now():
    print("2015-12-12")
f = now
print( f.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# decorator就是一个返回函数的高阶函数。

def log(func):
    def wrapper(*args,**kw):
        print("call %s()" % func.__name__)
        return func(*args,**kw)
    return wrapper

lg = log(f)
lg()


# 偏函数
#   Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

int('123456')
# 二进制
int('123145',base=2)

import functools
# 转成二进制方法
int2 = functools.partial(int, base=2)
int2('10000')

#   简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
