# 实例属性和类属性
#   由于Python是动态语言，根据类创建的实例可以任意绑定属性。

class Student(object):

    def __init__(self,name):
        self.name = name

st = Student('jack')
# 动态任意绑定
st.score = 90

print("{0}---->{1}".format(st.name,st.score))


# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。