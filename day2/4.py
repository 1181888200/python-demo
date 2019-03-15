# 递归函数
#   如果一个函数在内部调用自身本身，这个函数就是递归函数。

# 1*2*3*4*5*......n 的方法
def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
    
print( fact(5))


# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：


'''
    解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

    尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
    这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........

# 这个数列从第3项开始，每一项都等于前两项之和。

# f(n) = f(n-1) + f(n-2)

def fbnq(n):
    if n==1 or n==2:
        return 1
    else:
        return fbnq(n-1) + fbnq(n-2)
# 输出结果
print ( fbnq(7))


# 汉诺塔的移动可以用递归函数非常简单地实现。

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move(n,a,b,c):
    
    if n ==1:
        print(n,a,'---->',c)
    else:
        move(n-1,a,c,b)
        
        print(n,a,'---->',c)
        
        move(n-1,b,a,c)

move(3,'A','B','C')

'''
# 运行结果分析：
    1 A ----> C
    2 A ----> B
    1 C ----> B
    3 A ----> C
    1 B ----> A
    2 B ----> C
    1 A ----> C

    假设我们有三个柱子A,B,C ,现在我们有三个圆盘x,y,z ,依次变大，而且小的只能放在大的上 x < y < z
    原始柱子： A (x,y,z), B(), C()

    第一次移动： A(y,z) , B(), C(x)  为什么我们不移动到B柱子上呢？因为我们最终是都要移动到C柱子上，而且小圆盘只能在大圆盘上

    第二次移动： A(z), B(y), C(x) 

    第三次移动： A(z), B(x,y), C()    因为 y > x ,所有可以把x移动到 B柱子上的y 上面, 这里就提现第一次移动为什么在C柱子上，如果在B柱子上，那么此时的C柱子就被（x,y）占据着，导致(z)移动失败

    第四次移动： A(), B(x,y), C(z)  

    第五次移动： A(x), B(y), C(z)  

    第六次移动： A(x), B(), C(y,z)  

    第七次移动： A(), B(), C(x,y,z) 最终都把A柱子上的圆盘从大到小 依次移动到C柱子上  
'''