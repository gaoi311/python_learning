from threading import Thread
from multiprocessing import Process
import time

def func_daemon():
    time.sleep(3)
    # print('这是守护进程')
    print('这是守护线程')

def func():
    time.sleep(1)
    # time.sleep(5)
    # print('这是普通进程')
    print('这是普通线程')
# 守护进程是随着父进程的代码执行结束而结束
# 守护线程不是随着父线程的代码执行结束而结束
# 守护线程是随着父线程的执行结束而结束
if __name__ == '__main__':
    t = Thread(target=func_daemon,)
    t.daemon = True
    t.start()
    t1 = Thread(target=func, )
    t1.start()
    print('这里是父线程')
    time.sleep(20)
    # p = Process(target=func_daemon, )
    # p.daemon = True
    # p.start()
    # p1 = Process(target=func, )
    # p1.start()
    # print('这是父进程')