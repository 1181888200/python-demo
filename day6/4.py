# -*- coding: utf-8 -*-

# 多线程

'''
    多任务可以由多进程完成，也可以由一个进程内的多线程完成。

    我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

    由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

    Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

    启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
'''

import time, threading

# 新线程执行的代码:

def loop():

    print("thread %s is running ....." % threading.current_thread().name)

    n = 0
    
    while n<5:
        n = n+1
        print("thread %s >>>> %s " %( threading.current_thread().name , n))
        time.sleep(1)
    
    print("thread %s is end ....." % threading.current_thread().name)

def testLoopThread():
    print("thread %s is running ....." % threading.current_thread().name)

    t = threading.Thread( target= loop, name='LoopThread')

    t.start()

    t.join()

    print("thread %s is ended ....." % threading.current_thread().name)

'''
    由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
    Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
    主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
    名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''


# Lock
'''
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
    而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

'''

balance = 0

lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

def run_thread_lock(n):
    for i in range(100000):
        # 先获得锁
        lock.acquire()

        try:
            change_it(n)
        finally:
            #释放锁
            lock.release()


def testWithNoLock():
    t1 = threading.Thread( target=run_thread, args=(5,))
    t2 = threading.Thread( target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("结算后的值：",balance) # 多次运行，发现balance 不是0，而是其他数字

def testWithLock():
    t1 = threading.Thread( target=run_thread_lock, args=(5,))
    t2 = threading.Thread( target=run_thread_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("结算后的值：",balance) # 

   


if __name__ == "__main__":
    
    # 测试用例
    # testLoopThread()

    # 测试多线程中没有带锁
    # testWithNoLock()

    testWithLock()
    '''
        当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

        获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。

        锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
        坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
        其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
    '''

# 多核CPU

'''
    启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

    但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

    因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
    任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
    这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
'''