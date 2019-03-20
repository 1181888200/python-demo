
# datetime  datetime是Python处理日期和时间的标准库。



# 获取当前日期和时间

from datetime import datetime,timedelta

now = datetime.now() # 当前时间
print( now )

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

# 获取指定日期和时间
dt = datetime(2019,12,11,17,55)

print( dt )
print( type(dt) )

# 把datetime转换为timestamp

print( dt.timestamp() ) # 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。


# timestamp转换为datetime
t = 1576058100.0
td = datetime.fromtimestamp(t)
print(td)


# str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

cday = datetime.strptime( '2019-12-11 18:12:48' , '%Y-%m-%d %H:%M:%S' )
print( cday )

# datetime转换为str strftime()实现

print(now.strftime('%a, %b %d %H:%M'))


# datetime加减

# 加减可以直接用+和-运算符，不过需要导入timedelta这个类

now = now + timedelta(hours=10)
now = now - timedelta(days=1)
print(now)


