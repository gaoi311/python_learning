# from multiprocessing import Process
# import time
#
# def func():
#     time.sleep(100)
#     print('这里是儿子哦')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True # 将p进程设置为守护进程,必须要在start之前设置
#     p.start()
#     time.sleep(1)
#     print('这是爸爸')
# 总结一下：
#     守护进程：跟随着父进程的代码执行结束，守护进程就结束

############################################守护进程的特点

# from multiprocessing import Process
# import time
#
# def func1():
#     print('这里是孙子')
#
# def func():
#     p = Process(target=func1)
#     p.start()
#     time.sleep(5)
#     print('这里是儿子哦')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True # 将p进程设置为守护进程,必须要在start之前设置
#     p.start()
#     time.sleep(1)
#     print('这是爸爸')
#     守护进程：不允许开启子进程

#######################################  守护进程的用法
from multiprocessing import Process
import time


def func():
    for i in range(10):
        time.sleep(1)
        print(time.strftime('%H:%M:%S'))

if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True # 将p进程设置为守护进程,必须要在start之前设置
    p.start()
    time.sleep(5)
    print('这是爸爸')









