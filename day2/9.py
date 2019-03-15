# 返回函数
#   高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def lay_sun(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum

f = lay_sun(1,2,3,4,5)
print( f )
# 调用函数f时，才真正计算求和的结果：
print( f() )

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：'''

# 闭包
'''注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
   
   返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

'''

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n +1 
        return n 
    return counter


def createCounter2():
    fx = [0]
    def counter():
        fx[0] = fx[0] +1 
        return fx[0] 
    return counter

f = createCounter()
print( f() )
print( f() )
print( f() )

f2 = createCounter2()
print( f2() )
print( f2() )
print( f2() )


'''
    结果分析：
        f2()  -- >  f2()  -->  f2()

        第一次调用f2()的时候，fx = [0] 即  fx[0] =0 , 然后设置 fx[0] = fx[0] +1  即 fx[0] = 1 ,返回

        第二次调用f2()的时候，fx[0] = 1,此时又设置 了fx[0] = fx[0] +1  即 fx[0] = 2 ,返回

        第二次调用f3()的时候，fx[0] = 2,此时又设置 了fx[0] = fx[0] +1  即 fx[0] = 3 ,返回

        这个就有点类似于多线程中的并发，counter()是同步方法，当调用counter()之后 fx[0]的值会变动，导致再次调用counter()返回的结果就不一样

'''
print()
print("-------------------再举个例子----------------------")
# 再举个例子

def count():
    fs = []
    for i in range(1, 4): # range(1,4) = [1,2,3]
        def f():
             return i*i
        fs.append(f)

    return fs

f1,f2,f3 = count()

# 输出
print( f1() ) # 9
print( f2() ) # 9
print( f3() ) # 9

# 为什么结果都是9呢？ 而不是 1,4,9 

# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 我们来看一下 fs的内部结果：
#   fs =  [<function count.<locals>.f at 0x00000000010AA400>, <function count.<locals>.f at 0x00000000010AA488>, <function count.<locals>.f at 0x00000000010AA510>]
#   fs = [ f():return i*i , f():return i*i , f():return i*i ]
#   而我们期望的是 fs = [ f():return 1*1 , f():return 2*2 , f():return 3*3 ]
#   但是事实上，等我们去调用f1() 的时候，for循环已经结束，此时的i值已经为3，
#   f1() = f():return 3*3 ,因为i值变化并不是由f()方法引导的，

#   

'''

    小结
    一个函数可以返回一个计算结果，也可以返回一个函数。

    返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

'''
