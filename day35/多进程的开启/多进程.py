

from multiprocessing import Process
import time
import os
############################################开启子进程的一种方式
# def func(i):
#     time.sleep(1)
#     print('这里是儿子进程,儿子自己的pid是%s,儿子的父进程的pid是%s'%(os.getpid(),os.getppid()))
#
# # os.getpid()获取的是当前进程自己的pid
# # os.getppid()获取的是当前进程的父进程的pid
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))# 实例化一个进程对象
#     p.start()# 开启一个子进程
#     print('这里是父亲进程，父进程自己的pid是：%s,父亲的父亲的pid是%s'%(os.getpid(),os.getppid()))

######################################### 开启子进程的另外一种方式，以继承的方式

# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
#     def run(self):
#         print('这是以继承类的方式开启的子进程')
#
# if __name__ == '__main__':
#     p1 = MyProcess()
#     p1.start()# 是指，解释器告诉操作系统，去帮我开启一个进程，   就绪状态
#     # p1.run()# 告诉操作系统，现在马上帮我执行这个子进程           执行


# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()#  执行父类的__init__方法
#         # self.name = name
#
#     def run(self):
#         print('这是以继承类的方式开启的子进程,他的名字是%s'%self.name)
#
# if __name__ == '__main__':
#     p1 = MyProcess()
#     p1.start()# 是指，解释器告诉操作系统，去帮我开启一个进程，   就绪状态
    # p1.run()# 告诉操作系统，现在马上帮我执行这个子进程           执行





#################################################如何开启多个不同的子进程

# def func(i):
#     time.sleep(1)
#     print('这里是儿子%s进程,儿子自己的pid是%s,儿子的父进程的pid是%s'%(i,os.getpid(),os.getppid()))
#
# # os.getpid()获取的是当前进程自己的pid
# # os.getppid()获取的是当前进程的父进程的pid
# if __name__ == '__main__':
#     for i in range(2):
#         p = Process(target=func,args=(i,))# 实例化一个进程对象
#         p.start()# 开启一个子进程
#     print('这里是父亲进程，父进程自己的pid是：%s,父亲的父亲的pid是%s'%(os.getpid(),os.getppid()))





