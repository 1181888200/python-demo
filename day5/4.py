# -*- coding: utf-8 -*-

# 操作文件和目录
'''
    果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

    如果要在Python程序中执行这些目录和文件的操作怎么办？
    其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
'''
import os

print( os.name ) # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# os.uname()


# 环境变量
print( os.environ )

# 要获取某个环境变量的值，可以调用os.environ.get('key')：

print( os.environ.get('JAVA_HOME') )

print("---------------------------------------------------------------")

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用

print ("查看当前目录：",os.path.abspath('.'))

# 创建一个目录，如果已经存在，则会报错
# os.mkdir(os.path.abspath('.')+"\\new")

# 删除一个目录 【如果不存在，统找不到指定的文件】
# os.rmdir(os.path.abspath('.')+"\\new")


# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

path = 'C:\\Users\\Administrator\\Desktop\\read.txt'

print( os.path.split(path)[0] )

# os.path.splitext()可以直接让你得到文件扩展名

print( os.path.splitext(path) )

# 文件重命名
# os.rename(path, os.path.join(os.path.split(path)[0],'a.txt'))

#删除文件
# os.remove(path)

'''
    但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

    幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
'''

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

print( [x for x in os.listdir('.') if os.path.isdir(x)] )

print(  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] )

# 利用os模块编写一个能实现dir -l输出的程序。
print( [x for x in os.listdir('.') if os.path.isdir(x) or os.path.isfile(x) ] )





