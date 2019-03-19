# -*- coding: utf-8 -*-
# 序列化


'''

    我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

    Python提供了pickle模块来实现序列化。

'''

import pickle

path = 'C:\\Users\\Administrator\\Desktop\\a.txt'

d = dict( name='Bob', age = 20 , score =99)

print( pickle.dumps(d) )

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f= open(path,'wb')
pickle.dump(d,f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

fr = open(path,'rb')
dr = pickle.load(fr)
fr.close()
print( dr )

'''
    Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
    并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

'''

# JSON
#   Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json

print( json.dumps(d) )

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
jd = json.loads(json_str)
print( jd , type(jd ))

# JSON进阶
#   Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

class Student(object):

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('jack',22,100)

# print( json.dumps(s) ) # TypeError: <__main__.Student object at 0x00000000010CBCF8> is not JSON serializable

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
print( json.dumps(s, default=student2dict) ) 

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
print(json.loads(json_str,object_hook=dict2student))

