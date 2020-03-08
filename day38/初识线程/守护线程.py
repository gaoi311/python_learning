from threading import Thread
from multiprocessing import Process
import time


def func():
    time.sleep(2)
    print(123)

def func1():
    time.sleep(1)
    print('abc')

# 守护线程是根据主线程执行结束才结束
# 守护线程不是根据主线程的代码执行结束而结束
# 主线程会等待普通线程执行结束，再结束
# 守护线程会等待主线程结束，再结束
# 所以，一般把不重要的事情设置为守护线程
# 守护进程是根据主进程的代码执行完毕，守护进程就结束
if __name__ == '__main__':
    t = Thread(target=func)
    t.daemon = True
    t.start()
    # t1 = Thread(target=func1)
    # t1.start()
    # print(99999999999999999999)

############################################ 以下是验证守护进程
# from threading import Thread
# from multiprocessing import Process
# import time
#
#
# def func():
#     time.sleep(2)
#     print(123)
#
# def func1():
#     time.sleep(1)
#     print('abc')
#
# # 守护线程是根据主线程执行结束才结束
# # 守护线程不是根据主线程的代码执行结束而结束
# # 主线程会等待普通线程执行结束，再结束
# # 守护线程会等待主线程结束，再结束
# # 所以，一般把不重要的事情设置为守护线程
# # 守护进程是根据主进程的代码执行完毕，守护进程就结束
# if __name__ == '__main__':
#     t = Process(target=func)
#     t.daemon = True
#     t.start()
#     t1 = Process(target=func1)
#     t1.start()
#     print(99999999999999999999)