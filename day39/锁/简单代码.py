from threading import Thread,RLock
from threading import Semaphore
import time


def func(i,l):
    l.acquire()
    l.acquire()
    l.acquire()
    time.sleep(2)
    print(i)
    l.release()
    l.release()
    l.release()
# 第一种情况 在同一个线程内，递归锁可以无止尽的acquire，但是互斥锁不行
# 第二种情况，在不同的线程内，递归锁是保证只能被一个线程拿到钥匙，然后无止尽的acquire，其他线程等待

l = RLock()
for i in range(10):
    Thread(target=func,args=(i,l)).start()











