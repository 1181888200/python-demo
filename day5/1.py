# -*- coding: utf-8 -*-
# 文件读写
'''
    读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
    现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
    然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
'''


# 读文件

# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，标示符'r'表示读，这样，我们就成功地打开了一个文件。

f = open('C:\\Users\\Administrator\\Desktop\\read.txt','r')
content = f.read()

#关闭资源
f.close()

print( content )

def readContent(filePath):

    try:
        f = open(filePath,'r')
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

readContent('C:\\Users\\Administrator\\Desktop\\read.txt')

print("-----------------------------------------")

# 简化版
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

def readContent2(filePath):

    with open(filePath,'r') as f:
        print(f.read())

readContent2('C:\\Users\\Administrator\\Desktop\\read.txt')

print("-----------------------------------------")
'''
    调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
    每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

    如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便

'''
def readContent3(filePath):

    with open(filePath,'r') as f:
        for line in f.readlines():
            
            print(line.strip()) # 把末尾的'\n'删掉


readContent3('C:\\Users\\Administrator\\Desktop\\read.txt')

print("-----------------------------------------")
# file-like Object
'''
    像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
    除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

    StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''

# 二进制文件
#   前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

path_2 = 'C:\\Users\\Administrator\\Desktop\\tonWeb\\src\\common\\img\\2D.png'

f2 = open(path_2,'rb')

# print( f2.read() )


# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件

f3 = open('C:\\Users\\Administrator\\Desktop\\read.txt','r',encoding='UTF-8', errors='ignore')
print( f3.read())