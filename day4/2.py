# 调试


# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看
#   用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息


# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代

def foo(s):
    n = int(s)

    assert n!=0 , 'n  is zero!'
    return 10 /n

# foo('0')
'''
    Traceback (most recent call last):
    File "f:/pythonSpace/day4/2.py", line 16, in <module>
        foo('0')
    File "f:/pythonSpace/day4/2.py", line 13, in foo
        assert n!=0 , 'n  is zero!'
    AssertionError: n  is zero!
'''

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert


# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件



import logging
logging.basicConfig(level=logging.INFO)


def fooLog(s):
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

fooLog('0')

# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？
#   别急，在import logging之后添加一行配置再试试：
#   logging.basicConfig(level=logging.INFO)

'''
    这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
    当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
    这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
'''

# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态

# python -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
#   这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

# pdb.set_trace()
#   这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

'''
    import pdb

    s = '0'
    n = int(s)
    pdb.set_trace() # 运行到这里会自动暂停
    print(10 / n)
'''

# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

