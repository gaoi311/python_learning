import threading
from threading import Thread
import time


################################# 开启线程的一个比较low的方法
# def func():
#     print('这是一个子线程')
#     time.sleep(2)
#
# if __name__ == '__main__':
#     t = Thread(target=func,args=())
#     t.start()


################################# 装逼的方法


# class MyThread(Thread):
#     def __init__(self):
#         super(MyThread, self).__init__()
#     def run(self):
#         print('我是一个子线程')
#
# t = MyThread()
# t.start()







