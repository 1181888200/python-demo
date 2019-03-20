# -*- coding: utf-8 -*-
# 子进程

'''
    很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

    subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''

import subprocess

print("$ nslookup www.baidu.com ")

r = subprocess.call(['nslookup','www.baidu.com'])

print('Exit code: ', r)

'''
    运行结果：
    $ nslookup www.baidu.com
    DNS request timed out.
        timeout was 2 seconds.
    服务器:  UnKnown
    Address:  192.168.0.1

    非权威应答:
    DNS request timed out.
        timeout was 2 seconds.
    名称:    dualstack.python.map.fastly.net
    Address:  151.101.108.223
    Aliases:  www.baidu.com

    Exit code:  0

'''
print("------------------------------------------------")

# 如果子进程还需要输入，则可以通过communicate()方法输入：

print("$ nslookup ")

p = subprocess.Popen( ['nslookup'] , stdin= subprocess.PIPE, stdout= subprocess.PIPE, stderr= subprocess.PIPE)

output ,err = p.communicate( b' set q =mx\nbaidu.com\nexit\n')

print(output)
print('Exit code: ', p.returncode)

print("------------------------------------------------")


# 进程间通信

'''
    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

    我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    print(" Process to write :",os.getpid() )

    for v in ['A','B','C']:
        print("put {0} to queue....".format(v))

        q.put(v)

        time.sleep(random.random())

def read(q):
    print(" Process to read :",os.getpid() )
    while True:
        v = q.get(True)
        print("get {0} from queue.".format(v))

if __name__ == "__main__":
    
    q = Queue()

    pw = Process( target=write, args=(q,))
    pr = Process( target=read, args=(q,))

    pw.start()

    pr.start()

    pw.join()

    pr.terminate()

'''
    运行结果：
    Process to write : 8872
    put A to queue....
    Process to read : 8344
    get A from queue.
    put B to queue....
    get B from queue.
    put C to queue....
    get C from queue.
'''

'''
    在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
    因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
    所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

    小结
    在Unix/Linux下，可以使用fork()调用实现多进程。

    要实现跨平台的多进程，可以使用multiprocessing模块。

    进程间通信是通过Queue、Pipes等实现的。
'''