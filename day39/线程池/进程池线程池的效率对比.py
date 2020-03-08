from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from multiprocessing import Pool

#  concurrent.futures 这个模块是异步调用的机制
#  concurrent.futures 提交任务都是用submit
#  for + submit 多个任务的提交
#  shutdown 是等效于Pool中的close+join，是指不允许再继续向池中增加任务，然后让父进程(线程)等待池中所有进程执行完所有任务。

# from multiprocessing import Pool.apply / apply_async
import time

def func(num):
    sum = 0
    for i in range(num):
        for j in range(i):
            for x in range(j):
                sum += x ** 2
    print(sum)

if __name__ == '__main__':
    pass
    # pool的进程池的效率演示
    # p = Pool(5)
    # start = time.time()
    # for i in range(100):
    #     p.apply_async(func,args=(i,))
    # p.close()
    # p.join()
    # print('Pool进程池的效率时间是%s'%(time.time() - start))


    # 多进程的效率演示
    # tp = ProcessPoolExecutor(5)
    # start = time.time()
    # for i in range(100):
    #     tp.submit(func, i)
    # tp.shutdown()  # 等效于 进程池中的 close + join
    # print('进程池的消耗时间为%s' % (time.time() - start))




    # 多线程的效率
    # tp = ThreadPoolExecutor(20)
    # start = time.time()
    # for i in range(1000):
    #     tp.submit(func,i)
    # tp.shutdown()# 等效于 进程池中的 close + join
    # print('线程池的消耗时间为%s'%(time.time() - start))


# 结果：针对计算密集的程序来说
#   不管是Pool的进程池还是ProcessPoolExecutor()的进程池，执行效率相当
#   ThreadPoolExecutor 的效率要差很多
#   所以 当计算密集时，使用多进程。



