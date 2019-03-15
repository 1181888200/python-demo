# filter
#   和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

ls = range(1,10)

def is_odd(n):
    # 如果是奇数则返回true
    return n % 2 == 1

ls = filter(is_odd,ls)

print( list(ls) )

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def huishu(n):
    return int(str(n)[::-1])==n

ls = [11,15,22,12321,123421,909]

# 先把数字转成字符串，然后字符串反转，再转成数字，如果还是原来那个数字，则表示是回数

print( list( filter(huishu,ls) ) )
print()
print("--------------------------------------------")
print()

# sorted 排序算法
sl = [10,2,6,22,-2,-17,100]
#  默认是从小到大
sl = sorted(sl)
print(sl)

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
sl = sorted(sl , key=abs)
print(sl)

# 对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
el = ['bob', 'about', 'Zoo', 'Credit']
el = sorted(el)
print(el)

# 忽略大小写排序
el = sorted(el,key=str.lower)
print(el)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
# 也就是说可以倒序，也可以升序,默认是False

el = sorted(el,key=str.lower,reverse=True)
print(el)


# 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sortName(x):
    return x[0]

def sortScore(x):
    return x[1]


# 请用sorted()对上述列表分别按名字排序：
nl = sorted(L,key=sortName)
print(nl)
'''
    结果分析：
    sorted(L,key=sortScore,reverse=True)
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    k = [ 'B', 'A' , 'B' , 'L'] 根据K的值排序

    reverse = True 

'''

# 再按成绩从高到低排序：
sl = sorted(L,key=sortScore,reverse=True)
print(sl)
'''
    结果分析：
    sorted(L,key=sortScore,reverse=True)
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    k = [ 75, 92 , 66 , 88] 根据K的值排序

    reverse = True 

'''