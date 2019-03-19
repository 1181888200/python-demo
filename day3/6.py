# 当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

class Student(object):

    def set_score(self,score):
        self.score = score


st = Student()
# 动态添加属性
st.name = 'jack'

print( st.name )

# 动态添加方法
def set_age(self,age):
    self.age = age

from types import MethodType

st.set_age = MethodType(set_age,st)

st.set_age(25)

print( st.age )

#给一个实例绑定的方法，对另一个实例是不起作用的：
# st2 = Student()
# st2.set_age(25)
# print( st2.age )

# 为了给所有实例都绑定方法，可以给class绑定方法：

# class中 set_score 方法
# -----------------------------------------------------

# 使用__slots__

'''
    如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

    为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
'''

class Person(object):

    __slots__ = ('name','age') # 限定只能是name,age


p = Person()

p.name = 'jack'
p.age = 22
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# p.score = 33

print("{0}---->{1}".format(p.name,p.age))

# print("{0}---->{1}---->{2}".format(p.name,p.age,p.score))

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作