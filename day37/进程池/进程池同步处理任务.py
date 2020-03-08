from multiprocessing import Pool
import time




def func(num):
    num += 1
    return num

if __name__ == '__main__':
    p = Pool(5)
    start = time.time()
    for i in range(10000):
        res = p.apply(func,args=(i,))# 同步处理这100个任务，同步是指，哪怕我进程中有5个进程，也依旧是1个进程1个进程的去执行任务
        # time.sleep(0.5)
        print(res)
    print(time.time() - start)