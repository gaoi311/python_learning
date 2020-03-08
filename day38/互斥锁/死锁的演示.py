from multiprocessing import Process
from threading import Thread,Lock
import time,os



def man(l_tot,l_pap):
    l_tot.acquire()# 是男的获得厕所资源，把厕所锁上了
    print('alex在厕所上厕所')
    time.sleep(1)
    l_pap.acquire()# 男的拿纸资源
    print('alex拿到卫生纸了！')
    time.sleep(0.5)
    print('alex完事了!')
    l_pap.release()# 男的先还纸
    l_tot.release()# 男的还厕所

def woman(l_tot,l_pap):
    l_pap.acquire()  # 女的拿纸资源
    print('小雪拿到卫生纸了！')
    time.sleep(1)
    l_tot.acquire()  # 是女的获得厕所资源，把厕所锁上了
    print('小雪在厕所上厕所')
    time.sleep(0.5)
    print('小雪完事了!')
    l_tot.release()  # 女的还厕所
    l_pap.release()  # 女的先还纸


if __name__ == '__main__':
    l_tot = Lock()
    l_pap = Lock()
    t_man = Thread(target=man,args=(l_tot,l_pap))
    t_woman = Thread(target=woman,args=(l_tot,l_pap))
    t_man.start()
    t_woman.start()

