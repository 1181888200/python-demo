# 文档测试

def foo(s):
    '''
    print ('文档注释，只在命令行中显示，正式环境下不会显示')

    '''
    print("input value : ",s)


foo('jack')
# 运行结果:input value :  jack