
# psutil
'''
    在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
    顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，
    还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

'''

import psutil

# 统计CPU的用户／系统／空闲时间：
print( psutil.cpu_times() )

# 使用psutil获取物理内存和交换内存信息，分别使用：

print( psutil.virtual_memory() )

# 磁盘分区信息
print( psutil.disk_partitions()  )

# 磁盘使用情况
print( psutil.disk_usage('D:\\') )


#sutil可以获取网络接口和网络连接信息：
# 获取网络读写字节／包的个数
print(  psutil.net_io_counters()  )

# 获取网络接口状态
print(  psutil.net_if_stats()  )

# 要获取当前网络连接信息
print(  psutil.net_connections()  )


'''
    >>> psutil.pids() # 所有进程ID
    [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
    >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
    >>> p.name() # 进程名称
    'python3.6'
    >>> p.exe() # 进程exe路径
    '/Users/michael/anaconda3/bin/python3.6'
    >>> p.cwd() # 进程工作目录
    '/Users/michael'
    >>> p.cmdline() # 进程启动的命令行
    ['python3']
    >>> p.ppid() # 父进程ID
    3765
    >>> p.parent() # 父进程
    <psutil.Process(pid=3765, name='bash') at 4503144040>
    >>> p.children() # 子进程列表
    []
    >>> p.status() # 进程状态
    'running'
    >>> p.username() # 进程用户名
    'michael'
    >>> p.create_time() # 进程创建时间
    1511052731.120333
    >>> p.terminal() # 进程终端
    '/dev/ttys002'
    >>> p.cpu_times() # 进程使用的CPU时间
    pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
    >>> p.memory_info() # 进程使用的内存
    pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
    >>> p.open_files() # 进程打开的文件
    []
    >>> p.connections() # 进程相关网络连接
    []
    >>> p.num_threads() # 进程的线程数量
    1
    >>> p.threads() # 所有线程信息
    [pthread(id=1, user_time=0.090318, system_time=0.062736)]
    >>> p.environ() # 进程环境变量
    {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
    >>> p.terminate() # 结束进程
    Terminated: 15 <-- 自己把自己结束了
'''