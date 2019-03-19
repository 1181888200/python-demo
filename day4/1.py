# 错误处理

#   高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外

try:
    print("try........")

    r = 10 /0

    print("result : ",r)

except ZeroDivisionError as e:

    print("except " ,e)

finally:

    print("finally....")


print("------------end------------")
'''
    try........
    except  division by zero
    finally....
'''

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#   如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
#   如果有finally语句块，则一定执行finally语句块，至此，执行完毕。


# 记录错误
'''
    如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

    Python内置的logging模块可以非常容易地记录错误信息
'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# 测试
# main()

# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

# 抛出错误
'''
    因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

    如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例

'''

class FooError(ValueError):
    pass

def foo2(s):
    n = int(s)

    if n==0:
        raise FooError("invalid value: ",s)
    
    return 10/n

# 测试
foo2('0')

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
#   只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。