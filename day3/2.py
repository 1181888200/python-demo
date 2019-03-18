# 访问限制
#   在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

#   如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#   在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("{0} ----> {1}".format(self.__name,self.__score))

    # 内部属性 对外访问
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score


st = Student("tom",425)
# 虽然试图改变值，但是却无法成功
st.__name = "jack"
# 外面也无法直接获取
print(st.__name)

st.print_score()

'''
    需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
        并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。


    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
        但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
'''