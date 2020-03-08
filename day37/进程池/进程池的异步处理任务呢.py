from multiprocessing import Pool
import time




def func(num):
    num += 1
    return num

if __name__ == '__main__':
    p = Pool(5)
    start = time.time()
    l = []
    for i in range(10000):
        res = p.apply_async(func,args=(i,))# 异步处理这100个任务，异步是指，进程中有5个进程，一下就处理5个任务，接下来哪个进程处理完任务了，就马上去接收下一个任务
        l.append(res)
    p.close()
    p.join()
    print(time.time() - start)
    # [print(i.get()) for i in l]