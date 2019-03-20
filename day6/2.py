# -*- coding: utf-8 -*-
# 多进程

'''
    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
    但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

    子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
    所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
'''

# multiprocessing

'''
    如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？

    由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

    multiprocessing模块提供了一个Process类来代表一个进程对象，
'''

from multiprocessing import Process

import os

# 子进程要执行的代码
def run_proc(name):
    print("run child process %s ( %s )" % (name, os.getpid()))

def testProcess():

    print("Parent process %s " % os.getpid() )

    p = Process(target = run_proc, args=('test',))

    print("Child process will start")

    p.start()

    p.join()

    print("Child process end")

'''
    运行结果：
    Parent process 9096
    Child process will start
    run child process test ( 7452 )
    Child process end
'''

'''
    创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

    join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
'''


# Pool  如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print("Run task ",name,"  ",os.getpid(),"......")
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds " % ( name, (end - start)))


def testPool():
    print("Parent process %s " % os.getpid() )
     
    p = Pool(4)

    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    
    print("Waiting for all subprocesses done...")

    p.close()

    p.join()

    print("All subprocesses done ")

if __name__=='__main__':

    # testProcess()

    testPool()


'''
    运行结果：
    Parent process 8796
    Waiting for all subprocesses done...
    Run task  0    4584 ......
    Run task  1    6892 ......
    Run task  2    9160 ......
    Run task  3    3892 ......
    Task 0 runs 0.83 seconds
    Run task  4    4584 ......
    Task 3 runs 1.08 seconds
    Task 2 runs 2.69 seconds
    Task 1 runs 2.76 seconds
    Task 4 runs 2.47 seconds
    All subprocesses done

    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

    请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
    因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。

'''
        