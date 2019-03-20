# -*- coding: utf-8 -*-

# 正则表达式

'''

    \d可以匹配一个数字，
    \w可以匹配一个字母或数字
    .可以匹配任意字符
    *表示任意个字符（包括0个）
    +表示至少一个字符
    ?表示0个或1个字符
    {n}表示n个字符
    {n,m}表示n-m个字符
    \s可以匹配一个空格（也包括Tab等空白符）

'''

'''

    要做更精确地匹配，可以用[]表示范围，比如：

        [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

        [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

        [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

        [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

    A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

    ^表示行的开头，^\d表示必须以数字开头。

    $表示行的结束，\d$表示必须以数字结束。

    你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。`

'''

# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：

s = 'ABC\\-001'
# 对应的正则表达式
# 'ABC\-001'

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

s = r'ABC\-001'


import re

mtc = re.match(r'^\d{3}\-\d{3,8}','010-12345')
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
print(mtc)


'''
    编译
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：

    编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

    用编译后的正则表达式去匹配字符串。

    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
'''

re_telphone = re.compile(r'^(\d{3})-(\d{3,8})$')
mtc = re_telphone.match('010-1231245')
print( mtc.group(), mtc.group(1) )