from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import time

def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    print(sum)

if __name__ == '__main__':
    tp = Pool(20)
    start = time.time()
    for i in range(10000):
        tp.apply_async(func, args=(i, ))

    tp.close()
    tp.join()
    print(time.time() - start)