# 使用@property
'''
    在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
    为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
    但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

    有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

    还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''
class Student(object):

    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def birth(self):
        return self._birth

    # @score.setter，负责把一个setter方法变成属性赋值
    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2019-self._birth

s = Student()

s.birth = 2000

print( s.birth )

print( s.age )