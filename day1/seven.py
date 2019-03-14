# tuple的基本使用方法

#   另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

tuple = ("jack","tom","lwl")

print(tuple)
print(tuple[1])

# 要定义一个只有1个元素的tuple，定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
#   因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,，
t = (1)
print(t)

t = (1,)
print(t)

# 看一个可变的tuple
t = ('a','b',['X','Y'],'d')
t[2][0]='A'
t[2][1] = 'B'
print(t)

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#   即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

# 要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t = ('a','b',('X',),('Y',),'d')
print(t)