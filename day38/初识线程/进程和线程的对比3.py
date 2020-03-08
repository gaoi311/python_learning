from multiprocessing import Process
from threading import Thread,Lock
import time,os



def func():
    global num
    tmp = num
    time.sleep(0.00001)
    num = tmp - 1

if __name__ == '__main__':
    num = 100
    t_l = []
    for i in range(100):
        t = Thread(target=func)
        t.start()
        t_l.append(t)
    # time.sleep(1)
    [t.join() for t in t_l]
    print(num)












