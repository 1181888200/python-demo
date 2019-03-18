# 类和实例

#   面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
#   比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

class Student(object):
    pass

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的

# 创建实例
bart = Student()

# 给属性
bart.name = "jack"

print( bart, bart.name )

# 带构造参数的类
class Person(object):
    
    def __init__(self,name , score):
        self.name = name
        self.score = score

    def print_score(self):
        print("{0},{1}".format(self.name,self.score))
'''
    注意：特殊方法“__init__”前后分别有两个下划线！！！
    注意到__init__方法的第一个参数永远是self，表示创建的实例本身

    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
'''

person = Person('lwl','100')
print( person.name , person.score )


# 数据封装
person.print_score()



