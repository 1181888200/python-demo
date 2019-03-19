# 使用枚举类
#   更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value属性则是自动赋给成员的int常量，默认从1开始计数。

for name , member in Month.__members__.items():
    print(name ,  '==>', member , ' , ', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum , unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以帮助我们检查保证没有重复值。

print( Weekday.Mon )

print( Weekday['Tue'] )

print( Weekday['Tue'].value )

print ( Weekday(6) )

# 如果超出范围，则会报错
# print ( Weekday(7) )

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

