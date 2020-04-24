# !/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os, time, random


# 子进程要执行的代码

def run_task(name):
    print('Task %s (pid=%s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    #创建容量为3的进程池
    p = Pool(processes=3)
    #依次向池中添加5个任务
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    #join方法等待所有子进程执行完毕
    p.join()
    print('All subprocesses done.')

"""
结果表明：一开始运行了3个进程，每次至多也是3个；
当一个任务结束了，新的任务依次添加进来；
任务执行所用的进程依然是原来的进程，通过pid看出
"""