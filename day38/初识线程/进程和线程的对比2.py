from multiprocessing import Process
from threading import Thread
import time,os



def func(name):
    print('我是一个%s，我的pid是%s'%(name,os.getpid()))


if __name__ == '__main__':

    print('我是main，我的pid是%s'%(os.getpid()))
    for i in range(10):
        p = Process(target=func,args=('进程',))
        p.start()

    for i in range(10):
        p = Thread(target=func,args=('线程',))
        p.start()