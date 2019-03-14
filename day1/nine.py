# 循环

names = ['jack','tom','lwl','mark']

# for...in 循环
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
for name in names:
    print(name)

# 求和
sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum +=x

print(sum)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
# range() 是从0开始的，也就是range(10) = 0,1,2,3,4,5,6,7,8,9
sum = 0
for x in range(10):
    sum +=x
print(sum)

sum = 0
for x in list(range(10)):
    sum +=x
print(sum)

# while循环

n = 10
total = 0
while n>0:
    total += n
    n -=2
print(total)



# break 在循环中跳出 

k = 1
while k <100:
    k += 10
print("当前的K值：",k)


k = 1
while k <100:
    k += 10
    if k >50:
        break
print("当前的K值：",k)

# continue 跳过当前的这次循环，直接开始下一次循环。

k = 0
while k <10:
    k += 1
    if k %2==0:
        continue
    print("运行中的k:",k)
print("当前的K值：",k)

#  break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

#  要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
#  大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。