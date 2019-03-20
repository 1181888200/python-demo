# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple

Point = namedtuple('Point',['x','y'])

p = Point(1,2)

print(p.x , p.y)

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

# namedtuple('名称', [属性list]):
# 用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
'''
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''

from collections import deque

q = deque(['a','b','c'])
q.append('d')
q.appendleft('x')
print(q)

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。


# defaultdict
'''
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
'''

from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['key'] = 'abc'
print( dd['key'] )
print( dd['key2'] )

'''
    注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

    除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''


# OrderedDict
'''
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

    如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict

d =dict( [ ('a',1),('b',2),('c',3)] )
print(d) # 无序的

od = OrderedDict( [ ('a',1),('b',2),('c',3)] )
print( od ) # 有序的

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：



# ChainMap

'''
    ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

    什么时候使用ChainMap最合适？举个例子：
    应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
    我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
'''



from collections import ChainMap

import os , argparse

# 构造缺省参数

defaults = {
    'color':'red',
    'user':'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()

parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = { k: v for k,v in vars(namespace).items() if v}

# 组合成ChainMap

combined = ChainMap( command_line_args , os.environ , defaults)

#打印参数

print( 'color = %s' % combined['color'])
print( 'user = %s ' % combined['user'])



# Counter   是一个简单的计数器

from collections import Counter

c = Counter()

for ch in 'abcdaadetgojh':
    c[ch] = c[ch] + 1

print( c )