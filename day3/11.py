# 使用元类
#   动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

class Hello(object):

    def hello(self,name='hello'):
        print('hello {0}'.format(name))

h = Hello()

h.hello()

print( type(Hello) )

print( type(h) )

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Person类

def fn(self,name='person'):
    print('hello {0}'.format(name))

Person = type('Person',(object,) , dict(hello=fn)) # 创建Person类

p = Person()

p.hello()

'''
    要创建一个class对象，type()函数依次传入3个参数：

    1.class的名称；
    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

    通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

    正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
    也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
    要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''

# metaclass
'''
    除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

    metaclass，直译为元类，简单的解释就是：

    当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

    但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

    连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

    所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# # metaclass是类的模板，所以必须从`type`类型派生：

class ListMetaclass(type):

    def __new__(cls,name , bases, attrs):

        attrs['add'] = lambda self, value: self.append(value)

        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

class MyList(list , metaclass = ListMetaclass):
    pass

'''
    当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

    __new__()方法接收到的参数依次是：

    1. 当前准备创建的类的对象；

    2. 类的名字；

    3. 类继承的父类集合；

    4. 类的方法集合。
'''

ls = MyList()
ls.add(1)

print( ls )

'''
    动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

    但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

    ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

    要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''