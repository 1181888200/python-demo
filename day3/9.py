# 定制类
'''
    看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

    __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

    除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
'''

class Student(object):

    # 构造器
    def __init__(self,name):
        self.name = name

    # toString方法
    def __str__(self):
        return "Student toString :[name = {0}]".format(self.name)

    __repr__ = __str__

s = Student('jack')

print( s )

# 因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
#   而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。


# __iter__
'''
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''

# __getitem__

#   要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

# __getattr__
'''
    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
    要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
    def __getattr__(self, attr):
        if attr=='score':
            return 99

    当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值

    注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。



'''

# __call__

'''
    一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

    class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

    >>> s = Student('Michael')
    >>> s() # self参数不要传入
    My name is Michael.


'''


# Callable

'''
    怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

    >>> callable(Student())
    True
    >>> callable(max)
    True
    >>> callable([1, 2, 3])
    False
    >>> callable(None)
    False
    >>> callable('str')
    False

    通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
'''