from multiprocessing import Process
import time
import os

def func():
    print('这里是儿子,儿子的pid是%s'%(os.getpid()))

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.name = 'alex'
    print('儿子的名字是%s'%p.name)
    print('儿子的pid是%s'%p.pid)
    print('儿子是不是守护进程？',p.daemon)


