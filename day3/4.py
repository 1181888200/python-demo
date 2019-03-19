# 获取对象信息

#   我们来判断对象类型，使用type()函数

print( type(123) )

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

def fn():
    pass

print( type(fn)==types.FunctionType )

print(  type(abs)==types.BuiltinFunctionType )


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

# fag = isinstance(cat, Animal) # True  False 【3.py案例】
#   总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

print( dir('abc') )



# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

#    hasattr(obj, 'x') # 有属性'x'吗？
#    getattr(obj, 'y') # 获取属性'y'
#    setattr(obj, 'y', 19) # 设置一个属性'y'
