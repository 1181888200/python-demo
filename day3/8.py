# 多重继承

'''
    在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
    但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

    MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
'''

class Animal(object):
    pass


# 单继承
class Dog(Animal):
    pass


# ------------------------
# 奔跑
class Runnable(object):
    pass

# 飞翔
class Flyable(object):
    pass

# 多继承
class Chicken(Runnable,Flyable):
    pass

