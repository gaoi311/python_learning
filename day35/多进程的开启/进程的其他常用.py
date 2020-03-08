from multiprocessing import Process
import time


def func():
    time.sleep(1)
    print(123)


if __name__ == '__main__':
    p = Process(target=func,)
    p.start()
    p.terminate()# 杀死p进程,让解释器告诉操作系统，请杀掉p进程。
    print('子进程是否还活着？', p.is_alive())
    time.sleep(0.002)
    print('子进程是否还活着？', p.is_alive())
    # 返回一个bool值，如果返回True，代表进程还活着,如果返回False，代表子进程死了

# p.is_alive() 判断p进程是否还活着
# p.terminate() 杀死p进程